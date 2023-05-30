import requests
from bs4 import BeautifulSoup

def scrape_site():
    url = 'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now you can use soup to navigate through the HTML of the page
    # and pull out the data you're interested in.
