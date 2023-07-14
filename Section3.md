## Land use and boundary conditions
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Unsteady` `Hydraulic`

<div align="center">
<br>
<img alt="J.HRAS" src="../../.icons/0_HRAS.svg" width="400px">
<br><b>Giulia Sofia, PhD</b><br>
<br>giulia.sofia@uconn.edu<br>
<br></div>



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

