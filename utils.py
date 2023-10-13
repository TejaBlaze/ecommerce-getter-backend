from algoliasearch.search_client import SearchClient

def upload_to_algolia(data):
    # Connect and authenticate with your Algolia app
    client = SearchClient.create(os.environ.get('ALGOLIA_KEY'), os.environ.get('ALGOLIA_SECRET'))

    # Create a new index and add a record
    index = client.init_index("baskeasy-products")
    index.save_object(data).wait()

