# Demonstrating interactions with APIs and the requests library
# Install in your local environment with pip install requests
# We'll be working with the Apple API which will return a JSON object
# getting Tom Brady's walkout song and theme song from 80 for Brady

from json import dumps
from requests import get
from logging import INFO, basicConfig, info
from urllib.parse import quote

basicConfig(level=INFO)

info("🐐 start return- songs about the goat 🐐")

# Specific search terms for the songs
search_terms = ["JAY-Z Public Service Announcement", "John Cardon Debney Tom's Theme"]

# Function to make a request to the iTunes API and log the result
def fetch_song_info(search_term):
    encoded_search_term = quote(search_term)
    # the response api allows us to call the url of the apple api
    response = get(f"https://itunes.apple.com/search?entity=song&limit=1&term={encoded_search_term}")

    if response.status_code != 200:
        info(f"Failed to retrieve data for {search_term} from iTunes.")
        return

    song_info = response.json()
    # apple developer guide defines these as keys for the json object, allowing us to parse out desired data
    for result in song_info["results"]:
        info(f"Track Name: {result['trackName']}")
        info(f"Artist Name: {result['artistName']}")
        info(f"Album Name: {result['collectionName']}")
        info(f"Release Date: {result['releaseDate']}")
        info(f"Genre: {result['primaryGenreName']}")
        info(f"Track Price: {result.get('trackPrice', 'N/A')}")
        info(f"Album Price: {result.get('collectionPrice', 'N/A')}")

    info(dumps(song_info, indent=2))

# Fetch information for each song
for term in search_terms:
    fetch_song_info(term)

info("🐐 end return - songs about the goat 🐐")