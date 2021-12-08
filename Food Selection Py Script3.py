import pandas as pd
from pandasql import sqldf
df = pd.read_excel(r'C:\Users\Slaye\Documents\Food Data Program.xlsx')


sqlwhere = "SELECT * FROM df WHERE Style="
style_category = str(input("Enter categories: "))
print(sqldf(sqlwhere + "'" + style_category + "'"))

sql_in = "SELECT * FROM df WHERE Style IN"
style_categories = str(input("Enter categories seperated by commas: "))
style_list = style_categories.split()

print(style_list[1])

for i in style_list:
    print("'" + style_list[i] + "'")


"'" + style_list[i] + "'"

print(sql_in + " ('" + style_list + "');")
print(sqldf(sql_in + "('" + style_categories + "');"))     #Have to add apostrophes between each value, using split


print(sqldf("SELECT * FROM df WHERE Style IN ('Pizza', 'American');"))



