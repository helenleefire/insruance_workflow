"""Node: call_llm_for_proposal
Reads: state.decision_input
Does: calls the Decision Agent (LLM) to produce a verdict + reasoning + confidence
Returns: {"llm_proposal": DecisionProposal(...)}
"""

# from src.schemas.claim_schema import DecisionProposal, GraphState


def call_llm_for_proposal(state):
    raise NotImplementedError
