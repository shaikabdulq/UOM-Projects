# Python Web Networking Scripts

<br>

### Overview
This repository contains a collection of Python scripts demonstrating various aspects of web networking, including basic socket programming, web scraping, and HTML parsing. These scripts are ideal for educational purposes and provide a practical understanding of handling network requests, parsing HTML content, and working with web data in Python.

### Scripts
1. **web_socket_connection.py:** This script creates a socket connection to a specified server, sends a GET request, and prints the received response. It demonstrates basic socket programming in Python.
2. **urllib_web_text_reader.py:**This script retrieves text from a specific URL using urllib and prints each line of the text. It's a straightforward demonstration of using urllib to read web content.
3. **url_word_frequency_count.py:** This script reads a text file from a URL using urllib module, processes the text to find the most frequently occurring word, and then displays that word along with its frequency. 
4. **sum_numeric_in_html.py:** This script parses HTML, using BeautifulSoup Module, from a URL to extract and sum numeric values contained in 'span' tags. Then, it prints the total sum and count of numbers.
5. **html_links_scraper.py:** This script reads HTML from a user-input URL, parses it with BeautifulSoup, and prints the contents and href of 'a' tags. It also counts and displays the number of 'a' tags found.
6. **url_navigation_looper.py:** This script fetches HTML from a user-input URL and navigates through the links in a loop, based on user-input count and position. It uses BeautifulSoup for parsing and displays the current URL being retrieved.

### Installation
#### Prerequisites 
To use these scripts, you'll need Python 3.11 installed on your machine. BeautifulSoup4 Module is required for HTML Parsing.

#### Setting Up
1. Ensure Python 3.11 is installed on your system.
2. Install BeautifulSoup4:

```bash
pip install bs4
```

### Contributing
Feel free to fork this repository and contribute by adding more examples or enhancing the existing ones. Contributions that improve the code or demonstrate new aspects of web services and data processing in Python are always welcome!

### License
These scripts are provided for educational purposes and are not affiliated with any of the APIs used.

### Contact
If you have any questions or suggestions, please feel free to contact me at quddus1999@gmail.com.