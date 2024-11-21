## HECRAS sensitivity to parameters
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Terrain`

<div align="center">
<br>giulia.sofia@uconn.edu<br>
</div>

### Scope
This section presents an example of how to change and test differences in results, based on the simulation parameters


### Goals
* Test the sensitivity to hecras to various settings

### Mannings

The following image shows for example, the suggested association, where a value **n** is assigned to different land cover characteristics.

<div align="center">
<img alt="manning" src="images/manning-n-NLCD.png" width="85%">
</div>

<sub><i>Example Manning's n values for various NLCD Land Cover Types. From HEC-RAS manual</i></sub><br>


Repeat the steps to create the manning file, and create a new file Manning2. Attribute this file to the geometry, and change the values of mannings

| Landuse  | previous value | Next value |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

