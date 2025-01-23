import requests

class ProductCategories:
    def __init__(self, api_key, api_host):
        """
        Initializes the ProductCategories class with necessary API configuration.

        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host
    def product_categories(self, category_id = "247886801", page=1, country="US", sort_by='RELEVANCE', product_condition='ALL', is_prime='false', deals_and_discounts='NONE'):
        """
        Searches for products on Amazon based on various parameters.

        :param category_id: str - Category ID for the products.
        :param page: str - Page number for pagination support.
        :param country: str - Country/Marketplace to search in.
        :param sort_by: str - Sorting method of the results.
        :param product_condition: str - Condition of the products to include.
        :param is_prime: str - Whether to filter for Amazon Prime products.
        :param deals_and_discounts: str - Deals and discounts filter.
        :return: dict - The JSON response from the API.
        """
        url = "https://real-time-amazon-data.p.rapidapi.com/products-by-category"
        headers = {
            "x-rapidapi-key": '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            "x-rapidapi-host": 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            "category_id": category_id,
            "page": page,
            "country": country,
            "sort_by": sort_by,
            "product_condition": product_condition,
            "is_prime": is_prime,
            "deals_and_discounts": deals_and_discounts
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
# Usage example:
if __name__ == "__main__":
    pc = ProductCategories("your_rapidapi_key_here", "real-time-amazon-data.p.rapidapi.com")
    result = pc.product_categories()
    print(result)   