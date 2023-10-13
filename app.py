# External modules
import os
import json
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests
import json
# Custom modules

load_dotenv()

app = Flask(__name__)
CORS(app)
# TODO - Apply CORS properly else api will be fucked
# CORS(app, origins=["http://localhost:3000", "https://example.com"])


@app.route('/hello', methods=['GET'])
def hello():
    return 'active', 200

@app.route('/walmart', methods=['POST'])
def scrape_walmart_store():
    data = request.get_json()
    product = data.get('query')
    if not product:
        return jsonify({'error': 'Query is missing'}), 400
    
    # Return the query result as JSON
    data = search_walmart(product)
    answer = data
    response = {
        'answer':answer
    }
    return jsonify(response), 200

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
            "query":"banana",
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
    
    params = {
        'variables': json.dumps(variables)
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Unable to fetch the data. Status code: {response.status_code}"

# You can call this function and pass the search query you want
result = search_walmart("laptop")
print(result)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
