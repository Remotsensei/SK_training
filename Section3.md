## Manning Coefficients from Land Cover and boundary conditions
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Unsteady` `Hydraulic` `Manning` 

<div align="center">
<br><b>Giulia Sofia, PhD</b><br>
<br>giulia.sofia@uconn.edu<br>
<br></div>

### Scope
This class presents the recommended process for the definition of the Manning coefficient in the hydraulic model from a land cover file using RAS Mapper.

### Goals

* Know the procedure for loading land cover maps.
* Know the procedure for the adjustment and edition of the geometry from the information of Manning coefficients.
* Plot the upstream and downstream boundary condition.
#### Land cover maps

It is common for a project that involves  hydraulic modeling to have additional information such as land cover and land use. 
Based on this information on land cover and land use, it is possible to associate said information with **n** values ​​of the Manning coefficient, taking into account the recommendations mentioned in literature, attributing standard coefficients to standard landcovers
![image](https://github.com/Remotsensei/SK_training/assets/127943691/eb6ebd6f-48ac-4381-a7b6-7e4093621030)

<sub><i>Surface Roughness and Manning’s ‘n’ Table as suggested for HECRas, based on NLCD land cover types</i></sub><br>



The following image shows the association made for the example of the course, where a value **n** is assigned to different land cover characteristics.

<div align="center">
<img alt="Manning" src="Screens/Screen1.png" width="60%">
</div>

#### Manning coefficient map creation

1. In the HEC tool go to the RAS Mapper tool. Now we import the file in vector format with geographic elements by clicking on **Project → Create New RAS Layer → Land Cover Layer** (Project → Create a New RAS Layer → Land Cover Layer).

<div align="center">
<img alt="Manning" src="Screens/Screen2.png" width="60%">
</div>

2. In the displayed window select the <kbd>+</kbd> icon to add the file. Then select the file extension as **"Geometries"** and then add the Manning coefficients field (click <kbd>Add Fiel...</kbd> ).

<div align="center">
<img alt="Manning" src="Screens/Screen3.png" width="60%">
</div>

3. Review the classification names and information in the output file. Finally click on <kbd>Crate</kbd> and the process will start.

<div align="center">
<img alt="Manning" src="Screens/Screen4.png" width="60%">
</div>
 
4. Once the layer is created, you can view and review the information generated in the RAS Mapper.

<div align="center">
<img alt="Manning" src="Screens/Screen5.png" width="60%">
</div>

#### Geometry adjustment and definition of coefficients

1. For 1D geometry adjustment, start the edit option by clicking the <kbd>:pencil2:</kbd> button. Then right click on the cross sections and select **Update Cross Sections → Manning's Values**. Stop editing and save the changes.

<div align="center">
<img alt="Manning" src="Screens/Screen6.png" width="60%">
</div>

2. You will be able to view and review the fit to the information from the geometric information window with the help of the Manning values ​​edition table (Tables → Manning's n or k Values).
 
<div align="center">
<img alt="Manning" src="Screens/Screen7.png" width="60%">
</div>


### Boundary conditions

The spatial location of two different boundary conditions (BC – Boundary Condition Line) must not be defined on the same grid cell. Multiple boundary conditions can be added to the composite mesh. Multiple inlet hydrographs may be associated, for example, in the mainstem and laterals.

For modeling, at least one boundary condition line upstream and one downstream must be entered. Boundary condition lines can be drawn internally or externally. For example, base flow or ground flow can be defined in any internal zone of the model. BC lines can be drawn or imported using a shapefile. It is recommended to import these lines when dealing with non-straight elements such as circular or curved weirs.

The following is the recommended process for drawing the lines for boundary conditions:

1. In RAS Mapper edit mode, display the **Geometries** and **2D Flow Areas** tree. Then select the boundary condition lines and with the edit bar draw in plan the upstream and downstream BC lines. Take into account that the traced line must be located in front of the cells of the channel zone. It is recommended to draw lines BC from left to right taking the flow direction as a reference. When finished, save the editing changes.

<div align="center">
<img alt="Property" src="Screens/Screen4.png" width="70%">
<img alt="Property" src="Screens/Screen5.png" width="80%">
</div>


### References
- [HEC-RAS User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/rasum/latest)
- [HEC-RAS Hydraulic Reference Manual.2020](https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/latest)
- [HEC-RAS Documentation. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs)
- [HEC-RAS Mapper User's Manual](https://www.hec.usace.army.mil/confluence/rasdocs/rmum/latest)
- [HEC-RAS 2D User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/r2dum/latest)

