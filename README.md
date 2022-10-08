# youtube-thumbnail-scraper

This is a simple program which allows you to download every thumbnail from a specific Youtube channel written in Python!

# Getting Started

Git clone this project by running <code>git clone https://github.com/Rhysdabeast/youtube-thumbnail-scraper.git</code>

In order to use this program you will need to get a Youtube API token.

1. Head to https://console.cloud.google.com/apis/dashboard and log in with your Google account.
2. Select "Create Project" in the top right of the screen.
3. You will be prompted to enter a Project Name and Location. Enter whatever name you want (I used Python YT) and leave location as "No Organisation". After you've entered the name click "Create".
4. Once your Project has been created you should be taken to the Project's dashboard. At the top you should see "Enable API's and Services", click on it and it should take you to the list of API's Google has available.
5. From the list you need to select "YouTube Data API v3" and click "Enable".
6. Once it has been enabled you should be to see a button in the top right "Create Credentials", click on it and where it asks "What data will you be accessing?" select "Public Data" and click next.
7. You should now have a Youtube API Key! Keep this safe and DO NOT SHARE it with anyone else!

# Running the Scraper

1. You will first need to install the requirements in order to run the scraper. Run <code>pip install -r requirements.txt</code> to install the requirements.
2. Put your Youtube API Key into main.py, <code>YOUTUBE_API_KEY = "YOUR KEY HERE"</code>. If you don't have a Youtube API Key use the steps above to get one.
3. Run the scraper by using <code>python main.py</code>.
4. Enter "1" to scrape thumbnails or "2" to exit the program.
5. If "1" is entered you will be prompted to enter a valid Youtube channel URL like "https://www.youtube.com/c/F1".
6. If a valid channel URL is entered then the scraper will create a folder named after the channel name and will start downloading the thumbnails. The filename format is <code>{title}.jpg</code>.
