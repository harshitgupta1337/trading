import yfinance as yf
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import datetime

now = datetime.datetime.now()
start_day = now + datetime.timedelta(days=-600)
next_day = now + datetime.timedelta(days=1)
start_date = datetime.date.strftime(start_day, '%Y-%m-%d')
end_date = datetime.date.strftime(next_day, '%Y-%m-%d')

# Set the ticker
TICKERS = ["HLT"]
#TICKERS = ["F", "GOOGL", "GOOG", "NFLX", "KO"]
#TICKERS = ["FDX", "SBUX", "DT", "FDX", "UPS", "XLNX", "AMZN", "AMD",  "INTC", "PYPL", 'NET', "GSAT", "NVDA", "OCGN", "GE", "GM"]

plt.minorticks_on()
for ticker in TICKERS:
    # Get the data
    data = yf.download(ticker, start_date, end_date)
    df = data
    df.to_csv("data/%s.csv"%ticker)
    df = pd.read_csv("data/%s.csv"%ticker)
    
    long_rolling = df["Adj Close"].rolling(window=100).mean()
    short_rolling = df["Adj Close"].rolling(window=20).mean()
    
    plt.close()
    fig, ax = plt.subplots(figsize=(32,8))
   
    candidate_xticks = []
    for idx, row in df.iterrows():
        candidate_xticks.append((idx, str(row["Date"])))
    idx = len(candidate_xticks)-1
    xticks = []
    while idx >= 0:
        xticks.append(candidate_xticks[idx])
        idx -= 7
    xtick_positions = [x[0] for x in xticks]
    xtick_labels = [x[1] for x in xticks]
 
    up =df[df["Close"]>=df["Open"]]
    down =df[df["Close"]<df["Open"]]
    
    col1 = 'green'
    col2 = 'red'
    width = 1
    width2 = 0.2
    
    #plot up prices
    ax.bar(up.index,up["Close"]-up["Open"],width,bottom=up["Open"],color=col1)
    ax.bar(up.index,up["High"]-up["Close"],width2,bottom=up["Close"],color=col1)
    ax.bar(up.index,up["Low"]-up["Open"],width2,bottom=up["Open"],color=col1)
    
    #plot down prices
    ax.bar(down.index,down["Close"]-down["Open"],width,bottom=down["Open"],color=col2)
    ax.bar(down.index,down["High"]-down["Open"],width2,bottom=down["Open"],color=col2)
    ax.bar(down.index,down["Low"]-down["Close"],width2,bottom=down["Close"],color=col2)
    
    #rotate x-axis tick labels
    plt.xticks(rotation=45, ha='right')
    ax.set_xticks(xtick_positions)
    ax.set_xticklabels(xtick_labels)
    
    ax.plot(df.index, short_rolling.to_list(), label="20-day SMA")
    ax.plot(df.index, long_rolling.to_list(), label="100-day SMA")
    ax.grid()
    ax.legend()
    ax.set_title(ticker, fontsize=20)
    fig.savefig("%s.png"%ticker, bbox_inches="tight")	
