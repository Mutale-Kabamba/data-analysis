
# ☕ Coffee Shop Customer Survey Analysis

![Project Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Language](https://img.shields.io/badge/Language-R-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Last Updated](https://img.shields.io/badge/Last_Updated-April_2025-orange)

---

## 📋 Project Overview

This project analyzes survey data collected from customers of a coffee shop.  
It explores customer demographics, preferences, satisfaction levels, loyalty membership, and identifies key patterns and relationships to provide insights that could inform business strategies for improving customer experience and sales.

---

## 🔍 Main Insights

- **Average Age:** The average customer age is **40.9 years**.
- **Gender Distribution:**  
  - Male: **49%**  
  - Female: **43%**  
  - Other: **8%**
- **Product Popularity:**  
  - **Most Popular Product:** Tea  
  - **Least Popular Product:** Coffee
- **Visit Frequency Patterns:**  
  - **Males** visit slightly more frequently than females.
  - **Young Adults (18–29)** visit the shop the most often.
- **Loyalty Insights:**  
  - Loyalty members spend about **5 minutes more** per visit compared to non-members.
  - Loyalty membership is associated with a **higher likelihood to recommend** the coffee shop (p = 0.035).
- **Satisfaction and Recommendation Predictors:**
  - **Satisfaction score** is the strongest positive predictor of customer recommendations.
  - Surprisingly, loyalty membership showed a **negative effect** in predicting recommendations in the model.

---

## 📈 Key Metrics

| Metric | Value |
|:------|:------|
| Average Age | **40.9 years** |
| Most Popular Product | **Tea** |
| Least Popular Product | **Coffee** |
| Gender Split | **Male: 49**, **Female: 43**, **Other: 8** |
| Average Visit Frequency (Male) | **3.71 visits** |
| Average Visit Frequency (Female) | **3.16 visits** |
| Average Time Spent (Loyalty Members) | **35.67 minutes** |
| Average Time Spent (Non-Members) | **30.53 minutes** |
| Correlation (Visit Frequency vs Satisfaction) | **0.002 (very weak)** |
| Loyalty Membership & Recommendation (p-value) | **0.035 (significant)** |

---

## 📚 Methods & Tools Used

- **R Language**
- **Libraries:**
  - `tidyverse` (dplyr, ggplot2, readr, etc.)
  - `readxl`
  - `broom`
  - `rmarkdown`
- **Statistical Analysis:**
  - Descriptive Statistics (Means, Counts)
  - Correlation Analysis
  - T-Tests
  - Chi-Square Test
  - Linear Regression
  - Logistic Regression
- **Visualization:**
  - Bar Charts
  - Scatter Plots
  - Correlation Plots
  - Regression Summaries

---

## 📂 Project Structure

```bash
coffee_survey_analysis/
├── data/
│   └── coffee_shop_survey.xlsx
├── reports/
│   └── coffee_survey_report.pdf
├── scripts/
│   └── coffee_analysis_script.R
├── README.md
```

---

## ⚡ Quick Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/coffee_survey_analysis.git
```

2. **Install required R packages:**

```R
install.packages(c("dplyr", "ggplot2", "readr", "readxl", "broom", "rmarkdown"))
```

3. **Run the analysis:**

```R
source("scripts/coffee_analysis_script.R")
```

---

## 📈 Results Highlights

- Customers between **18–44 years** are the most frequent visitors.
- **Tea lovers** are the largest customer segment.
- **Loyalty program members** are more engaged but **not guaranteed** to be more satisfied.
- **Customer satisfaction** is the **main driver** for customer recommendations.

---

## 🛠 Future Improvements

- Explore clustering customer types (segmentation).
- Deep dive into dissatisfaction reasons among coffee buyers.
- Analyze temporal patterns (e.g., best days/times for visits).
- Expand survey to include customer income and spending behavior.

---

## 📬 Contact

For any questions, suggestions, or collaborations, feel free to reach out:

- **Email**: kabamba@example.com  
- **LinkedIn**: [Your LinkedIn Profile]  
- **GitHub**: [Your GitHub Profile]

---

> _"Good coffee is a pleasure, good data is a treasure."_
