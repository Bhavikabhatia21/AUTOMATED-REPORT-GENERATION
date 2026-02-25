import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

df = pd.read_csv("C:\\Users\\mayan\\Downloads\\global air pollution dataset.csv")
df = df.dropna(subset=["Country", "City", "AQI Value"])
total_countries = df["Country"].nunique()
total_cities = df["City"].nunique()
avg_aqi = df["AQI Value"].mean()
max_aqi = df["AQI Value"].max()
min_aqi = df["AQI Value"].min()
cat_counts = df["AQI Category"].value_counts()
percentages = (cat_counts / cat_counts.sum()) * 100

plt.figure(figsize=(8, 8))
cat_counts.plot(kind="pie", startangle=90, labels=None)
plt.title("AQI Category Distribution")
plt.ylabel("")

legend_labels = [
    f"{cat} ({percent:.1f}%)"
    for cat, percent in zip(cat_counts.index, percentages)
]

plt.legend(legend_labels, loc="center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig("aqi_category_pie.png")
plt.close()


country_avg = df.groupby("Country")["AQI Value"].mean()
top5 = country_avg.sort_values(ascending=False).head(5)

plt.figure()
top5.plot(kind="bar")
plt.title("Top 5 Most Polluted Countries")
plt.xlabel("Country")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top5_countries.png")
plt.close()
plt.figure()
df["AQI Value"].plot(kind="hist", bins=20)
plt.title("Distribution of AQI Values")
plt.xlabel("AQI Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("aqi_histogram.png")
plt.close()

doc = SimpleDocTemplate("Global_AQI_Analysis_Report.pdf")
elements = []
styles = getSampleStyleSheet()
elements.append(Paragraph("Global Air Pollution Analysis Report", styles['Heading1']))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Project Summary", styles['Heading2']))
elements.append(Spacer(1, 10))

summary_text = f"""
This dataset contains air quality records from {total_countries} countries 
and {total_cities} cities.

The overall average AQI value is {avg_aqi:.2f}. 
The maximum recorded AQI is {max_aqi}, while the minimum AQI observed is {min_aqi}.

These values indicate noticeable variation in air quality levels across different regions.
"""
elements.append(Paragraph(summary_text, styles['Normal']))
elements.append(Spacer(1, 15))
elements.append(Paragraph(
    "Observation: A significant portion of cities fall under Good and Moderate AQI categories, "
    "while a smaller percentage fall under Very Unhealthy and Hazardous levels.",
    styles['Normal']
))
elements.append(Spacer(1, 20))
elements.append(Paragraph("AQI Category Distribution", styles['Heading2']))
elements.append(Spacer(1, 10))
elements.append(Image("aqi_category_pie.png", width=4*inch, height=4*inch))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Top 5 Most Polluted Countries (Average AQI)", styles['Heading2']))
elements.append(Spacer(1, 10))

table_data = [["Country", "Average AQI"]]

for country, value in top5.items():
    table_data.append([country, round(value, 2)])

table = Table(table_data)

table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER')
]))

elements.append(table)
elements.append(Spacer(1, 20))
elements.append(Image("top5_countries.png", width=4*inch, height=3*inch))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Distribution of AQI Values", styles['Heading2']))
elements.append(Spacer(1, 10))
elements.append(Image("aqi_histogram.png", width=4*inch, height=3*inch))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Conclusion", styles['Heading2']))
elements.append(Spacer(1, 10))

conclusion_text = """
This analysis highlights global air quality trends and identifies countries 
with comparatively higher pollution levels. The visualizations provide a clear 
understanding of AQI distribution patterns and pollution intensity.

The analysis is based on the available dataset and may vary with real-time AQI changes.

This project demonstrates the practical application of Python for environmental 
data analysis and automated report generation.
"""

elements.append(Paragraph(conclusion_text, styles['Normal']))

doc.build(elements)

print("PDF Report Generated Successfully!")