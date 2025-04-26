
# ☕ Coffee Shop Customer Survey Analysis (R Project)

![Project Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Built With](https://img.shields.io/badge/Built%20With-R-blue)
![Last Updated](https://img.shields.io/badge/Last_Updated-April_2025-orange)
![Documentation](https://img.shields.io/badge/Documentation-Complete-brightgreen)
![Author](https://img.shields.io/badge/Author-Kabamba%20Mutale-blueviolet)



An interactive coffee shop customer analysis project built in R as part of an exploratory data analysis exercise from the School of Statisticians – Mentorship Program.. This project transforms raw survey data into actionable business insights through statistical modeling and visualizations, allowing users to explore customer demographics, product preferences, visit behaviors, loyalty trends, and satisfaction drivers.

---

## 📚 Table of Contents

1. [Overview](#-overview)  
2. [Data Preview](#-data-preview)  
3. [Dataset Summary](#-dataset-summary)  
4. [Data Cleaning](#-data-cleaning)  
5. [Business Questions Answered](#-business-questions-answered)  
6. [Analysis Techniques Used](#-analysis-techniques-used)  
7. [Key Insights](#-key-insights)  
8. [Recommendations](#-recommendations)  
9. [How to Reproduce](#-how-to-reproduce)  

---

## 📄 Overview

This project explores customer survey data from a coffee shop.  
The goal was to transform raw survey responses into actionable business insights by analyzing demographics, visit behaviors, loyalty membership impact, and satisfaction scores.

**Key Highlights:**

- Customer demographics analysis  
- Product popularity insights  
- Loyalty and recommendation patterns  
- Satisfaction score analysis  
- Predictive modeling (logistic regression)

---

## 📸 Data Preview

Here’s a basic glimpse of the raw survey data structure:

| Customer ID | Age | Gender | Visit Frequency | Favorite Product | Satisfaction Score | Time Spent (min) | Loyalty Member | Would Recommend |
|:-----------|:---|:------|:---------------|:----------------|:------------------|:----------------|:--------------|:---------------|
| CUST001 | 56 | Male | 1 | Sandwich | 2 | 53 | Yes | No |
| CUST002 | 46 | Male | 2 | Sandwich | 1 | 32 | No | Yes |
| CUST003 | 32 | Male | 6 | Pastry | 5 | 36 | Yes | Yes |

---

## 📂 Dataset Summary

- **Records:** 100 customers  
- **Fields:** 9 columns

**Key Fields:**

- `Age`
- `Gender`
- `Visit Frequency`
- `Favorite Product`
- `Satisfaction Score`
- `Time Spent (min)`
- `Loyalty Member`
- `Would Recommend`

---

## 🧼 Data Cleaning

Applied the following cleaning steps before analysis:

- **Checked for Missing Values**: No missing entries were found.
- **Renamed Columns**: Simplified column names (e.g., changed `Time_Spent (min)` ➔ `Time_Spent_min`).
- **Categorized Age Groups**:  
  - Child (0–17)  
  - Young Adult (18–29)  
  - Adult (30–44)  
  - Old (45–59)  
  - Senior (60+)
- **Formatted Variables**:  
  - Converted loyalty membership and favorite product to categorical factors.

---

## 🧠 Business Questions Answered

### 🎯 Demographic Trends
- What is the average age of visitors?
- What is the gender distribution?

### 🛍 Product Popularity
- Which product is most and least popular?

### 📊 Visit Behavior
- Do visit frequencies vary by gender and age group?

### 🤝 Loyalty and Satisfaction
- Do loyalty members spend more time at the shop?
- Is loyalty associated with higher satisfaction or recommendation likelihood?

### 🔎 Predictive Modeling
- Can we predict customer recommendations based on satisfaction, age, loyalty, and gender?

---

## ⚙️ Analysis Techniques Used

- **Descriptive Statistics** (mean, frequency counts)
- **Data Visualization** (bar charts, scatter plots)
- **T-Tests** (comparing loyalty members vs non-members)
- **Chi-Square Tests** (association between loyalty and recommendation)
- **Linear Regression** (factors influencing satisfaction score)
- **Logistic Regression** (predicting customer recommendations)

---

## 💡 Key Insights

- **Average Age**: 40.9 years.
- **Gender Split**: 49% Male, 43% Female, 8% Other.
- **Most Popular Product**: **Tea**.
- **Least Popular Product**: **Coffee**.
- **Visit Frequency**: Males and Young Adults visit slightly more often.
- **Loyalty Members**:
  - Spend 5 minutes more per visit on average.
  - More likely to recommend the coffee shop (p = 0.035).
- **Satisfaction Score** is the strongest predictor for customer recommendations.

---

## ✅ Recommendations

- Focus promotions on **Young Adults** (18–29 age group).
- Expand the **Tea** menu, as it's the top favorite.
- Encourage **loyalty program enrollment**, but also work on loyalty member engagement to ensure satisfaction.
- Boost **satisfaction efforts** to drive higher recommendation rates, as satisfaction has the greatest impact.

---

## 🧭 How to Reproduce

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/coffee_survey_analysis.git
```

2. **Install required R packages:**

```R
install.packages(c("dplyr", "ggplot2", "readr", "readxl", "broom", "rmarkdown"))
```

3. **Run the analysis script:**

```R
source(./coffee_survey.Rmd)
```

4. **Explore the outputs** including:
   - Plots for demographics, product popularity, loyalty impact
   - Statistical test summaries
   - Regression model outputs

---

👉 Want the full survey dataset?
👉 [Download the dataset](./coffee_shop_survey.xlsx)

---

> _"Good coffee is a pleasure, good data is a treasure."_
