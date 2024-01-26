import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the webpage containing the images
url = 'http://svips.ac.in/portfolio.php'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags with the specified source attribute
    image_tags = soup.find_all('img', {'src': True})

    # Directory to save the images
    save_directory = 'scrape'
    os.makedirs(save_directory, exist_ok=True)

    # Download each image
    for img_tag in image_tags:
        # Get the source URL of the image
        img_src = img_tag['src']

        # Join the URL parts to get the absolute URL
        img_url = urljoin(url, img_src)

        # Get the image filename from the URL
        img_filename = os.path.join(save_directory, os.path.basename(img_url))

        # Send a GET request for the image
        img_response = requests.get(img_url)

        # Save the image to the specified directory
        with open(img_filename, 'wb') as img_file:
            img_file.write(img_response.content)

        print(f"Downloaded: {img_filename}")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
