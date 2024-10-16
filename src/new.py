import pandas as pd
from pathlib import Path


def main():
    """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1

        Returns:
        int:Returning value
 
    """
    print(1)
    print(Path.cwd())
    print(Path(__file__))
    data_file_location_1 = Path(__file__).parent.joinpath("tutorialpkg","data","paralympics_events_raw.csv")
    print(data_file_location_1)
    dataframe_paralympics_events_raw = pd.read_csv(data_file_location_1)
    data_file_location_2 = Path(__file__).parent.joinpath("tutorialpkg","data","paralympics_all_raw.xlsx")
    dataframe_paralympics_all_raw = pd.read_excel(data_file_location_2)

    dataframe_page2 = pd.read_excel(data_file_location_2, sheet_name="medal_standings")



if __name__ == '__main__':
    main()


