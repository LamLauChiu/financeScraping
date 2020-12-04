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

symbol = '9988.HK'
stock = Ticker(symbol)

print("P/E Ratio Worked")
print(stock.key_stats[symbol])

print(stock.summary_detail)
print(stock.earning_history)
print(stock.earnings)
print(stock.index_trend)

types = ['PeRatio']
#print(stock.get_financial_data(types, trailing=False)['PeRatio'])

trailingPE = stock.summary_detail[symbol]['trailingPE']
print("trailingPE:",stock.summary_detail[symbol]['trailingPE'])
print("forwardPE:",stock.summary_detail[symbol]['forwardPE'])

#PERatio = stock.index_trend[symbol]['peRatio']
#print(PERatio)

trailingEps = stock.key_stats[symbol]['trailingEps']
print(trailingEps)
forwardEps = stock.key_stats[symbol]['forwardEps']
print(forwardEps)
# print(stock.all_financial_data())
# stock.all_financial_data().to_csv('Result.csv')

PERatioWorked = trailingPE * trailingEps
ForwardPERatioWorked = trailingPE * forwardEps
print(PERatioWorked)
print(ForwardPERatioWorked)
