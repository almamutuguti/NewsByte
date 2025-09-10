import requests # making http requests to the news API
import tkinter as tk # GUI library for Python
from tkinter import messagebox, ttk, scrolledtext
from datetime import datetime
import webbrowser # to open links in a web browser

# create main application class
class NewsBot:
    def __init__(self, root):
        self.root = root
        self.root.title("NewsBytes - Your Daily News Bot")
        self.root.geometry("900x700")
        self.root.configure(bg="#f5f7fa")

        # api key for News API
        self.api_key = "274efe85e2144792976a40552aa5f110"

        # available news categories
        self.categories = [
            "General", "Business", "Entertainment", "Health",
            "Science", "Sports", "Technology"
        ]

        # country codes for news sources
        self.countries = [
            "US", "GB", "IN", "CA", "AU", "DE", "FR", "JP", "CN", "BR", "RU", "MX"
        ]

        self.setup_ui()


        
