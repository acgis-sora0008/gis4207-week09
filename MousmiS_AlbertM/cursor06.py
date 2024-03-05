import zipfile
import os

def zip_kmz(output_folder, kml_filename, kmz_filename):
    # Create a Zip file containing the KML file
    with zipfile.ZipFile(os.path.join(output_folder, kmz_filename), 'w') as kmz:
        kmz.write(os.path.join(output_folder, kml_filename), os.path.basename(kml_filename))

output_folder = r'C:\acgis\gis4207_prog\week_09\lab\output'
kml_filename = 'Cities.kml'
kmz_filename = 'Cities.kmz'

zip_kmz(output_folder, kml_filename, kmz_filename)