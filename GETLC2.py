import urllib,os,re
import subprocess

from osgeo import gdal,osr

import urllib,os,re
from osgeo import gdal,osr

intersect_shp = QgsProject.instance().mapLayersByName('selected_area')[0]
cn=0

vrt_path='F:\\SK_Qgis\\training\\Wed27\\outputs\\LUSE2.vrt'
outputFolder='F:\\SK_Qgis\\training\\Wed27\\outputs\\'



for feature1 in intersect_shp.getFeatures():
    intersect_shp.selectByIds([feature1.id()])
    result = os.path.join(outputFolder, 'LUSE'+feature1['layer']+'.tif')
    if not os. path. isfile(result):
        print(result)
        vrt_path2 = os.path.join(outputFolder, 'prov_vrt2.tif')
        bounds=intersect_shp.boundingBoxOfSelected()
        processing.run("gdal:cliprasterbyextent", {'INPUT':vrt_path,'PROJWIN':'{x},{y},{z},{u} [EPSG:4326]'.format(x=bounds.xMinimum(),y=bounds.xMaximum(),z=bounds.yMinimum(),u=bounds.yMaximum()),'OVERCRS':False,'NODATA':None,'OPTIONS':'','DATA_TYPE':0,'EXTRA':'','OUTPUT':vrt_path2})
        line='gdalwarp -s_srs EPSG:4326 -t_srs EPSG:32237 -r near -of GTiff {aa} {bb}'.format(aa=vrt_path2,bb=result)
        subprocess.run(line)
        os.remove(vrt_path2)
    else:
        print('skipped')#break