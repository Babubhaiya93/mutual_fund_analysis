-- DIMENSION TABLE: Funds
CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT,
    category TEXT
);

-- DIMENSION TABLE: Date
CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

-- FACT TABLE: NAV
CREATE TABLE fact_nav (
    id INTEGER PRIMARY KEY,
    fund_name TEXT,
    date TEXT,
    nav REAL
);

-- FACT TABLE: Performance Metrics
CREATE TABLE fact_performance (
    fund_name TEXT PRIMARY KEY,
    CAGR REAL,
    Volatility REAL,
    Sharpe_Ratio REAL
);