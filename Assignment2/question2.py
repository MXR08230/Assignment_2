import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./data.csv")
data.head()

#Show the basic statistical description about the data.
print("data statistical description\n", data.describe())

#Check if the data has null values. a. Replace the null values with the mean
data.isnull().any()
data.fillna(data.mean(), inplace=True)
print("Null re-check \n", data.isnull().any())

#Select at least two columns and aggregate the data using: min, max, count, mean.
dt_agg = data.agg({'Maxpulse':['min','max','count','mean'],'Calories':['min','max','count','mean']})
print("aggregate data \n", dt_agg)

#Filter the dataframe to select the rows with calories values between 500 and 1000
print("Calories data between 500 and 1000 \n", data.loc[(data['Calories']>500)&(data['Calories']<1000)], "\n")

# 6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
print("Calories>500 and pulse<100 \n", data.loc[(data['Calories']>500)&(data['Pulse']<100)], "\n")

# 7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = data[['Duration','Pulse','Calories']]
print("modified dataframe with all columns except Maxpulse \n", df_modified.head(), "\n")

# 8. Delete the “Maxpulse” column from the main df dataframe
print("After deleting the Maxpulse column \n", data.drop('Maxpulse', axis=1).head(), "\n")

# 9. Convert the datatype of Calories column to int datatype.
data['Calories'] = data['Calories'].astype(int)
print(data.dtypes, "\n")

# 10. Using pandas create a scatter plot for the two columns (Duration and Calories).
data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')
plt.show()