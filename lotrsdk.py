import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv


# Getting variables from env
dotenv_path = join(dirname(__file__), 'prod.env')
load_dotenv(dotenv_path)
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
BASE_URL_MOVIE = os.environ.get('BASE_URL_MOVIE')


# Get all movies with details
def get_movies():

    headers = {'Authorization' : 'Bearer ' + ACCESS_TOKEN}
    response = requests.get(BASE_URL_MOVIE,headers=headers)
    print(response.text)

# Get a details from one specific movie
def get_one_movie(id):
    
    headers = {'Authorization' : 'Bearer ' + ACCESS_TOKEN}
    response = requests.get(f"{BASE_URL_MOVIE}/{id}",headers=headers)
    print(response.text)

# get all quotes from one movie - Only works for the thrilogy
def get_quote_fom_movie(id):
    
    headers = {'Authorization' : 'Bearer ' + ACCESS_TOKEN}
    response = requests.get(f"{BASE_URL_MOVIE}/{id}/quote",headers=headers)
    print(response.text)

# get_quote_fom_movie('5cd95395de30eff6ebccde5c')

# 5cd95395de30eff6ebccde5c fellowship of the ring