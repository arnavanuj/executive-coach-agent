from unittest.mock import patch
from app.agents.executive_coach import ExecutiveCoachAgent


@patch("ollama.chat")
def test_agent_run(mock_chat):

    mock_chat.return_value = {
        "message": {"content": "Test response"}
    }

    agent = ExecutiveCoachAgent()
    response = agent.run("Hello")

    assert response == "Test response"