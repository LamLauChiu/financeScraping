# financeScraping

https://yahooquery.dpguthrie.com/guide/ticker/premium/#p_all_financial_data

https://pypi.org/project/yfinance/

from yahooquery import Ticker
aapl = Ticker('aapl')

print(aapl.summary_detail)
print(aapl.all_financial_data())
aapl.all_financial_data().to_csv('Result.csv')
