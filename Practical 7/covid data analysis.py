import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
s = []
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[10:21,0:3:2])
for i in range(1, len(covid_data)):
    location = covid_data.iloc[i - 1, 1]
    if location == "Afghanistan":
        s.append(i - 1)  # add the row numbers in which row the location is "Afghanistan"
print(covid_data.loc[
          s, "total_cases"])  # I tried another way.

print(covid_data.loc[0:81, "total_cases"])  
date = []
new_cases = []
new_deaths = []
rows = []
rows1 = []
for i in range(1, len(covid_data)):  # sort out the data from the China, and store it into 3 lists.
    country = covid_data.iloc[i - 1, 1]
    if country == "China":
        date.append(covid_data.iloc[i - 1, 0])
        new_cases.append(covid_data.iloc[i - 1, 2])
        new_deaths.append(covid_data.iloc[i - 1, 3])
        rows.append(i - 1)
china_dates = covid_data.iloc[rows, 0]
mean1 = sum(new_deaths) / len(date)
mean2 = sum(new_cases) / len(new_cases)
print('the mean of new deaths in China is',mean1, '\nthe mean of new cases in China is',mean2)
Spain_dates_list = [] #
Spain_dates_list_3 = []
spain_new_cases = [] #
Total_cases = 0
Total_cases_list = [] #
for i in range(1, len(covid_data)):
    location = covid_data.iloc[i - 1, 1]
    if location == "Spain":
        Spain_dates_list.append(covid_data.iloc[i - 1, 0])
        spain_new_cases.append(covid_data.iloc[i - 1, 2])
        Total_cases += covid_data.iloc[i - 1, 2]
        Total_cases_list.append(Total_cases)




fig = plt.figure(figsize=(18, 10), dpi=100) # set the total size and space of the figure
plt.subplots_adjust( wspace=0.5, hspace=0.5)

plt.subplot(2, 3, 1)
plt.boxplot(new_cases, showfliers=False)  # to avoid excessive numerical influence on results
plt.xlabel('new cases from China')
plt.ylabel('numbers of China new cases')
plt.title('Boxplot of China new cases')

plt.subplot(2, 3, 2)
plt.boxplot(new_deaths, showfliers=False)
plt.xlabel('new deaths from China')
plt.ylabel('numbers of China new deaths')
plt.title('Boxplot of China new deaths')

plt.subplot(2, 3, 3)
plt.plot(date, new_cases, 4, 'r+')  # I don't know why there is only one figure created.
plt.ylabel("new cases")
plt.title("The new cases of COVID-19 in China")
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90, fontsize=5)

plt.subplot(2, 3, 4)
plt.plot(date, new_deaths, 4, 'r')
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90, fontsize=5)
plt.ylabel('number of China new deaths')
plt.title('The change with time of China new deaths')

x = plt.subplot(2, 3, 5)
plt.plot(Spain_dates_list, spain_new_cases, 4, 'r')
plt.plot(Spain_dates_list, Total_cases_list, 4, 'r')
plt.xticks(Spain_dates_list[0:len(Spain_dates_list):4], rotation=-90, fontsize=5)
plt.ylabel('new cases and total cases in Spain')
plt.title('The new cases (in blue) and total cases in Spain (in red)')
plt.show()
