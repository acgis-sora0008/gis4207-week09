import arcpy

def main():
    
    ws = r"..\..\..\..\data\canada\Can_Mjr_Cities.shp"

    fc = 'canada\Can_Mjr_Cities.shp'
    fields = ['Name', 'Prov']

    with arcpy.da.SearchCursor(ws,["Name", "Prov"]) as cursor:
        print("Name, Prov")
        count = 0
        for row in cursor:
            count += 1
            print(f"{row[0]}, {row[1]}")
        
        print(f"\nThere are {count} cities in the above list.")
                
if __name__ == "__main__":
    main()        


