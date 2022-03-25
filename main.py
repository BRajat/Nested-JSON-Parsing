"""Fetch and extract JSON data from Google Maps."""
import requests

from extract import json_extract

def google_maps_distance():
    """Fetch distance between two points."""
    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
       'units': 'imperial',
       'key': API_KEY,                         # API_KEY not available
       'origins': 'New York City, NY',
       'destinations': 'Philadelphia,PA',
       'transit_mode': 'car'
    }
    r = requests.get(endpoint, params=params)
    return r.json()


