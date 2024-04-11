import pandas as pd




# =====================================================================
# Series宣言
# =====================================================================
def define_series():
    series_data = [10,15,20,25]
    ser = pd.Series(series_data)
    print(ser)


# =====================================================================
# DataFrame宣言
# =====================================================================
def define_dataframe():
    dataframe_data = ([
        [100, "a", True],
        [150, "b", False],
        [300, "c", False],
        [550, "d", True]
    ])
    df = pd.DataFrame(dataframe_data)   
    
    # Index設定(行名)
    df.index=["01","02","03","04"]

    # Column設定（列）
    df.columns=["A","B","C"]
    # print(df)
    # 列指定
    # print(df["A"])
    # print(df[["B","C"]])
    
    # 行指定
    print(df[0:2])
    # print(df[0])
    
    
    # print(df)

define_dataframe()