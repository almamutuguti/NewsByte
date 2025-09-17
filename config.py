from decouple import config
# Load environment variables from .env file


def load_config():
    """Load configuration from environment variables using python-decouple."""
    return {
        'NEWS_API_KEY': config('NEWS_API_KEY', default=''),
        'DEFAULT_COUNTRY': config('DEFAULT_COUNTRY', default='us'),
        'DEFAULT_PAGE_SIZE': config('DEFAULT_PAGE_SIZE', default=10, cast=int)
    }

def setup_environment():
    """Check if required environment variables are set."""
    api_key = config('NEWS_API_KEY', default=None)
    return api_key is not None and api_key != ''

def check_api_key(api_key):
    """Validate the API key."""
    if not api_key or api_key == '':
        return False, "API key is missing or invalid."
    return True, "API key is valid."


# Temporary test code
# if __name__ == "__main__":
#     config = load_config()
#     print("Loaded API Key:", config['API_KEY'])
#     # is_valid, message = check_api_key(config['API_KEY'])
#     # print("Validation Result:", is_valid)
#     # print("Message:", message)
    
    


