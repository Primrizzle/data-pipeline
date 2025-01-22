import requests
from requests.exceptions import HTTPError

class APIClient:
    def __init__(self):
        """Initializes the API client with the necessary base URL and API key."""
        self.base_url = "https://real-time-amazon-data.p.rapidapi.com/influencer-post-products"
        self.headers = {
            'X-RapidAPI-Key': '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            'X-RapidAPI-Host': 'real-time-amazon-data.p.rapidapi.com'
        }

    def get_data(self, params=None):
        """
        Sends a GET request to the API with optional parameters.
        
        :param params: dict - Optional parameters for the GET request.
        :return: dict - The JSON response from the API.
        """
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None

# Usage example:
if __name__ == "__main__":
    client = APIClient()
    params = {"influencer_name": "madison.lecroy", "post_id": "amzn1.ideas.382NVFBNK3GGQ"}
    data = client.get_data(params)
    print(data)
