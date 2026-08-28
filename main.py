import pandas as pd


# =========================================================
# 1. LOAD RAW DATA
# =========================================================

df = pd.read_csv("data/digital_channels.csv")

print("Raw rows:", len(df))


# =========================================================
# 2. DATA QUALITY CHECK
# =========================================================

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nChannel values before cleaning:")
print(df["channel"].unique())


# =========================================================
# 3. CLEAN DATA
# =========================================================

# Convert date text into real dates.
# Invalid dates become missing values instead of crashing Python.
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Standardize channel names.
# LinkedIn, linkedin and LINKEDIN all become "linkedin" first.
df["channel"] = (
    df["channel"]
    .str.strip()
    .str.lower()
)

# Convert standardized names into professional display names.
channel_names = {
    "linkedin": "LinkedIn",
    "instagram": "Instagram",
    "website": "Website"
}

df["channel"] = df["channel"].replace(channel_names)

# Standardize other text columns.
df["content_type"] = (
    df["content_type"]
    .str.strip()
    .str.title()
)

df["campaign"] = df["campaign"].str.strip()

# Remove duplicate records.
df = df.drop_duplicates()

# Remove impossible data.
# Impressions cannot be zero or negative.
df = df[df["impressions"] > 0]

# Remove rows missing important KPI values.
df = df.dropna(
    subset=[
        "date",
        "impressions",
        "clicks",
        "engagements"
    ]
)


# =========================================================
# 4. CALCULATE ROW-LEVEL KPIs
# =========================================================

df["ctr"] = (
    df["clicks"]
    / df["impressions"]
    * 100
).round(2)

df["engagement_rate"] = (
    df["engagements"]
    / df["impressions"]
    * 100
).round(2)


# =========================================================
# 5. CHANNEL PERFORMANCE ANALYSIS
# =========================================================

channel_performance = df.groupby("channel")[[
    "impressions",
    "clicks",
    "engagements"
]].sum()

channel_performance["ctr"] = (
    channel_performance["clicks"]
    / channel_performance["impressions"]
    * 100
)

channel_performance["engagement_rate"] = (
    channel_performance["engagements"]
    / channel_performance["impressions"]
    * 100
)

print("\nChannel Performance:")
print(channel_performance.round(2))


# =========================================================
# 6. CAMPAIGN PERFORMANCE ANALYSIS
# =========================================================

campaign_performance = df.groupby("campaign")[[
    "impressions",
    "clicks",
    "engagements"
]].sum()

campaign_performance["ctr"] = (
    campaign_performance["clicks"]
    / campaign_performance["impressions"]
    * 100
)

campaign_performance["engagement_rate"] = (
    campaign_performance["engagements"]
    / campaign_performance["impressions"]
    * 100
)

print("\nCampaign Performance:")
print(campaign_performance.round(2))


# =========================================================
# 7. AUTOMATIC PERFORMANCE FINDINGS
# =========================================================

best_ctr_campaign = campaign_performance["ctr"].idxmax()
best_engagement_campaign = campaign_performance["engagement_rate"].idxmax()
best_ctr_channel = channel_performance["ctr"].idxmax()
best_engagement_channel = channel_performance["engagement_rate"].idxmax()

print("\nPerformance Findings:")
print("Best CTR Campaign:", best_ctr_campaign)
print("Best Engagement Rate Campaign:", best_engagement_campaign)
print("Best CTR Channel:", best_ctr_channel)
print("Best Engagement Rate Channel:", best_engagement_channel)


# =========================================================
# 8. AUTOMATED BUSINESS INSIGHTS
# =========================================================

highest_reach_channel = channel_performance["impressions"].idxmax()
highest_reach_campaign = campaign_performance["impressions"].idxmax()
lowest_ctr_channel = channel_performance["ctr"].idxmin()

ctr_difference = (
    channel_performance["ctr"].max()
    - channel_performance["ctr"].min()
)

engagement_difference = (
    channel_performance["engagement_rate"].max()
    - channel_performance["engagement_rate"].min()
)

insights = [
    (
        f"{best_ctr_channel} has the highest click-through rate "
        f"at {channel_performance.loc[best_ctr_channel, 'ctr']:.2f}%."
    ),
    (
        f"{best_engagement_channel} has the highest engagement rate "
        f"at {channel_performance.loc[best_engagement_channel, 'engagement_rate']:.2f}%."
    ),
    (
        f"{highest_reach_channel} generated the highest reach with "
        f"{channel_performance.loc[highest_reach_channel, 'impressions']:,.0f} impressions."
    ),
    (
        f"{best_ctr_campaign} is the strongest campaign for click efficiency "
        f"with a CTR of {campaign_performance.loc[best_ctr_campaign, 'ctr']:.2f}%."
    ),
    (
        f"{best_engagement_campaign} has the highest campaign engagement rate "
        f"at {campaign_performance.loc[best_engagement_campaign, 'engagement_rate']:.2f}%."
    ),
    (
        f"The CTR gap between the strongest and weakest channels is "
        f"{ctr_difference:.2f} percentage points."
    ),
    (
        f"{highest_reach_campaign} generated the highest campaign reach "
        f"with {campaign_performance.loc[highest_reach_campaign, 'impressions']:,.0f} impressions."
    )
]

print("\nAutomated Business Insights:")
for number, insight in enumerate(insights, start=1):
    print(f"{number}. {insight}")


# =========================================================
# 9. DATA QUALITY SUMMARY
# =========================================================

print("\nData Quality Summary:")
print("Clean rows:", len(df))

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nChannels after cleaning:")
print(df["channel"].unique())

print("\nContent types after cleaning:")
print(df["content_type"].unique())


# =========================================================
# 10. EXPORT CLEAN DATA FOR POWER BI
# =========================================================

df.to_csv(
    "data/processed_digital_channels.csv",
    index=False
)


# =========================================================
# 11. EXPORT AUTOMATED INSIGHTS
# =========================================================

with open(
    "data/business_insights.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("DIGITAL CHANNEL PERFORMANCE INSIGHTS\n\n")
    for number, insight in enumerate(insights, start=1):
        file.write(f"{number}. {insight}\n")

print("\nProcessed dataset exported successfully.")
print("Business insights exported successfully.")
