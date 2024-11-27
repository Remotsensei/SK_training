import urllib,os,re
import subprocess
from osgeo import gdal,osr

s3_url_prefix = "https://esa-worldcover.s3.eu-central-1.amazonaws.com"

input_shp = QgsProject.instance().mapLayersByName('esa_worldcover_2020_grid')[0]

tempOutputFolder='F:\\SK_Qgis\\training\\Wed27\\tempOutput\\'
outputFolder='F:\\SK_Qgis\\training\\Wed27\\outputs\\'


for feature1 in intersect_shp.getFeatures():
    intersect_shp.selectByIds([feature1.id()])
    output=processing.run("native:extractbylocation",
    {'INPUT':input_shp,
    'PREDICATE':[0],
    'INTERSECT':QgsProcessingFeatureSourceDefinition(intersect_shp.id(),
    selectedFeaturesOnly=True,
    featureLimit=-1,
    geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),
    'OUTPUT':'TEMPORARY_OUTPUT'})
    layer1 = output['OUTPUT']
    print(output)
    result = os.path.join(outputFolder, 'LUSE'+feature1['layer']+'.tif')
    if not os. path. isfile(result):
        print(result)
        l = []
        for feature in layer1.getFeatures():
            attrs = feature.attributes()
            print(attrs) 
            if not os.path.isfile(tempOutputFolder+attrs[0]+'.tif'):
                url = s3_url_prefix+"/v100/2020/map/ESA_WorldCover_10m_2020_v100_"+attrs[0]+"_Map.tif"
                urllib.request.urlretrieve(url, tempOutputFolder+attrs[0]+'.tif')
            l.append(tempOutputFolder+attrs[0]+'.tif')
        vrt_path = os.path.join(tempOutputFolder, 'prov_vrt.vrt')
        vrt_path2 = os.path.join(tempOutputFolder, 'prov_vrt2.tif')
        vrt_path3 = os.path.join(tempOutputFolder, 'prov_vrt3.tif')
        vrt_options = gdal.BuildVRTOptions(resampleAlg='cubic', addAlpha=True)            
        my_vrt = gdal.BuildVRT(vrt_path, l,options=vrt_options)
        bounds=intersect_shp.boundingBoxOfSelected()
        processing.run("gdal:cliprasterbyextent", {'INPUT':vrt_path,'PROJWIN':'{x},{y},{z},{u} [EPSG:4326]'.format(x=bounds.xMinimum(),y=bounds.xMaximum(),z=bounds.yMinimum(),u=bounds.yMaximum()),'OVERCRS':False,'NODATA':None,'OPTIONS':'','DATA_TYPE':0,'EXTRA':'','OUTPUT':vrt_path2})
        line='gdalwarp -s_srs EPSG:4326 -t_srs EPSG:32237 -r near -of GTiff {aa} {bb}'.format(aa=vrt_path2,bb=result)
        subprocess.run(line)
        line='gdal_translate -b 1 {aa} {bb}'.format(aa=vrt_path2,bb=result)
        subprocess.run(line)
        os.remove(vrt_path)
        os.remove(vrt_path2)
        os.remove(vrt_path3)
    else:
        print('skipped')#break
