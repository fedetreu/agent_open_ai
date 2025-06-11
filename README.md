# News Agent Example

This repo provides a minimal example of creating an agent using the [Google Agent Development Kit](https://google.github.io/adk-docs/).
The agent can search the web and load pages to answer questions about current news.

## Requirements
- Python 3.12+
- `google-adk` Python package
- A Google API key or Vertex AI project configured for Gemini models

## Setup
1. Create and activate a virtual environment (optional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install `google-adk`:
   ```bash
   pip install google-adk
   ```
3. Create a folder named `news_agent/` with the provided `agent.py` and `__init__.py` files.
4. Add a `.env` file to configure your API credentials. For example using Google AI Studio:
   ```dotenv
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
   ```
   Or for Vertex AI:
   ```dotenv
   GOOGLE_GENAI_USE_VERTEXAI=TRUE
   GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
   GOOGLE_CLOUD_LOCATION=LOCATION
   ```

## Running the agent
From the repository root, run:
```bash
adk run news_agent
```
This starts an interactive CLI where you can ask questions about recent news.
