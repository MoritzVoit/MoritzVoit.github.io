
#Import relevant libraries and load the csv files into respective Dataframes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')


#Inspecting the Data

print(wood.head())
print(wood.count())
print(wood.describe())
print(wood.columns)
print(wood.dtypes)
print("--------------------------")
print(steel.head())
print(steel.count())
print(steel.describe())
print(steel.columns)
print(steel.dtypes)
print("--------------------------")


# Write a function that will plot the ranking of a given roller coaster over time as a line. 
# Your function should take a roller coaster’s name and a ranking DataFrame as arguments. 
# Make sure to include informative labels that describe your visualization.
 

def plot_rc(rollercoaster, dataframe, parkname):
    coaster_rankings = dataframe[(dataframe["Name"] == rollercoaster) & (dataframe["Park"]== parkname)]
    fig, ax = plt.subplots()
    ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'])
    ax.set_xticks(coaster_rankings['Year of Rank'].values)
    ax.set_yticks(coaster_rankings['Rank'].values)
    ax.invert_yaxis()
    plt.title("{} Rankings".format(rollercoaster))
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.show()
    plt.clf()
    
#Test the function:
#plot_rc('El Toro', wood, 'Six Flags Great Adventure')
#plot_rc('Millennium Force',steel,'Cedar Point')

# Write a function that will plot the ranking of two given roller coasters over time as lines. 
# Your function should take both roller coasters’ names and a ranking DataFrame as arguments. 
# Make sure to include informative labels that describe your visualization.

def plot_rc_2(rollercoaster_1, parkname_1, rollercoaster_2, parkname_2, dataframe):
    coaster_rankings_1 = dataframe[(dataframe["Name"] == rollercoaster_1) & (dataframe["Park"]== parkname_1)]
    coaster_rankings_2 = dataframe[(dataframe["Name"] == rollercoaster_2) & (dataframe["Park"]== parkname_2)]
    fig, ax = plt.subplots()
    ax.plot(coaster_rankings_1['Year of Rank'], coaster_rankings_1['Rank'], color = 'red', label = rollercoaster_1)
    ax.plot(coaster_rankings_2['Year of Rank'], coaster_rankings_2['Rank'], color = 'green', label = rollercoaster_2)
    ax.invert_yaxis()
    plt.title("{} vs. {} Rankings".format(rollercoaster_1, rollercoaster_2))
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend()
    plt.show()
    plt.clf()

#Test the function:
#plot_rc_2('El Toro', 'Six Flags Great Adventure', 'Boulder Dash','Lake Compounce', wood)
#plot_rc_2('Millennium Force',steel,'Cedar Point')


# Write a function that will plot the ranking of the top n ranked roller coasters over time as lines. 
# Your function should take a number n and a ranking DataFrame as arguments. 
# Make sure to include informative labels that describe your visualization.

def plot_n_rc(n, dataframe):
    top_n_rankings = dataframe[dataframe['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(12,12))
    for rollercoaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == rollercoaster]
        ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=rollercoaster)
    ax.set_yticks([i for i in range(1,6)])
    ax.invert_yaxis()
    plt.title("Top {} Rankings".format(n))
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend(loc = 4)
    plt.show()
    plt.clf()

#Test the function:
#plot_n_rc(5, wood)
#plot_n_rc(6, steel)


#Now that you’ve visualized rankings over time, let’s dive into the actual statistics of roller coasters themselves. 
# Captain Coaster is a popular site for recording roller coaster information. Data on all roller coasters documented on 
# Captain Coaster has been accessed through its API and stored in roller_coasters.csv. 
# Load the data from the csv into a DataFrame and inspect it to gain familiarity with the data.


rc = pd.read_csv('roller_coasters.csv')



print("--------------------------")
print(rc.head())
print(rc.count())
print(rc.describe())
print(rc.columns)
print(rc.dtypes)
print("--------------------------")


# Write a function that plots a histogram of any numeric column of the roller coaster DataFrame. 
# Your function should take a DataFrame and a column name for which a histogram should be constructed as arguments. 
# Make sure to include informative labels that describe your visualization.

def plt_hist(dataframe, column_name):
    hist_data = dataframe[column_name].dropna()
    plt.hist(hist_data)
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.title('{} of Rollercoaster'.format(column_name))
    plt.show()
    plt.clf()
    
#Test the function:
#plt_hist(rc, "num_inversions")



# Write a function that creates a bar chart showing the number of inversions for each roller coaster at an amusement park. 
# Your function should take the roller coaster DataFrame and an amusement park name as arguments. 
# Make sure to include informative labels that describe your visualization.

def plt_bar(dataframe, park_name):
    rollercoasters = dataframe[dataframe['park'] == park_name].sort_values('num_inversions', ascending=False)
    names = rollercoasters['name']
    inversions = rollercoasters['num_inversions']
    plt.bar(names, inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names,rotation=90)
    plt.title("Number of Inversion of Rides at {}".format(park_name))
    plt.xlabel('Roller Coaster')
    plt.ylabel('Inversions')
    plt.show()
    plt.clf()


#Test the function:
#plt_bar(rc, 'Parc Asterix')


# Write a function that creates a pie chart that compares the number of operating roller 
# coasters ('status.operating') to the number of closed roller coasters ('status.closed.definitely'). 
# Your function should take the roller coaster DataFrame as an argument. 
# Make sure to include informative labels that describe your visualization.

def plt_pie(dataframe):
    operating = len(dataframe[dataframe.status == 'status.operating'])
    not_operating = len(dataframe[dataframe.status == 'status.closed.definitely'])
    status = [operating,not_operating]
    labels =['operating','not operating']
    plt.pie(status, labels = labels,autopct='%0.1f%%')
    plt.title('Rollercoasters operating vs. indefinitly not working.')
    plt.axis('equal')
    plt.show()
    plt.clf()

#Test the function:
#plt_pie(rc)

# Write a function that creates a scatter plot of speed vs height of the roller coaster DataFrame. 
# Your function should take the roller coaster DataFrame and two-column names as arguments. 
# Make sure to include informative labels that describe your visualization.


def plot_scatter(dataframe, column_1, column_2):
    dataframe = dataframe[dataframe['height'] < 140]
    plt.scatter(dataframe[column_1], dataframe[column_2])
    plt.xlabel(column_1)
    plt.ylabel(column_2)
    plt.title('Speed vs. Height')
    plt.show()
    plt.clf()

#Test the function:
#plot_scatter(rc,'speed','height')




