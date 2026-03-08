from app.agents.executive_coach import ExecutiveCoachAgent

agent = ExecutiveCoachAgent()

response = agent.run(
    "I have a team member who constantly misses deadlines"
)

print("\nAgent Response:\n")
print(response)