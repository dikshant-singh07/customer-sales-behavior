# customer-sales-behavior
End-to-end data analytics project analyzing customer shopping and sales behavior using Python, Power BI and MySQL integration for structured data storage and querying.

### *An end-to-end data analytics project using Python, MySQL & Power BI.*

---

## Project Overview

This project analyzes **customer shopping patterns** and **sales behavior** to identify key trends, improve engagement, and support data-driven marketing decisions.  
The workflow covers **data cleaning**, **analysis with Python and SQL**, and **visual insights** built in **Power BI**.

---

## Objectives
- Understand **customer purchase behavior** and identify loyal segments.  
- Analyze how **discounts, promo codes, and subscriptions** affect sales.  
- Find **top-performing categories** and **customer demographics** driving revenue.  
- Build an interactive **Power BI dashboard** for business insights.

---

## Tools & Technologies
| Category | Tools |
|-----------|--------|
| **Programming** | Python (pandas) |
| **Database** | MySQL |
| **Visualization** | Power BI |
| **Integration** | SQLAlchemy |
| **IDE** | VS Code |
| **Version Control** | Git & GitHub |

---

## Project Files

| File Name | Description |
|------------|-------------|
| `customer_shopping_behavior.csv` | Raw dataset containing customer purchase information |
| `customer_shopping_behavior_analysis.py` | Python script for data cleaning, analysis & MySQL integration |
| `sales analysis.sql` | SQL queries for business insights & trend analysis |
| `Customer Shopping Behavior Analysis.pdf` | Final analysis report |
| `Customer-Shopping-Behavior-Analysis ppt.pptx` | Presentation summary |
| `problem statement.pdf` | Business objective document |
| `customer_Behavior_dashboard.pdf` | Power BI dashboard (final visualization) |

---

## Data Cleaning & Transformation (Python)

- Removed duplicates and standardized column names.  
- Handled 37 missing values in **Review Rating** using **category-wise median imputation**:
  
  df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

* Dropped redundant column: `Promo Code Used`.
* Loaded cleaned data into MySQL using **SQLAlchemy**:

  from sqlalchemy import create_engine
  engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/customer_sales_db")
  df.to_sql('customer_shopping_behavior', con=engine, if_exists='replace', index=False)

---

## 🧠 SQL Analysis

Key queries performed in `sales analysis.sql`:

| # | Analysis                | Description                                   |
| - | ----------------------- | --------------------------------------------- |
| 1 | Total Revenue by Gender | Compare male vs. female purchase totals       |
| 2 | Discount Effect         | Identify high-value customers using discounts |
| 3 | Top-Rated Products      | Find 5 products with highest average ratings  |
| 4 | Shipping Type Analysis  | Compare purchase amounts by shipping method   |
| 5 | Subscription Analysis   | Examine subscriber vs. non-subscriber revenue |
| 6 | Customer Loyalty        | Classify customers by purchase frequency      |
| 7 | Category Insights       | Rank categories by revenue and review rating  |

---

## Power BI Dashboard

**File:** `customer_Behavior_dashboard.pdf`

### Key Metrics

* **Total Customers:** 3,900
* **Avg Purchase Amount:** $59.76
* **Avg Review Rating:** 3.75
* **Subscribers:** 27%
* **Loyal Customers:** 3,116

## Dashboard Insights

* Clothing & Accessories lead in total revenue.
* Young Adults spend the most on online shopping.
* Discounts drive more sales but don’t always increase total revenue.
* Subscription users purchase more frequently than non-subscribers.




