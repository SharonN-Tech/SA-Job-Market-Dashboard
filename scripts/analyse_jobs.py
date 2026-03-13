import pandas as pd
 

#load excel file
file_path="../data/SA_Jobs_raw.xlsx"

df=pd.read_excel(file_path)

#show first rows
print("First 5 rows of the dataset:")
print(df.head())
 
#show dataset info
print("\nDataset info:")
print(df.info())

#count most common skills
skills_series=df["Skills"].dropna()

all_skills=[]

for skills in skills_series:
    split_skills=skills.split(",")
    for skill in split_skills:
        all_skills.append(skill.strip().lower())

from collections import Counter

skill_counts=Counter(all_skills)

print("\nTop 10 most In-Demand Skills:")
print(skill_counts.most_common(10))

import matplotlib.pyplot as plt

top_skills=skill_counts.most_common(10)

skills=[skill[0] for skill in top_skills]
counts=[skill[1] for skill in top_skills]

plt.bar(skills,counts)
plt.title("Top 10 In-Demand Data Skills in South Africa")
plt.xlabel("Skills")
plt.ylabel("Number of Job Listings")

plt.xticks(rotation=45)

plt.show()

top_skills_df=pd.DataFrame(top_skills,
columns=["Skill", "Count" ])

top_skills_df.to_csv("../top_skills.csv",
 index=False)
 
print("Top skills exported to CSV successfully!!!")