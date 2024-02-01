#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:47:42 2024

@author: christo
"""

"""
Question 1:
What is the highest rated movie in the dataset? 

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Calculate the highest rating.
max_rating = max(df["Rating"])

print(max_rating)

#Made a new dataset with only the movies with a rating of 9.0 and higher.
df1 = df[df["Rating"] > 8.9]

print(df1)

"""
I found out what the highest rating for a movie is and filtered the df so that
the movies with a rating of 9.0 would show. And only Th Dark Knight showed in the new 
dataset.

Also

To get the highest rated movie. Go to the Variable Explorer and open df.
Then filter the ratings from the highest to the lowest.
There one will see that The Dark Knight is the highest rated movie.
"""

"""
Question 2:
What is the average revenue of all movies in the dataset? 

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Removing all the rwos with a NaN
df.dropna(inplace=True)

#Calculating the average revenue in millions.
avg_revenue = sum(df["Revenue (Millions)"])/len(df)

print(avg_revenue)


"""
Question 3:
What is the average revenue of movies from 2015 to 2017 in the dataset?

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Removing rows with Nan.
df.dropna(inplace=True)

#Creating a new dataset so that I only have years 2015 to 2017.
df2 = df[df["Year"] > 2014]
df2 = df2[df2["Year"]< 2018]

#Calculating the average revenue.
avg_revenue1 = sum(df2["Revenue (Millions)"])/len(df2)

print(avg_revenue1)

"""
Question 4:
How many movies were released in the year 2016? 
   
"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Calculate and print the number of movies from 2016.
print(df["Year"].value_counts()[2016])


"""
Question 5:
How many movies were directed by Christopher Nolan? 

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")


#Calculate and print the number of movies from Christopher Nolan.
print(df["Director"].value_counts()["Christopher Nolan"])


"""
Question 6:
How many movies in the dataset have a rating of at least 8.0?

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Creating a new dataset with all of the movies with rating 8.0 and above.
df3 = df[df["Rating"] > 7.9]

#Calculating the length of the df3 dataset.
print(len(df3))


"""
Question 7 :
What is the median rating of movies directed by Christopher Nolan? 

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Creating a dataset with only Christopher Nolen movies.
Christopher_Nolan = df[df["Director"] == 'Christopher Nolan']

#Creating a new dataset with only the rating of his movies.
mean_rating_CN_movies = (Christopher_Nolan["Rating"])

#Calculating the mean value of all the movie ratings from Christopher Nolan.
mean_rating_CN_movies2 = sum(Christopher_Nolan["Rating"])/len(Christopher_Nolan)

print(mean_rating_CN_movies2)


"""
Question 8 :
Find the year with the highest average rating? 

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Calculating the number of movies per year.
years = df['Year'].value_counts()


#Creating a new dataset with all the years and the number of movies.
years2 = years[years >= 44]

#Calculating the average of each year on it's own and creating a new dataset with it.
year_avg_score = df.loc[df['Year'].isin(years2.index)].groupby('Year')['Rating'].mean()

"""
To find the year with the highest average rating, one can open the Variable Explorer and filter the 
year_avg_score from highest rating to the lowest to see the year with the highest average rating.

"""

"""
Question 9 :
What is the percentage increase in number of movies made between 2006 and 2016? 

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

years = df['Year'].value_counts()



x = (years.pct_change())*(-1)*(100)

"""
One can get the percentage change by going to the variable explorere.
Once there you can open up dataframe "x" where one can see that the percentage
increase between the years of 2006 - 2016 is 57%.

"""

"""
Question 10 :
Find the most common actor in all the movies?

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

#Split the actors into more columns.
df2 = df['Actors'].str.split("," ,expand = True)

#Renaming column names.
df2.rename(columns={0: "A", 1: "B", 2: "C", 3: "D"}, inplace=True)

#Filling all NaN with x.
df2[:].fillna("x",inplace=True)

#Trying to remove blank spaces.
df2["A"] = df2["A"].apply(lambda x: x.strip())
df2["B"] = df2["B"].apply(lambda x: x.strip())
df2["C"] = df2["C"].apply(lambda x: x.strip())
df2["D"] = df2["D"].apply(lambda x: x.strip())

#Combining columns into one column
df3 = df2["A"]
df4 = df2["B"]
df5 = df2["C"]
df6 = df2["D"]
df7 = pd.concat([df3,df4,df5,df6],ignore_index=True)

#Calculating the highest used actor.
Counts1 = df7[:].value_counts()

print(max(Counts1))


"""
When one goes to the variable explorer and open Counts1,
we can see that Mark Whalberg was used the most with 15 times.

"""

"""
Question 11 :
How many unique genres are there in the dataset?
    
"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")


#Split the actors into more columns.
df2 = df["Genre"].str.split("," ,expand = True)

#Renaming column names.
df2.rename(columns={0: "A", 1: "B", 2: "C"}, inplace=True)


#Filling all NaN with x.
df2[:].fillna("x",inplace=True)

#Trying to remove blank spaces.
df2["A"] = df2["A"].apply(lambda x: x.strip())
df2["B"] = df2["B"].apply(lambda x: x.strip())
df2["C"] = df2["C"].apply(lambda x: x.strip())


#Combining columns into one column
df3 = df2["A"]
df4 = df2["B"]
df5 = df2["C"]

df7 = pd.concat([df3,df4,df5],ignore_index=True)

#Calculating the highest used actor.
Counts1 = df7[:].value_counts()

#Printing number of genres but subtracting 1 for the "x" that filled all the NaN.
print(len(Counts1)-1)

"""
Question 12:
Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.

"""

import pandas as pd

#Read the movie file.
df = pd.read_csv("movie_dataset.csv")

corr_matrix = df.corr()[:]