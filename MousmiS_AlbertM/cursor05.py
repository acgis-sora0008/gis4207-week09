import arcpy
import os

# Path to the MajorCities feature class

def main():
    shapefile_path = r"..\..\..\..\data\Canada\Canada.gdb\MajorCities"

    # Output KML file path
    output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'output'))
    os.makedirs(output_folder, exist_ok = True)
    output_kml_path = os.path.join(output_folder, 'Cities.kml')

    # Create the KML header
    kml_header = '''<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
    '''

    # Create the KML footer
    kml_footer = '''</Document>
    </kml>
    '''

    # Open the KML file for writing
    with open(output_kml_path, 'w') as kml_file:
        # Write the KML header
        kml_file.write(kml_header)
        
        # Create a search cursor to iterate through the features
        fields = ["Name", "Prov", "UTM_MAP", "SHAPE@X", "SHAPE@Y"]
        with arcpy.da.SearchCursor(shapefile_path, fields) as cursor:
            for row in cursor:
                city_name, province, utm_map, longitude, latitude = row
                
                # Construct the description with the URL
                description = f"http://www.canmaps.com/topo/nts50/map/{utm_map}.htm"
                
                # Create the Placemark element
                placemark = f'''  <Placemark>
        <name>{city_name}, {province}</name>
        <description>{description}</description>
        <Point>
        <coordinates>{longitude},{latitude},0</coordinates>
        </Point>
    </Placemark>
    '''
                # Write the Placemark element to the KML file
                kml_file.write(placemark)

        # Write the KML footer
        kml_file.write(kml_footer)

    print(f"KML file saved to: {output_kml_path}")
    
if __name__ == "__main__":
    main()     
