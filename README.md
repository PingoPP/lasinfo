# lasinfo v.1.0
This program is used for viewing LiDAR data information
## Las Info

Las Info is a Python program designed for viewing and analyzing LiDAR data stored in `.las` and `.laz` file formats. The program reads the selected file, processes the data, and displays various statistics and metadata in the `show_stats` window.

The following information is available:

### File Information

* File name
* File size
* Point format
* LAS version

### Coordinate System

* Coordinate Reference System (CRS)[EPSG code and related information]

### Spatial Extent

* X coordinates (min and max values)
* Y coordinates (min and max values)
* Z coordinates (min and max values)

### Point Statistics

* Point density
* Edge of flight line
* Intensity
* Scan angle
* GPS time

### Return Information

* Return number (min and max values)
* First returns
* Last returns
* Intermediate returns

### Classification

* Never Classified
* Unassigned
* Ground
* Low Vegetation
* Medium Vegetation
* High Vegetation
* Building
* Low Point
* Water
* High Noise

### RGB Information

* Red
* Green
* Blue

### NIR Information

* Near-Infrared [NIR]
