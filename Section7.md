## Hydraulic modeling in linux
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Unsteady` `Hydraulic`  `Linux`

<div align="center">
<br><b>Giulia Sofia, PhD</b><br>
<br>giulia.sofia@uconn.edu<br>
<br></div>

### Scope
This section presents the recommended steps for removing roads and bridges from a terrain data.

### Goals

* Visualize the terrain
* remove the bridges/roads


<ins> 1.	Load the Terrain and visualize the roads </ins>

Step 1: Add Your Elevation Raster
Next, go to Layer > Add Layer > Add Raster Layer to add your elevation raster. For this example, we will use the Terrain provided

Step 3: Access the Hillshade Tool
videos/hillshade1.mp4


<ins> 2.	Define your area of interest </ins>

In Qgis, we can ‘draw’ the area for which we want to remove the roads. At this stage, we can draw a simple ‘square’ area, around a single road. Optionally, one could create one for each road/bridge they want to remove

a.	Add the road file
b.	zoom to the road

<div align="center">
<img alt="road" src="images/roads1.png" width="55%">
</div>

c.  Create an empty layer  and save it in your working folder

<div align="center">
<img alt="Fig03" src="images/Picture3.png" width="55%">
</div>


c.	Set the parameters for the file
It is important to set a path where to save, select the type as polygon, and set the coordinates as EPSG:32237  [it must be the same coordinate system of your terrain!)

Once the layer is added automatically, right click on it, and set it as editable


  <div align="center">
<img alt="Fig05" src="images/Picture5.png" width="55%">
</div>


d.	Draw a bounding box able to contain the whole extent of the road

On the toolbar, activate the ‘polygon’ tool

  <div align="center">
<img alt="Fig06" src="images/poly1.png" width="55%">
</div>

Once you do this, you will have a ‘shape digitizing’ toolbar, with the option to add a rectangle
There is a Shape Digitizing toolbar which has an option to add rectangle using different methods:
 
  <div align="center">
<img alt="Fig07" src="images/Picture7.png" width="55%">
</div>

To show the toolbar, right-click the main menu and select Shape Digitizing toolbar
Draw your polygon to encompass the visible road on the terrain

  <div align="center">
<img alt="Fig10" src="images/roads2.png" width="55%">
</div>

Save the editing by making the layer ‘uneditable’, and confirm the changes

------------------------------------
