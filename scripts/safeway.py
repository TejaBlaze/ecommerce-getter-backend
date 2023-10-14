import requests
import json
import os

def search_safeway(search_query):
    # Base URL
    base_url = "https://www.safeway.com/abs/pub/xapi/pgmsearch/v1/search/products"
    
    # Parameters
    headers = {
    'authority': 'www.safeway.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en;q=0.5',
    'ocp-apim-subscription-key': '5e790236c84e46338f4290aa1050cdd4',
    'referer': f'https://www.safeway.com/shop/search-results.html?q={search_query}',
    'cookie': os.environ.get('SAFEWAY_COOKIE'),
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        # ! THIS REQUEST ID IS UNIQUE TO EACH SESSION and ROTATES EVERY 5mins
        'request-id': '6681697245858172644',
        'url': 'https://www.safeway.com',
        'pageurl': 'https://www.safeway.com',
        'pagename': 'search',
        'rows': '30',
        'start': '0',
        'search-type': 'keyword',
        'storeid': '3132',
        'featured': 'true',
        'search-uid': '',
        'q': search_query,
        'sort': '',
        'featuredsessionid': '',
        'screenwidth': '947',
        'dvid': 'web-4.1search',
        'channel': 'instore',
        'cross-seller-max-count': '14',
        'wineshopstoreid': '5799',
        'wineshopwidgetid': 'nlvkox9e',
        'timezone': 'America/Los_Angeles',
        'zipcode': '94611',
        'pgm': 'mkp-crossseller,wineshop',
        'banner': 'safeway',
    }

    
    # Make the request
    response = requests.get(base_url, headers=headers, params=params)
    
    # Check the response status and return the result
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Unable to fetch the data. Status code: {response.status_code}"

