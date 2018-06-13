

import pandas as pd
import numpy as np
# This is for printing the version of pandas
#print(pd.__version__)

print(pd.Series(['San Francisco', 'San Jose', 'Sacramento',"America", "San paulo"]));
# This uses pandas series
print()


city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
ranking = pd.Series([20, 10, 2])
stars = pd.Series([1,3,4,6])
#This too uses pandas series

 
print(pd.DataFrame({ 'City name': city_names, 'Population': population, 'Ranking': ranking, 'Stars':stars }))
#This example uses dataframes
print()
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())
 
print()
print(california_housing_dataframe.head())
 
print()
#This is a graphing tool and you all you you can't graph in the console
#print(california_housing_dataframe.hist('housing_median_age'))
 
print()
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(cities['City name'])
 
print()
print(cities['Population'])
 
 
print()
print(cities['City name'][1])
 
print("1**************************************************")
print(cities[0:2])
 
print()
 
print("2**************************************************")
# this is for manipulating the data
print(population / 1000)
 
 
print("3**************************************************")
#data manipulation
print("Sandiego "+city_names)


#Numpy example
print("Numpy example")
print(np.log(population))

print()


#maping lamda expression to dataset
print("Mapping lamda expression to lamda")
print(population.apply(lambda val: val >1000000))

print()
#Modifying dataframes in a straight forward manner
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)


#Excercises
print("***********************************Excercise")
cities['Area square miles > 50'] =  cities['Area square miles'].apply(lambda val: val >50)
cities['Begins with san']= cities['City name'].apply(lambda val: val.startswith("San"))

cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities)


print()
print("********************************")
print(city_names.index)
print()
print(cities.index)


print()
print("********************************")
print(cities.reindex([2, 0, 1]))



print()
print("***************************************")
print(cities.reindex(np.random.permutation(cities.index)))


print()
print("***************************************")
print(cities.reindex(np.random.permutation(cities.index)))


print()
print("*****************************************")
print(cities.reindex([0, 4, 5, 2]))
#values that are not in the table will be ordered as NaN

