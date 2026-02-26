# AUTOMATED-REPORT-GENERATION
Company: CODTECH IT SOLUTION PVT.LTD

Name: BHAVIKA BHATIA

Intern Id: CTIS4942

Domain: Python Programming

Duration: 6 Weeks

Mentor: Neela Santosh

## Project Description

This project is based on the concept of Automated Report Generation using Python. The main objective was to create a script that reads air pollution data from a CSV file, analyzes it, and automatically generates a formatted PDF report.

For this task, I used the Global Air Pollution dataset from Kaggle. The dataset includes information about different countries, cities, AQI (Air Quality Index) values, and AQI categories. The goal of this project was to extract meaningful insights from the dataset and present them in a structured report format.

The project was developed using Visual Studio Code (VS Code).

## Objectives

- To read and process a CSV file using Python

- To clean and analyze air pollution data

- To calculate statistical values such as average, maximum, and minimum AQI

- To create visualizations using graphs

- To generate an automated PDF report using ReportLab

## Technologies Used

- Python

- Pandas

- Matplotlib

- ReportLab

- Kaggle Dataset

- Visual Studio Code

## Working of the Project

- The dataset is loaded using Pandas.
- Data cleaning is performed by removing missing values from important columns like Country, City, and AQI Value.
- The script calculates:
  - Total number of unique countries
  - Total number of unique cities
  - Average AQI value
  - Maximum AQI value
  - Minimum AQI value
  - AQI category distribution
  - Top 5 most polluted countries
- Data visualization is performed using Matplotlib:
  - Pie chart for AQI category distribution
  - Bar chart for top 5 polluted countries
  - Histogram for AQI value distribution
- A formatted PDF report is generated using ReportLab.

## Conclusion

The entire process is automated. When the script is executed, it performs analysis and generates the complete PDF report automatically.

## Learning Outcomes

Through this project, I gained practical experience in data cleaning, visualization, and automated PDF generation. It helped me understand how Python can be used to build automated reporting systems for real-world datasets.

## How to Run

Install required libraries:
```
pip install Pandas, Reportlab, Matplotlib
```

## Output

The final output file generated is:

Global_AQI_Analysis_Report.pdf

The PDF contains summary statistics, visual charts, tables, and conclusions. After successful execution, the terminal displays:

PDF Report Generated Successfully!

