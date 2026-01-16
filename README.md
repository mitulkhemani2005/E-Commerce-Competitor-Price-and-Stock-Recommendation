# Flipkart Competitors: Automated E-Commerce Demand Forecasting & Price Recommendation System

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Latest-FF6B35?style=flat-square)](https://xgboost.readthedocs.io/)
[![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

**An end-to-end automated system that predicts next-day demand and optimizes pricing for e-commerce products using machine learning and revenue optimization algorithms.**

[Key Features](#-key-features) • [Architecture](#-system-architecture) • [Quick Start](#-quick-start) • [API Documentation](#-api-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Key Design Principle](#-key-design-principle)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [How It Works](#-how-it-works)
- [Why This Project Is Different](#-why-this-project-is-different)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This project implements a **production-grade automated system** for forecasting product demand and recommending optimal prices for e-commerce platforms. It combines real-world data ingestion, feature engineering, machine learning, automation, and deployment using industry-standard practices.

Unlike traditional approaches that predict prices directly, this system:
- **Predicts demand** using machine learning (XGBoost)
- **Optimizes pricing** using revenue simulation logic
- **Automates daily pipelines** for continuous predictions
- **Deploys with Docker & CI/CD** for scalability

---

## ⚠️ Problem Statement

E-commerce sellers face two recurring challenges:

1. **Demand Forecasting**: How many customers are likely to purchase a product tomorrow?
2. **Price Optimization**: What price should be set to maximize revenue?

Most pricing decisions are made heuristically and manually. This project **automates the entire process** using historical data, machine learning, and optimization algorithms.

---

## 🔑 Key Design Principle

> **Demand is predicted. Price is optimized.**

Price is treated as a **decision variable**, not a prediction target. The system simulates multiple pricing scenarios and selects the one that maximizes expected revenue.

---

## ✨ Key Features

- ✅ **Automated Daily Pipeline**: Scrapes data, cleans, engineers features, predicts demand, and saves results automatically
- ✅ **Time-Series Demand Forecasting**: Uses lagged and rolling features to capture temporal demand patterns
- ✅ **Revenue Optimization**: Simulates multiple price points to find the optimal price
- ✅ **Machine Learning**: XGBoost models with time-aware train-test splits (no data leakage)
- ✅ **FastAPI Layer**: RESTful API for serving predictions and recommendations
- ✅ **Production-Ready**: Docker containerization and GitHub Actions CI/CD pipeline
- ✅ **Real Data**: Continuously collected Flipkart product data
- ✅ **SQL Database**: Append-only historical records for full audit trail

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Daily Scheduler (Cron)                     │
│             (Windows Task Scheduler / Linux cron)            │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│               daily_pipeline.py                              │
│  (Orchestrates the entire ML workflow)                      │
└──────────┬────────────────────────────────┬─────────────────┘
           │                                │
    ┌──────▼────────┐                ┌─────▼──────────┐
    │   Data Layer  │                │   ML Layer     │
    ├───────────────┤                ├────────────────┤
    │ • Scraping    │                │ • Feature Eng. │
    │ • Cleaning    │                │ • XGBoost      │
    │ • Validation  │                │ • Prediction   │
    └──────┬────────┘                │ • Optimization │
           │                         └─────┬──────────┘
           │                               │
           └───────────────┬───────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  SQL Database │
                    └──────────────┘
                           │
           ┌───────────────┴───────────────┐
           │                               │
           ▼                               ▼
      ┌────────────┐              ┌──────────────┐
      │  FastAPI   │              │  Git Push    │
      │   Layer    │              │  CI/CD       │
      │(REST API)  │              │ Docker Build │
      └────────────┘              │  Docker Hub  │
                                  └──────────────┘
```

---

## 💻 Technology Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.8+ |
| **ML Framework** | XGBoost, Pandas, NumPy |
| **Web Framework** | FastAPI |
| **Database** | SQLite / PostgreSQL |
| **Containerization** | Docker |
| **CI/CD** | GitHub Actions |
| **Scheduling** | Windows Task Scheduler / cron |
| **Data Source** | Flipkart Web Scraping |

---

## 📁 Project Structure

```
flipkart_competitors/
├── app.py                          # FastAPI application
├── main.py                         # Entry point/main script
├── dockerfile                      # Docker configuration
├── package.json                    # Node.js dependencies (if applicable)
├── requirements.txt                # Python dependencies
├── project_steps.txt               # Project documentation & steps
├── daily_pipeline.py               # Automated daily workflow orchestrator
├── .github/
│   └── workflows/
│       └── ci-cd.yml               # GitHub Actions CI/CD pipeline
│
├── data/                           # Data directory
│   ├── create_db_schema.py         # Database schema initialization
│   ├── predict.csv                 # Prediction results
│   └── sales.db                    # SQLite database
│
├── model/                          # Trained ML models
│   ├── basemodel.py                # Base model architecture
│   ├── customer.pkl                # Serialized customer model
│   ├── encoder.pkl                 # Feature encoder
│   ├── scaler.pkl                  # Data scaler
│   ├── next_day_model_train.py     # Model training script
│   └── next_day_predict.py         # Model prediction script
│
├── notebooks/                      # Jupyter notebooks for analysis
│   ├── explanation.txt             # Analysis explanations
│   ├── sales.db                    # Analysis database
│   ├── sql_data_cleaning.ipynb     # SQL data cleaning notebook
│   ├── sql_database_setup.ipynb    # Database setup notebook
│   ├── temp_data.ipynb             # Temporary data analysis
│   └── web_scrap_data.ipynb        # Web scraping notebook
│
├── process/                        # Data & prediction processing scripts
│   ├── data_cleaning.py            # Data cleaning & validation
│   ├── predict_order.py            # Order/demand prediction logic
│   └── __pycache__/                # Python cache
│
└── __pycache__/                    # Python cache files
```

### Key Files Overview

- **app.py**: FastAPI application serving predictions via REST API
- **main.py**: Main entry point for running the application
- **daily_pipeline.py**: Orchestrates the complete ML workflow (scraping → cleaning → predicting)
- **next_day_model_train.py**: Trains the XGBoost model on historical data
- **next_day_predict.py**: Generates next-day demand predictions
- **data_cleaning.py**: Cleans and validates raw data
- **create_db_schema.py**: Sets up SQLite database schema
- **ci-cd.yml**: GitHub Actions workflow for automated testing & deployment

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip or conda
- (Optional) Docker for containerization

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mitulkhemani2005/flipkart_competitors.git
   cd flipkart_competitors
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database** (if needed)
   ```bash
   python scripts/setup_db.py
   ```

5. **Run the application**
   ```bash
   # Start FastAPI server
   uvicorn main:app --reload

   # Run the daily pipeline manually (optional)
   python daily_pipeline.py
   ```

### Docker Installation

1. **Build the Docker image**
   ```bash
   docker build -t flipkart_competitors:latest .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 flipkart_competitors:latest
   ```

---

## 📖 Usage

### Running the Daily Pipeline

The pipeline automatically runs on a schedule (configured via Task Scheduler). To manually trigger:

```bash
python daily_pipeline.py
```

**What it does:**
1. Scrapes latest product data from Flipkart
2. Cleans and validates the data
3. Engineers time-series features
4. Generates demand predictions
5. Recommends optimal prices
6. Saves results to the database

### Accessing the API

Once the FastAPI server is running, navigate to:
- **API Documentation**: `http://localhost:8000/docs`


---

## 🎓 How It Works

### 1. Data Ingestion (Daily)
- Scrapes Flipkart for product data including:
  - Original & selling prices
  - Discounts, ratings, stock status
  - Seller information, review counts
- Stores daily snapshots in SQL (append-only pattern)

### 2. ETL & Feature Engineering
- **Cleans** raw scraped data (handles missing values, outliers)
- **Computes demand proxy** using daily review growth
- **Engineers time-series features**:
  - `lag_1_review`: Previous day's reviews
  - `lag_2_review`: 2 days ago reviews
  - `rolling_3_day_average`: 3-day rolling average

### 3. Demand Forecasting (ML)
- **Model**: XGBoost Regressor
- **Target**: Next-day demand
- **Features**: Price, discount, ratings, seller info, temporal features
- **Validation**: Time-aware train-test splits (prevents data leakage)

### 4. Price Recommendation (Optimization)
Instead of predicting prices:
1. Generates price scenarios (e.g., -5%, current, +5%)
2. Estimates demand for each scenario
3. Calculates expected revenue
4. Selects price that maximizes revenue

### 5. Automation
- **Script**: `daily_pipeline.py` orchestrates the entire workflow
- **Scheduler**:
  - Development: Windows Task Scheduler
  - Production: Linux cron or cloud scheduler
- **Frequency**: Daily execution (configurable)

### 6. API Layer
- **Framework**: FastAPI
- **Role**: Serves latest predictions & recommendations
- **Note**: Does NOT retrain models (use pipeline for that)

---

## 🌟 Why This Project Is Different

| Aspect | This Project | Typical Approach |
|--------|-------------|-----------------|
| **Data** | Real, continuously collected | Kaggle datasets or simulated |
| **Pricing** | Optimized via simulation | Predicted as regression problem |
| **Architecture** | System with automation | Single notebook |
| **Deployment** | Docker + CI/CD | Manual deployment |
| **Scheduling** | Dedicated cron/scheduler | API-triggered or manual |
| **Design** | Production-grade patterns | Proof-of-concept |

### Design Decisions Explained

**1. Why optimize price instead of predicting it?**
- Price has no single ground truth (depends on market, inventory, strategy)
- Price is a decision variable, not an observed outcome
- Optimization allows us to maximize a specific objective (revenue)

**2. Why XGBoost instead of deep learning?**
- Limited historical data makes deep learning less effective
- XGBoost provides better interpretability
- Faster training and deployment

**3. Why separate pipeline from API?**
- CI/CD is for code changes, not long-running data jobs
- Pipelines need reliability and scheduling, not HTTP requests
- Cleaner separation of concerns

---

## 🔮 Future Enhancements

- [ ] **Constraints in Pricing**: Add margin and inventory constraints
- [ ] **Multi-Product Support**: Scale to handle multiple SKUs
- [ ] **Cloud Scheduler**: Migrate to Airflow, AWS EventBridge, or Google Cloud Scheduler
- [ ] **Monitoring & Alerting**: Add Prometheus, Grafana, or similar tools
- [ ] **Advanced Models**: Experiment with LSTM for longer-term forecasts
- [ ] **A/B Testing Framework**: Test recommended prices in production
- [ ] **Real-Time Predictions**: Switch to stream processing for live data
- [ ] **Competitor Analysis**: Incorporate competitor pricing data

---

## 📊 Performance Metrics

To evaluate the model's performance, check:

- **Mean Absolute Error (MAE)**: Average prediction error in units
- **Mean Absolute Percentage Error (MAPE)**: Percentage-based error metric
- **R² Score**: Proportion of variance explained
- **Revenue Uplift**: Expected revenue improvement vs. baseline

See `notebooks/model_evaluation.ipynb` for detailed analysis.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Guidelines:**
- Write clean, documented code
- Add tests for new features
- Update README if adding new functionality
- Follow PEP 8 style guidelines

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mitul Khemani**
- GitHub: [@mitulkhemani2005](https://github.com/mitulkhemani2005)
- Email: [khemanimitul@gmail.com]

---

## 🙏 Acknowledgments

- Flipkart for providing publicly accessible product data
- XGBoost team for the powerful ML framework
- FastAPI team for the modern web framework
- GitHub Actions for CI/CD capabilities

---

## 📞 Support

If you have questions or run into issues:

1. Check existing [GitHub Issues](https://github.com/mitulkhemani2005/flipkart_competitors/issues)
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs. actual behavior
   - Environment details (Python version, OS, etc.)

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Pandas Guide](https://pandas.pydata.org/docs/)
- [Docker Documentation](https://docs.docker.com/)

---

<div align="center">

**Made with ❤️ by Mitul Khemani**

If you find this project useful, please consider giving it a ⭐

</div>