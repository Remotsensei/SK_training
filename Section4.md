## 2D two-dimensional hydraulic modeling
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Unsteady` `Hydraulic`  

<div align="center">
<br><b>Giulia Sofia, PhD</b><br>
<br>giulia.sofia@uconn.edu<br>
<br></div>

### Reach
This class presents the recommended process for the definition of data and boundary conditions and the two-dimensional (2D) simulation in unsteady flow conditions.

### Goals

* Define flow information and boundary conditions.
* Carry out the configuration of the simulation plan.
* Configure variable time intervals.
* Define the system of equations to solve the hydraulic model.
* Run the two-dimensional hydraulic simulation.

### Flow information and boundary conditions

1. To start, we are going to enter the **Unsteady flow data** window, from the menu **Edit → Unsteady flow data**. In the popup window select **File → New/Save unsteady flow data** and enter the name you want to give the flow data and click the <kbd button >**OK**</kbd>.


![image](https://github.com/Remotsensei/SK_training/assets/127943691/f8c1406d-7cb7-4ca0-a008-643f8260a936)


2. In the **Unsteady flow data** window, you can enter a description of the flow information, as well as define the boundary conditions, initial conditions and add meteorological or observed information in the system to model. For this exercise, we will add a flow hydrograph upstream of the channel for each upstream, and define smooth flow in the downstream section (BC Line 28). Once you enter all the information click on the <kbd>**Apply Data**</kbd> button that you will find in the upper right part of the window. Finally, select <kbd>**Plot Data**</kbd> to verify and review the data upload. Remember to save the changes made to the flow characteristics and hydraulic conditions

![image](https://github.com/Remotsensei/SK_training/assets/127943691/9f992a1a-00a2-4ec3-bce1-f5e4cabc9786)

![image](https://github.com/Remotsensei/SK_training/assets/127943691/829fce67-4382-4609-a18c-3f6dac75bc8b)


> Remember that in the case of hydrographs or station-flow curves, you must correctly define the start and end times of the hydrograph, as well as the time interval and the slope of the energy line (EG slope for distributing flow, we can use 0.015).


### Simulation plan and simulation

1. Enter the **Unsteady flow analysis** window. And in the popup window select **File → New/Save plan** (File → Save plan). Then enter the name with which you want to save the plan. A file in the format <kbd>.p*</kbd> will be created.

![image](https://github.com/Remotsensei/SK_training/assets/127943691/c876c50d-b152-4542-84d4-ce76cc655a51)


2. In the flow analysis window, enter a description and check that the geometry file and flow data are correctly selected. Then select the modeling features or programs (geometry preprocessor, unsteady flow simulation, sediments, post-processor, flood mapping). You must also define the simulation start and end times and the calculation properties (calculation interval, output hydrograph interval, output map interval, and output file).

![image](https://github.com/Remotsensei/SK_training/assets/127943691/c77d71a1-d1f4-469a-81bd-d1dc78d7c26e)

In the menu **Options → Calculation options and tolerances**, there you can define and/or select the calculation options, equations, initial conditions, tolerances, among others. Likewise, in the <kbd>Advanced Time Step Control</kbd> tab you can leave the time fixed or self-adjusting based on the Courant condition.

3. Finally click on the <kbd>**Compute**</kbd> button and the simulation calculations will start.

![image](https://github.com/Remotsensei/SK_training/assets/127943691/380e01a7-abd6-4424-a831-125322456111)


---
> **Note 1: Equations to solve the model** <br> HEC-RAS has the option to run the following sets of equations: 2D diffusion wave equations, local inertia approximation (SWE-LIA) and the Saint-Venant equations or Shallow Water Equations (SWE) with two different advection approaches (Eulerian-Lagrangian (SWE-ELM) and Eulerian (SWE-EM)). In general, all solvers use a combination of finite difference and finite volume methods on an unstructured polygon mesh with subgrid bathymetry.<br><br>
The SWE solution method (formerly *full momentum*), is more conservative of momentum, but may require smaller time steps and produce longer execution times. The default equations are the diffusive wave equations, with which many flooding applications will work well. <br><br> The <kbd>Diffusion Wave</kbd> set of equations will run faster and is inherently more stable. However, there are applications where the <kbd>SWE 2D</kbd> should be used for better accuracy. <br><br> The user can test multiple equation sets and compare the answers efficiently by selecting the equation set to use and running the simulation. It is suggested that users first create a new plan file and then use a different set of equations to easily compare the results. For more information, you can consult the [User Manual](https://www.hec.usace.army.mil/confluence/rasdocs/r2dum/latest/running-a-model-with-2d-flow-areas/2d-computation -options-and-tolerances) or the [Reference Manual.](https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/latest/theoretical-basis-for-one-dimensional-and-two -dimensional-hydrodynamic-calculations/2d-unsteady-flow-hydrodynamics/numerical-methods) <br><br> **Recommendation** Some particular situations in which the use of SWE (*full momentum*) equations is recommended They are: <br> • High variation in flow wave dynamics: dam breaks and instantaneous flow modeling.  

> **Note 2: Variable time intervals (Advanced Time Step Control)** <br> Recent versions of HEC-RAS allow the definition of self-adjusting times based on the Courant condition, to optimize the numerical precision of the data. values ​​calculated from the hydraulic equations of the model. This criterion evaluates the spacing between the cross sections or the size of the faces of the cells of the mesh and the wave velocity of the flow. In general, the defined calculation interval should be equal to or less than the time it takes for water to move from one section or cell to another. <br><br> In models with multiple cross sections or with very small cells, using this condition can cause the model to require a long time to solve. If the distance between two cross sections or the side of a cell is very large, the Courant number should be less than 1. <br> <br> HEC-RAS has two methodologies for applying the Courant criterion, the first based on the velocity of the wave and the second based on the residence time of the flow in the control volume. <br><br> The values ​​defined for maximum and minimum Courant will depend on the type of equations used to hydraulically solve the model. This configuration must be applied independently to each plan. To apply the full Saint-Venant equation (full momentum) or Shallow Water Equations (SWE), it is recommended to use Courant values ​​between +-1 and 3. For Diffusive Wave equations only, use values ​​between +-2 and 5. For more information, you can consult the [Manual.](https://www.hec.usace.army.mil/confluence/rasdocs/r2dum/latest/running-a-model-with-2d-flow-areas/variable-time -step-capabilities) <br><br> The new <kbd>SWE</kbd> solver (SWE-EM) is an explicit solution scheme that is based on a more conservative form of the momentum equation. This solver requires time steps to be selected to ensure that the Courant number is generally less than 1 (not always). This solver produces less numerical diffusion than the original SWE solver. In general, however, SWE-EM is needed only when users are interested in closely observing changes in water surfaces and velocities in and around hydraulic structures. pillars/pillars and tight contractions and expansions. The original SWE (*full momentum*) solver is more than adequate for most problems that require the solution scheme based on the full momentum equation.
---


### References
- [HEC-RAS User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/rasum/latest)
- [HEC-RAS Hydraulic Reference Manual.2020](https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/latest)
- [HEC-RAS Documentation. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs)
- [HEC-RAS Mapper User's Manual](https://www.hec.usace.army.mil/confluence/rasdocs/rmum/latest)
- [HEC-RAS 2D User’s Manual. US Army Corps of Engineers.](https://www.hec.usace.army.mil/confluence/rasdocs/r2dum/latest)
