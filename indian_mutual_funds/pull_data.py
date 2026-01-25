import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mftool import Mftool
import datetime as dt

def main():
  print ("Hello world")

  #mf = Mftool()
  #result = mf.get_available_schemes('hdfc')
  #for scheme_code, scheme in result.items():
  #  print(scheme_code, scheme)

  #mf = Mftool()
  #mutual_fund_code = "101762"
  #d1 = mf.get_scheme_quote(mutual_fund_code)
  #d2 = mf.get_scheme_details(mutual_fund_code)

  #print (d1)
  #print (d2)

  #df = mf.get_scheme_historical_nav(mutual_fund_code, as_Dataframe=True).reset_index()
  #df.to_csv("/tmp/mf.csv", index=False)

  df = pd.read_csv("/tmp/mf.csv")

  df['nav'] = df['nav'].astype(float)
  df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
  startDate = dt.datetime(2023, 1,  1)
  df = df[df['date'] > startDate]
  
  df = df.sort_values('date').reset_index(drop=True)
  df.plot(x='date', y='nav')
  plt.title("mutual_fund")
  plt.savefig("mf.png")

if __name__ == "__main__":
  main()
