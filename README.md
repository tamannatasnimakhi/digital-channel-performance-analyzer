# Digital Channel Performance Analyzer

## Project Overview

This project demonstrates an end-to-end analytics workflow for digital channel performance data.

The project takes raw and intentionally imperfect campaign data, validates and cleans it using Python, calculates key performance indicators, generates automated business insights, and prepares an analytics-ready dataset for an interactive Power BI dashboard.

The goal is to demonstrate how digital communication data can be transformed into useful information for campaign and channel decision-making.

## Analytics Workflow

Raw CSV Data  
→ Data Quality Validation  
→ Python Data Cleaning  
→ KPI Calculation  
→ Channel & Campaign Analysis  
→ Automated Business Insights  
→ Processed Dataset  
→ Power BI Dashboard

## Dataset

The raw dataset contains 50 digital performance records across:

- LinkedIn
- Instagram
- Website

The data covers three campaigns:

- Sustainability Campaign
- Product Innovation
- Employer Branding

Content types include:

- Video
- Article
- Image

The dataset intentionally contains common data-quality problems to simulate a more realistic analytics workflow.

## Data Quality Process

Python is used to identify and handle several data-quality issues before reporting.

The raw dataset contained:

- Missing KPI values
- Duplicate records
- Inconsistent channel naming
- Inconsistent text formatting
- An invalid negative impression value

The cleaning pipeline:

1. Converts dates into a consistent datetime format.
2. Standardizes channel and content-type names.
3. Removes duplicate records.
4. Removes impossible impression values.
5. Removes records with missing critical KPI values.
6. Validates the cleaned dataset before analysis.

The process reduced the dataset from **50 raw records to 46 validated records** with no missing KPI values remaining.

## Key Performance Indicators

### Impressions

The number of times digital content was displayed.

### Click-Through Rate (CTR)

Measures how efficiently impressions generate clicks.

CTR = Clicks / Impressions × 100

### Engagement Rate

Measures how efficiently impressions generate audience interactions.

Engagement Rate = Engagements / Impressions × 100

## Python Analysis

Python and Pandas are used to aggregate performance at both channel and campaign level.

The analysis automatically identifies:

- Channel with the highest CTR
- Channel with the highest engagement rate
- Channel generating the greatest reach
- Campaign with the highest CTR
- Campaign with the highest engagement rate
- Campaign generating the greatest reach
- Performance differences between channels

Aggregate KPIs are calculated using total clicks, engagements and impressions rather than averaging individual percentages.

## Automated Business Insights

The Python pipeline automatically converts calculated performance results into human-readable business findings.

Example outputs include:

- Website has the highest click-through rate at approximately 8.56%.
- Instagram has the highest engagement rate at approximately 11.88%.
- Instagram generated the highest channel reach with approximately 279,800 impressions.
- Product Innovation achieved the highest campaign CTR at approximately 5.73%.
- Product Innovation achieved the highest campaign engagement rate at approximately 9.95%.

The insight generation is rule-based and data-driven. It is designed to demonstrate how repetitive analytical interpretation can be automated without presenting the functionality as generative AI.

## Power BI Dashboard

The cleaned dataset is exported from Python and used as the data source for an interactive Power BI dashboard.

The dashboard includes headline KPIs for:

- Total Impressions
- Total Clicks
- Total Engagements
- Overall CTR
- Overall Engagement Rate

It also compares channel and campaign performance across reach, engagement volume, CTR and engagement rate.

Interactive slicers allow the user to filter the dashboard by:

- Campaign
- Content type

DAX measures dynamically recalculate CTR and engagement rate according to the active filter context.

## Key Insights

The complete cleaned dataset generated approximately:

- **659K impressions**
- **35K clicks**
- **61K engagements**
- **5.37% overall CTR**
- **9.27% overall engagement rate**

Channel analysis shows that:

- **Website** achieves the highest CTR, indicating the strongest click efficiency.
- **Instagram** achieves the highest engagement rate and total reach, indicating stronger audience interaction and exposure.
- Different channels therefore perform better for different communication objectives.

Campaign analysis shows that:

- **Product Innovation** generates the highest campaign reach.
- **Product Innovation** also achieves the highest CTR and engagement rate.
- Campaign performance should be evaluated using both volume and efficiency metrics rather than reach alone.

## Tools Used

- **Python** — data validation, cleaning, KPI calculation and automated analysis
- **Pandas** — data transformation, aggregation and quality processing
- **Power BI** — interactive dashboard development and visualization
- **DAX** — dynamic KPI calculations and filter-aware measures
- **CSV** — raw and processed data exchange

## Project Structure

```text
digital-channel-performance-analyzer/
│
├── data/
│   ├── digital_channels.csv
│   ├── processed_digital_channels.csv
│   └── business_insights.txt
│
├── main.py
├── digital_channel_performance_dashboard.pbix
└── README.md
```

## Skills Demonstrated

- Data cleaning and validation
- Data quality management
- Python and Pandas
- KPI development
- Data aggregation
- Digital channel analytics
- Campaign performance analysis
- Automated insight generation
- Power BI dashboard development
- DAX measures
- Interactive reporting
- Translating analytical results into business insights
