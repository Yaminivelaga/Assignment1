data = data.drop_duplicates()
data

#Compute Final Grade (Average of Math, Reading, and Writing scores)
data['final_grade'] = data[['math score', 'reading score', 'writing score']].mean(axis=1)
data.head(10)
