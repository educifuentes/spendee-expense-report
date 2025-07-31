def summarize_by_category(df):
    return df.groupby('category')['amount'].sum().sort_values(ascending=False)

def monthly_expenses(df):
    df['month'] = df['date'].dt.to_period('M')
    return df.groupby('month')['amount'].sum()