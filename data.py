from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

BASE_URL = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/quote"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,                           
    "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com", # Which API we're exactly calling
}

def get_stock_price(ticker : str):
    params = {                      # query parameters
        "ticker" : ticker,
        "type" : "STOCKS"
    }

    response = requests.get(BASE_URL, headers = HEADERS, params = params)

    data = response.json()
    return data

def extract_price(data: dict):
    try:
        body =  data.get("body", {})
        primary = body.get("primaryData", {})

        return {
            "company" : body.get("companyName", "N/A"),
            "price" : primary.get("lastSalePrice", "N/A"),
            "change" : primary.get("netChange", "N/A"),
            "change_pct" : primary.get("percentageChange", "N/A"),
            "volume" : primary.get("volume", "N/A")
        }
    except Exception as e:
        return {
            "Error extracting price" : str(e)
        }

def get_company_profile(ticker: str):
    url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules"

    params = {
        "ticker" : ticker,
        "module" : "asset-profile"
    }

    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def extract_profile(data: dict):
    try:
        body = data.get("body", {})

        return {
            "sector" : body.get("sector", "N/A"),
            "industry" : body.get("industry", "N/A"),
            "country" : body.get("country", "N/A"),
            "employees" : body.get("fullTimeEmployees", "N/A"),
            "website" : body.get("website", "N/A") 
        }
    
    except Exception as e:
        return {
            "Error extracting profile" : str(e)
        }
