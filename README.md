# google-images-scraper
Simple web scraper for Google images. Currently scrapes up to ~180 thumbnail images for any search query, and will save images in a subdirectory named `photos`.
## Setup
Install dependencies from requirements.txt
```
pip install -r requirements.txt
```
Download the [Chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your platform. The scraper uses this to scroll down on the search result and load more images. To use the scraper without modifications, add the webdriver's location to your system's PATH environment variable. Otherwise, change this line of code to link to the webdriver:
```
driver = webdriver.Chrome()
# change to:
driver = webdriver.Chrome('/path/to/chromedriver.exe')
```
## Usage
Example:
```
python scraper.py
```
The scraper will prompt you for a search query and a maximum number of images to download. Images will be saved into a subdirectory named `photos`. If there is not already a subdirectory with that name, the scraper will create one.