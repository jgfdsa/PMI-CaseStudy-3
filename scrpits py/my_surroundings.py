# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:56:34 2018

@author: gregorio ferreira
"""
import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df
import numpy as np

#load json object
with open('./data/Surroundings.json') as my_list:
    my_list = json.load(my_list)

## Sanity check 1, there are only two keys:store_code, surroundings 
for x in my_list:
    if len(x) != 2:
        print(x)  

## Extracting surroundings details
colNames = ('store_code','col_name','name', 'place_id', 'latitude', 'longitude', 'country', 'postal_code')

# Define a dataframe with the required column names
df_out = pd.DataFrame(columns = colNames)        

for x in my_list:
    my_surr = json_normalize(x['surroundings'])
    
    cols = list(my_surr.columns)
    #col = 84
    for col in cols:
        my_list_l2 = json_normalize(x['surroundings'][col])      
    
        if(len(my_list_l2) != 0):
              
                for ii in range(0, len(my_list_l2)):
                    temp = json_normalize(my_list_l2.address_components[ii])
                    
                    postal_code_test = temp.loc[temp['types'].astype(str) == "['postal_code']",'short_name']
                    
                    if(len(postal_code_test) != 0):
                        postal_code = postal_code_test.values[0]
                    else:
                        postal_code = np.nan
                        
                    country_test = temp.loc[temp['types'].astype(str) == "['country', 'political']",'short_name']
                    
                    if(len(country_test) != 0):
                        country = country_test.values[0]
                    else:
                        country = np.nan
                    
                    df_out = df_out.append([{'store_code':x['store_code'],
                                   'col_name' : col,
                                   'name' : my_list_l2.name[ii],
                                   'place_id' : my_list_l2.place_id[ii],
                                   'latitude' : my_list_l2.latitude[ii],
                                   'longitude' : my_list_l2.longitude[ii],
                                   'postal_code' : postal_code,
                                   'country' : country,
                                   }],ignore_index=True)  

surroundings_details = df_out[['store_code', 'name', 'place_id', 'latitude', 'longitude',
                        'country', 'postal_code']].drop_duplicates(keep='first')

surroundings_details.to_csv("C:/Users/plgrfer/Google Drive/PMI/UseCase_3_Datasets/surroundings_details.csv",
                            sep=',', encoding='utf-8')

surroundings_count = df_out[['store_code', 'col_name']].pivot_table(index = 'store_code',
                           columns = 'col_name', aggfunc = len, fill_value = 0)

surroundings_count.to_csv("C:/Users/plgrfer/Google Drive/PMI/UseCase_3_Datasets/surroundings_count.csv",
                          sep=',', encoding='utf-8')

repeated_names = surroundings_details.groupby(['name'])['name'].agg(['count'])

repeated_names = repeated_names[(repeated_names['count'] > 1)]

repeated_names.to_csv("C:/Users/plgrfer/Google Drive/PMI/UseCase_3_Datasets/repeated_names.csv",
                          sep=',', encoding='utf-8')

## extra    
colNames = ('store_code','col_name','name', 'place_id', 'latitude', 'longitude', 'country', 'postal_code')

# Define a dataframe with the required column names
df_out = pd.DataFrame(columns = colNames)    
x = 400
my_surr = json_normalize(my_list[x]['surroundings'])
    
cols = list(my_surr.columns)
#col = 84
for col in cols:
    my_list_l2 = json_normalize(my_list[x]['surroundings'][col])

    if(len(my_list_l2) != 0):
      
        for ii in range(0, len(my_list_l2)):
            temp = json_normalize(my_list_l2.address_components[ii])      
            
            df_out = df_out.append([{'store_code': my_list[x]['store_code'],
                           'col_name' : col,
                           'name' : my_list_l2.name[ii],
                           'place_id' : my_list_l2.place_id[ii],
                           'latitude' : my_list_l2.latitude[ii],
                           'longitude' : my_list_l2.longitude[ii],
                           'postal_code' : temp.loc[temp['types'].astype(str) == "['postal_code']",'short_name'].values[0],
                           'country' : temp.loc[temp['types'].astype(str) == "['country', 'political']",'short_name'].values[0]
                           }],ignore_index=True)   
    
    
    
if(len(my_list_l2) != 0)
        
        df_out = pd.DataFrame({'store_code': [my_list[10]['store_code']],
                       'name': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       'B': [b],
                       })
       country = my_list_l2[0]['address_components'][5]['short_name'] 
        
        
        
        
    else:
        
# len(test_df_bar)   
    test_df_bar = test_df['bar'][0]
    
    country = test_df_bar[0]['address_components'][5]['short_name']
    latitude = test_df_bar[0]['latitude']
    longitude = test_df_bar[0]['longitude']
    name = test_df_bar[0]['name']
    place_id = test_df_bar[0]['place_id']
    

    
    flat = flatten_json(test_df_bar)
    temp = json_normalize(flat)

labels = ['store_code', 'surroundings']

my_list_l1 = pd.DataFrame(my_list_l1, columns=labels)
    
    
list(my_surr_0)
#['accounting',
# 'airport',
# 'amusement_park',
# 'aquarium',
# 'art_gallery',
# 'atm',
# 'bakery',
# 'bank',
# 'bar',
# 'beauty_salon',
# 'bicycle_store',
# 'book_store',
# 'bowling_alley',
# 'bus_station',
# 'cafe',
# 'campground',
# 'car_dealer',
# 'car_rental',
# 'car_repair',
# 'car_wash',
# 'casino',
# 'cemetery',
# 'church',
# 'city_hall',
# 'clothing_store',
# 'convenience_store',
# 'courthouse',
# 'dentist',
# 'department_store',
# 'doctor',
# 'electrician',
# 'electronics_store',
# 'embassy',
# 'fire_station',
# 'florist',
# 'funeral_home',
# 'furniture_store',
# 'gas_station',
# 'gym',
# 'hair_care',
# 'hardware_store',
# 'hindu_temple',
# 'home_goods_store',
# 'hospital',
# 'insurance_agency',
# 'jewelry_store',
# 'laundry',
# 'lawyer',
# 'library',
# 'liquor_store',
# 'local_government_office',
# 'locksmith',
# 'lodging',
# 'meal_delivery',
# 'meal_takeaway',
# 'mosque',
# 'movie_rental',
# 'movie_theater',
# 'moving_company',
# 'museum',
# 'night_club',
# 'painter',
# 'park',
# 'parking',
# 'pet_store',
# 'pharmacy',
# 'physiotherapist',
# 'plumber',
# 'police',
# 'post_office',
# 'real_estate_agency',
# 'restaurant',
# 'roofing_contractor',
# 'rv_park',
# 'shoe_store',
# 'shopping_mall',
# 'spa',
# 'stadium',
# 'storage',
# 'store',
# 'subway_station',
# 'synagogue',
# 'taxi_stand',
# 'train_station',
# 'transit_station',
# 'travel_agency',
# 'university',
# 'veterinary_care',
# 'zoo']
    
my_surr_accounting = json_normalize(d[0]['surroundings']['accounting'])
list(my_surr_accounting)
len(list(my_surr_accounting))
#['address_components',
# 'formatted_address',
# 'icon',
# 'international_phone_number',
# 'latitude',
# 'longitude',
# 'name',
# 'opening_hours.open_now',
# 'opening_hours.periods',
# 'opening_hours.weekday_text',
# 'place_id',
# 'types',
# 'website']
json_normalize(my_surr_accounting['opening_hours.periods'].dropna()[0])
#   close.day close.time  open.day open.time
#0          1       1700         1      0900
#1          2       1700         2      0900
#2          3       1700         3      0900
#3          4       1700         4      0900
#4          5       1700         5      0900
test = my_surr_accounting['opening_hours.weekday_text'].dropna()[0].tolist() # .reset_index()

df= pd.DataFrame([sub.split(",") for sub in test],columns = ['temp'])
df = pd.DataFrame(df.temp.str.split(':',1).tolist(),columns = ['weekday','opening_hours'])
#     weekday       opening_hours
#0     Monday   9:00 AM – 5:00 PM
#1    Tuesday   9:00 AM – 5:00 PM
#2  Wednesday   9:00 AM – 5:00 PM
#3   Thursday   9:00 AM – 5:00 PM
#4     Friday   9:00 AM – 5:00 PM
#5   Saturday              Closed
#6     Sunday              Closed
## ==== 

my_surr_accounting.get('opening_hours.weekday_text', 'nan')[0]


my_surr_restaurant = json_normalize(d[0]['surroundings']['restaurant'])
list(my_surr_restaurant)
len(list(my_surr_restaurant))
#['address_components',
# 'formatted_address',
# 'icon',
# 'international_phone_number',
# 'latitude',
# 'longitude',
# 'name',
# 'opening_hours.open_now',
# 'opening_hours.periods',
# 'opening_hours.weekday_text',
# 'place_id',
# 'rating',                 ## Not in accounting
# 'reviews',                ## Not in accounting
# 'types',
# 'user_ratings_total',     ## Not in accounting
# 'website']



    


