from flask import Flask, jsonify

from bs4 import BeautifulSoup
import requests

def get_currency_rate(from_currency, to_currency):
    """Fetches the currency conversion rate using web scraping."""
    url = f'https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        rate_element = soup.find("span", class_="ccOutputRslt")
        if rate_element:
            return float(rate_element.get_text()[:-4])  # Remove trailing currency symbol
        else:
            return None  # Rate not found on the page
    except requests.exceptions.RequestException as e:
        print(f"Error fetching currency rate: {e}")
        return None

app = Flask(__name__, static_url_path='/static')  # Set static folder path

@app.route('/')
def home():
    """Displays a simple home page."""
    return app.send_static_file('index.html')  # Serve index.html from static folder

@app.route('/api/v1/<from_currency>-<to_currency>')
def get_rate(from_currency, to_currency):
    """Retrieves the currency rate and returns it as JSON."""
    rate = get_currency_rate(from_currency, to_currency)
    if rate is None:
        return jsonify({'error': 'Currency rate not found'}), 404  # Return error for missing rate
    result = {
        'input_currency': from_currency.upper(),
        'output_currency': to_currency.upper(),
        'rate': rate
    }
    return jsonify(result)

if __name__ == '__main__':
    # Remove app.run for GitHub Pages deployment
    pass  # Comment out this line
