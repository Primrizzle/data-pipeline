import requests

class ProductReviews:
    def __init__ (self, api_key, api_host):
        """
        Initializes the ProductReviews class with necessary API configuration.

        :param api_key: str - The API key for authentication.
        :param api_host: str - The host URL for the API.
        """
        self.api_key = api_key
        self.api_host = api_host

    def product_reviews(self, asin='B07ZPKN6YR', country='US', sort_by='TOP_REVIEWS', star_rating='ALL', verified_purchases_only='false', images_or_videos_only='false', current_format_only='false', page=1):
        """
        Retrieves the reviews of a product on Amazon based on its ASIN.

        :param asin: str - The ASIN of the product.
        :param country: str - Country/Marketplace to search in.
        :param sort_by: str - Sorting method of the reviews.
        :param star_rating: str - Filter reviews by star rating.
        :param verified_purchases_only: str - Filter reviews by verified purchases.
        :param images_or_videos_only: str - Filter reviews by images or videos.
        :param current_format_only: str - Filter reviews by current format only.
        :param page: str - Page number for pagination support.
        :return: dict - The JSON response from the API.
        """
        url = f"https://real-time-amazon-data.p.rapidapi.com/product-reviews"
        headers = {
            "x-rapidapi-key": '7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2',
            "x-rapidapi-host": 'real-time-amazon-data.p.rapidapi.com'
        }
        params = {
            "country": country,
            "asin": asin,
            "sort_by": sort_by,
            "star_rating": star_rating,
            "verified_purchases_only": verified_purchases_only,
            "images_or_videos_only": images_or_videos_only,
            "current_format_only": current_format_only,
            "page": page
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()  # Return the parsed JSON data
# Usage example:
if __name__ == "__main__":
    pr = ProductReviews("7ac802826emsh5fb7ad718ea78c9p121460jsncd71237a35b2", "real-time-amazon-data.p.rapidapi.com")
    result = pr.product_reviews("B07ZPKN6YR")  # Make sure the ASIN is correct and relevant
    print(result)
