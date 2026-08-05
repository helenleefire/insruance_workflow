"""Node: get_reviewed_by_human
Reads: state.validated_proposal (and decision_input for context)
Does: LangGraph interrupt() — pauses graph execution, waits for a human response,
resumes with that response. Only reached when validated_proposal.verdict == "review".
human_verdict is restricted to approve/reject — the human is the final decision-maker,
no further escalation tier.
Returns: {"review": ReviewOutcome(...)}
"""

# from src.schemas.claim_schema import ReviewOutcome, GraphState


def get_reviewed_by_human(state):
    raise NotImplementedError
