import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



df=pd.read_csv(r'C:/Users/KOLLA/Downloads/PYTHONDATASET.csv')
print("DATASET: ",df)
print("DATASET without na values",df.dropna())
print(df.head())
print(df.describe())
print(df.isnull().sum())
sns.set(style="whitegrid")


#OBJECTIVE 1  (SCATTER PLOT)
# Clean and convert population columns
df["Population_Males"] = pd.to_numeric(df["Population_Males"], errors="coerce")
df["Population_Females"] = pd.to_numeric(df["Population_Females"], errors="coerce")
df_clean = df.dropna(subset=["Population_Males", "Population_Females"])
# Create scatter plot using Seaborn
plt.figure(figsize=(7, 6))
sns.scatterplot(
    data=df_clean,
    x="Population_Males",
    y="Population_Females",
    color="blue",
)
plt.title("Scatter Plot of Male vs Female Population")
plt.xlabel("Population Males")
plt.ylabel("Population Females")
plt.show()



#OBJECTIVE 2 (BAR CHART) Population Distribution Across States using Bar Chart
# Filter for only state-level and total area data
states = df[(df["Region"] == "STATE") & (df["Area_type"] == "Total")]
# Convert population to numeric
states.loc[:, "Population_Persons"] = pd.to_numeric(states["Population_Persons"], errors="coerce")
# Sort states by population
states = states.sort_values("Population_Persons", ascending=True)
# Plot bar chart
plt.figure(figsize=(12, 8))
plt.barh(states["Name"], states["Population_Persons"], color='skyblue')
plt.xlabel("Population")
plt.title("Population Distribution Across States")
#plt.gca().invert_yaxis() Highest population on top
plt.tight_layout()
plt.show()





#OBJECTIVE 3(PIE CHART) Urban vs Rural Population Distribution in India using pie chart
# Filter rural and urban data
data = df[(df["Region"] == "INDIA") & (df["Area_type"].isin(["Rural", "Urban"]))]
# Use shades of blue
colors = ["lightgreen", "deepskyblue"]
# Plot pie chart
plt.pie(data["Population_Persons"], labels=data["Area_type"],  autopct="%1.1f%%",colors=colors, startangle=90)
plt.title("Urban vs Rural Population in India")
plt.axis("equal")
plt.show()






#OBJECTIVE 4(PAIR PLOT) Sub-District-wise Relationship Analysis using Pair Plot
df.columns = df.columns.str.strip()
# Use correct column names from your dataset
data = df[df["Region"] == "SUB-DISTRICT"][[
    "Population_Persons", 
    "Number_of_households", 
    "Area", 
    "Population_per_sq_km."]]
data = data.apply(pd.to_numeric, errors='coerce').dropna()
sns.pairplot(data)
plt.suptitle("Sub-Districts: Population, Households, Area & Density", y=1.02)
plt.show()





#OBJECTIVE 5 (HEAT MAP) Heatmap for Number_of_towns vs Population_per_sq_km. using heat map
# Create a heatmap with a different color map
plt.figure(figsize=(8,5))
plt.figure(figsize=(8,5))
corr = df[['Number_of_towns', 'Population_per_sq_km.','Number_of_households','Population_Persons']].corr()
print(corr)
colors=["lightgreen","orange"]
sns.heatmap(corr, annot=True, cmap=colors, fmt='.2f', linewidths=5)  # Changed cmap here
plt.title("Heatmap for Number_of_towns vs Population_per_sq_km.")
plt.show()





#OBJECTIVE 6 (BOX PLOT) Distribution of Number of Households by Region using box plot
# Convert to numeric
df["Number_of_households"] = pd.to_numeric(df["Number_of_households"], errors="coerce")
# Create box plot with a single color
plt.figure(figsize=(10, 6))
sns.boxplot(x="Region", y="Number_of_households", data=df, color="salmon")  # You can change "skyblue" to any other color
plt.title("Distribution of Number of Households by Region")
plt.xlabel("Region")
plt.ylabel("Number of Households")
plt.show()








#OBJECTIVE 7(LINE PLOT) compare Number_of_towns vs Number_of_households using line plot
plt.figure(figsize=(8,5))
#Creating a line plot 
sns.lineplot(data=df,x='Number_of_towns',y='Number_of_households',marker='o',color='blue')
plt.title('Number_of_towns vs Number_of_households')
plt.xlabel('Number_of_towns')
plt.ylabel('Number_of_households')
plt.show()























































































































































