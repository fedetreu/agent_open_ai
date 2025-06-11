from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.load_web_page import load_web_page

root_agent = Agent(
    name="news_agent",
    model="gemini-2.0-pro",
    description="Agent that can search the web and answer questions about current news.",
    instruction=(
        "Use google_search to look up recent news articles. "
        "Use load_web_page to fetch page contents if needed."
    ),
    tools=[google_search, load_web_page],
)
