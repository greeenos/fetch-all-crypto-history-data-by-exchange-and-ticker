
# fetch-all-crypto-history-data-by-exchange-and-ticker

## Description

This project is designed to fetch historical cryptocurrency data for specified exchanges and tickers. It utilizes APIs from various cryptocurrency exchanges to gather historical trading data and store it locally for analysis and further use.

## Features
- Fetch historical data for multiple cryptocurrencies.
- Support for multiple exchanges.
- Easy configuration for specifying desired tickers and exchanges.
- Data storage in a structured format for easy access and analysis.

## Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.8 or later
- pip (Python package installer)
- Git

## Setup Guide

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```sh
git clone https://github.com/greeenos/fetch-all-crypto-history-data-by-exchange-and-ticker.git
cd fetch-all-crypto-history-data-by-exchange-and-ticker
```

### 2. Create a Virtual Environment (Optional but recommended)

Create a virtual environment to manage dependencies.

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages using pip.

```sh
pip install -r requirements.txt
```

### 4. Configure the Settings

Edit the settigns in main file to specify the exchanges and tickers you are interested in. Dont forget you can also change timeframe and start date of fetching.

For example:
```yaml
exchanges:
  - binance
  - coinbase
tickers:
  - BTC/USD
  - ETH/USD
timeframes:
  - 1m,5m,15m,30m
  - 1h,4h
  - D,W
```

### 5. Run the Script

Once you have configured the settings, you can run the script to fetch the data.

```sh
python gethistoricaldata.py 
```

### 6. Access the Data

The fetched data will be stored in the specified directory in the configuration file. You can access and analyze it using your preferred data analysis tools.

## Troubleshooting

- **ModuleNotFoundError**: Ensure all dependencies are installed correctly. Run `pip install -r requirements.txt` again.
- **API Limitations**: Be aware of the rate limits imposed by different exchanges. You might need API keys for higher rate limits.
- **Configuration Issues**: Double-check your configuration file for any syntax errors or incorrect values.

## Contribution

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's style guidelines and includes appropriate tests.

## Support
Any support is highly appreciated https://buymeacoffee.com/greeenos
Solana: ETTSLqMB4FAFLUM5k1ieYDD3W1CdkiiFCT2oW7yP5YXs
BTC (segwit): bc1q28e85w6m47hk5fux3y2nkzgpr2v4t3fukgp53l
Polygon: 0x530f7b2219Bb58cfDf328F17F4CD0417f9cD0117

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/greeenos/fetch-all-crypto-history-data-by-exchange-and-ticker/blob/main/LICENSE) file for details.
```
