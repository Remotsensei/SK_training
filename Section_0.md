## QGIS Terrain model creation and processing

Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Terrain`

<div align="center">
<br>giulia.sofia@uconn.edu<br>
</div>

### Scope
This section presents the recommended steps to create a project, provide the correct configuration for RAS Mapper, and create the main terrain model.

### Goals
* Create and dowload public terrain and landuse datasets
* Embed hydraulic structures on terrain


### DEM Access via OpenTopography's API
Users can get terrain data product by using OpenTopography's API. Users can build the REST API call and it will output the appropriate request to use in a curl command, or a http GET request. Here is the URL request that can be used via https for COP30 data over Jeddah:

[https://portal.opentopography.org/API/globaldem?west=1&east=2&north=3&south=4&outputFormat=GTiff&demtype=COP30&API_Key=3bcf47df576e2b194d675751e70f98a5
](https://portal.opentopography.org/API/globaldem?west=39.11007123294027&east=40.66417151110259&north=21.70811841496722&south=21.055901572307814&outputFormat=GTiff&demtype=COP30&API_Key=3bcf47df576e2b194d675751e70f98a5)

Note that the DEMs downloaded from this API are in degrees. The data must be converted to meters for better processing in HEC-RAS 


### TERRAIN PREPARATION IN QGIS

1.	Pre-requisites

We rely on existing global DEMs at 30m. These data can be downloaded for multiple sources, directly from the Copernicus GLO-30
[https://registry.opendata.aws/copernicus-dem/]

To ‘automate’ the download, we can use a python routine in QGIS that relies on the package dem-stitcher to ‘fix’ the terrain data based on a certain extent and ‘rasterio’ to deal with rasters

	a.	Open OSGeo4W Shell as an administrator
	b.	pip install dem-stitcher
	c. 	pip install rasterio

After this, you can launch Qgis

To work on ‘’altering’ the terrain and add rivers, we rely on the toolbox ‘whiteboxtools’
WhiteboxTools is an advanced geospatial data analysis platform created by Prof. John Lindsay at the University of Guelph's Geomorphometry and Hydrogeomatics Research Group (GHRG). The project began in January 2017 and quickly evolved in terms of its analytical capabilities. The WhiteboxTools homepage contains more project information about the platform and the software download site.
For this, we need to install the toolbox in qgis
From the main menu’ select ‘Plugins’

 <div align="center">
<img alt="Fig01" src="images/picture1.png" width="85%">
</div>

Then select’ ALL’
And start searching for whitebox workflows for qgis

 <div align="center">
<img alt="Fig02" src="images/picture2.png" width="85%">
</div>


Install the plugin by clicking ‘install plugin’

------------------------------------

2.	Define your area of interest

In Qgis, we can ‘draw’ the area for which we want to run our analysis. At this stage, we can draw a simple ‘square’ area, around Jeddah, to get the bounding box of our entire domain. We will further improve this area for HEC ras in the following exercise.

a.	Add the boundary condition file (BoundaryConditions.shp)
b.	Create an empty layer  and save it in your working folder

  <div align="center">
<img alt="Fig03" src="images/picture3.png" width="85%">
</div>


c.	Set the parameters for the file
It is important to set a path where to save, select the type as polygon, and set the coordinates as EPSG: 4326 WGS84  (we need this at this stage, to be able to download the terrain data)

  <div align="center">
<img alt="Fig04" src="images/picture4.png" width="85%">
</div>

Once the layer is added automatically, right click on it, and set it as editable


  <div align="center">
<img alt="Fig05" src="images/picture5.png" width="85%">
</div>


d.	Draw a bounding box able to contain the whole extent of the BCs

On the toolbar, activate the ‘polygon’ tool

  <div align="center">
<img alt="Fig06" src="images/picture6.png" width="85%">
</div>

Once you do this, you will have a ‘shape digitizing’ toolbar, with the option to add a rectangle
There is a Shape Digitizing toolbar which has an option to add rectangle using different methods:
 
  <div align="center">
<img alt="Fig07" src="images/picture7.png" width="85%">
</div>

To show the toolbar, right-click the main menu and select Shape Digitizing toolbar
	
 <div align="center">
<img alt="Fig08" src="images/picture8.png" width="85%">
</div>


Add a field to the layer, using the field calculator. 

  <div align="center">
<img alt="Fig09" src="images/picture9.png" width="85%">
</div>

Set the field name ‘layer’ and content as ‘area1’. Set the field type as ‘string’

  <div align="center">
<img alt="Fig10" src="images/picture10.png" width="85%">
</div>

Save the editing by making the layer ‘uneditable’, and confirm the changes

3.	Get the terrain data

a.	Load the python console in qgis
 <div align="center">
<img alt="Fig11" src="images/picture11.png" width="85%">
</div>

 

To ‘automate’ the download, we can use a python routine in QGIS that relies on the package dem-stitcher to ‘fix’ the terrain data based on a certain extent.
Load the script GEtglo30.py
Set the path where you want to save the DEM file at the 
outputFolder=’’


Run the script.


4.	Alter the terrain

Load the files for rain_water_network and surface_water_network

Activate the toolbox bar, from the menu ‘processing’

  <div align="center">
<img alt="Fig12" src="images/picture12.png" width="85%">
</div>


In the toolbox bar, navigate to the whitebox workflows, go to ‘hydrology’
Then ‘fill_burn’
  <div align="center">
<img alt="Fig13" src="images/picture13.png" width="85%">
</div>


Run the tool, using the rain network first. Let’s use the DEM produced at the previous step, as stream we select the Rain_water_network, ad select an appropriate output path

  <div align="center">
<img alt="Fig14" src="images/picture14.png" width="85%">
</div>


Repeat the step, but using the dem burned, and adding the surface water network
 

 <div align="center">
<img alt="Fig15" src="images/picture15.png" width="85%">
</div>


Let’s observe differences.
 
### LANDUSE PREPARATION

To ‘automate’ the download, we can use a python routine in QGIS that relies on the package dem-stitcher to ‘fix’ the terrain data based on a certain extent.
Load the file esa_worldcover_2020_grid

Create in your local drive a tempOutput folder where we can save intermediate files

Load the script GETLC2.py

Set the path where you want to save the intermediate files at the 
tempOutputFolder='F:\\SK_Qgis\\training\\Wed27\\tempOutput\\'

and the final files
outputFolder='F:\\SK_Qgis\\training\\Wed27\\outputs\\'

Run the script.

Let’s load the dataset and observe it

  <div align="center">
<img alt="Fig16" src="images/picture16.png" width="85%">
</div>

