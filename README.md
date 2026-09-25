# Multi-Agent Research Assistant

An autonomous AI-powered research assistant that searches the web, extracts relevant information, and generates structured research reports using multiple specialized agents.

## Overview

The system uses multiple AI agents working together as a research workflow:

* **Search Agent** — searches the live web for relevant and recent information.
* **Reader Agent** — visits selected URLs and extracts useful content.
* **Writer Chain** — analyzes the collected information and generates a structured research report.
* **Critic Chain** — reviews the generated report and provides feedback on its quality.

## Architecture

```text
User Research Query
        ↓
   Search Agent
        ↓
    Tavily API
        ↓
  Search Results
        ↓
   Reader Agent
        ↓
 BeautifulSoup
        ↓
  Extracted Content
        ↓
   Writer Chain
        ↓
 Research Report
        ↓
   Critic Chain
        ↓
 Evaluation & Feedback
        ↓
   Final Output
```

## Tech Stack

* Python
* LangChain
* OpenAI API
* Tavily API
* BeautifulSoup
* Streamlit
* uv
* Python dotenv

## Features

* Real-time web research
* Multi-agent workflow
* Automated web scraping
* LLM-powered research synthesis
* Research report generation
* Automated report evaluation
* Interactive Streamlit interface

## Project Structure

```text
multi-agent-research-assistant/
│
├── agents.py
├── tools.py
├── requirements.txt
├── .env
├── .gitignore
├── app.py
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ujjwalsingh888/multi-agent-research-assistant.git

cd multi-agent-research-assistant
```

### 2. Create the virtual environment

```bash
uv venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

## Future Improvements

* Add additional research agents
* Improve source verification
* Add citation generation
* Implement persistent research history
* Deploy the application to the cloud
* Add support for multiple LLM providers

## Author

**Ujjwal Singh**

GitHub: https://github.com/ujjwalsingh888
