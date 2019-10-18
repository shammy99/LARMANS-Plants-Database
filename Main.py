import pandas as pd
from Price_List_Updater import Dictionary_Generator
print("Dictionary Generator Imported!")
from Andreasens_Prices import Andreasens_Plant_Prices
print("Andreasens Plant Dictionary Imported!")
from Downes_Nursery_Prices import Downes_Plant_Prices
print("Downes Nursery Plant Dictionary Imported!")
from Budget_Wholesale_Nursery import Budget_Wholesale_Nursery_Plant_Prices
print("Budget Wholesale Nursery Plant Dictionary Imported!")
from Common_Names_Dictionary import Common_Name
print("Common Names Dictionary Imported!")
from Andreasens_Common_Names_List import Andreasens_Common_Name

# Reads Empty Plant Schedule
Empty_BOQ = pd.read_csv("Empty_BOQ.csv")
Num_Items = len(Empty_BOQ)
# Tests If plant is Recognisable by it's Common Name
Not_in_Database = []
def Search_Common_Name(Name):
    Name = Name.lower()
    print(Name)
    if Name in Andreasens_Common_Name:
        print("Common Name Exists in Nursery!")
        print(Name)
        Count = Andreasens_Common_Name.count(Name)
        if Count == 1:
            Index = Andreasens_Common_Name.index(Name)
            print(Index)
# Stores the Calculatated Values in the Lists
def Value_Append(Nursery,Rate,Total_Price):
    if Nursery == "Andreasens":
        Andreasens_Rates.append(Rate)
        Andreasens_Total_Prices.append(Total_Price)
    elif Nursery == "Downes":
        Downes_Rates.append(Rate)
        Downes_Total_Prices.append(Total_Price)
    elif Nursery == "Budget":
        Budget_Nursery_Rates.append(Rate)
        Budget_Nursery_Total_Prices.append(Total_Price)
    else:
        print("Re-Check the spelling of the Nursery!")
# Assigns a Zero Value and stores it in the lists      
def Zero_Value(Nursery):
    if Nursery == "Andreasens":
        print("Plant is not in Andreasens database")
        Value_Append("Andreasens",0,0)
    elif Nursery == "Downes":
        print("Plant is not in Downes database")
        Value_Append("Downes",0,0)
    elif Nursery == "Budget":
        print("Plant is not in Budget Wholesale Nursery database")
        Value_Append("Budget",0,0)
    else:
        print("Re-Check the spelling of the Nursery!")
# Exports the table
def Export_Table():
    Name_Table = pd.DataFrame({'Botanical Name': Names})
    Size_Table = pd.DataFrame({'Size': Sizes})
    QTY_Table = pd.DataFrame({'QTY': QTYs})
    Andreasens_Rate_Table = pd.DataFrame({'Andreasens Rate': Andreasens_Rates})
    Andreasens_Total_Price_Table = pd.DataFrame({'Andreasens Total Price': Andreasens_Total_Prices})
    Downes_Rate_Table = pd.DataFrame({'Downes Rate': Downes_Rates})
    Downes_Total_Price_Table = pd.DataFrame({'Downes Total Price': Downes_Total_Prices})
    Budget_Nursery_Rate_Table = pd.DataFrame({'Budget Wholesale Nursery Rate': Budget_Nursery_Rates})
    Budget_Nursery_Price_Table = pd.DataFrame({'Budget Wholesale Nursery Price': Budget_Nursery_Total_Prices})
    Final_Table = pd.concat([Name_Table, Size_Table, QTY_Table, Andreasens_Rate_Table, Andreasens_Total_Price_Table,
                             Downes_Rate_Table,Downes_Total_Price_Table,Budget_Nursery_Rate_Table,Budget_Nursery_Price_Table], axis=1)
    print(Final_Table)
    Final_Table.to_csv("Completed Plant Schedule.csv")
    print("The Table has been stored as 'Completed Plant Schedule.csv'! ")
# This is where all the data will be stored
Names = []
Sizes = []
QTYs = []
Andreasens_Rates = []
Andreasens_Total_Prices = []
Downes_Rates = []
Downes_Total_Prices = []
Budget_Nursery_Rates = []
Budget_Nursery_Total_Prices = []
# Generates The Final Plant Schedules including Rates and Total Prices
def BOQ_Generator():
    for i in range(Num_Items):
        Name = Empty_BOQ.at[i,"Botanic Name"]
        Common_Name = Empty_BOQ.at[i,"Common Name"].lower()
        Size = Empty_BOQ.at[i,"Size"]
        QTY = Empty_BOQ.at[i,"QTY"]
        Names.append(Name)
        Sizes.append(Size)
        QTYs.append(QTY)
        Name_Plus_Price = str(Name) + " " + str(Size)
        print(Name_Plus_Price)
        # Andreasens Nursery
        if Name_Plus_Price in Andreasens_Plant_Prices:
            print("Plant is in database")
            Andreasens_Rate = Andreasens_Plant_Prices[Name_Plus_Price]
            Andreasens_Total_Price = Andreasens_Rate * QTY
            print(Andreasens_Total_Price)
            Value_Append("Andreasens",Andreasens_Rate,Andreasens_Total_Price)
        elif Name_Plus_Price not in Andreasens_Plant_Prices and Common_Name in Andreasens_Common_Name:
            print("Botanical Name is NOT Recognised but the Common Name is recognised!" )
            Zero_Value("Andreasens") # TEMPORARY - Will be changed once Search_Common_Name is finished
        else:
            Zero_Value("Andreasens")
        # Downes Nursery
        if Name_Plus_Price in Downes_Plant_Prices:
            print("Plant is in database")
            Downes_Rate = Downes_Plant_Prices[Name_Plus_Price]
            Downes_Total_Price = Downes_Rate * QTY
            print("At Downes Nursery, the price is: " + str(Downes_Total_Price))
            Value_Append("Downes",Downes_Rate,Downes_Total_Price)
        else:
            Zero_Value("Downes")
        # Budget Wholesale Nursery
        if Name_Plus_Price in Budget_Wholesale_Nursery_Plant_Prices:
            print("Plant is in database")
            Budget_Nursery_Rate = Budget_Wholesale_Nursery_Plant_Prices[Name_Plus_Price]
            Budget_Nursery_Total_Price = Budget_Nursery_Rate * QTY
            print("At Budget Nursery, the price is: " + str(Budget_Nursery_Total_Price))
            Value_Append("Budget",Budget_Nursery_Rate,Budget_Nursery_Total_Price)
        else:
            Zero_Value("Budget")
BOQ_Generator()
Export_Table()
