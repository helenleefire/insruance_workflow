"""Graph assembly for Ops Copilot.

Nodes (in order):
    extract_claim -> flatten_for_decision -> call_llm_for_proposal -> apply_config_rules
    -> [conditional] get_reviewed_by_human (only if validated_proposal.verdict == "review")
    -> finalize

Edges:
    1 -> 2 -> 3 -> 4 (fixed)
    4 -> 5 if validated_proposal.verdict == "review", else 4 -> 6
    5 -> 6 (fixed, when reached)
    6 is terminal
"""

# TODO: build with langgraph.graph.StateGraph once nodes are implemented
