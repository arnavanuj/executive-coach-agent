from langgraph.graph import StateGraph
from typing import TypedDict
from app.agents.executive_coach import ExecutiveCoachAgent
from app.memory.memory_store import retrieve_memory, store_message

# state object that flows through the graph
class AgentState(TypedDict):
    user_input: str
    response: str
    memory_context: str
    session_id: str


coach_agent = ExecutiveCoachAgent()


# memory node function
def memory_retrieval_node(state: AgentState):

    context = retrieve_memory(
        state["session_id"],
        state["user_input"]
    )

    return {
        "memory_context": context
    }


# node function
def coach_node(state: AgentState):

    input_text = state["user_input"]

    if state["memory_context"]:
        input_text = f"""
                        Previous context:
                        {state['memory_context']}

                        User question:
                        {state['user_input']}
                    """

    result = coach_agent.run(input_text)

    store_message(
        state["session_id"],
        state["user_input"],
        result
    )

    return {
        "response": result
    }

# build graph
def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("memory", memory_retrieval_node)
    graph.add_node("coach", coach_node)

    graph.set_entry_point("memory")

    graph.add_edge("memory", "coach")

    graph.set_finish_point("coach")

    return graph.compile()