import arcpy
from arcpy import env
import sys

if len(sys.argv) != 2:
        print("Usage: python script_name.py <province_abbreviation>")
        sys.exit()

province = sys.argv[1].upper()

valid_provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
if province not in valid_provinces:
        print(f"Invalid province abbreviation: {province}")
        sys.exit()

shapefile_path = r"../../../../data/Canada/Canada.gdb/MajorCities"
env.workspace=shapefile_path
    # Move the SearchCursor inside the main function
with arcpy.da.SearchCursor(shapefile_path, ["Name", "Prov", "SHAPE@X", "SHAPE@Y"], where_clause=f"{arcpy.AddFieldDelimiters(shapefile_path, 'Prov')} = '{province}'") as cursor:
        cities = []
        city_count = 0
        
        print("Name,Prov,Longitude,Latitude")

        for row in cursor:
            city_name, province, longitude, latitude = row
            city_count += 1
            print(f"{city_name},{province},{longitude},{latitude}")

print(f"\nThere are {city_count} cities in {province}.")