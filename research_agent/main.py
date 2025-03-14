import os
import json
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables
load_dotenv()

# API Keys
gemini_api_key = os.getenv("GEMINI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")
if not serper_api_key:
    raise ValueError("SERPER_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Function to fetch latest news articles using Serper
def search_latest_news():
    url = "https://google.serper.dev/news"
    headers = {"X-API-KEY": serper_api_key, "Content-Type": "application/json"}
    payload = json.dumps({"q": "latest news 2025", "num": 5})  # General news

    response = requests.post(url, headers=headers, data=payload)
    results = response.json()

    if "news" in results:
        return [{"title": res["title"], "link": res["link"]} for res in results["news"]]
    else:
        return []

# Function to extract full news article text from a URL
def extract_news_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract text content from paragraphs
        paragraphs = soup.find_all("p")
        full_text = "\n".join([p.get_text() for p in paragraphs])

        if len(full_text) < 100:  # If extracted text is too short, return error
            return "⚠ Unable to extract full article content."
        
        return full_text
    except Exception as e:
        return f"⚠ Error fetching article: {str(e)}"

# ✅ Create the General News Researcher Agent
agent = Agent(
    name="General News Researcher",
    instructions="You are a news researcher that fetches and summarizes the latest global news articles.",
    model=model
)

# 🔍 Fetch latest general news
news_list = search_latest_news()
news_content = ""

for idx, news in enumerate(news_list):
    full_article = extract_news_content(news["link"])
    news_content += f"## {idx+1}. {news['title']}\n\n"
    news_content += f"🔗 **Source:** {news['link']}\n\n"
    news_content += f"{full_article}\n\n---\n\n"

print("\n🔍 **Latest Global News Fetched & Extracted**")

# 🎯 Run the agent with full news articles
result = Runner.run_sync(agent, f"Summarize these global news articles:\n{news_content}", run_config=config)

print("\n📢 **Global News Summary:**\n", result.final_output)

# Save the latest full news and summary in a markdown file
news_filename = "news.md"

with open(news_filename, "w", encoding="utf-8") as file:
    file.write("# 🔍 Latest Global News\n\n")
    file.write(news_content + "\n\n")
    file.write("# 📢 Global News Summary\n\n")
    file.write(result.final_output + "\n")

print(f"\n✅ Global news saved to {news_filename} successfully!")
