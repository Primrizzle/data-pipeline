import requests

class PromocodeDetails: 
    def __init__ (self, api_key, api_host):
        """ Initializes the PromocodeDetails class with the promo_code of the seller.
        
        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host
    
    def promocode_details(self, promo_code='AZDIA7AYE39P2', country='US'):
        """ Retrieves the details of a promo code on Amazon based on its promo_code.
        
        :param promo_code: str - The promo_code of the seller.
        :param country: str - Country/Marketplace to search in.
        :return: dict - The JSON response from the API.
        """
    
        url = f"https://real-time-amazon-data.p.rapidapi.com/promo-code-details"
        headers = {
        'x-rapidapi-key': '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
        'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
        'country': country,
        'promo_code': promo_code
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
# Usage example:
if __name__ == '__main__':
    pc = PromocodeDetails('7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2', 'real-time-amazon-data.p.rapidapi.com')
    result = pc.promocode_details('AZDIA7AYE39P2')
    print(result)
    