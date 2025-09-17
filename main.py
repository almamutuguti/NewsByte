import tkinter as tk
from gui import NewsChatApp
from config import load_config, setup_environment, check_api_key  
import sys
# from decouple import config


def main():
    """Main entry point for the app
    Handles startup, configuration and error handling
    """
    print("Starting NewsByte...")
    print("=" * 40)

    try: 
        if not setup_environment():
            print("Please set up your .env file first")
            input("Press enter to exit...")
            
            return
        
        # load config from environment vars
        print("Loading configuration...")
        config = load_config()

        #Validate the API key
        is_valid, message = check_api_key(config['NEWS_API_KEY'])

        if not is_valid:
            print(f"{message}")
            input("Press Enter to exit...")
            return
        
        print("Configuration loaded successfully")
        print(f"Country: {config['DEFAULT_COUNTRY']}")
        print(f"Page Size: {config['DEFAULT_PAGE_SIZE']}")

        #create the main app window
        print("Creating Application window...")
        root = tk.Tk()

        # create and intialize app
        print("Initializing application...")
        app = NewsChatApp(root, config)

        print("NewsByte is ready!")
        print("=" * 40)

        # Start the main event loop
        root.mainloop()

    except Exception as e:
        print(f"Failed to start NewsByte: {str(e)}")
        print("=" * 40)
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
    






