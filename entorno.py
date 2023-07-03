import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.options.display.max_rows = 15

df = pd.read_csv(r'C:\Users\Eva\Desktop\Python\programas\data\data_sheets\coaster_db.csv')

df = df[['coaster_name', 
        # 'Length', 'Speed', 
        'Location',  'Status', 
        # 'Opening date','Type', 
       'Manufacturer', 
    #    'Height restriction', 'Model', 'Height',
    #    'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
    #    'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
    #    'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
    #    'Track layout', 'Fastrack available', 'Soft opening date.1',
    #    'Closing date', 
    'Opened', 
    # 'Replaced by', 'Website',      
    #    'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
    #    'Single rider line available', 'Restraint Style',        
    #    'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 
       'longitude',  'Type_Main', 
       'opening_date_clean',
    #    'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
    #    'height_value', 'height_unit', 
    'height_ft', 
       'Inversions_clean', 'Gforce_clean']].copy()

df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])

def ver_h(n):
    print(df.head(n))
def ver_c():
    for i in df.columns:
        print(i)

df = df.rename(columns={'coaster_name':'Coaster_Name', 
'year_introduced':'Year_Introduced', 
'latitude':'Latitude', 
'longitude':'Longitude',  
'opening_date_clean':'Opening_Data', 
'speed_mph':'Speed_mph',
'height_ft':'Height_ft', 
'Inversions_clean':'Inversions',
'Gforce_clean':'Gforce'})

# print(df.loc[df.duplicated(subset=['Coaster_Name'])].head(5))

print(df.query("Coaster_Name == 'Crystal Beach Cyclone'"))

