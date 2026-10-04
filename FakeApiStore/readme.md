# 🛒 FakeStore ETL Data Pipeline

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Database](https://img.shields.io/badge/Database-MS%20SQL%20Server-red?style=for-the-badge&logo=microsoftsqlserver)
![Pipeline](https://img.shields.io/badge/Architecture-ETL-green?style=for-the-badge)

An automated Data Engineering pipeline built with **Python**, **Pandas**, and **SQLAlchemy** that extracts e-commerce data from [FakeStoreAPI](https://fakestoreapi.com/), cleans and flattens nested JSON responses, and efficiently loads structured records into an **MS SQL Server** database.

---

## 📌 Features

- **Extract**: Pulls real-time e-commerce dataset (Products, Users, Carts) from RESTful API endpoints.
- **Transform**: 
  - Flattens nested JSON structures (`rating`, `address`, and `geolocation`).
  - Normalizes and explodes nested transactional arrays in shopping carts.
  - Handles string URL encoding, data type casting, and schema validation using Pandas.
- **Load**: Seamlessly loads structured DataFrames into Microsoft SQL Server tables with specific data type mappings (`SQLAlchemy`).
- **Robust Configuration**: Environment-driven configuration using `.env` file for secure credential management and cross-platform execution.

---

## 🏗️ Project Architecture

```
         +--------------------+
         |   FakeStore API    |
         +---------+----------+
                   |
                   | (Extract)
                   v
         +--------------------+
         |  Data Cleaning     |
         | & Transformation   |  (Pandas)
         +---------+----------+
                   |
                   | (Load)
                   v
    +------------------------------+
    | MS SQL Server Data Warehouse |
    +------------------------------+
```

---

## 📁 Repository Structure

```
├── ETL/
│   ├── __init__.py
│   ├── config.py       # DB connection, safety checks, & environment variables
│   ├── extract.py      # Module to fetch data from API endpoints
│   ├── transform.py    # Pandas normalization & schema transformation logic
│   └── load.py         # Database loader functions using SQLAlchemy engine
├── .env.example        # Environment variables template
├── .gitignore          # Excluded sensitive and cache files
├── main.py             # Pipeline execution entry point
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have the following installed on your machine:
- **Python 3.8+**
- **MS SQL Server** with ODBC Driver 17 installed
- **Git**

### 2. Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/your-username/fakestore-etl-pipeline.git
cd fakestore-etl-pipeline

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install pandas requests sqlalchemy pyodbc python-dotenv
```

### 3. Environment Setup

Create a `.env` file in the project root folder (you can use `.env.example` as reference):

```env
DB_SERVER=localhost
DB_DATABASE=FakeStoreDB
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

---

## ⚡ Execution

Run the complete pipeline using the `main.py` entry script:

```bash
python main.py
```

### Expected Output
```text
Starting FakeStore ETL Pipeline...

Fetching Products...
Loaded 20 records into table: 'products'
Fetching Users...
Loaded 10 records into table: 'users'
Fetching Carts...
Loaded 20 records into table: 'carts'

Pipeline Execution Finished!
```

---

## 📊 Database Schema Details

- **`products`**: `product_id`, `product_name`, `product_price`, `description`, `product_category`, `rating_rate`, `rating_count`
- **`users`**: `user_id`, `email`, `username`, `FirstName`, `LastName`, `phone`, `city`, `street`, `house_number`, `zipcode`, `latitude`, `longitude`
- **`carts`**: `cart_id`, `user_id`, `date`, `product_id`, `quantity`

---

## 🛠️ Tech Stack

- **Language**: Python
- **Data Manipulation**: Pandas
- **API Interaction**: Requests
- **Database Engine & ORM**: MS SQL Server, PyODBC, SQLAlchemy
- **Environment Management**: Python-Dotenv