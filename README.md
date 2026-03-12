# Users Data Analysis with Python

A professional Python data analysis project that explores user data collected from the DummyJSON API using **Pandas**, **Matplotlib**, and **Seaborn**.

---

## Project Overview

This project focuses on loading, exploring, cleaning, and analyzing user data retrieved from the DummyJSON API.  
The analysis answers business-style questions about user demographics and physical attributes, then supports the findings with clear visualizations.

The project includes:

- Data extraction from API
- Basic data exploration
- Data cleaning and preparation
- Exploratory data analysis (EDA)
- Visual storytelling using charts
- Supporting notebooks from NumPy and Pandas practice

---

## Project Structure

```text
users-data-analysis-with-python/
│
├── Day1_NumPy/
│   └── NumPy_lab_solution.ipynb
│
├── Day2_Pandas/
│   ├── Pandas_lab_solution.ipynb
│   └── students.csv
│
├── Final_Project/
│   ├── DataAnalysis_with_Python.ipynb
│   ├── reading_users_data.py
│   ├── users.csv
│   │
│   └── Images/
│       ├── Average Age by Gender.png
│       ├── Correlation Matrix.png
│       ├── Distribution of users Age.png
│       ├── Height Distribution by Gender.png
│       ├── Overall Averages- Height Vs Weight.png
│       ├── Role Distribution by Gender.png
│       ├── Top 10 cities with most users.png
│       ├── User count by gender.png
│       └── Screenshot 2026-03-12 163810.jpg
│
├── requirements.txt
└── README.md
```

---

## Data Source

The dataset was collected from the DummyJSON Users API:

`https://dummyjson.com/users?limit=100`

A separate Python script was used to fetch user records in batches and save them into a CSV file for analysis.

---

## Objectives

This project covers the following tasks:

### 1. Data Loading

* Fetch user data from the API
* Convert the response into a Pandas DataFrame
* Save the collected data as a CSV file

### 2. Data Exploration

* Inspect dataset shape
* Review columns and data types
* Check missing values
* Detect duplicates
* Generate descriptive statistics
* Explore categorical distributions

### 3. Data Cleaning

* Prepare nested or missing fields when needed
* Handle missing values in important numeric columns

### 4. Data Analysis

The project answers questions such as:

* What is the average age of users?
* What is the average age by gender?
* How many users belong to each gender?
* What are the top 10 cities with the most users?
* What are the overall average height and weight?
* Is there any visible relationship between age and height/weight?

---

## Tools and Libraries

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Requests
* Jupyter Notebook

---

## Main Files

### `Final_Project/DataAnalysis_with_Python.ipynb`

The main notebook containing the full workflow:

* loading the dataset
* exploring and cleaning the data
* analysis
* visualizations

### `Final_Project/reading_users_data.py`

Python script used to fetch users from the API and save them as `users.csv`.

### `Final_Project/users.csv`

The saved dataset used in the final analysis.

---

# Key Visualizations

Since the images are now inside `Final_Project/Images`, the paths must change.

## Distribution of Users Age

![Distribution of users Age](Final_Project/Images/Distribution%20of%20users%20Age.png)

## Average Age by Gender

![Average Age by Gender](Final_Project/Images/Average%20Age%20by%20Gender.png)

## User Count by Gender

![User count by gender](Final_Project/Images/User%20count%20by%20gender.png)

## Top 10 Cities with Most Users

![Top 10 cities with most users](Final_Project/Images/Top%2010%20cities%20with%20most%20users.png)

## Height Distribution by Gender

![Height Distribution by Gender](Final_Project/Images/Height%20Distribution%20by%20Gender.png)

## Overall Averages: Height vs Weight

![Overall Averages- Height Vs Weight](Final_Project/Images/Overall%20Averages-%20Height%20Vs%20Weight.png)

## Role Distribution by Gender

![Role Distribution by Gender](Final_Project/Images/Role%20Distribution%20by%20Gender.png)

## Correlation Matrix

![Correlation Matrix](Final_Project/Images/Correlation%20Matrix.png)

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/users-data-analysis-with-python.git
cd users-data-analysis-with-python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the data extraction script

```bash
python Final_Project/reading_users_data.py
```

### 4. Open the notebook

Open:

```text
Final_Project/DataAnalysis_with_Python.ipynb
```

and run the cells in Jupyter Notebook.

---

## Learning Outcomes

Through this project, I practiced:

* Working with APIs in Python
* Transforming JSON responses into tabular data
* Cleaning and preparing data for analysis
* Performing exploratory data analysis
* Building effective visualizations
* Organizing a data analysis project in a professional GitHub repository

---

## Author

**Abdelrahman Maged**

---

## Notes

This repository also includes supporting practice work from:

* NumPy lab
* Pandas lab

These files demonstrate the learning path that supported the final project implementation.
