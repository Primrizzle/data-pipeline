import requests

class ProductOffers:
    def __init__(self, api_key, api_host):
        """
        Initializes the ProductOffers class with necessary API configuration.

        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host
    def product_offers(self, asin='B09SM24S8C', country='US', limit='100', page=1):
        """ Retrieves the offers of a product on Amazon based on its ASIN.
            
            :param asin: str - The ASIN of the product.
            :param country: str - Country/Marketplace to search in.
            :param limit: str - Number of offers to retrieve.
            :param page: str - Page number for pagination support.
            :return: dict - The JSON response from the API.
            """
        url = f'https://real-time-amazon-data.p.rapidapi.com/product-offers'
        headers = {
            'x-rapidapi-key': '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            'country': country,
            'asin': asin,
            'limit': limit,
            'page': page
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    # Usage example:
if __name__ == "__main__":
    po = ProductOffers("your_rapidapi_key_here", "real-time-amazon-data.p.rapidapi.com")
    result = po.product_offers("B09SM24S8C")
    print(result)