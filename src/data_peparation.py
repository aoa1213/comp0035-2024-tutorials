import pandas as pd
from pathlib import Path
import numpy as np

def readfile():
    """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1

        Returns:
        int:Returning value
 
    """
    try:
        # print(Path.cwd())
        # print(Path(__file__))
        data_file_location_1 = Path(__file__).parent.joinpath("tutorialpkg", "data", "paralympics_events_raw.csv")
        dataframe_paralympics_events_raw = pd.read_csv(data_file_location_1)
        data_file_location_2 = Path(__file__).parent.joinpath("tutorialpkg", "data", "paralympics_all_raw.xlsx")
        dataframe_paralympics_all_raw = pd.read_excel(data_file_location_2)
        dataframe_page2 = pd.read_excel(data_file_location_2, sheet_name="medal_standings")

        # put all locaions and dataframe into a array 
        locationarray = [data_file_location_1, data_file_location_2, data_file_location_2]
        dataframearray = [dataframe_paralympics_events_raw, dataframe_paralympics_all_raw, dataframe_page2]
        return locationarray, dataframearray
    except:
        print("File not exsist")


def describe_dataframe(locationarray, dataframearray):
    for i in range(len(dataframearray)):
        location = locationarray[i]
        dataframe = dataframearray[i]
        column = dataframe.columns
        dtypes = dataframe.dtypes
        describe = dataframe.describe()
        number = {0: "first", 1: "second", 2: "third"}
        print(f"The {number[i]} dataframe is \n{dataframe}")
        print(f"The first five rows are: \n{dataframe.head()}")
        print(f"The last five rows are: \n{dataframe.tail()}")
        print(f"The column labels are \n{column}")
        print(f"The data types of columon are: \n{dtypes}")
        dataframe.info()
        print(f"The {describe}")

def data_preparation(dataframearray):
    # Convert a specific column from float64 to int
    df_event = dataframearray[0]
    df_medal = dataframearray[2]
    df_event_columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
    df_medal_columns_to_change = ['Rank']
    print(df_event['start'])
    print(df_event['end'])
    if 'start' in df_event.columns:
        df_event['start'] = pd.to_datetime(df_event['start'], format='%d/%m/%Y')
    if 'start' in df_medal.columns:
        df_medal['start'] = pd.to_datetime(df_medal['start'], format='%d/%m/%Y')

    for col in df_event_columns_to_change:
        if col in df_event.columns:
            # df_event[col] = pd.to_numeric(df_event[col], errors='coerce')  # 转换为数字
            df_event[col] = df_event[col].fillna(0)  # fill in the NaN value with 0
            df_event[col] = df_event[col].replace([np.inf, -np.inf], 0)  # replace inf and -inf with 0
            df_event[col] = df_event[col].astype(int)  # convert into int

    for col in df_medal_columns_to_change:
        if col in df_medal.columns:
            # df_medal[col] = pd.to_numeric(df_medal[col], errors='coerce')  # 转换为数字
            df_medal[col] = df_medal[col].fillna(0)
            df_medal[col] = df_medal[col].replace([np.inf, -np.inf], 0)
            df_medal[col] = df_medal[col].astype(int)



    

if __name__ == '__main__':
    locationarray,dataframearray = readfile()
    describe_dataframe(locationarray, dataframearray)
    data_preparation(dataframearray)

