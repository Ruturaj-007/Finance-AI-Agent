from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

BASE_URL = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/quote"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com",
}

def get_stock_price(ticker : str):
    params = {
        "ticker" : ticker,
        "type" : "STOCKS"
    }

    response = requests.get(BASE_URL, headers = HEADERS, params = params)

    data = response.json()
    return data