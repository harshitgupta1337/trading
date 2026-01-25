import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mftool import Mftool
import datetime as dt
import argparse

def main(schemes_code_filepath, num_last_days, data_dir):
  # Check if scheme codes file exists
  try:
    with open(schemes_code_filepath, 'r') as file:
      scheme_codes = [line.strip() for line in file.readlines()]
  except FileNotFoundError:
    print(f"Scheme codes file not found: {schemes_code_filepath}")
    return

  # Create the data_dir
  import os
  os.makedirs(data_dir, exist_ok=True)

  # Create a set of threads to fetch data concurrently
  import threading
  def fetch_and_save_data(scheme_code):
    mf = Mftool()
    try:
      df = mf.get_scheme_historical_nav(scheme_code, as_Dataframe=True).reset_index()
      df['nav'] = df['nav'].astype(float)
      df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
      startDate = dt.datetime.now() - dt.timedelta(days=num_last_days)
      df = df[df['date'] > startDate]
      df = df.sort_values('date').reset_index(drop=True)
      filepath = os.path.join(data_dir, f"{scheme_code}.csv")
      df.to_csv(filepath, index=False)
      print(f"Saved data for scheme code {scheme_code} to {filepath}")
    except Exception as e:
      print(f"Error fetching data for scheme code {scheme_code}: {e}")

  threads = []
  for scheme_code in scheme_codes:
    thread = threading.Thread(target=fetch_and_save_data, args=(scheme_code,))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

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

  # df = pd.read_csv("/tmp/mf.csv")

  # df['nav'] = df['nav'].astype(float)
  # df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
  # startDate = dt.datetime(2023, 1,  1)
  # df = df[df['date'] > startDate]
  
  # df = df.sort_values('date').reset_index(drop=True)
  # df.plot(x='date', y='nav')
  # plt.title("mutual_fund")
  # plt.savefig("mf.png")

if __name__ == "__main__":
  # Use argparse to handle command-line args
  parser = argparse.ArgumentParser(description="Mutual Fund Data Download")
  parser.add_argument("-S", "--scheme-codes-filepath", type=str, help="Path to scheme codes file", required=True)
  parser.add_argument("-N", "--num-last-days", type=int, help="Number of days to look back", default=180)
  parser.add_argument("-D", "--data-dir", type=str, help="Directory to store data files", default="/tmp/indian_mutual_funds")
  args = parser.parse_args()

  main(args.scheme_codes_filepath, args.num_last_days, args.data_dir)
