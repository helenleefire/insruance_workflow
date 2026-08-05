"""Node: apply_config_rules
Reads: state.llm_proposal, config/decision_rules.yaml
Does: validates the LLM's proposed verdict against config constraints (thresholds,
required fields, eligibility window). Overrides if a constraint is violated.
Writes to a NEW field (validated_proposal) rather than overwriting llm_proposal,
so both the raw LLM proposal and the post-config result stay visible for the audit trail.
Returns: {"validated_proposal": ValidatedProposal(...)}
"""

# from src.schemas.claim_schema import ValidatedProposal, GraphState


def apply_config_rules(state):
    raise NotImplementedError
