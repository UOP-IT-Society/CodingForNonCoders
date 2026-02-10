# Python Project Portfolio: Finance, Science & Data Analytics

---

## 💰 Finance & Accounting

### 1. Personal Finance Analyzer

* **Core Functionality:** Reads bank transactions via CSV, categorizes expenses (rent, food, transport), generates monthly summaries, and visualizes spending trends.
* **Tech Stack:** `Pandas` (groupby, aggregation), `Seaborn` (bar + line plots), File automation.
* **Stretch Goals:** Budget alerts, rolling averages, and category pie charts.

### 2. Loan & Investment Simulator

* **Core Functionality:** Calculates loan amortization schedules, compares interest rates/terms, and simulates compound interest growth.
* **Tech Stack:** `NumPy`, Python functions, `Matplotlib`.
* **Stretch Goals:** Monte Carlo simulations and CSV schedule exports.

### 3. Business Revenue Dashboard

* **Core Functionality:** Processes sales data from CSV/Excel to compute revenue, profit margins, and growth rates using multi-subplot dashboards.
* **Tech Stack:** `Pandas`, `Seaborn`, Data cleaning modules.
* **Stretch Goals:** Scenario analysis (price sensitivity) and KPI summary tables.

---

## 🔬 Science & Engineering

### 4. Experimental Data Analysis Tool

* **Core Functionality:** Loads measurements, cleans noisy datasets, performs curve fitting, and visualizes residuals.
* **Tech Stack:** `NumPy` curve fitting, `Pandas`, `Matplotlib`.
* **Stretch Goals:** Automated multi-experiment comparison.

### 5. Physics Simulation & Visualization

* **Core Functionality:** Models projectile motion with air resistance, harmonic oscillators, or population growth.
* **Tech Stack:** `NumPy` arrays, time-series visualization, parameter exploration.
* **Stretch Goals:** Animated results and batch simulations.

---

## 📊 Data Analytics & General Python

### 6. CSV Batch Processing System

* **Core Functionality:** Automates reading, cleaning, and merging dozens of CSV files from a single directory to generate summary reports.
* **Tech Stack:** File automation, `Pandas` aggregation, Error handling.
* **Real-world Context:** Mimics professional data analyst workflows.

### 7. Student Grades & Performance Analyzer

* **Core Functionality:** Aggregates grades to calculate averages and rankings while identifying at-risk students.
* **Stretch Goals:** Performance trend prediction and summary exports.

### 8. Inventory & Sales Forecast Tool

* **Core Functionality:** Tracks stock levels, identifies moving speeds (fast/slow), and flags restocking requirements.
* **Tech Stack:** `Pandas`, time-based aggregation, `Seaborn`.

---

## 🎛️ Interactive & High-Impact

### 9. Interactive Data Dashboard (Notebook-Based)

* **Core Functionality:** Dynamic plot updates based on user-selected parameters.
* **Best For:** Demonstrations, teaching, and presentations.

### 10. “One-Click” Data Report Generator

* **Core Functionality:** End-to-end automation. Inputting raw data produces a folder containing cleaned CSVs, summary tables, and PNG charts.
* **Tech Stack:** Integration of all concepts (Weeks 1–9).


## 💰 Dataset 1: Personal Finance Transactions

**Use cases:**
Expense analysis, budgeting tools, dashboards

```csv
date,description,category,amount
2025-01-01,Rent,Housing,-1200
2025-01-03,Grocery Store,Food,-145.32
2025-01-05,Electric Bill,Utilities,-89.50
2025-01-08,Internet Bill,Utilities,-65.00
2025-01-10,Restaurant,Food,-42.75
2025-01-12,Gas Station,Transport,-55.20
2025-01-15,Salary,Income,3200
2025-01-18,Movie Theater,Entertainment,-28.00
2025-01-20,Gym Membership,Health,-45.00
2025-01-25,Online Shopping,Misc,-120.99
```

**Key skills**

* Pandas grouping & aggregation
* Time-series analysis
* Spending category visualization

---

## 📈 Dataset 2: Business Sales Data

**Use cases:**
Revenue dashboards, profit analysis, KPI tracking

```csv
date,product,units_sold,price_per_unit,cost_per_unit
2025-01-01,Widget A,120,15.00,9.00
2025-01-02,Widget B,75,22.00,14.00
2025-01-03,Widget A,90,15.00,9.00
2025-01-04,Widget C,60,30.00,18.00
2025-01-05,Widget B,110,22.00,14.00
2025-01-06,Widget C,40,30.00,18.00
2025-01-07,Widget A,130,15.00,9.00
```

**Derived metrics**

* Revenue = `units_sold × price_per_unit`
* Profit = `units_sold × (price_per_unit − cost_per_unit)`

---

## 🔬 Dataset 3: Experimental Physics Data

**Use cases:**
Curve fitting, numerical analysis, scientific plots

```csv
time_seconds,position_meters
0,0.0
1,4.9
2,19.6
3,44.1
4,78.4
5,122.5
6,176.4
7,240.1
8,313.6
9,396.9
```

**Great for**

* Quadratic regression
* Residual analysis
* Model validation

---

## 🎓 Dataset 4: Student Grades

**Use cases:**
Performance analysis, data cleaning, reporting

```csv
student_id,exam1,exam2,final,attendance
S001,78,82,85,92
S002,65,70,68,85
S003,90,88,91,98
S004,55,60,58,72
S005,83,79,88,90
S006,72,75,70,80
```

**Analysis ideas**

* Weighted averages
* Risk classification
* Attendance vs performance plots

---

## 🧪 Dataset 5: Inventory Levels

**Use cases:**
Inventory tracking, automation, forecasting

```csv
date,product,stock_level,units_sold
2025-01-01,Item A,500,40
2025-01-02,Item A,460,35
2025-01-03,Item A,425,50
2025-01-04,Item B,300,20
2025-01-05,Item B,280,25
2025-01-06,Item C,150,15
```
