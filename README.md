# 📚 Web Scraping Data Pipeline & Dashboard

## 📌 Project Overview

This project demonstrates an **end-to-end data pipeline** that collects book data from a website, processes it, stores it in a database, and visualizes insights through an interactive dashboard.

The pipeline automatically:

* Scrapes book information from the web
* Cleans and validates the data
* Stores structured data in a database
* Performs exploratory data analysis
* Displays insights using an interactive dashboard

This project showcases practical data engineering and data analysis skills using Python.

---

## 🛠️ Tech Stack

* **Python**
* **BeautifulSoup** – Web scraping
* **Pandas & NumPy** – Data cleaning and analysis
* **SQLite** – Database storage
* **Streamlit** – Interactive data dashboard

---

## 📂 Project Structure

```
web-scraping-data-pipeline
│
├── scraper.py          # Scrapes book data from website
├── database.py         # Stores cleaned data into SQLite database
├── dashboard.py        # Streamlit dashboard for visualization
├── books_data.csv      # Processed dataset
├── books.db            # SQLite database
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ How the Pipeline Works

```
Website
   ↓
Web Scraper (BeautifulSoup)
   ↓
Data Cleaning & Validation (Pandas)
   ↓
Database Storage (SQLite)
   ↓
Data Analysis & Visualization (Streamlit Dashboard)
```

---

## 📊 Key Features

* Scrapes book information such as **title, price, and rating**
* Cleans and validates data using Pandas
* Stores structured data in a SQL database
* Performs **exploratory data analysis**
* Visualizes insights through a **Streamlit dashboard**
* Provides interactive views of pricing and rating patterns

---

## 📈 Example Insights

The dashboard provides insights such as:

* Average book price
* Distribution of book ratings
* Top 10 most expensive books
* Dataset preview and exploration

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/vanshika7605/web-scraping-data-pipeline.git
cd web-scraping-data-pipeline
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the scraper

```
python scraper.py
```

### 4️⃣ Launch the dashboard

```
streamlit run dashboard.py
```

---

## 🌐 Live Dashboard

You can view the interactive dashboard here:

🔗 **Live App:**
https://web-scraping-data-pipeline.streamlit.app

The dashboard allows users to explore book data, analyze pricing trends, and view rating distributions interactively.

---

## 🎯 Skills Demonstrated

* Web Scraping
* Data Cleaning
* Data Analysis
* Database Management
* Data Visualization
* Building Interactive Dashboards

---

## 👩‍💻 Author

**Vanshika**

GitHub:
https://github.com/vanshika7605

---

## ⭐ If you found this project useful

Give the repository a ⭐ on GitHub!
