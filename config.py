import os
from dotenv import load_dotenv
# Load environment variables from .env file


def load_config():
    """Load configuration from environment variables."""

    print("Loading environment variables")

    # env_path = '.env'

    # if os.path.exists(env_path):
    #     print(f"Found env file at: {os.path.abspath(env_path)}")

    # else:
    #     print(f"env file not found at: {os.path.abspath(env_path)}")

    load_dotenv() # look for the .env file in the current directory

    # api_key_from_env = os.getenv('NEWS_API_KEY')
    # print(f"NEWS_API_KEY from environment: {'Found' if api_key_from_env else 'NOT FOUND'}")
    # if api_key_from_env:
    #     print(f"Key value: {api_key_from_env[:10]}...")

    default_news_api_key = '274efe85e2144792976a40552aa5f110 '

    # Define the configuration dictionary
    config = {
        'API_KEY': os.getenv('NEW_API_KEY', default_news_api_key),
        'API_SECRET': os.getenv('API_SECRET'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'DEBUG_MODE': os.getenv('DEBUG_MODE', 'False').lower() in ('true', '1', 't')
    }

    # dbHOMW=[MY DB]

    # print("Final config values:")
    # for key, value in config.items():
    #     print(f"   {key}: {value if key != 'NEWS_API_KEY' else value[:10] + '...'}")

    return config

def check_api_key(api_key):
    """Check if the API key is valid."""

    if not api_key or not api_key == '274efe85e2144792976a40552aa5f110':
        return False, "Please set a valid API key in the .env file. Get free API key from https://newsapi.org"
    
    if len(api_key) != 32 or not api_key.isalnum():
        return False, "Invalid API key format. Please check your .env file. API key should be a 32-character alphanumeric string with numbers and letters only."
    
    return True, "API key is valid."

def setup_environment():
    """Check if env file exists and guide the user if not.Returns True if setupis complete false otherwise"""
    if not os.path.exists('.env'):
        print("Welcome to News Byte!")
        print("It looks like you have not set up your API key yet")
        print("Please create a .env file with the following content:")
        print("NEWS_API_KEY=your_actual_api_key")
        print("Get your free API key from: https://newsapi.org")
        
        return False
    
    return True


# Temporary test code
# if __name__ == "__main__":
#     config = load_config()
#     print("Loaded API Key:", config['API_KEY'])
#     is_valid, message = check_api_key(config['API_KEY'])
#     print("Validation Result:", is_valid)
#     print("Message:", message)
    
    


