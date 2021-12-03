import pandas as pd

df = pd.read_csv("TDCS_M06A_20190830_080000.csv")
df.columns = ["vehicle_type","derectiontime_o","gantryid_o","derectiontime_d",
              "gantryid_d","trip_len","trip_end","info"]


class Data:
    
    def __init__(self, df):
        self.df = df
        self.vehicle_type = self.df["vehicle_type"]
        self.derectiontime_o = pd.to_datetime(self.df["derectiontime_o"])
        self.gantryid_o = df["gantryid_o"]
        self.derectiontime_d = pd.to_datetime(self.df["derectiontime_d"])
        self.gantryid_d = self.df["gantryid_d"]
        self.trip_len = self.df["trip_len"]
        self.trip_end = self.df["trip_end"] == "Y"
        self.info = self.df["info"]
    
        
class Sort:
    
    def __init__(self, df, variable_list):
        self.data = Data(df).df
        self.variable = variable_list
        
    def sort_data(self):
        return self.data.sort_values(by=self.variable)


d = Data(df)
print(Sort(d.df,["vehicle_type","trip_len"]).sort_data())

        
