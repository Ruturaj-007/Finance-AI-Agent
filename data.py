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

def build_final_data(ticker: str):
    price_raw = get_stock_price(ticker)
    profile_raw = get_company_profile(ticker)

    price = extract_price(price_raw)
    profile = extract_profile(profile_raw)

    return {
        "ticker": ticker.upper(),
        "company": price.get("company"),
        "price_data": price,
        "profile_data": profile
    }

def prepare_for_ai(final: dict):
    return {
        "ticker": final["ticker"],
        "company": final["company"],
        "price": final["price_data"]["price"],
        "change_pct": final["price_data"]["change_pct"],
        "volume": final["price_data"]["volume"],
        "sector": final["profile_data"]["sector"],
        "industry": final["profile_data"]["industry"]
    }