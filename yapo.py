import pandas as pd
import os
import glob
import json
import re


os.chdir("C:\\Users\\AndrésJerez\\Downloads\\products\\june")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#print(combined_csv.head())

#print("LARGO creation_date: ", len(combined_csv['creation_date']))
#print("LARGO product_name: ", len(combined_csv['product_name']))

#print("UNICOS creation_date: ", len(combined_csv['creation_date'].unique().tolist()))
#print("UNICOS product_name: ", len(combined_csv['product_name'].unique().tolist()))

df_creation_date = pd.DataFrame(combined_csv['creation_date'].unique().tolist())
df_product_name = pd.DataFrame(combined_csv['product_name'].unique().tolist())

df_product_name_all = pd.DataFrame(combined_csv['product_name'].tolist())



#print(len(df_product_name))
list_creation_date = combined_csv['creation_date'].tolist()
list_product_name = combined_csv['product_name'].tolist()

list_creation_date_unique = combined_csv['creation_date'].unique().tolist()
list_product_name_unique = combined_csv['product_name'].unique().tolist()

 
# list to hold visited values
unique_product_name = combined_csv['product_name'].unique().tolist()
unique_creation_date = combined_csv['creation_date'].unique().tolist()


#print(combined_csv['product_name'].value_counts())

Daily_Bump = []
bump = []
Monthly_Store = []
Quarterly_Store = []
Pack_Autos_10_Monthly = []
Gallery = []
Weekly = []
Pack_Autos_20_Monthly = []
Annual_Store = []
Biannual_Store = []



for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Monthly Store"):
        Monthly_Store.append(list_creation_date[i])

for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Bump"):
        bump.append(list_creation_date[i])

for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Quarterly Store"):
        Quarterly_Store.append(list_creation_date[i])


for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Pack Autos 10 Monthly"):
        Pack_Autos_10_Monthly.append(list_creation_date[i])


for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Gallery"):
        Gallery.append(list_creation_date[i])


for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Weekly"):
        Weekly.append(list_creation_date[i])


for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Pack Autos 20 Monthly"):
        Pack_Autos_20_Monthly.append(list_creation_date[i])


for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Annual Store"):
        Annual_Store.append(list_creation_date[i])

for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Biannual Store"):
        Biannual_Store.append(list_creation_date[i])

for i in range(len(list_creation_date)):
    if(list_product_name[i] == "Daily Bump"):
        Daily_Bump.append(list_creation_date[i])


df_bump = pd.DataFrame(bump)
df_Daily_Bump = pd.DataFrame(Daily_Bump)
df_Monthly_Store = pd.DataFrame(Monthly_Store)
df_Quarterly_Store = pd.DataFrame(Quarterly_Store)
df_Pack_Autos_10_Monthly = pd.DataFrame(Pack_Autos_10_Monthly)
df_Gallery = pd.DataFrame(Gallery)
df_Weekly = pd.DataFrame(Weekly)
df_Pack_Autos_20_Monthly = pd.DataFrame(Pack_Autos_20_Monthly)
df_Annual_Store = pd.DataFrame(Annual_Store)
df_Biannual_Store = pd.DataFrame(Biannual_Store)


result2 = df_Annual_Store.value_counts().to_json(orient="index")
parsed2 = json.loads(result2)

result = df_Biannual_Store.value_counts().to_json(orient="index")
parsed = json.loads(result)

result_bump = df_bump.value_counts().to_json(orient="index")
parsed_bump = json.loads(result_bump)

result_df_Daily_Bump = df_Daily_Bump.value_counts().to_json(orient="index")
parsed_df_Daily_Bump = json.loads(result_df_Daily_Bump)

result_df_Monthly_Store = df_Monthly_Store.value_counts().to_json(orient="index")
parsed_df_Monthly_Store = json.loads(result_df_Monthly_Store)

result_df_Quarterly_Store = df_Quarterly_Store.value_counts().to_json(orient="index")
parsed_df_Quarterly_Store = json.loads(result_df_Quarterly_Store)


result_df_Pack_Autos_10_Monthly = df_Pack_Autos_10_Monthly.value_counts().to_json(orient="index")
parsed_df_Pack_Autos_10_Monthly = json.loads(result_df_Pack_Autos_10_Monthly)

result_df_Gallery = df_Gallery.value_counts().to_json(orient="index")
parsed_df_Gallery = json.loads(result_df_Gallery)

result_df_Weekly = df_Weekly.value_counts().to_json(orient="index")
parsed_df_Weekly = json.loads(result_df_Weekly)

result_df_Pack_Autos_20_Monthly = df_Pack_Autos_20_Monthly.value_counts().to_json(orient="index")
parsed_df_Pack_Autos_20_Monthly = json.loads(result_df_Pack_Autos_20_Monthly)

result = df_Biannual_Store.value_counts().to_json(orient="index")
parsed = json.loads(result)
#print(json.dumps(parsed, indent=4))

f = {}
f["Biannual Store"] = json.dumps(parsed, indent=4)
f["Annual Store"] = json.dumps(parsed2, indent=4)
f["Bump"] = json.dumps(parsed_bump, indent=4)
f["Daily Bump"] = json.dumps(parsed_df_Daily_Bump, indent=4)
f["Monthly Store"] = json.dumps(parsed_df_Monthly_Store, indent=4)
f["Quarterly Store"] = json.dumps(parsed_df_Quarterly_Store, indent=4)
f["Pack Autos 10 Monthly"] = json.dumps(parsed_df_Pack_Autos_10_Monthly, indent=4)
f["Gallery"] = json.dumps(parsed_df_Gallery, indent=4)
f["Weekly"] = json.dumps(parsed_df_Weekly, indent=4)
f["Pack Autos 20 Monthly"] = json.dumps(parsed_df_Pack_Autos_20_Monthly, indent=4)

with open('C:\\Users\\AndrésJerez\\Downloads\\products\\test\\json.txt', 'w', encoding='utf-8') as b:
    json.dump(f, b, ensure_ascii=False, indent=4)


