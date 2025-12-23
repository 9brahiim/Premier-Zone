# Setup Guide

## Prerequisites
- Python 3.8+
- Node.js and npm
- PostgreSQL database

## Backend Setup

1. Navigate to the backend directory:
```bash
cd BackendPy
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env` (if it exists) or create a `.env` file
   - Set `DATABASE_URL` (default: `postgresql://postgres:password@localhost:5432/pl_data`)
   - Optionally set `ALLOWED_ORIGINS` (comma-separated)

5. Run the backend:
```bash
uvicorn app.main:app --reload --app-dir BackendPy
```

The API will be available at `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

## Frontend Setup

1. Navigate to the frontend directory:
```bash
cd Frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## Database Setup

Make sure PostgreSQL is running and create the database:
```sql
CREATE DATABASE pl_data;
```

The backend will automatically create the `player_stats` table on first run.

