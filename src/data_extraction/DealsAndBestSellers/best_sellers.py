import requests

class BestSellers:
    def __init__(self, api_key, api_host):
        """
        Initializes the ProductDetails class with necessary API configuration.

        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host

    def best_sellers(self, category='software', type='BEST_SELLERS', page=1, country='US'):
        """
        Retrieves the best sellers of a product category on Amazon.

        :param category: str - The category of the product.
        :param type: str - The type of the best sellers.
        :param page: int - The page number of the best sellers.
        :param country: str - Country/Marketplace to search in.
        :return: dict - The JSON response from the API.
        """
        url = f"https://real-time-amazon-data.p.rapidapi.com/best-sellers"
        headers = {
            "x-rapidapi-key": '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            "x-rapidapi-host": 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            "category": category,
            "type": type,
            "page": page,
            "country": country,
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()
# Usage example:
if __name__ == "__main__":
    bs = BestSellers("7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2", "real-time-amazon-data.p.rapidapi.com")
    result = bs.best_sellers("software")
    print(result)
