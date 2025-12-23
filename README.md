# PremierZone

PremierZone is a comprehensive project designed to scrape match statistics for over 700 players, manipulate and present the data dynamically, and predict match outcomes using machine learning. The project is divided into four main components: Backend, Frontend, Data Scraping, and Machine Learning.

## ⚠️ Disclaimer

This project is for educational purposes only. Premier League, Barclays Premier League, and all related trademarks are the property of their respective owners. This project is not affiliated with, endorsed by, or associated with the Premier League or any of its official partners.

## Features

- **Data Scraping**: Engineered a comprehensive data scraping of match statistics for 700+ players using Python and pandas.
- **Backend**: Dynamic manipulation and presentation of the scraped data through a FastAPI application (Python) connected to Postgres.
- **Database**: Real-time data manipulation within a Postgres database using SQL queries.
- **Frontend**: Seamless integration with a user-friendly ReactJS interface.
- **Machine Learning**: Created a model to predict match outcomes by integrating data scraping with pandas and machine learning with scikit-learn.

## Backend (Python / FastAPI)

Location: `BackendPy/`

### Quick start
1) Install deps: `pip install -r BackendPy/requirements.txt`
2) Set `DATABASE_URL` env var (defaults to `postgresql://postgres:password@localhost:5432/pl_data`).
3) Optional: set `ALLOWED_ORIGINS` (comma-separated, defaults to `http://localhost:3000`).
4) Run: `uvicorn app.main:app --reload --app-dir BackendPy`

### API
- `GET /api/v1/player` with optional query params `team`, `name`, `position`, `nation`
- `POST /api/v1/player` (create)
- `PUT /api/v1/player/{player_name}` (update by name)
- `DELETE /api/v1/player/{player_name}`



