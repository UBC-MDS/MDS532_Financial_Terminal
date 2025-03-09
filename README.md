# MDS532 Financial Terminal

## Author

Ke Gao (kegao1995@gmail.com)

## Project Overview

MDS532 Financial Terminal is a desktop tool for financial data analysis, real-time stock market queries, and related information display. This project aims to provide users with an efficient and intuitive financial data terminal solution.

[https://financial-terminal.streamlit.app/](https://financial-terminal.streamlit.app/)

## Features

This application is a financial data visualization tool primarily focused on **Treasury Yield Curve Analysis** and **US Stock Return Analysis**, suitable for investors, analysts, and financial researchers.

1. **Treasury Yield Curve Analysis**:

   - Allows users to select countries (e.g., USA, Canada, China).
   - Displays yield curves for different maturities in line charts.
   - Provides comparisons of current yield, yield one month ago, and yield one year ago to analyze yield curve trends.
2. **US Stock Return Comparison**:

   - Allows users to select time ranges (e.g., 2024-01-01 to 2025-03-09).
   - Allows users to select multiple stocks (e.g., AAPL, MSFT, NVDA).
   - Displays cumulative returns of selected stocks over the time range in line charts.
   - Provides key performance indicators table, including:
     - **Cumulative Return**
     - **Annualized Return**
     - **Max Drawdown**
     - **Calmar Ratio**
     - **Annualized Volatility**
     - **Sharpe Ratio**
3. **Interactive Features**:

   - **Dynamic Country Selection**: Switch between yield curves of different countries.
   - **Custom Time Range**: Adjust the time range for stock return analysis.
   - **Stock Code Selection**: Select multiple stocks for return comparison analysis.

## Installation

1. Clone the project code:
   ```
   git clone https://github.com/UBC-MDS/MDS532_Financial_Terminal.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the application:
   ```
   streamlit run src/pages/Index.py --server.port 8501
   ```
4. Open the webpage:
   ```
   http://localhost:8501
   ```

## Usage

- After starting the application, you can view real-time market data on the main interface.
- Use the sidebar to switch between different data views, such as historical charts, indicator analysis, etc.
- For detailed usage instructions, please refer to the project documentation or the built-in help feature.

## Video Walkthrough

![Video Walkthrough](img/demo.mp4)

## Contribution Guidelines

We welcome contributions to this project. If you have new feature suggestions or find any issues, please contact us via Issue or Pull Request:

## License

This project is licensed under the GNU AGPL 3.0 License. Please see the [LICENSE](./LICENSE) file for more details.

## Contact

If you have any questions or suggestions, please contact Ke Gao (kegao1995@gmail.com).
