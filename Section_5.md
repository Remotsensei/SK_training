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

| Landuse  | previous value | Updated value |
| ------------- | ------------- | ------------- |
| tree cover  | 0.1  | 0.2 |
| shrubland | 0.08  | 0.16 |
| grassland | 0.04  | 0.05 |
| croplad | 0.05  | 0.020 |
| built up | 0.15  | 0.2 |
| bare/sparse | 0.03  | 0.023 |
| permanent water bodies | 0.035  | 0.035 |
| herbaceous | 0.06  | 0.05 |
| mangroves | 0.1  | 0.06 |

Make sure you attribute this manning to the geometry. 
Start a new plan, name it Plan 2, and run the software. Compare the results

### Plan settings


Start a new plan and name it Plan 3

* Switch the computation option to Either full momentum, or diffusion wave
* Add a warmup time of 6 hrs
* Change the computational timestep to dynamic

Run the software. Compare the results
  
<div align="center">
<img alt="catt" src="images/Cattura.png" width="85%">
</div>
