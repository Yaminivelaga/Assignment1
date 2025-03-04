sns.boxplot(x='test preparation course', y='math score', data=data)
plt.title('Math Scores by Test Preparation Course Completion')
plt.xlabel('Test Preparation Course')
plt.ylabel('Math Score')
plt.show()
plt.savefig("Math Scores by Test Preparation Course Completion.png")  
plt.close()

sns.barplot(x='gender', y='final_grade', hue='gender', data=data, palette='coolwarm', legend=False)
plt.title('Average Final Grades by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade')
plt.show()
plt.savefig("Average Final Grades by Gender.png")  
plt.close()

plt.hist(data['final_grade'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Final Grades')
plt.xlabel('Final Grade')
plt.ylabel('Frequency')
plt.show()
plt.savefig("Distribution of Final Grades.png")  
plt.close()

sns.stripplot(x='parental level of education', y='math score', data=data)
plt.title('Math Scores by Parental Level of Education')
plt.xlabel('Parental Level of Education')
plt.xticks(rotation=45)
plt.ylabel('Math Score')
plt.show()
plt.savefig("Math Scores by Parental Level of Education.png")  
plt.close()

# Pie chart for race/ethnicity
data['race/ethnicity'].value_counts().plot.pie(
    autopct='%1.1f%%',
    colors=['#FF9999', '#FFCC99', '#FFB266', '#FF6666', '#FF9966'],
    startangle=90
)
plt.title('Distribution of Race/Ethnicity')
plt.ylabel('')  # Remove y-axis label for clarity
plt.show()
plt.savefig("Distribution of Race.png")  
plt.close()
