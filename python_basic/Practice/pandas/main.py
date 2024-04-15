import pandas as pd

def define_dataframe():
    df = pd.read_csv("./titanic.csv")   
    
    print(df)
    # print(df["Age"]>30)
    # print(df[df["Age"]>30])
    print(df.at[0,"Age"])
    # print(df[df["Age"].isin([20,30,40])])
    
define_dataframe()