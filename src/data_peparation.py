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
        cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
        'participants_m', 'participants_f', 'participants']
        event_raw_location = Path(__file__).parent.joinpath("tutorialpkg", "data", "paralympics_events_raw.csv")
        df_paralympics_events_raw = pd.read_csv(event_raw_location,usecols=cols)

        all_raw_location = Path(__file__).parent.joinpath("tutorialpkg", "data", "paralympics_all_raw.xlsx")
        df_paralympics_all_raw = pd.read_excel(all_raw_location,usecols=cols)


        df_paralympics_all_raw_page2 = pd.read_excel(all_raw_location, sheet_name="medal_standings")
        # put all locaions and dataframe into a array 

        locationarray = [event_raw_location, all_raw_location, all_raw_location]
        dataframearray = [df_paralympics_events_raw, df_paralympics_all_raw, df_paralympics_all_raw_page2]
        return locationarray, dataframearray
    except:
        print("File not exsist")


def describe_dataframe(dataframearray):
    for i in range(len(dataframearray)):
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

    # print(df_event['start'])
    # print(df_event['end'])
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


def add_new_column(dataframearray):
    df = dataframearray[1]
    df.insert(df.columns.get_loc('end'), 'duration', df['end'] - df['start'])
    df["duration"] = df["duration"].dt.days.astype(int)
    dataframearray[1] = df
    return dataframearray

def remove_column_strip(dataframearray):
    df_e = dataframearray[0]
    df_e = df_e.drop(index=[0,17,31])
    df_e = df_e.reset_index(drop=True)
    print(df_e['type'].unique())
    df_e['type'] = df_e['type'].str.strip().str.lower()
    # df_striped = df_e.str.strip()
    # df_lowercase_striped = df_striped.str.lower()
    dataframearray[0]=df_e
    return dataframearray

def replace_country_name(dataframearray):
    df_e = dataframearray[0]
    replacement_names = {
    'UK': 'Great Britain',
    'USA': 'United States of America',
    'Korea': 'Republic of Korea',
    'Russia': 'Russian Federation',
    'China': "People's Republic of China"
    }
    df_e = df_e.replace(to_replace=replacement_names)
    dataframearray[0]=df_e
    return dataframearray

def dataframe_combine(dataframearray):
    df_e = dataframearray[0]
    df_e_f = df_e.loc[:,['country']]

    data_npc = Path(__file__).parent.joinpath("tutorialpkg", 'data', 'npc_codes.csv')
    df_npc = pd.read_csv(data_npc, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])

    df_result = df_e_f.merge(df_npc, how='left', left_on='country', right_on='Name')

    dataframearray[0] = df_result
    return dataframearray

def output_csv(dataframearray):
        location = Path(__file__).parent.joinpath("tutorialpkg","data","paralympics_events_prepared.csv")
        dataframearray[0].to_csv(location, index=False)



    

if __name__ == '__main__':
    locationarray,dataframearray = readfile()
    dataframearray_altered = add_new_column(dataframearray)
    describe_dataframe(dataframearray_altered)
    data_preparation(dataframearray_altered)

    combined_dataframe_array = dataframe_combine(dataframearray_altered)
    output_csv(combined_dataframe_array)
    
