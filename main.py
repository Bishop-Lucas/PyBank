import pandas as pd
import os

# creating the path
data = "PyBank/Resources/budget_data.csv"

output = open("PyBank/Resources/Pybank_output.txt", "a")
data_pd =pd.read_csv(data)


      

total = data_pd["Profit/Losses"].sum()
max = data_pd["Profit/Losses"].max()
min = data_pd["Profit/Losses"].min()
average = data_pd["Profit/Losses"].mean()
months = data_pd["Profit/Losses"].count()

average = round(average,2)


min_month = data_pd.loc[data_pd["Profit/Losses"] == min]
max_month = data_pd.loc[data_pd["Profit/Losses"] == max]
#max_month = data_pd.loc[max]
max_m = list(max_month['Date'])
min_m = list(min_month['Date'])

ma = ""
mi = ""

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
        
ma = listToString(max_m)
mi = listToString(min_m)
print(ma)

L1 = "Financial Analysis"
L2 = "---------------------------------"
L3 = "Total Months: " + str(months)
L4 = "Total: " + "$" + str(total)
L5 = "Average Change: " + "$" + str(average)
L6 = "Greatest Increase in Profits: " + ma + '  ' + "($" + str(max) + ")"
L7 = "Greatest Decrease in Profits: " + mi + '  ' + "($" + str(min) + ")"
L8 = '\n'+L1+'\n'+L2+'\n'+L3+'\n'+L4+'\n'+L5+'\n'+L6+'\n'+L7
    
print(L8)
output.write(L8)