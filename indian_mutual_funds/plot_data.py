import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mftool import Mftool
import datetime as dt
import argparse
import os
import threading

def plot_file(filepath, plot_dir, scheme_code, scheme_name):
    # Instead of using plt use figure to avoid conflicts in threads
    fig, ax = plt.subplots()
    df = pd.read_csv(filepath)
    df['nav'] = df['nav'].astype(float)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df = df.sort_values('date').reset_index(drop=True)
    df.plot(x='date', y='nav', title=scheme_name, ax=ax)
    plot_filepath = os.path.join(plot_dir, f"{scheme_code}.png")
    # set gridlines in the plot
    ax.grid(True)
    fig.savefig(plot_filepath)
    print(f"Saved plot for {scheme_name} to {plot_filepath}")
    
def main(data_dir, plot_dir, scheme_mapping_file):
    # Load scheme mappings from JSON file
    import json
    try:
        with open(scheme_mapping_file, 'r') as json_file:
            scheme_mappings = json.load(json_file)
    except FileNotFoundError:
        print(f"Scheme mapping file not found: {scheme_mapping_file}")
        return

    # read all files in data_dir
    import os
    os.makedirs(plot_dir, exist_ok=True)

    threads = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".csv"):

            # create a thread for plotting each file
            scheme_code = filename.replace(".csv", "")
            scheme_name = scheme_mappings.get(scheme_code, "Unknown Scheme")
            thread = threading.Thread(target=plot_file, args=(os.path.join(data_dir, filename), plot_dir, scheme_code, scheme_name))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

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
  parser = argparse.ArgumentParser(description="Mutual Fund Data Plotting")
  parser.add_argument("-D", "--data-dir", type=str, help="Directory to store data files", default="/tmp/indian_mutual_funds")
  # argument for scheme code mapping json file
  parser.add_argument("-S", "--scheme-mapping-file", type=str, help="Filepath for scheme code mapping JSON file", required=True)
  parser.add_argument("-P", "--plot-dir", type=str, help="Directory to store plot files", default="/tmp/indian_mutual_funds/plots")
  args = parser.parse_args()

  main(args.data_dir, args.plot_dir, args.scheme_mapping_file)
