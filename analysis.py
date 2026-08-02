print("Analysis imported")

import numpy as np 
import laspy
import os

def analyze_las(selected_file): 
    las = laspy.read(selected_file)

    data = selected_file
    size_in_by = os.path.getsize(selected_file)
    size_in_kb = size_in_by / 1024
    size_in_mb = size_in_kb / 1024

    all_points = len(las.points)

    x = las.x
    y = las.y
    z = las.z

    las_header = las.header.point_format.id
    version = las.header.version
    crs = las.header.parse_crs()

    area = (x.max() - x.min()) * (y.max()-y.min())
    pt = all_points / area

    edge_of_flight_line = las.edge_of_flight_line
    intensity = las.intensity
    #scan angle
    if las.point_format.id <= 5:
        scan_angle = las.scan_angle_rank
        scan_min = scan_angle.min()
        scan_max = scan_angle.max()
    else: 
        scan_angle = las.scan_angle
        scan_min = scan_angle.min() * 0.006
        scan_max = scan_angle.max() * 0.006
    try: 
        gps = las.gps_time
    except AttributeError:
        gps = None 

    return_number = np.asarray(las.return_number)
    num_returns = np.asarray(las.num_returns)
    classification = las.classification
    

    try: 
        red = las.red
        green = las.green
        blue = las.blue
    except AttributeError:
        red = green = blue = None 
    
    try: 
        nir = las.nir
    except AttributeError:
        nir = None 

    stats = {
        "file_information": {
            "file": selected_file,
            "file_size": size_in_mb,
            "point_format": las_header,
            "las_version": version,
            "total_points": all_points
        },

        "coordinate_system": {
            "crs": crs
        },

        "spatial_extent": {
            "x_min": x.min(),
            "x_max": x.max(),
            "y_min": y.min(),
            "y_max": y.max(),
            "z_min": z.min(),
            "z_max": z.max(),
        },

        "point_statistics": {
            "point_density": pt,
            "edge_of_flight_line_min": edge_of_flight_line.min(),
            "edge_of_flight_line_max": edge_of_flight_line.max(),
            "intensity_min": intensity.min(),
            "intensity_max": intensity.max(),
            "scan_angle_min": scan_min,
            "scan_angle_max": scan_max,
            "gps_min": gps.min(),
            "gps_max": gps.max(),
        },

        "return_information":{
#            "return_number": return_number,
            "return_number_min": return_number.min(),
            "return_number_max": return_number.max(),
                    "first_return": np.sum(return_number == 1),
                    "last_return": np.sum(return_number == num_returns),
                    "intermediate_returns": np.sum((return_number > 1) & (return_number < num_returns))
        },

        "classification":{
            "never_classified": np.sum(classification == 0),
            "unassigned": np.sum(classification == 1),
            "ground": np.sum(classification == 2),
            "low_vegetation": np.sum(classification == 3),
            "medium_vegetation": np.sum(classification == 4),
            "high_vegetation": np.sum(classification == 5),
            "building": np.sum(classification == 6),
            "low_point": np.sum(classification == 7),
            "water": np.sum(classification == 9),
            "high_noise": np.sum(classification == 18),
        },

        "rgb":{
            "red_min": red.min(),
            "red_max": red.max(),
            "green_min": green.min(),
            "green_max": green.max(),
            "blue_min": blue.min(),
            "blue_max": blue.max(),
        } if red is not None else None,
        

        "nir":{
            "nir_min": nir.min(),
            "nir_max": nir.max(),
        } 
        if nir is not None else None 
    }

    return stats
print("Analysis loaded successfully!")