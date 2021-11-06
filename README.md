
# Notes
  - The scraper should only be used for educational purposes
  - Kindly refrain from scraping sensitive or private information
  - It is highly recommended to scrape public (and not private) groups
  - Ask for consent from the group adminstrator and/or group members before running any code
  - I am not responsible for any misuse of the code in any shape or form

# Facebook Group Scraping Using Beautiful Soup & Selenium 
Extract Facebook group posts that are related to a specific topic and write them to a .json file.
This project was created in order to gather data needed to build a chatbot for a university's website.

# Input
  - User's Credentials
  - Facebook Group URL
  - Number of Scrolls 
    - Number of posts you want to collect
  - Directory of the Chromedriver
  - Optional: Specific topic to be searched
  
# What the Scraper Does
  - Logs into Facebook using the User's Credentials
  - Enters the group specified by the User
  - Searches for the topic
  - Extracts all posts & their comments 

# Scraper Output
.json file that includes: <br/>
  - Each post <br/>
  - The comments replying to it

### Format of file:
```.json
{ 
   "tag": "Topic 1",
   "patterns":  [ "Post text" ],
   "responses": [ "Comment 1", 
        "Comment 2",
        "Comment 3"  
    ]
}
```

# Setup Requirements
 1. Make sure chrome is installed
 2. Install [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.54/) and place it in the same directory as the file
 3. Enter inputs required by the code
 4. Run the code


# Updates
- [ ] Scrape comments found in "view more comments"
- [ ] Add an option to scrape the general group discussions and not specific topics
