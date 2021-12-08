import pandas as pd

df = pd.read_excel(r'C:\Users\Slaye\Documents\Food Data Program.xlsx')

def Distance():
    global distance_choice
    global zero_stage

    while True:
        try:
            distance_choice = float(input("What is the maximum distance you are willing to travel?  "))
            zero_stage = (df[df["Distance"] <= distance_choice])
            return (zero_stage)
        except Exception as e:
            print(e)

def Style():
    global style_choice
    global first_stage
    style_choice = (str(input("What style of food?  ")))

    if style_choice in zero_stage.values:
        first_stage = (zero_stage[zero_stage["Style"] == style_choice])
    else:
        print("Passed/Incorrect Input")
        first_stage = zero_stage

def Type():
    global type_choice
    global second_stage
    type_choice = input("What type of food? ")

    if type_choice in first_stage.values:
        second_stage = (first_stage[first_stage["Type"] == type_choice])
    else:
        print("Passed/Incorrect Input")
        second_stage = first_stage

def new():
    global new_choice
    global final_stage
    new_choice = input("Old or New? ")

    if new_choice in second_stage.values:
        final_stage = second_stage[second_stage["New"] == new_choice]
    else:
        print("Passed/Incorrect Input")
        final_stage = second_stage




###############################
Distance()

print("\n")
print(df["Style"].unique())
print("\n")

Style()

print(df["Type"].unique())

Type()
new()



samplesize = int(input("How many restaurants? "))

def Random():
    #samplesize = input("How many restaurants? ")
    sample = final_stage.sample(n=samplesize, replace=False)
    print(sample)

Random()

########### Replace current code with SQL

df.execute(SELECT Name)























