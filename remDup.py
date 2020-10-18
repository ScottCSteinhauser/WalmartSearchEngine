# importing pandas package 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("allinfo.csv") 
  
# sorting by first name 
data.sort_values("title", inplace = True) 
  
# dropping ALL duplicte values 
data.drop_duplicates(subset ="title", 
                     keep = "first", inplace = True) 
  
# displaying data 
data.to_csv('nodups2.csv', index = False) 