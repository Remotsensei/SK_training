import dem_stitcher
from dem_stitcher import stitch_dem
import urllib,os,re
from osgeo import gdal,osr
import rasterio
import subprocess

intersect_shp = QgsProject.instance().mapLayersByName('selected_area')[0]
cn=0

outputFolder='F:\\SK_Qgis\\training\\Wed27\\outputs\\'

for feature1 in intersect_shp.getFeatures():
    cn=cn+1
    print(feature1['layer'])
    intersect_shp.selectByIds([feature1.id()])
    result = os.path.join(outputFolder, 'DEM_'+feature1['layer']+'merged.tif')
    output_raster= os.path.join(outputFolder, 'DEM_'+feature1['layer']+'t.tif')     
    if not os.path.isfile(result):
        # as xmin, ymin, xmax, ymax in epsg:4326
        bounds=intersect_shp.boundingBoxOfSelected()
        bounds=[bounds.xMinimum(),bounds.yMinimum(),bounds.xMaximum(),bounds.yMaximum()]
        X, p = stitch_dem(bounds,
                          dem_name='glo_30',
                          dst_ellipsoidal_height=False,
                          dst_area_or_point='Point')

        with rasterio.open(output_raster, 'w', **p) as ds:
           ds.write(X, 1)
           ds.update_tags(AREA_OR_POINT='Point')
        line='gdalwarp -s_srs EPSG:4326 -t_srs EPSG:32237 -r near -of GTiff {aa} {bb}'.format(aa=output_raster,bb=result)
        subprocess.run(line)
        os.remove(output_raster)
