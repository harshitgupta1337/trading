# Prerequisites
1. Create a Python virtual environment using `python3 -m venv ./venv`.
2. Activate the virtual environment using `source ./venv/bin/activate`.
3. Install the required packages from `requirements.txt` using the command `pip3 install -r requirements.txt`.
4. Install `apt-get install imagemagick-6.q16`. Edit the file `/etc/ImageMagick-6/policy.xml` and the following line to it.

```xml
<policy domain="coder" rights="read | write" pattern="PDF" />
```

# Steps to use this repo
1. Populate the tickers in a file in `tickers/` folder.
2. Run the following script.

```bash
./candlesticks/plot_multi_charts.sh ./tickers/<file-containing-tickers>
```

3. The output plots are located in the `plots/` directory. You can combine them into 1 PDF file using the script `./merge-pdfs.sh`.
