import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
import re 
from news_api import NewsAPIHandler
from chatbot import NewsChatBot
from config import load_config

class NewsChatApp:
    def __init__(self, root, config):
        """Initailize the new app window
        root: The tkinter root window
        config: configuration dictionary from config.py
        """

        self.root = root
        self.config = load_config()

        # set up the news api and chatbot

        try:
            self.news_api = NewsAPIHandler(config['NEWS_API_KEY'])
            self.chatbot = NewsChatBot(self.news_api)

        except ValueError as e:
            # if api keyis invalid 
            messagebox.showerror("API Error", str(e))
            self.root.destroy()
            return
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize: {str(e)}")
            self.root.destroy()

        # set up the gui
        self.setup_gui()

        # show welcome message
        self.show_welcome_message()


    def setup_gui(self):
        """Set up all gui components"""
        # configure the main window

        self.root.title('NewsByte - Your News Chat Bot')
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")

        # main frame to hold everything
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        #Header with title
        header = tk.Frame(main_frame, bg='#2c3e50', height=80)
        header.pack(fill=tk.X, pady=(0, 10))

        title = tk.Label(header, text="News Byte", font=('Arial', 20, 'bold'), 
                        fg='white', bg='#2c3e50')
        title.pack(pady=20)
        
        subtitle = tk.Label(header, text="Your Personal News Assistant", 
                           font=('Arial', 12), fg='#ecf0f1', bg='#2c3e50')
        subtitle.pack(pady=(0, 15))
        
        # Category buttons
        categories_frame = tk.Frame(main_frame, bg='#f0f0f0')
        categories_frame.pack(fill=tk.X, pady=(0, 10))
        
        categories = ['Business', 'Technology', 'Sports', 'Science', 'Health', 'Entertainment']
        colors = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6', '#f39c12', '#1abc9c']
        
        # Create buttons for each category
        for i, category in enumerate(categories):
            btn = tk.Button(categories_frame, text=category, font=('Arial', 10, 'bold'),
                          command=lambda c=category.lower(): self.category_click(c),
                          bg=colors[i], fg='white', relief=tk.FLAT, padx=10, pady=5)
            btn.pack(side=tk.LEFT, padx=5)
        
        # Chat display area (where messages appear)
        chat_frame = tk.Frame(main_frame, bg='white', relief=tk.SUNKEN, bd=1)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, 
                                                    font=('Arial', 11), state=tk.DISABLED,
                                                    bg='white', fg='#2c3e50', padx=10, pady=10)
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.chat_display.tag_config('bot', foreground='#2c3e50')
        self.chat_display.tag_config('user', foreground='#2980b9')
        self.chat_display.tag_config('link', foreground='#3498db', underline=1)
        self.chat_display.tag_config('error', foreground='#e74c3c')
        
        # Make links clickable
        self.chat_display.tag_bind('link', '<Button-1>', self.open_link)
        
        # Input area (where user types)
        input_frame = tk.Frame(main_frame, bg='#f0f0f0')
        input_frame.pack(fill=tk.X)
        
        self.input_field = tk.Entry(input_frame, font=('Arial', 12), 
                                   bg='white', fg='#2c3e50', relief=tk.SUNKEN, bd=1)
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.input_field.bind('<Return>', self.send_message)
        self.input_field.focus_set()  # Focus on input field when app starts
        
        # Send button
        send_btn = tk.Button(input_frame, text="Send", command=self.send_message,
                           bg='#27ae60', fg='white', font=('Arial', 12, 'bold'),
                           relief=tk.FLAT, padx=15)
        send_btn.pack(side=tk.RIGHT)
        
        # Status bar at bottom
        status_bar = tk.Frame(main_frame, bg='#34495e', height=20)
        status_bar.pack(fill=tk.X)
        
        self.status_label = tk.Label(status_bar, text="Ready", fg='white', bg='#34495e',
                                    font=('Arial', 9))
        self.status_label.pack(side=tk.LEFT, padx=5)
        
        # Show remaining API requests
        remaining = self.news_api.get_remaining_requests()
        self.requests_label = tk.Label(status_bar, text=f"Requests: {remaining}/100", 
                                      fg='white', bg='#34495e', font=('Arial', 9))
        self.requests_label.pack(side=tk.RIGHT, padx=5)

    def show_welcome_message(self):
        """Display welcome message when app starts"""

        welcome_msg = "Hello! I'm News Byte, your personal news assistant. \n\n"
        welcome_msg += "I can help you discover the latest news across various categories.\n\n"
        welcome_msg += "Try asking me for:\n"
        welcome_msg += "• Specific categories (technology, business, sports, etc.)\n"
        welcome_msg += "• News about specific topics or keywords\n"
        welcome_msg += "• General headlines\n\n"
        welcome_msg += "You can also click the category buttons above for quick access!"
        
        self.add_message(welcome_msg, 'bot')

    def add_message(self, message, sender='bot'):
        """Add a message to the chat display"""
        self.chat_display.config(state=tk.NORMAL)  # Enable editing
        
        # Add sender label
        if sender == 'user':
            self.chat_display.insert(tk.END, "You: ", 'user')
        else:
            self.chat_display.insert(tk.END, "News Byte: ", 'bot')
        
        # Check if this is an error message
        if "error" in message.lower() or "sorry" in message.lower():
            self.chat_display.insert(tk.END, message, 'error')
        else:
            # Process the message to handle links
            lines = message.split('\n')
            for line in lines:
                # Look for [Read more](URL) pattern
                link_match = re.search(r'\[Read more\]\((http[^)]+)\)', line)
                if link_match:
                    url = link_match.group(1)
                    line_text = line.replace(link_match.group(0), 'Read more')
                    self.chat_display.insert(tk.END, line_text)
                    self.chat_display.insert(tk.END, "Read more", ('link', url))
                else:
                    self.chat_display.insert(tk.END, line + '\n')
        
        self.chat_display.insert(tk.END, '\n')
        self.chat_display.config(state=tk.DISABLED)  # Disable editing
        self.chat_display.see(tk.END)  # Scroll to bottom


    def send_message(self, event=None):
        """Handle sending user messages"""
        user_input = self.input_field.get().strip()
        if not user_input:  # Don't send empty messages
            return
            
        self.add_message(user_input, 'user')
        self.input_field.delete(0, tk.END)  # Clear input field
        
        # Get response from chatbot
        response = self.chatbot.process_query(user_input)
        self.add_message(response, 'bot')
        
        # Update remaining requests counter
        remaining = self.news_api.get_remaining_requests()
        self.requests_label.config(text=f"Requests: {remaining}/100")


    def category_click(self, category):
        """Handle category button clicks"""
        self.add_message(f"Show me {category} news", 'user')
        response = self.chatbot.get_category_news(category)
        self.add_message(response, 'bot')
        
        # Update remaining requests counter
        remaining = self.news_api.get_remaining_requests()
        self.requests_label.config(text=f"Requests: {remaining}/100")

    def open_link(self, event):
        """Open clicked links in default web browser"""
        # Find what was clicked
        index = self.chat_display.index(f"@{event.x},{event.y}")
        tags = self.chat_display.tag_names(index)
        
        # Look for link tags and open the URL
        for tag in tags:
            if tag != 'link' and tag.startswith('link'):
                parts = tag.split(' ', 1)
                if len(parts) > 1:
                    url = parts[1]
                    webbrowser.open(url)
                break
 


        




          