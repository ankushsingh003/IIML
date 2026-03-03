# Bangalore Restaurant Market Analysis
**GitHub Repository:** [https://github.com/ankushsingh003/IIML.git](https://github.com/ankushsingh003/IIML.git)

## Project Overview
This project provides a professional, data-driven analysis of the restaurant market in Bangalore. It includes a complete data processing pipeline: data cleaning, advanced bivariate analysis, and machine learning-powered feature importance selection.

## Final Deliverables
- **Insight Report**: [Restaurant_Market_Analysis_Report.pdf](Restaurant_Market_Analysis_Report.pdf) - A comprehensive professional report with 13 key visualizations and strategic business inferences.
- **Cleaned Dataset**: `cleaned_restaurant_data.csv` - The processed and cleaned version of the original dataset.

## Scripts
- `clean_data.py`: Handles missing values, duplicates, and data standardization.
- `analyze_data.py`: Performs univariate/bivariate analysis and calculates feature importance using Random Forest.
- `generate_report.py`: Generates the final indigo-themed professional PDF report.

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn fpdf2 scikit-learn
   ```
2. Run the cleaning script:
   ```bash
   python clean_data.py
   ```
3. Run the analysis:
   ```bash
   python analyze_data.py
   ```
4. Generate the report:
   ```bash
   python generate_report.py
   ```
