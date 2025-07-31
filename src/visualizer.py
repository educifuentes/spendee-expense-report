import altair as alt
import pandas as pd

def bar_chart_category(summary_df):
    summary_df = summary_df.reset_index()
    return alt.Chart(summary_df).mark_bar().encode(
        x='category',
        y='amount',
        tooltip=['category', 'amount']
    ).properties(
        title='Total Expenses by Category'
    )

def line_chart_monthly(monthly_df):
    monthly_df = monthly_df.reset_index()
    monthly_df['month'] = monthly_df['month'].astype(str)
    return alt.Chart(monthly_df).mark_line(point=True).encode(
        x='month',
        y='amount',
        tooltip=['month', 'amount']
    ).properties(
        title='Monthly Expenses Over Time'
    )