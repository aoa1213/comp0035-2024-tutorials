import pandas as pd
from pathlib import Path


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
        data_file_location_1 = Path(__file__).parent.joinpath("tutorialpkg","data","paralympics_events_raw.csv")
        dataframe_paralympics_events_raw = pd.read_csv(data_file_location_1)
        data_file_location_2 = Path(__file__).parent.joinpath("tutorialpkg","data","paralympics_all_raw.xlsx")
        dataframe_paralympics_all_raw = pd.read_excel(data_file_location_2)
        dataframe_page2 = pd.read_excel(data_file_location_2, sheet_name="medal_standings")

        # put all locaions and dataframe into a array 
        locationarray=[data_file_location_1,data_file_location_2,data_file_location_2]
        dataframearray=[dataframe_paralympics_events_raw,dataframe_paralympics_all_raw,dataframe_page2]
        return locationarray,dataframearray
    except:
        print("File not exsist")


def describe_dataframe(locationarray,dataframearray):
    for i in range(len(dataframearray)):
        location = locationarray[i]
        dataframe = dataframearray[i]
        column = dataframe.columns
        dtypes = dataframe.dtypes
        info = dataframe.info()
        describe = dataframe.describe()
        number = {0:"first" ,1:"second", 2:"third"}
        print(f"The {number[i]} dataframe is \n{dataframe}")
        print(f"The first five rows are: \n{dataframe.head()}")
        print(f"The last five rows are: \n{dataframe.tail()}")
        print(f"The column labels are \n{column}")
        print(f"The data types of columon are: \n{dtypes}")
        print(f"The informaiton: \n{info} ")
        print(f"The {describe}")

def data_preparation():
    

if __name__ == '__main__':
    locationarray,dataframearray=readfile()
    describe_dataframe(locationarray,dataframearray)

