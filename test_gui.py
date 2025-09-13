import tkinter as tk
from gui import NewsChatApp
from config import load_config

def test_gui():
    """Test the GUI without full functionality"""
    root = tk.Tk()
    
    # Create a minimal config for testing
    test_config = {
        'NEWS_API_KEY': 'test_key_123456789012345678901234567890',  # 32-char fake key
        'DEFAULT_COUNTRY': 'us',
        'DEFAULT_PAGE_SIZE': 10,
        'MAX_REQUESTS_PER_DAY': 100
    }
    
    # Test just the GUI layout
    app = NewsChatApp(root, test_config)
    
    # Add some sample messages to see how they look
    app.add_message("Hello! I'm News Byte, your personal news assistant.", 'bot')
    app.add_message("Show me technology news", 'user')
    app.add_message("Here are the latest technology news:\n\n1. Apple announces new iPhone - Tech News (May 15, 2024)\n   [Read more](https://example.com/news1)\n\n2. Microsoft unveils AI tool - Tech Daily (May 14, 2024)\n   [Read more](https://example.com/news2)", 'bot')
    
    root.mainloop()

if __name__ == "__main__":
    test_gui()