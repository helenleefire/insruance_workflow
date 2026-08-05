"""Node: finalize
Reads: state.validated_proposal, state.review
Does: sets final_verdict ONCE as an explicit stored fact (never re-derived elsewhere),
which is what the audit trail depends on.
    final_verdict = review.human_verdict if review and review.reviewed else validated_proposal.verdict
Returns: {"final_verdict": ...}
"""

# from src.schemas.claim_schema import GraphState


def finalize(state):
    raise NotImplementedError
