# News Byte

News Byte is a Python desktop chat bot application that provides users with a conversational interface to access the latest news headlines and trending topics. Built with Tkinter and NewsAPI, it combines an intuitive chat-style interface with powerful news filtering capabilities, making news discovery engaging and personalized through natural conversation.

## Project Goals
1. Create an accessible chat bot for discovering the latest news across various categories

2. Enable users to filter news by topics, categories, and keywords through natural language conversations

3.  Provide a clean, modern chat interface that makes news browsing enjoyable

4. Deliver relevant news with direct access to full articles through conversational interactions


## Features
- User Experience
    - Browse news by category (business, technology, sports, science, health, entertainment)

    - Search for specific topics using natural language queries

    - Conversational interface that understands user requests

    - Clickable links to full news articles

    - Clean, modern GUI with intuitive navigation

    - News Filtering ; 
    Category-based filtering (6 main categories)

    - Keyword search across all news sources

    - Trending topics discovery

    - Date-based filtering (last 30 days)

## Tech Stack
| Layer           | Technologies Used       |
|-----------------|-------------------------|
| Frontend        | Tkinter (Python GUI)    |
| API Integration | NewsAPI                 |
| HTTP Requests   | Python Requests library |
| Configuration   | python-dotenv           |
| Language        | Python 3.8+             |


## API Integration
- NewsAPI provides access to:

    - Top headlines from major news sources

    - Comprehensive search across thousands of publications

    - Category-based filtering

    - Real-time news updates

## Project Structure
    news-byte/
    ├── main.py                 # Application entry point
    ├── news_api.py            # News API integration
    ├── chatbot.py             # Natural language processing and conversation logic
    ├── gui.py                 # Tkinter chat interface implementation
    ├── config.py              # Configuration management
    ├── .env                   # Environment variables (API key)
    └── README.md              # Project documentation

## Installation & Setup

- Prerequisites: Python 3.8+ and NewsAPI account

- Install dependencies: pip install -r requirements.txt

- Configure API key: Add your NewsAPI key to the .env file

- Run application: python main.py

## Conversation Flow
- User sends message

- Bot parses message for intent and entities

- Bot fetches relevant news from API

- Bot formats response in conversational style

- User continues conversation or asks new questions
## Future Enhancements

- Machine learning for improved natural language understanding

- Voice interface for hands-free interaction

- Personalized news preferences based on conversation history

- Multi-turn conversation capabilities for refined searches