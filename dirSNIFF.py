import requests
from bs4 import BeautifulSoup

url = input("Enter the website URL (Beginning with http or https): ")

# Get the content of the given website
r = requests.get(url)
html = r.text

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Get all links
links = soup.find_all('a')

# Print the directories
print("All known directories of the website are: ")
for link in links:
    print(link.get('href'))

# Print the hidden directories
print("\nAll hidden directories of the website are:")
for link in links:
    if link.get('href').startswith('/'):
        print(link.get('href'))