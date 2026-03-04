from dotenv import load_dotenv
load_dotenv()
import requests
import os

API_KEY = os.getenv("API_KEY")
URL_GET = 'https://api.api-ninjas.com/v1/animals'

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """

    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}

    res = requests.get(URL_GET, params=params, headers=headers)
    res.raise_for_status()

    return res.json()
