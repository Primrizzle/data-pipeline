import requests 

class InfluencerPostProducts: 
    def __init__(self, api_key, api_host): 
        """ Initializes the InfluencerPostProducts class with the influencer_id of the influencer.
        
        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host

    def influencer_postproducts(self, influencer_name='tastemade', post_id='amzn1.ideas.382NVFBNK3GGQ'):
        """ Retrieves the products of an influencer on Amazone based on its influencer_name.
        
        :param influencer_name: str - The influencer_name of the influencer.
        :param post_id: str - The post_id of the influencer.
        :return: dict - The JSON response from the API.
        """
        url = f'https://real-time-amazon-data.p.rapidapi.com/influencer-post-products'
        headers = {
            'x-rapidapi-key': '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            'influencer_name': influencer_name,
            'post_id': post_id
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
# Usage example:
if __name__ == '__main__':
    ip = InfluencerPostProducts('7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2', 'real-time-amazon-data.p.rapidapi.com')
    result = ip.influencer_postproducts('tastemade', 'amzn1.ideas.382NVFBNK3GGQ')
    print(result)