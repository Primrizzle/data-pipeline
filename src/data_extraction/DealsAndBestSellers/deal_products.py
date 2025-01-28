import requests

class DealProducts:
    def __init__(self, api_key, api_host):
        """
        Initializes the ProductDetails class with necessary API configuration.

        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host

    def deal_products(self, country='US', sort_by='FEATURED', page=1):
        """
        Retrieves the best sellers of a product category on Amazon.

        :param country: str - Country/Marketplace to search in.
        :param sort_by: str - The sorting of the products.
        :param page: int - The page number of the products.
        :return: dict - The JSON response from the API.
        """
        url = f'https://real-time-amazon-data.p.rapidapi.com/deal-products'
        headers = {
            'x-rapidapi-key': '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            'country': country,
            'sort_by': sort_by,
            'page': page
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()
# Usage example:
if __name__ == "__main__":
    dp = DealProducts("7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2", "real-time-amazon-data.p.rapidapi.com")
    result = dp.deal_products()
    print(result)
