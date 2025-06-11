from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="news_agent",
    model="gemini-2.0-flash",
    description="Agent that can search the web and answer questions about current news.",
    instruction=(
        "Use google_search to look up recent news articles. "
    ),
    tools=[google_search],
)



