# Resource Allocation and Budget Tracking Dashboard

A comprehensive dashboard for tracking project resources, budgets, and performance metrics using real financial market data.

## Features

- Real-time financial data integration
- Resource allocation tracking
- Budget monitoring and forecasting
- Project performance metrics
- Agile sprint tracking
- Interactive dashboard
- Executive summary

## Directory Structure
```
resource-dashboard/
│
├── src/
│   ├── __init__.py
│   ├── data_downloader.py
│   ├── excel_generator.py
│   └── utils.py
│
├── notebooks/
│   └── Resource_Budget_Dashboard.ipynb
│
├── tests/
│   ├── __init__.py
│   ├── test_data_downloader.py
│   └── test_excel_generator.py
│
├── data/
│   └── README.md
│
├── docs/
│   ├── setup.md
│   └── usage.md
│
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/resource-dashboard.git
cd resource-dashboard
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Local Python Script
```bash
python src/excel_generator.py
```

### Google Colab
1. Open `notebooks/Resource_Budget_Dashboard.ipynb` in Google Colab
2. Run all cells in sequence
3. Download the generated Excel file

## Data Sources

- Real-time stock market data via yfinance
- Derived metrics for:
  - Resource allocation
  - Project tracking
  - Budget management
  - Performance analysis

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)
Project Link: [https://github.com/yourusername/resource-dashboard](https://github.com/yourusername/resource-dashboard)
