import arcpy


shapefile_path = r"../../../data/Canada/Can_Mjr_Cities.shp"

with arcpy.da.SearchCursor(shapefile_path, ["Name", "Prov"]) as cursor:
    cities = []
    city_count=0
    for row in cursor:
        city_name, province = row
        print(f"{city_name}, {province}")
        city_count+=1
        
print(f"\nThere are {city_count} cities in the above list.")