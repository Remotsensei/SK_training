## Hydraulic modeling in linux
Keywords: `Hydraulics` `HEC-RAS` `2D` `Modeling` `Unsteady` `Hydraulic`  `Linux`

<div align="center">
<br><b>Giulia Sofia, PhD</b><br>
<br>giulia.sofia@uconn.edu<br>
<br></div>

### Reach
This class presents the recommended process for running the two-dimensional (2D) simulation in Linux.

### Goals

* Prepare the project
* Prepare the input flows
* Run the python scripts
* Launch HEC-Ras to run the two-dimensional hydraulic simulation.

### HEC RAS Linux packet
The RAS_507_linux.zip contains the rasUnsteady64 Linux executable and supporting libraries

![image](https://github.com/Remotsensei/SK_training/assets/127943691/2b9a4767-fff9-49f8-b557-775aaa89ad00)

![image](https://github.com/Remotsensei/SK_training/assets/127943691/954d0388-eadb-42df-a193-d1092b32e61e)

1. The HEC-RAS GUI will need to be run to provide a base set of the input files for the Linux compute.
   
Geometry based files

	- *.c01 
	- *.x01 
> Note: Text based files will need to have the ending carriage return character stripped to be Linux compatible (.x04 and b04). 

- *.g01.hdf 
- *.b01 
- *.p01.tmp.hdf
- *.p01.hdf

The file tmp.hdf is needed to run HEC-Ras in linux. The *.tmp.hdf* is derived from an HEC-RAS GUI version of the original *.p01.hdf* that includes bcs, plan and geometry data, but has been stripped of the results.  The file must have consistent name, and extension

![image](https://github.com/Remotsensei/SK_training/assets/127943691/6ae89aa4-3cf6-43fc-8255-abf51b1da782)

Below is an example of the python script which copies all data groups but “Results” from the Muncie.p04.hdf into Muncie.p04.tmp.hdf 

![image](https://github.com/Remotsensei/SK_training/assets/127943691/4b5a0bd9-990a-42ca-bd02-7943a2fa0932)
