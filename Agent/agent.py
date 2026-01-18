
from typing import Annotated, Sequence
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessage
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from Agent.prompt import get_model, SYSTEM_PROMPT
from Agent.tools import graphiti_tools, set_graphiti_client


# Define agent state
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


# Create the agent graph
def create_agent_graph():
    model = get_model().bind_tools(graphiti_tools)
    
    async def call_model(state: AgentState):
        messages = state["messages"]
        if not messages or not isinstance(messages[0], SystemMessage):
            messages = [SystemMessage(content=SYSTEM_PROMPT)] + list(messages)
        response = await model.ainvoke(messages)
        return {"messages": [response]}
    
    def should_continue(state: AgentState):
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END
    
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", ToolNode(graphiti_tools))
    workflow.set_entry_point("agent")
    workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
    workflow.add_edge("tools", "agent")
    
    return workflow.compile()


# Create the agent
graphiti_agent = create_agent_graph()


# Run a single query
async def run_query(graphiti_client, query: str):
    set_graphiti_client(graphiti_client)
    
    messages = [SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=query)]
    result = await graphiti_agent.ainvoke({"messages": messages})
    
    for message in reversed(result["messages"]):
        if isinstance(message, AIMessage):
            return message.content
    
    return "No response"
