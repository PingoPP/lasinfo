from tkinter import messagebox

print("Import helper")

#This file is for storing all the help functions for the GUI. 
#Each function will display a messagebox with informatio about the specific topic.
#The funcions will be called when the user clicks on the button with the "?"
#Then the messagebox will display the information about the topic.
#sources of that all text are from the following links:
                                            #my brain
                                            #laspy.readthedocs.io
                                            #info from research papers - if you want know more about that, contact me --> https://pingopp.github.io/Website/?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAcGRvZgJleHRuA2FlbQIxMQBzcnRjBmFwcF9pZA85MzY2MTk3NDMzOTI0NTkAAafE-Zbl0FcZhrjQK29ItdOcvxVunLEdtsTXFoIru5decV5WoPavUK0Udxa81w_aem_JQWpgnP2JiBxMM8Al-wY7g

def file_information():
    text= "ENG: File information provides details about the selected LiDAR file, including its name, size, point format, LAS version, and total number of points contained within the file.\n\nSLO: Informacije o datoteki zagotavljajo podrobnosti o izbrani LiDAR datoteki, vključno z njenim imenom, velikostjo, formatom točk, verzijo LAS in skupnim številom točk v datoteki."
    messagebox.showinfo("File Information", text)

def point_source_button():
    text = "ENG: The point source ID is a unique identifier for each point in the point cloud.\n\nSLO: ID točke je edinstven identifikator za vsako točko v oblaku točk."
    messagebox.showinfo("Point Source ID", text)


def crs_button():
    text = "ENG: (Coordinate Reference System), also known as a Spatial Reference System (SRS), defines the spatial reference for LiDAR data, allowing it to be accurately mapped and analyzed. A CRS defines how geographic locations on Earth's surface correspond to coordinates in a Geographic Information System (GIS). Geographic CRS uses latitude and longitude, while projected CRS uses planar coordinates, typically measured in meters.\n\nSLO: Koordinatni referenčni sistem (Coordinate Reference System - CRS), znan tudi kot prostorski referenčni sistem (Spatial Reference System - SRS), določa prostorsko referenco podatkov LiDAR, kar omogoča njihovo natančno kartiranje in analizo. CRS določa, kako geografske lokacije na Zemljini površini ustrezajo koordinatam v geografskem informacijskem sistemu (GIS). Geografski CRS uporablja zemljepisno širino in dolžino, medtem ko projicirani CRS uporablja ravninske koordinate, ki so običajno izražene v metrih."
    messagebox.showinfo("CRS", text)


def spatial_extent():
    text = "ENG: The spatial extent of a LiDAR dataset refers to the geographic area covered by the data. It defines the boundaries within which the LiDAR points were collected and provides information about the size and shape of the surveyed area. The spatial extent is typically represented as a bounding box or polygon that encompasses all the LiDAR points in the dataset (X as east-west axis, Y as north-south axis and Z as up-down axis).\n\nSLO: Prostorski obseg podatkov LiDAR se nanaša na geografsko območje, ki ga pokrivajo podatki. Določa meje, znotraj katerih so bile zbrane točke LiDAR, in zagotavlja informacije o velikosti in obliki preučenega območja. Prostorski obseg je običajno predstavljen kot omejitvena škatla ali poligon, ki zajema vse točke LiDAR v naboru podatkov (X kot os vzhod-zahod, Y kot os jug-sever in Z kot os gor-dol)."
    messagebox.showinfo("Spatial Extent", text)


def point_density():
    text = "ENG: Point density represents the average number of LiDAR points within a specific area. It is commonly expressed as points per square meter (pts/m²). Applications and density requirements: General terrain modelling and flood analysis: 1-5 pts/m², Agriculture, Crop Surface Models and Archaeology: 15-20 pts/m², Robotics and AI identification: 50+ pts/m².\n\nSLO: Gostota točk predstavlja povprečno število LiDAR točk na določeni površini. Najpogosteje se izraža kot število točk na kvadratni meter (pts/m²). Uporaba in zahteve: Splošno modeliranje terena in analiza poplav: 1-5 pts/m², Agronomija, površinski modeli in arheologija: 15-20 pts/m², Robotika in identifikacija s pomočjo umetne inteligence: 50+ pts/m²."
    messagebox.showinfo("Point Density", text)


def intensity_button():
    text = "ENG: Intensity represents the strength of the returned laser pulse detected by the sensor. It provides information about the reflectivity of the surface where the laser pulse was reflected. Higher intensity values indicate more reflective surfaces, while lower values indicate less reflective surfaces.\n\nSLO: Intenzivnost predstavlja moč povratnega laserskega signala, ki ga zazna senzor. Podaja informacije o odbojnosti površine, na katero je laserski pulz naletel. Višje vrednosti pomenijo bolj odbojne površine, nižje vrednosti pa manj odbojne površine."
    messagebox.showinfo("Intensity", text)


def scan_angle():
    text = "ENG: The scan angle is measured between -90° and +90°. At 0° the laser pulse is directly below the aircraft. Most modern LiDAR systems operate within approximately ±30°.\n\nSLO: Kot skeniranja je izražen med -90° in +90°. Pri 0° je laserski pulz neposredno pod letalom. Večina sodobnih LiDAR sistemov uporablja kote manjše od-do približno ±30°."
    messagebox.showinfo("Scan Angle", text)


def gps():
    text = "ENG: GPS time represents the exact timestamp when each LiDAR point was recorded.\n\nSLO: GPS čas predstavlja točen časovni zapis, ko je bila posamezna LiDAR točka zajeta."
    messagebox.showinfo("GPS Time", text)


def edge_of_line():
    text = "ENG: Indicates whether a point is located at the edge of the flight line. Value: 0 = not an edge point, 1 = edge point.\n\nSLO: Označuje, ali se točka nahaja na robu letalske linije. Vrednosti: 0 = ni robna točka, 1 = robna točka"
    messagebox.showinfo("Edge of Line", text)


def scan_direction():
    text = "ENG: Scan direction indicates the direction in which the laser scanner was moving when the point was recorded.\n\nSLO: Smer skeniranja označuje smer premikanja laserskega skenerja ob zajemu točke."
    messagebox.showinfo("Scan Direction", text)


def number_of_returns():
    text = "ENG: Number of returns indicates how many times a laser pulse was reflected back to the sensor after hitting a surface. Common return types include: First return, Last return, Intermediate return, Single return.\n\nSLO: Število odbojev označuje, kolikokrat se je laserski pulz odbil nazaj do senzorja po zadetku površine. Poznamo: prvi odboj, zadnji odboj, vmesni odboj, enojni odboj."
    messagebox.showinfo("Number of Returns", text)


def classification():
    text = "ENG: Classification is the process of assigning a class to each point in a point cloud based on its characteristics and attributes. It is one of the most important steps in LiDAR point cloud processing.\n\nSLO: Klasifikacija je proces dodeljevanja razreda posamezni točki oblaka točk glede na njene značilnosti in atribute. Predstavlja enega najpomembnejših korakov pri obdelavi LiDAR podatkov."
    messagebox.showinfo("Classification", text)


def rgb():
    text = "ENG: RGB (Red, Green, Blue) values represent the color information associated with each LiDAR point. These values are typically derived from aerial imagery or other sources and provide additional context for visualizing and analyzing the point cloud data.\n\nSLO: RGB (rdeča, zelena, modra) vrednosti predstavljajo barvne informacije, povezane z vsako LiDAR točko. Te vrednosti so običajno pridobljene iz zračnih posnetkov ali drugih virov in zagotavljajo dodatni kontekst za vizualizacijo in analizo podatkov oblaka točk."
    messagebox.showinfo("RGB Values", text)


def nir():
    text = "ENG: NIR (Near-Infrared) values represent the near-infrared reflectance information associated with each LiDAR point. These values are typically derived from specialized sensors that capture the near-infrared portion of the electromagnetic spectrum. NIR data can provide valuable insights into vegetation health, water content, and other environmental characteristics.\n\nSLO: NIR (bližnji infrardeči) vrednosti predstavljajo informacije o odbojnosti v bližnjem infrardečem območju, povezane z vsako LiDAR točko. Te vrednosti so običajno pridobljene iz specializiranih senzorjev, ki zajemajo bližnji infrardeči del elektromagnetnega spektra. NIR podatki lahko nudijo dragocene vpoglede v zdravje vegetacije, vsebnost vode in druge okoljske značilnosti."
    messagebox.showinfo("NIR Values", text)