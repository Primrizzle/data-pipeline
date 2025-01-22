# Module to fetch data using the API client

import requests
import json
import os
import sys
import logging
from datetime import datetime
from src.data_extraction.api_client import APIClient

class DataFetcher:
    def __init__(self, api_client):
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)

    def fetch_data(self, start_date, end_date, data_type):
        """
        Fetch data from the API client for the given date range and data type
        :param start_date: Start date of the data range
        :param end_date: End date of the data range
        :param data_type: Type of data to be fetched
        :return: Data fetched from the API client
        """
        data = self.api_client.get_data(start_date, end_date, data_type)
        return data

    def save_data(self, data, file_path):
        """
        Save the data fetched from the API client to a file
        :param data: Data fetched from the API client
        :param file_path: Path to save the data
        """
        with open(file_path, 'w') as file:
            json.dump(data, file)
        self.logger.info(f'Data saved to {file_path}')

    def fetch_and_save_data(self, start_date, end_date, data_type, file_path):
        """
        Fetch data from the API client for the given date range and data type and save it to a file
        :param start_date: Start date of the data range
        :param end_date: End date of the data range
        :param data_type: Type of data to be fetched
        :param file_path: Path to save the data
        """
        data = self.fetch_data(start_date, end_date, data_type)
        self.save_data(data, file_path)
        self.logger.info(f'Data fetched and saved successfully')