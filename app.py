# External modules
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from scripts.walmart import search_walmart
from scripts.safeway import search_safeway 
from utils import upload_to_algolia
# Custom modules

load_dotenv()

app = Flask(__name__)
CORS(app)

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
    itemsV2_array = data['data']['search']['searchResult']['itemStacks'][0]['itemsV2']
    for product_data in itemsV2_array:
        # TODO: Extract the data from the response and sanitize
        extracted_data = {
            "objectID": product_data.get("id", "N/A"),
            "name": product_data.get("name", "N/A"),
            "basePrice": product_data['priceInfo']['currentPrice'].get('price', "N/A"),
            "unitOfMeasure": product_data.get("salesUnitType", "N/A"),
            "pricePer": product_data['priceInfo']['unitPrice'].get('priceString', "N/A"),
            "averageWeight": product_data.get("weightIncrement", "N/A"),
            "storeName": "Walmart",
        }
        upload_to_algolia(extracted_data)
    return jsonify(data), 200



@app.route('/safeway', methods=['POST'])
def scrape_safeway_store():
    data = request.get_json()
    product = data.get('query')
    if not product:
        return jsonify({'error': 'Query is missing'}), 400
    
    # Return the query result as JSON
    data = search_safeway(product)
    product_items_array = data['pgmList'][0]['response']['docs']
    for product_data in product_items_array:
        # TODO: Extract the data from the response and sanitize
        extracted_data = {
        "objectID": product_data.get("id", "N/A"),
        "name": product_data.get("name", "N/A"),
        "basePrice": product_data.get('price', "N/A"),
        "unitOfMeasure": product_data.get("unitOfMeasure", "N/A"),
        "pricePer": product_data.get('pricePer', "N/A"),
        "averageWeight": product_data.get("averageWeight", ["N/A"])[0],  # Taking the first element of the list
        "storeName": "Safeway",
    }
        upload_to_algolia(extracted_data)
    return jsonify(data), 200



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
