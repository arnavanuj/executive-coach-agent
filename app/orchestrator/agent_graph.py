from langgraph.graph import StateGraph
from typing import TypedDict
from app.agents.executive_coach import ExecutiveCoachAgent


# state object that flows through the graph
class AgentState(TypedDict):
    user_input: str
    response: str


coach_agent = ExecutiveCoachAgent()


# node function
def coach_node(state: AgentState):

    result = coach_agent.run(state["user_input"])

    return {
        "response": result
    }


# build graph
def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("coach", coach_node)

    graph.set_entry_point("coach")

    graph.set_finish_point("coach")

    return graph.compile()