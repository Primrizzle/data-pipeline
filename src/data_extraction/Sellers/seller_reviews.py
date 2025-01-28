import requests

class SellerReviews:
    def __init__ (self, api_key, api_host):
        """ Initializes the SellerProfile class with the seller_id of the seller."""
        self.api_key = api_key
        self.api_host = api_host

    def seller_reviews(self, seller_id='A02211013Q5HP3OMSZC7W', country='US', star_rating='ALL', page=1):
        """ Retrieves the reviews of a seller on Amazone based on its seller_id.
    
        :param seller_id: str - The seller_id of the seller.
        :param country: str - Country/Marketplace to search in.
        :param star_rating: str - The star rating of the reviews.
        :param page: int - The page number of the reviews.
        :return: dict - The JSON response from the API.
        """
        url = f'https://real-time-amazon-data.p.rapidapi.com/seller-reviews'
        headers = {
            'x-rapidapi-key': '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            'country': country,
            'seller_id': seller_id,
            'star_rating': star_rating,
            'page': page
        }
        response = requests.get(url, headers=headers, params=params)    
        response.raise_for_status()
        return response.json()
# Usage example:
if __name__ == '__main__':
    sr = SellerReviews('7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2', 'real-time-amazon-data.p.rapidapi.com')
    result = sr.seller_reviews('A02211013Q5HP3OMSZC7W')
    print(result)