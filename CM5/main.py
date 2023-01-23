import json

import requests

r = requests.get("https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_3_1_Climate_Indicators_Annual_Mean_Global_Surface_Temperature/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")

json_data = json.loads(r.text)

for data in json_data["features"]:

    print("Nom du pays:" + data["properties"]["Country"])

    print("Données pour l'année 1961:"+str(data["properties"]["F1961"]))

    print("Données pour l'année 2021:"+str(data["properties"]["F2021"]))