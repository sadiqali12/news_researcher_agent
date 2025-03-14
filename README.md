# 📢 AI News Researcher Agent

## 🔍 Overview
This project is an **AI-powered news researcher agent** that fetches the latest global news, extracts full articles, summarizes them using an AI model (Gemini), and saves the results in a `news.md` file.

## 🚀 Features
- **Fetches Latest News**: Uses the Serper API to get the latest news headlines.
- **Extracts Full Articles**: Scrapes news content from URLs using BeautifulSoup.
- **Summarizes News**: Uses Google Gemini AI (via OpenAI-compatible API) to generate concise summaries.
- **Saves News & Summary**: Stores the fetched articles and AI-generated summaries in `news.md`.

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/sadiqali12/news_researcher_agent.git
cd news_researcher_agent
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys
Create a `.env` file in the project directory and add the following keys:
```ini
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

## 🏃‍♂️ Usage
Run the script to fetch, summarize, and save the latest news:
```sh
python main.py
```

After execution, the latest news and summaries will be stored in `news.md`.

## 📄 File Structure
```
├── researcher.py        # Main script to fetch and summarize news
├── requirements.txt     # Required dependencies
├── .env                 # API keys (not committed to Git)
├── news.md              # Output file containing news and summaries
├── README.md            # Project documentation
```

## 📝 Dependencies
- Python 3.8+
- `requests`
- `beautifulsoup4`
- `python-dotenv`
- `agents` (OpenAI Agents SDK / CrewAI)

## 🌟 Contributions
Feel free to contribute! Open an issue or submit a pull request. 🚀

## 📜 License
MIT License. Free to use and modify. 🎉

