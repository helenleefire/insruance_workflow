# Ops Copilot

A document-to-decision automation agent for insurance claim intake triage,
with a human-in-the-loop review gate and full audit trail.

Generalized/fictionalized pattern inspired by decision-automation work on
veteran benefit claims processing — built as a portfolio project, not a
reproduction of any real system or data.

## Architecture

LangGraph pipeline:

    extract_claim -> flatten_for_decision -> call_llm_for_proposal -> apply_config_rules
        -> [conditional] get_reviewed_by_human (only when verdict == "review")
        -> finalize

Decision logic is hybrid: the LLM proposes a verdict, and a config file
(`src/config/decision_rules.yaml`) validates/constrains it. Every step writes
to its own state field rather than overwriting prior results, so the full
reasoning chain — raw LLM proposal, post-config result, human override if any,
and final verdict — stays auditable.

## Status

Phase 1 (schema + graph shape) complete. Phase 2 (single-document CLI
pipeline) in progress — see project plan.

## Structure

    src/
      schemas/    Pydantic models (ClaimExtraction, DecisionInput, GraphState, ...)
      agents/     Graph nodes, one file per node
      config/     decision_rules.yaml
      audit/      Audit logger
    data/synthetic_claims/   Fake test documents
    tests/
