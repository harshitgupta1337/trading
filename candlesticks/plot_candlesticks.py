import yfinance as yf
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Set the start and end date
start_date = '2020-01-01'
end_date = '2022-02-03'
# Set the ticker
TICKERS = ["F", "GOOGL", "GOOG", "NFLX", "KO"]
#TICKERS = ["FDX", "SBUX", "DT", "FDX", "UPS", "XLNX", "AMZN", "AMD",  "INTC", "PYPL", 'NET', "GSAT", "NVDA", "OCGN", "GE", "GM"]

plt.minorticks_on()
for ticker in TICKERS:
	# Get the data
	data = yf.download(ticker, start_date, end_date)
	
	# Print 5 rows
	df = data
	df.to_csv("data/%s.csv"%ticker)
	
	long_rolling = df["Adj Close"].rolling(window=100).mean()
	short_rolling = df["Adj Close"].rolling(window=20).mean()
	
	plt.close()
	fig, ax = plt.subplots(figsize=(24,8))
	ax.plot(range(len(df)), df.loc[:, "Adj Close"], label="Price")
	ax.plot(range(len(df)), short_rolling.to_list(), label="20-day SMA")
	ax.plot(range(len(df)), long_rolling.to_list(), label="100-day SMA")
	ax.grid()
	ax.legend()
	ax.set_title(ticker, fontsize=20)
	fig.savefig("%s.png"%ticker, bbox_inches="tight")	
