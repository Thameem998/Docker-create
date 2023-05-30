import requests
from bs4 import BeautifulSoup

def get_data():
    url = "https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx"
    r = requests.get(url)
    print(r)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find the table
    table = soup.find('table')

    # Iterate over table rows
    for row in table.find_all('tr')[1:]:  # [1:] to skip the header
        columns = row.find_all('td')

        # Extract the data
        deal_date = columns[0].text
        security_code = columns[1].text
        security_name = columns[2].text
        client_name = columns[3].text
        deal_type = columns[4].text
        quantity = columns[5].text
        price = columns[6].text

        # Now, you can insert this data into your database
