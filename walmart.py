def search_walmart(search_query):
    base_url = "https://www.walmart.com/orchestra/snb/graphql/Search/8fda6bfee2198e53d801ff1b8dbdb11f8d604542adb91463fdb83d0ad33465fd/search"
    
    variables = {
        "id":"",
        "dealsId":"",
        "query":search_query,
        "page":1,
        "prg":"desktop",
        "catId":"",
        "facet":"",
        "sort":"best_match",
        "rawFacet":"",
        "seoPath":"",
        "ps":40,
        "limit":40,
        "ptss":"",
        "trsp":"",
        "beShelfId":"",
        "recall_set":"",
        "module_search":"",
        "min_price":"",
        "max_price":"",
        "storeSlotBooked":"",
        "additionalQueryParams":{
            "hidden_facet":None,
            "translation":None,
            "isMoreOptionsTileEnabled":True
        },
        "searchArgs":{
            "query":search_query,
            "cat_id":"",
            "prg":"desktop",
            "facet":""
        },
        "fitmentFieldParams":{
            "powerSportEnabled":True,
            "dynamicFitmentEnabled":False,
            "extendedAttributesEnabled":False
        },
        #    "fitmentSearchParams":{
        #       // ... (same structure as above)
        #    },
        "enableFashionTopNav":False,
        "enableRelatedSearches":True,
        "enablePortableFacets":True,
        "enableFacetCount":True,
        "fetchMarquee":True,
        "fetchSkyline":True,
        "fetchGallery":False,
        "fetchSbaTop":True,
        "fetchDac":True,
        "tenant":"WM_GLASS",
        "enableFlattenedFitment":False,
        "enableMultiSave":False,
        "pageType":"SearchPage"
        # ... (you can continue to set other parameters as needed)
    }

    headers = {
        "authority": "www.walmart.com",
        "Accept": "application/json",
        "accept-language":"en-US",
        "content-type":"application/json",
        "cookie":os.environ.get('WALMART_COOKIE'),
    'device_profile_ref_id': 'scI09kIAtvzLHMAULdSBBswMhAzRQNRUGcgf',
    'referer': 'https://www.walmart.com/search?q=' + search_query,
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'traceparent': '00-12e8cdc29e0e5866eca9f83c2d74f0df-9eb2d8bf678d9077-00',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'wm_mp': 'true',
    'wm_page_url': 'https://www.walmart.com/search?q=' + search_query,
    'wm_qos.correlation_id': 'rX-q8hukUOFGFojsraPecwLPzI7G72C9RxmQ',
    'x-apollo-operation-name': 'Search',
    'x-enable-server-timing': '1',
    'x-latency-trace': '1',
    'x-o-bu': 'WALMART-US',
    'x-o-ccm': 'server',
    'x-o-correlation-id': 'rX-q8hukUOFGFojsraPecwLPzI7G72C9RxmQ',
    'x-o-gql-query': 'query Search',
    'x-o-mart': 'B2C',
    'x-o-platform': 'rweb',
    'x-o-platform-version': 'us-web-1.103.0-87cb97a69fa41e97cf5fc7ce18fa7e3101592ca5-1012',
    'x-o-segment': 'oaoh'

        # ... (you can add more headers as needed)
    }
    
    params = {
        'variables': json.dumps(variables)
    }
    
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Unable to fetch the data. Status code: {response.status_code}"
