# Python API Services 
This repository showcases a collection of Python scripts demonstrating various aspects of web APIs using 'urllib' and 'json' modules.

### Overview
The repository contains a series of Python scripts, and these scripts are arranged in order of increasing complexity.:

<br>

1. **pokemon_stats_api_search** It takes a Pokémon name as user input, constructs a URL for the PokeAPI, and then makes a request to the API. The script uses a custom header in the request to simulate a browser ('User-Agent':'Mozilla/5.0'). After receiving the response, it decodes and loads the JSON data, and then prints out specific details about the Pokémon (such as name and other attributes).

<br>

2. **google_maps_api_request.py:** Its takes name of a location as input, constructs a dynamic URL for making an API request to the Google Maps Geocoding API, processes the json response and then prints Name, Address, Latitude and Longitude. The program is functional but requires an API key for access, which is not included in the script.

<br>

3. **geocode_api_address_lookup.py:** It uses the PY4E GeoCode API to retrieve address data without any rate limiting. The user is prompted to enter a location, and the script constructs a request URL. Then, it makes an HTTP request to the PY4E GeoCode API, receives the response, decodes the data, and processes the JSON response and prints details about the entered location, such as coordinates and other relevant geographical information.

<br>

4. **weather_api_query.py:** is designed to check the current weather using latitude and longitude coordinates through an API request to the OpenWeatherMap API. The script prompts the user to input latitude and longitude values, constructs a URL with these coordinates and an API key (which needs to be provided), and then makes an HTTP request to the OpenWeatherMap API. After receiving the response, it decodes the JSON data and displays the current weather information

<br>

5. **weather_forecast_api_query.py:** is programmed to check the weather forecast for the next four days using user provided latitude and longitude coordinates. It makes an API request to the OpenWeatherMap API. The script prompts the user to input coordinates, includes an API key (which must be provided by the user), constructs a URL with these parameters, and then sends a request to the OpenWeatherMap API and displays the weather forecast for the next 4 days.

<br>

6. **twitter_api_self_data.py:** fetches and displays information about the authenticated user's Twitter account. The script sends a request to the Twitter API's endpoint and parses the JSON data returned by the API. The script extracts the user's ID, name, and username from the response and prints them out. 

<br>

7. **twitter_api_friends_db.py:** This script is designed to interact with the Twitter API to build a social graph database using SQLite (twfriends.sqlite). It creates two tables, People and Follows. The People table stores Twitter user names and a flag indicating whether their friends have been retrieved. The Follows table records relationships between users, showing who follows whom. The script allows the user to enter a Twitter account name, fetches the friends list for that account, and updates the database accordingly. It handles network connections, JSON parsing, and database updates, demonstrating how to build a social network graph from API data. 

### Requirements
- To use these scripts, you'll need Python 3.11 installed on your machine.

- The required external modules for twfriends and twuser can be downloaded from the following links:
    - twurl.py : [link](https://www.py4e.com/code3/twurl.py)
    - hidden.py : [link](https://www.py4e.com/code3/hidden.py)
    - oauth.py : [link](https://www.py4e.com/code3/oauth.py)
- Install 'ssl' module: 
    ```bash 
    pip install ssl
    ```

- API Keys will be required when running scripts that use OpenWeatherMap API, Google Maps API or Twitter API. You can get the API keys as follows:
    - OpenWeatherMap API : [link](https://openweathermap.org/api)
    - Google Maps API : [link](https://developers.google.com/maps/documentation/geocoding)
    - twitter API : [link](https://apps.twitter.com/) (Create App, get 4 strings and put them in hidden.py)

### Contributing
Feel free to fork this repository and contribute by adding more examples or enhancing the existing ones. Contributions that improve the code or demonstrate new aspects of web services and data processing in Python are always welcome!

### Contact
If you have any questions or suggestions, please feel free to contact me at quddus1999@gmail.com.
