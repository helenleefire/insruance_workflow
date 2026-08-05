from pydantic import BaseModel
from typing import Literal
from datetime import date


# --- Extraction-stage models (nested, mirrors the source document) ---

class ClaimTypeClassification(BaseModel):
    raw_description: str  # free-text "what happened," as written in the document
    predicted_type: Literal["medical", "disability", "property_damage", "death_benefit", "other"]
    confidence: float


class ClaimantInfo(BaseModel):
    claimant_id: str
    full_name: str
    contact_email: str | None = None
    relationship_to_incident: Literal["self", "dependent", "survivor"] = "self"


class IncidentDetails(BaseModel):
    incident_date: date
    classification: ClaimTypeClassification


class SupportingDocumentation(BaseModel):
    document_types_provided: list[str]  # e.g. ["medical_record", "police_report"]
    documentation_complete: bool


class ExtractionCompleteness(BaseModel):
    missing_fields: list[str] = []
    extraction_confidence: float


class ClaimExtraction(BaseModel):
    claimant: ClaimantInfo
    incident: IncidentDetails
    documentation: SupportingDocumentation
    requested_amount: float | None = None
    completeness: ExtractionCompleteness


# --- Flattened, for the Decision Agent ---

class DecisionInput(BaseModel):
    claim_type: str
    claim_type_confidence: float
    incident_date: date
    requested_amount: float | None
    missing_fields: list[str]
    extraction_confidence: float
    documentation_complete: bool
    relationship_to_incident: str
    claim_summary: str  # short LLM-generated summary, not the full raw text


# --- Decision + review stage ---

class DecisionProposal(BaseModel):
    verdict: Literal["approve", "review", "reject"]
    confidence: float
    reasoning: str
    flagged_fields: list[str] = []


class ReviewOutcome(BaseModel):
    reviewed: bool
    human_verdict: Literal["approve", "reject"] | None = None  # human is the final decision-maker — no "review" escalation tier
    override_reason: str | None = None


class ValidatedProposal(BaseModel):
    verdict: Literal["approve", "review", "reject"]
    was_overridden: bool
    override_reason: str | None = None


# --- LangGraph state ---
# Accumulates across nodes rather than being replaced. final_verdict is set
# once, by a dedicated `finalize` node, so it's an explicit stored fact —
# never re-derived — which is what the audit trail depends on.

class GraphState(BaseModel):
    raw_document_text: str
    extraction: ClaimExtraction | None = None
    decision_input: DecisionInput | None = None
    llm_proposal: DecisionProposal | None = None
    validated_proposal: ValidatedProposal | None = None
    review: ReviewOutcome | None = None
    final_verdict: Literal["approve", "review", "reject"] | None = None
