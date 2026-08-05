"""Node: extract_claim
Reads: state.raw_document_text
Does: calls the Extraction Agent (LLM) to parse raw document text into a ClaimExtraction
Returns: {"extraction": ClaimExtraction(...)}
"""

# from src.schemas.claim_schema import ClaimExtraction, GraphState


def extract_claim(state):
    raise NotImplementedError
