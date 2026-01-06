from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

file_path = "/mnt/data/insights_summary.pdf"

doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

content = [
    "INSIGHT SUMMARY\nSpotify Global Chart 2024 – Exploratory Data Analysis",
    "",
    "1. Project Overview",
    "This project analyzes the Spotify Global Top 200 dataset for the year 2024 "
    "to understand music popularity patterns, artist dominance, and chart dynamics. "
    "The analysis focuses on descriptive statistics and exploratory data analysis "
    "without applying predictive models.",
    "",
    "Dataset: 10,600 weekly records from Spotify Global Charts 2024.",
    "",
    "2. Key Insights",
    "",
    "Insight 1: Stream Distribution",
    "The distribution of streams is heavily right-skewed, indicating that a small number "
    "of songs account for a disproportionately large share of total streams.",
    "",
    "Insight 2: Rank and Streams Relationship",
    "Songs with higher chart positions generally receive more streams, although some "
    "exceptions suggest the influence of viral trends and external promotion.",
    "",
    "Insight 3: Artist Dominance",
    "A limited group of artists appears frequently in the charts, reflecting strong brand "
    "presence and sustained popularity.",
    "",
    "Insight 4: Chart Longevity",
    "Most songs remain on the chart for a short period, while only a few achieve long-term "
    "stability across multiple weeks.",
    "",
    "Insight 5: New Entries",
    "Newly released songs represent a smaller portion of the chart, indicating high competition "
    "and barriers to entry.",
    "",
    "3. Conclusion",
    "Spotify Global Chart 2024 demonstrates a highly competitive environment dominated by hit songs "
    "and established artists. Exploratory analysis provides valuable insights into user listening "
    "behavior and market dynamics.",
    "",
    "4. Limitations and Future Work",
    "This analysis does not include audio features from the Spotify API. Future work may integrate "
    "audio characteristics and time-series analysis."
]

for line in content:
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 12))

doc.build(story)

file_path