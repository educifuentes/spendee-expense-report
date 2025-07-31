from src.loader import load_spendee_data
from src.analyzer import summarize_by_category, monthly_expenses
from src.visualizer import bar_chart_category, line_chart_monthly

import altair as alt

df = load_spendee_data('data/spendee_export.csv')

category_summary = summarize_by_category(df)
monthly_summary = monthly_expenses(df)

bar = bar_chart_category(category_summary)
line = line_chart_monthly(monthly_summary)

bar.save('output/category_expenses.html')
line.save('output/monthly_expenses.html')

print("Charts saved to output/")