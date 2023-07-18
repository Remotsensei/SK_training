### Resources

This subfolder contains all the files needed for this course

1. inputFlows_radar.zip > flow hydrographs for multiple outlets for the Jeddah area, for the event of nov 2022. The hydrographs are computed by CREST using radar rainfall.
2. inputFlows_WRF.zip > flow hydrographs for multiple outlets for the Jeddah area, for the event of nov 2022. The hydrographs are computed by CREST using forecasted data from WRF.
3. run_me.py > python pipeline to run hecras in linux.
4. Geotiffs.zip > terrain and landuse data for HECRas
5. BC.zip > boundary condition lines location
6. boundary2CREST.csv > correspondence between the CRESt outlet names, and the BC lines in HECRas
7. Python_scripts.zip > subroutines to [partially] run the NCM system. This folder contains
		mplleaflet > a Python library that converts a matplotlib plot into a webpage containing a pannable, zoomable Leaflet map. The folder is a modified version of https://github.com/jwass/mplleaflet [modified to be compatible with the NCM system and cluster]
		binner.py > routine to quickly create the hexagons
		helpers.py > all subroutines needed to prepare the hecras files and create the final outputs
		rasterutils.py > a serie of scripts to work with raster data.
		utm.py > routines to convert from UTM to lat-lon
	all these folders/scripts should be uploaded in the main directory
