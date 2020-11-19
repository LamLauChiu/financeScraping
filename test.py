"""
On macOS and Linux:
- Creating a virtual environment:
python3 -m venv virtualEnvironment

- Activating a virtual environment:
source virtualEnvironment/bin/activate

- Install the lists of requirements:
pip install -r config/requirements.txt
"""
#import yfinance as yf
from yahooquery import Ticker
aapl = Ticker('aapl')

print(aapl.summary_detail)
print(aapl.all_financial_data())
aapl.all_financial_data().to_csv('Result.csv')

