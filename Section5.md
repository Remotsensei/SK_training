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


### Needed project files

1. After running the HEC-RAS GUI, we can upload to the HPC, the following files

![image](https://github.com/Remotsensei/SK_training/assets/127943691/2f4e7d6a-6ef1-4601-9818-ca2bbb2e3183)

2. In addition to these files, the system needs a *.csv file [boundary2CREST.csv] that links the names of the BC in hecras, to the names of the corresponding outlets from CREST
   
 ![image](https://github.com/Remotsensei/SK_training/assets/127943691/0547f632-82e6-4567-9318-567e97da6cff)

> Note: this file can be created using any GIS software, and providing a spatial join between the outlets and the HECras BC. It can also be created manually, provided that the user knows the abovementioned information. Note that the file header **must** be consistent with the example above, for the script to run
