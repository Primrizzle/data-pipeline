import requests

class Deals:
    def __init__(self, api_key, api_host):
        """
        Initializes the ProductDetails class with necessary API configuration.

        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host

    def deals(self, country='US', min_product_star_rating='ALL', price_range='ALL', discount_range='ALL'):
        """
        Retrieves the best sellers of a product category on Amazon.

        :param country: str - Country/Marketplace to search in.
        :param min_product_star_rating: str - The minimum star rating of the product.
        :param price_range: str - The price range of the product.
        :param discount_range: str - The discount range of the product.
        :return: dict - The JSON response from the API.
        """

        url = f'https://real-time-amazon-data.p.rapidapi.com/deals-v2'
        headers = {
            'x-rapidapi-key': '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            'country': country,
            'min_product_star_rating': min_product_star_rating,
            'price_range': price_range,
            'discount_range': discount_range
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()
# Usage example:
if __name__ == "__main__":
    d = Deals("7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2", "real-time-amazon-data.p.rapidapi.com")
    result = d.deals()
    print(result)
