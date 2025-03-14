## Manning Coefficients from Land Cover and boundary conditions
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Unsteady` `Hydraulic` `Manning` 

<div align="center">
<br><b>Giulia Sofia, PhD</b><br>
<br>giulia.sofia@uconn.edu<br>
<br></div>

### Scope
This section presents the recommended steps to set the Manning coefficient in the hydraulic model starting from a land cover file.

### Goals

* Know the procedure for loading land cover maps.
* Know the procedure for the adjustment and edition of the geometry from the information of Manning coefficients.
* Set the upstream and downstream boundary conditions.
#### Land cover maps

From an analytical point of view, it is possible to associate landcover data with **n** values ​​of the Manning coefficient, taking into account the recommendations mentioned in literature, attributing standard coefficients to standard landcovers. The following image shows for example, the suggested association, where a value **n** is assigned to different land cover characteristics.

<div align="center">
<img alt="manning" src="images/manning-n-NLCD.png" width="85%">
</div>

<sub><i>Example Manning's n values for various NLCD Land Cover Types. From HEC-RAS manual</i></sub><br>

#### Manning coefficient map creation


 
The ESA landcover classes are as follows

</table>
<table class="eecat">
<tr>
<th scope="col">Value</th>
<th scope="col">Color</th>
<th scope="col">Description</th>
</tr>
<tr>
<td>10</td>
<td><span style="background-color:#006400">#006400</span></td>
<td>Tree cover</td>
</tr>
<tr>
<td>20</td>
<td><span style="background-color:#ffbb22">#ffbb22</span></td>
<td>Shrubland</td>
</tr>
<tr>
<td>30</td>
<td><span style="background-color:#ffff4c">#ffff4c</span></td>
<td>Grassland</td>
</tr>
<tr>
<td>40</td>
<td><span style="background-color:#f096ff">#f096ff</span></td>
<td>Cropland</td>
</tr>
<tr>
<td>50</td>
<td><span style="background-color:#fa0000">#fa0000</span></td>
<td>Built-up</td>
</tr>
<tr>
<td>60</td>
<td><span style="background-color:#b4b4b4">#b4b4b4</span></td>
<td>Bare / sparse vegetation</td>
</tr>
<tr>
<td>70</td>
<td><span style="background-color:#f0f0f0">#f0f0f0</span></td>
<td>Snow and ice</td>
</tr>
<tr>
<td>80</td>
<td><span style="background-color:#0064c8">#0064c8</span></td>
<td>Permanent water bodies</td>
</tr>
<tr>
<td>90</td>
<td><span style="background-color:#0096a0">#0096a0</span></td>
<td>Herbaceous wetland</td>
</tr>
<tr>
<td>95</td>
<td><span style="background-color:#00cf75">#00cf75</span></td>
<td>Mangroves</td>
</tr>
<tr>
<td>100</td>
<td><span style="background-color:#fae6a0">#fae6a0</span></td>
<td>Moss and lichen</td>
</tr>
</table>

<sub><i>Landcover class [Source: https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v100]</i></sub><br>


 
2. From the HEC GUI go to RAS Mapper. We can import the file in raster format by clicking on **Project → Tools → New Land Cover**
   In the displayed window select the <kbd>+</kbd> icon to add the file. Then we have to create the correct legend (3), and add the Manning coefficients for each class (4). 
   We will start with the recommended value, and then do a further run using the higher end of the table above.
   
Review the classification names and information in the output file. Finally, click on <kbd>Crate</kbd> and the process will start.

<div align="center">
<img alt="Fig12" src="images/Fig12.jpg" width="85%">
</div>

4. Once the layer is created, you can view and review the information generated in RAS Mapper.

 >Note: It is important to associate this layer with the geometry data. This is a commonly overlooked step for new users.

<div align="center">
<img alt="Fig13" src="images/Fig13.jpg" width="85%">
</div>

### Boundary conditions

> Note: The spatial location of two different boundary conditions (BC – Boundary Condition Line) can not be defined on the same grid cell.

Multiple boundary conditions can be added to the composite mesh, and each can be associated to a hydrograph.
For modeling, at least one boundary condition line upstream and one downstream must be entered. Boundary condition lines can be drawn internally or externally, and they can be drawn or imported using a shapefile.

The following is the recommended process for importing the lines

1. In RAS Mapper edit mode, display the **Geometries** and **2D Flow Areas** tree. Then select the boundary condition lines and click layer properties. From there, select 'features' and select 'import features'. We can import the file BC.shp

<div align="center">
<img alt="Fig14" src="images/Fig14.jpg" width="85%">
</div>

Once you imported the features, you have to make sure that the lines are all covered by the extent of the domain, and by the computational area. Boundary conditions must allways be set as 'Internal'. The only exception is the downstream condition, which can be 'External' [In this project, this downstream feature corresponds to the BC 28]. In RAS Mapper edit mode, you can manually adjust the features and eventually delete those that you do not need, or add more where needed.


If you have to manually draw the lines, you can follow the following procedure. In RAS Mapper edit mode, display the **Geometries** and **2D Flow Areas** tree. Then select the boundary condition lines and with the edit bar draw in plan the upstream and downstream BC lines. Take into account that the traced line must be located in front of the cells of the channel zone. It is recommended to draw lines BC from left to right taking the flow direction as a reference. When finished, save the editing changes.


### References
- [HEC-RAS 2D User's Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/r2dum/latest)
- [HEC-RAS Mapper User's Manual](https://www.hec.usace.army.mil/confluence/rasdocs/rmum/latest)
