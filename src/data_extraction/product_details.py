import requests

class ProductDetails:
    def __init__(self, api_key, api_host):
        """
        Initializes the ProductDetails class with necessary API configuration.

        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host

    def get_product_details(self, asin='B07ZPKBL9V', country='US'):
        """
        Retrieves the details of a product on Amazon based on its ASIN.

        :param asin: str - The ASIN of the product.
        :param country: str - Country/Marketplace to search in.
        :return: dict - The JSON response from the API.
        """
        url = f"https://real-time-amazon-data.p.rapidapi.com/product-details"
        headers = {
            "x-rapidapi-key": '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            "x-rapidapi-host": 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            "country": country,
            "asin": asin
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()
# Usage example:
if __name__ == "__main__":
    pd = ProductDetails("your_rapidapi_key_here", "real-time-amazon-data.p.rapidapi.com")
    result = pd.get_product_details("B07ZPKBL9V")
    print(result)