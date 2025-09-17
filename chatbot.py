# # This file uses the NewsAPIHandler we created to fetch data based on user input.
# # No external imports are needed beyond our own module.

# class NewsChatBot:
#     def __init__(self, news_api_handler):

#         """Initialize the chat bot by making a connection tothe news api handler"""

#         self.news_api = news_api_handler # the engine we built
        
#         # set of categories that the bot will recognize
#         self.categories = {

#             "business", "entertainment", "health", "science", "sports", "technology"
#         }

#         self.context = {} # to remember context in future versions

#     def process_query(self, user_input):
#         """Proces the users input"""

#         user_input = user_input.lower().strip()

#         #1.Check if user is asking for help
#         if any(word in user_input for word in ['help', 'how to', 'what can', 'commands']):
#             return self.get_help_response()
        
#         #2. check if user has mention a category
#         for category in self.categories:
#             if category in user_input:
#                 return self.get_category_news(category)
            
#         # 3. check if user wants general news
#         if any (word in user_input for word in ['news', 'headlines', 'latest', 'update']):
#             return self.get_general_news()
        
#         #4. if none treat as a search query
#         return self.search_news(user_input)
    
#     # create the methods called in the process query

#     def get_category_news(self, category):
#         """fetch and format news for the particular category"""

#         result = self.news_api.get_top_headlines(category=category)

#         #check for error message
#         if result.get('status') == 'error':
#             return result['message'] # return error message to the user
        
#         articles = result.get('articles', [])
#         if not articles:
#             return f"Sorry unable to find {category} news at the moment"
        
#         # format the articles
#         formatted_articles = [self.news_api.format_article(article) for article in articles]
        
#         # Generate final response
#         return self.generate_response(formatted_articles, f"latest {category} news")
    
#     def get_general_news(self):
#         """Fetch and format general headlines"""

#         result = self.news_api.get_top_headlines()

#         #check for error message
#         if result.get('status') == 'error':
#             return result['message'] # return error message to the user
        
#         articles = result.get('articles', [])
#         if not articles:
#             return f"Sorry unable to find news headlines at the moment"
        
#         # format the articles
#         formatted_articles = [self.news_api.format_article(article) for article in articles]
        
#         # Generate final response
#         return self.generate_response(formatted_articles, "latest news")
    
#     def search_news(self, query):
#         """Search news based on query"""

#         result = self.news_api.search_news(query)

#         #check for error message
#         if result.get('status') == 'error':
#             return result['message'] # return error message to the user
        
#         articles = result.get('articles', [])
#         if not articles:
#             return f"Sorry unable to find news about {query}"
        
#         # format the articles
#         formatted_articles = [self.news_api.format_article(article) for article in articles]
        
#         # Generate final response
#         return self.generate_response(formatted_articles, f"news about {query}")
    
    
    
#     def generate_response(self, articles, query_type):
#         """Generate a formated response srting from a list of articles"""

#         response = f"Here are the {query_type}: \n \n"

#         # number each article and format it with title, source, date, link

#         for i, article in enumerate(articles, 1):
#             response += f"{i}. {article['title']} - {article['source']} ({article['published_at']})\n"

#             response += f"[Read More]({article['url']})\n \n" # creates a clickable link

#             # a helpful footer for remaining api requests
#             remaining = self.news_api.get_remaining_requests()
#             response += f"\nRemaining Api requests today: {remaining}/100"

#             return response
        
        
#     # get help on how to interact with the bot
#     def get_help_response(self):
#         "Return a help message with instructions"
#         response = "I'm News Byte, your news assistant! Here's what I can do: \n \n"

#         response += "1. **Get news by category**: 'technology news', 'sports updates', 'business headlines'\n"

#         response += "2. **Search for topics**: 'news about artificial intelligence', 'find articles on climate change'\n"

#         repsonse += "3. **Get general headlines**: 'latest news', 'headlines', 'what's happening?'\n\n"

#         response += " **Available Categories**: 'business', 'entertainment', 'health', 'science', 'sports', 'technology\n\n"

#         response += " You an also click the category buttons for quick access!"

        
#         return response
    
# This file uses the NewsAPIHandler we created to fetch data based on user input.
# No external imports are needed beyond our own module.

class NewsChatBot:
    def __init__(self, news_api_handler):
        """Initialize the chat bot by making a connection to the news api handler"""
        self.news_api = news_api_handler # the engine we built
        
        # set of categories that the bot will recognize
        self.categories = {
            "business", "entertainment", "health", "science", "sports", "technology"
        }

        self.context = {} # to remember context in future versions

    def process_query(self, user_input):
        """Process the users input"""
        user_input = user_input.lower().strip()

        # 1. Check if user is asking for help
        if any(word in user_input for word in ['help', 'how to', 'what can', 'commands']):
            return self.get_help_response()
        
        # 2. check if user has mentioned a category
        for category in self.categories:
            if category in user_input:
                return self.get_category_news(category)
            
        # 3. check if user wants general news
        if any(word in user_input for word in ['news', 'headlines', 'latest', 'update']):
            return self.get_general_news()
        
        # 4. if none treat as a search query
        return self.search_news(user_input)
    
    # create the methods called in the process query

    def get_category_news(self, category):
        """fetch and format news for the particular category"""
        result = self.news_api.get_top_headlines(category=category)

        # check for error message
        if result.get('status') == 'error':
            return result.get('message', 'Unknown error occurred') # return error message to the user
        
        articles = result.get('articles', [])
        if not articles:
            return f"Sorry unable to find {category} news at the moment"
        
        # format the articles
        formatted_articles = []
        for article in articles:
            formatted_article = self.news_api.format_article(article)
            if formatted_article:  # Only add if formatting was successful
                formatted_articles.append(formatted_article)
        
        if not formatted_articles:
            return f"Sorry, couldn't format {category} news properly"
        
        # Generate final response
        return self.generate_response(formatted_articles, f"latest {category} news")
    
    def get_general_news(self):
        """Fetch and format general headlines"""
        result = self.news_api.get_top_headlines()

        # check for error message
        if result.get('status') == 'error':
            return result.get('message', 'Unknown error occurred')
        
        articles = result.get('articles', [])
        if not articles:
            return "Sorry unable to find news headlines at the moment"
        
        # format the articles
        formatted_articles = []
        for article in articles:
            formatted_article = self.news_api.format_article(article)
            if formatted_article:
                formatted_articles.append(formatted_article)
        
        if not formatted_articles:
            return "Sorry, couldn't format news properly"
        
        # Generate final response
        return self.generate_response(formatted_articles, "latest news")
    
    def search_news(self, query):
        """Search news based on query"""
        result = self.news_api.search_news(query)

        # check for error message
        if result.get('status') == 'error':
            return result.get('message', 'Unknown error occurred')
        
        articles = result.get('articles', [])
        if not articles:
            return f"Sorry unable to find news about {query}"
        
        # format the articles
        formatted_articles = []
        for article in articles:
            formatted_article = self.news_api.format_article(article)
            if formatted_article:
                formatted_articles.append(formatted_article)
        
        if not formatted_articles:
            return f"Sorry, couldn't format news about {query} properly"
        
        # Generate final response
        return self.generate_response(formatted_articles, f"news about {query}")
    
    def generate_response(self, articles, query_type):
        """Generate a formatted response string from a list of articles"""
        response = f"Here are the {query_type}: \n\n"

        # number each article and format it with title, source, date, link
        for i, article in enumerate(articles[:5], 1):  # Limit to 5 articles
            response += f"{i}. **{article.get('title', 'No title')}**\n"
            response += f"   - Source: {article.get('source', 'Unknown')}\n"
            response += f"   - Date: {article.get('publishedAt', 'Unknown date')}\n"
            response += f"   - [Read More]({article.get('url', '#')})\n\n"

        # Add helpful footer for remaining API requests
        remaining = self.news_api.get_remaining_requests()
        response += f"Remaining API requests today: {remaining}/100"

        return response
        
    # get help on how to interact with the bot
    def get_help_response(self):
        """Return a help message with instructions"""
        response = "I'm News Byte, your news assistant! Here's what I can do: \n\n"

        response += "1. **Get news by category**: 'technology news', 'sports updates', 'business headlines'\n"
        response += "2. **Search for topics**: 'news about artificial intelligence', 'find articles on climate change'\n"
        response += "3. **Get general headlines**: 'latest news', 'headlines', 'what's happening?'\n\n"
        response += "**Available Categories**: business, entertainment, health, science, sports, technology\n\n"
        response += "You can also click the category buttons for quick access!"

        return response
    

    

    






    

        
        

        