import arcpy
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <province_abbreviation>")
    sys.exit(1)

province = sys.argv[1].upper()

valid_provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
if province not in valid_provinces:
    print(f"Invalid province abbreviation: {province}")
    sys.exit(1)

shapefile_path = "data/Canada/Can_Mjr_Cities.shp"

with arcpy.da.SearchCursor(shapefile_path, ["Name", "Prov"], where_clause=f"{arcpy.AddFieldDelimiters(shapefile_path, 'Prov')} = '{province}'") as cursor:
    # 初始化城市列表
    cities = []

    # 循环遍历数据并打印城市名和省份
    for row in cursor:
        city_name, province = row
        print(f"{city_name}, {province}")
        
        # 将城市名添加到列表中
        cities.append(city_name)

# 打印城市总数
city_count = len(cities)
print(f"\nThere are {city_count} cities in {province}.")
