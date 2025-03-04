#Convert 'Frailty' to 'Binary Values'
df['Frailty'] = df['Frailty'].replace({'N': 0, 'Y': 1})
df

df.to_csv("cleaned_data.csv",index=False)

# Summary Statistics
df.describe()
