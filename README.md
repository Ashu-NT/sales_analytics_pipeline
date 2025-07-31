# Sales Analytics Pipeline

This project is a modular and extensible data pipeline for sales analytics, built with Python and PostgreSQL. It is designed to extract, transform, validate, and visualize sales data, providing actionable insights for business decision-making.

## Features
- **Data Extraction:** Ingests raw sales data from CSV files or databases.
- **Data Transformation:** Cleans, processes, and enriches data for analysis.
- **Data Validation:** Ensures data quality and integrity before loading.
- **Database Handling:** Interacts with PostgreSQL for data storage and retrieval.
- **Visualization:** Generates insightful charts and reports.
- **Logging:** Tracks pipeline execution and errors for debugging and auditing.

## Project Structure
```
├── data/
│   ├── raw/            # Raw input data (e.g., sales_data.csv)
│   └── processed/      # Processed/cleaned data
├── logs/               # Pipeline logs
├── src/
│   ├── components/     # Core components (db_handler, exception, visualizer)
│   └── pipeline/       # Pipeline stages (extract, transform, validate, run_pipeline)
├── requirements.txt    # Python dependencies
├── setup.py            # Project setup script
├── LICENSE
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL database

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd sales_analytics_pipeline
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure your PostgreSQL connection in `src/config.py`.

### Usage
1. Place your raw sales data in `data/raw/sales_data.csv`.
2. Run the pipeline:
   ```sh
   python src/pipeline/run_pipeline.py
   ```
3. Check processed data in `data/processed/` and logs in `logs/pipeline.log`.

### Customization
- Modify or extend pipeline stages in `src/pipeline/` as needed.
- Add new visualizations in `src/components/visualizer.py`.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.
