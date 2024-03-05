import arcpy
from arcpy import env
from arcpy import env
import sys

# Check if the province abbreviation argument is provided
def main():
    if len(sys.argv) != 2:
        print("Usage: python cursor02.py <province abbreviation>")
        sys.exit()
        
    # Extract the province abbreviation from the command-line argument
    province_abbreviation = sys.argv[1].upper()   

    # Validate the province abbreviation
    valid_provinces = ["NF", "PE", "NS", "NB", "BC", "YT", "ON", "QC", "MB", "SK", "AB"]
    if province_abbreviation not in valid_provinces:
        print("Invalid province abbreviation.")
        sys.exit()  

    #Relative path
    ws = r"..\..\..\..\data\canada"
    env.workspace = ws
    fc = 'Can_Mjr_Cities.shp'

    fields = ['Name', 'Prov']

    # Construct the where clause
    field = arcpy.AddFieldDelimiters(ws, 'Prov')
    where_clause = f"{field} = '{province_abbreviation}'"

    with arcpy.da.SearchCursor(fc, fields, where_clause) as cursor:
        # print("Name, Prov")
        count = 0
        for row in cursor:
            count += 1
            print(f"{row[0]}, {row[1]}")
            
    print(f"\nThere are {count} cities in {province_abbreviation}.")
    
if __name__ == "__main__":
    main()       
        
 
        


