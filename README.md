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

* Near-Infrared [NIR]*

## How to use an app lasinfo

<h1>How to Use LAS.INFO</h1>

<h2>Step 1 – Download the Application</h2>

<ol>
    <li>Open the <strong>Releases</strong> section of this repository (see Picture 1).</li>

  <figure>
            <img width="1732" height="1344" alt="Posnetek zaslona 2026-08-03 180742" src="https://github.com/user-attachments/assets/a36c2326-6a17-4d20-9f0f-dbe361546c25" />
    </figure>

  <br><br>
    
  <li>Under <strong>Assets</strong>, you will find the available files (see Picture 2).</li>
    <li>Download <code>lasinfo.exe</code> (approximately <strong>37 MB</strong>).</li>

  <figure>
    <img width="1624" height="442" alt="Posnetek zaslona 2026-08-03 180807" src="https://github.com/user-attachments/assets/5067b9e2-964e-45ff-9f9a-e2ef92b04e72" />
  </figure>
 
  <li>
        Depending on your Windows security settings, you may see a warning because
        the application is not digitally signed. If you downloaded the file from
        this official GitHub repository, you can choose to keep the file and continue.
    </li>
</ol>

<h2>Step 2 – Run the Application</h2>

<p>
Launch <code>lasinfo.exe</code>. The application will open with a graphical user
interface built using <strong>Tkinter</strong>.
</p>

<p>On the left side of the window, you will find two tabs:</p>
  
<ul>
    <li><strong>Intro</strong> – Displays basic information about the application.</li>
    <li><strong>Info</strong> – Displays information about the selected LAS/LAZ file.</li>
</ul>

<p>At the bottom of the window, there are two buttons:</p>

<figure>
  <img width="2880" height="1518" alt="Posnetek zaslona 2026-08-03 181159" src="https://github.com/user-attachments/assets/d16cdfbf-5b99-4ed5-98ce-abfb60343342" />
</figure>  

<ul>
    <li>
        <strong>Select .LAS File</strong> – Opens the Windows File Explorer,
        allowing you to select a LAS or LAZ file for analysis.
    </li>
    <li><strong>Exit</strong> – Closes the application.</li>
</ul>

<figure>
  <img width="2880" height="1518" alt="Posnetek zaslona 2026-08-03 181239" src="https://github.com/user-attachments/assets/76752a8d-024a-4d9f-a62f-c6c5e4049562" />
</figure>

<figure>
  <img width="2878" height="1518" alt="Posnetek zaslona 2026-08-03 181304" src="https://github.com/user-attachments/assets/4164ec83-d96e-4b58-bbeb-81c7dcc29779" />
</figure>

<p>
After selecting a file, LAS.INFO automatically displays the available metadata
and file information in the <strong>Info</strong> tab.
</p>

## About app
Name: lasinfo <br>
Version: 1.0 <br>

Developed by Jaka Dacar

Using libaries in that app <br>
◦ laspy <br>
◦ numpy <br>
◦ tkinter <br>
◦ OS <br>
◦ PIL <br>
Sources <br>
◦ https://laspy.readthedocs.io/en/latest/intro.html <br>
◦ https://numpy.org/ <br>
◦ https://www.geeksforgeeks.org/python/python-gui-tkinter/ <br>
◦ https://m.youtube.com/watch?v=UnwwZg1nFmM&pp=0gcJCWQCo7VqN5tD <br>
◦ https://docs.python.org/3/library/main.html <br>
