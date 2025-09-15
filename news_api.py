import requests # to make web requests
from datetime import datetime, timedelta # Import datetime and timedelta for date manipulation
# from config import check_api_key # import this function from config.py
from decouple import config

api_key = config("NEWS_API_KEY")

class NewsAPIHandler:
    def __init__(self, api_key):

        """Initialize the NewsAPIHandler with the provided API key."""
        self.api_key = api_key
        self.base_url = "https://newsapi.org/{}"  # Base URL for News API
        self.request_count = 0 # a counter to track the number of requests made limit is 100 per day
        self.last_request_time = None  # to track the time of the last request

        # validate the api key as soon as the handler is created
        # is_valid, message = check_api_key(api_key)
        # if not is_valid:
        #     raise ValueError(message)  # Raise an error if the API key is invalid
        
    def make_request(self, endpoint, params=None):
        """Make a request to the News API.
         Handles rate limiting and erros
         returns the JSON response or an error dict

        """
        
        # build the full URL
        url = f"{self.base_url}{endpoint}"

        # add api key to the parameters
        params['apiKey'] = api_key

        try:
            # send get request to the API
            response = requests.get(url, params=params, timeout=10)  # Set a timeout for the request
            self.request_count += 1  # Increment the request count

            # check the http status code
            if response.status_code == 200:
                return response.json()  # Return the JSON response if the request was successful
            elif response.status_code == 401:
                return{"status": "error", "message": "Invalid API key. Please check your News API key."}
            elif response.status_code == 429:
                return {"status": "error", "message": "Rate limit exceeded. Please try again later."}
            else:
                return {"status": "error", "message": f"API Error {response.status_code}: {response.text}"}
            
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions (no internet, network issues, timeouts, server errors, etc.)
            return {"status": "error", "message": f"Request failed: {str(e)}"}
    
    
    def get_top_headlines(self, category=None, country ='us', page_size=10):
        """Fetch top headlines from NewsAPI."""

        endpoint = "top-headlines"
        params = {
            'country': country,
            'pageSize': page_size
        }

        if category:
            params['category'] = category
        
        return self.make_request(endpoint, params)
    
    
    def search_news(self, query, language='en', sort_by='publishedAt', page_size=10):
        """search for news based on query strings"""

        # Calculate the 30 days ago to limit search to recent news
        from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        endpoint = 'everything'
        params = {
            'q': query, # serach queary from the user
            'language': language,
            'sortBby': sort_by,
            'pageSize': page_size,
            'from': from_date # only get articles from the last 30 days
        }

        return self.make_request(endpoint, params)
    
    
    # Create helper method to format the articles


    def format_article(self, article):
        """Extract and format the info needed from the raw article"""

        title = article.get('title', 'No title')
        source = article.get('source', {}).get('name', 'Unknown Source')
        url = article.get('url', '#')
        publishedAt = article.get('publishedAt', '')

        # Format the date from "2024-05-10T12:34:56Z" to "May 10, 2024"
        if publishedAt:
            try:
                date_obj = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
                published_at = datetime.strftime('%b %d, %Y')
            except ValueError:
                published_at = published_at.split("T")[0] # just get the date part

        return {
            'title': title,
            'source': source,
            'url': url,
            'publishedAt': published_at
        }
    
    def get_remaining_requests(self):
        """Estimate remaining requests based on free tier limits"""
        return max(0, 100 - self.request_count) 
    

    
