#import ollma
import concurrent.futures as exe
from utils import generateQWEN
import pdb;
db = pdb.set_trace


BlogList = ["https://app-development.uk/near-me/buckinghamshire/",
"https://app-development.uk/near-me/cambridgeshire/ ",
"https://app-development.uk/near-me/staffordshire/",
"https://app-development.uk/near-me/worcestershire/",
"https://app-development.uk/near-me/northamptonshire/",
"https://app-development.uk/near-me/surrey/",
"https://app-development.uk/near-me/somerset/",
"https://app-development.uk/near-me/bedfordshire/",
"https://app-development.uk/near-me/warwickshire/",
"https://app-development.uk/near-me/devon/",
"https://app-development.uk/near-me/cumbria/",
"https://app-development.uk/near-me/shropshire/",
"https://app-development.uk/near-me/merseyside/",
"https://app-development.uk/near-me/dorset/",
"https://app-development.uk/near-me/glasgow/",
"https://app-development.uk/near-me/norfolk/",
"https://app-development.uk/near-me/gloucestershire/",
"https://app-development.uk/near-me/lancashire/",
"https://app-development.uk/near-me/suffolk/",
"https://app-development.uk/near-me/derbyshire/",
"https://app-development.uk/near-me/cardiff/",
"https://app-development.uk/near-me/hertfordshire/",
"https://app-development.uk/near-me/cheshire/",
"https://app-development.uk/near-me/nottinghamshire/",
"https://app-development.uk/near-me/hampshire/",
"https://app-development.uk/near-me/oxfordshire/",
"https://app-development.uk/near-me/wiltshire/",
"https://app-development.uk/near-me/edinburgh/",
"https://app-development.uk/near-me/kent/",
"https://app-development.uk/near-me/northumberland/"]

ignoreList = [
"https://app-development.uk/near-me/buckinghamshire/",
"https://app-development.uk/near-me/cambridgeshire/ ",
"https://app-development.uk/near-me/staffordshire/",
"https://app-development.uk/near-me/worcestershire/",
"https://app-development.uk/near-me/northamptonshire/",
"https://app-development.uk/near-me/surrey/",
"https://app-development.uk/near-me/somerset/",
"https://app-development.uk/near-me/bedfordshire/",
"https://app-development.uk/near-me/warwickshire/",
"https://app-development.uk/near-me/devon/",
"https://app-development.uk/near-me/cumbria/",
"https://app-development.uk/near-me/shropshire/",
"https://app-development.uk/near-me/merseyside/",
"https://app-development.uk/near-me/dorset/",
"https://app-development.uk/near-me/glasgow/",
"https://app-development.uk/near-me/norfolk/",
"https://app-development.uk/near-me/gloucestershire/",
"https://app-development.uk/near-me/lancashire/",
"https://app-development.uk/near-me/suffolk/",
"https://app-development.uk/near-me/derbyshire/",
"https://app-development.uk/near-me/cardiff/",
"https://app-development.uk/near-me/hertfordshire/",
"https://app-development.uk/near-me/cheshire/",
"https://app-development.uk/near-me/nottinghamshire/",
"https://app-development.uk/near-me/hampshire/",
"https://app-development.uk/near-me/oxfordshire/",
"https://app-development.uk/near-me/wiltshire/",
"https://app-development.uk/near-me/edinburgh/",
"https://app-development.uk/near-me/kent/",
"https://app-development.uk/near-me/northumberland/"]


import requests
from bs4 import BeautifulSoup

def fetch_text_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the parsed HTML
        text = soup.get_text(separator=' ', strip=True)
        
        return text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def run(url):
    text_content = fetch_text_from_url(url)
    if not text_content:
        text_content = ""
    return text_content

def make_request(url_list,parallel=5):

  
    
    with exe.ProcessPoolExecutor(parallel) as exec:
        blogs = list(exec.map(run,url_list))
        return blogs


# Example URL

blogs = "\n********************************************\n".join(make_request(BlogList[:5]))
ignore = "\n********************************************\n".join(make_request(ignoreList))

generateQWEN(blogs)


db()
