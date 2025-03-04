sns.boxplot(x='Frailty', y='Grip strength', data=df)
plt.show()
plt.savefig("Grip Strength by Frailty.png")  
plt.close()

# Calculate average grip strength for each age group and frailty status
avg_grip_strength = df.groupby(['Age', 'Frailty'])['Grip strength'].mean().reset_index()

# Create the bar plot
sns.barplot(x='Age', y='Grip strength', hue='Frailty', data=avg_grip_strength, palette='coolwarm')
plt.title('Average Grip Strength by Age and Frailty')
plt.show()
plt.savefig("Average Grip Strength by Age and Frailty.png")  
plt.close()

sns.scatterplot(x='Weight', y='Grip strength', hue='Frailty', data=df, palette='coolwarm')
plt.title('Grip Strength vs weight')
plt.show()
plt.savefig("Grip Strength vs weight.png")  
plt.close()

# Importing necessary library
from scipy.stats import ttest_ind

# Perform T-Test: Comparing Grip Strength in Frail vs Non-Frail Participants
non_frail = df.loc[df['Frailty'] == 0, 'Grip strength']
frail = df.loc[df['Frailty'] == 1, 'Grip strength']


# Conducting the t-test
t_statistic, p_val = ttest_ind(non_frail, frail, equal_var=False)  # Using Welch's t-test

# Display results
print(f"T-Test Results: t-statistic = {t_statistic:.2f}, p-value = {p_val:.4f}")

# Interpretation
if p_val < 0.05:
    print("There is a statistically significant difference in grip strength between frail and non-frail individuals.")
else:
    print("No statistically significant difference in grip strength between frail and non-frail individuals.")
