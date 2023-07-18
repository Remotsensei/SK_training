
import glob,os,re,shutil,h5py,subprocess,re,datetime,requests,json
import warnings
import numpy as np
import pandas as pd
import gc
from time import sleep

import matplotlib.pyplot as plt
from mplleaflet import mplexporter
from mplleaflet import leaflet_renderer
from mplleaflet import _display
import utm
import rasterutil as rutil

import scipy.interpolate as spint
import scipy.spatial.qhull as qhull
import itertools

from helpers import *

#####
warnings.filterwarnings('ignore')

###construct all the directory parameters
input_dir='/home/giulia/Training/Project_folder'
flow_dir=input_dir+'/input_flows/'

#hecras
hecPath='/home/giulia/Training/bin_ras/rasUnsteady64 '

#result folder
working_dir=input_dir+'/results/'

#name of DEM
DEMfile='DEM.asc'

#account info for HPC
account=''
partition='postproc'
ntasks=1 #number of cores for parallel processing
nnodes=1 #numbr of nodes for parallel processing


#default duration in case of no flows
duration_in_h=1
evST='2022/11/22:01' #start time in format %Y/%m/%d:%H
evE= '2022/11/22:02'#end time in format %Y/%m/%d:%H [must be consistent with above duration]


# HEC RAS project information
# Example: for the
#  the plan file, SMC_010.b06, project_name=SMC_010; plan_index=6 (see below)
geom_index=1 # @geom_index: index of geometry files. submit as an integer; zero-packing will be done.
plan_index=1 # @plan_index: index of plan files. submit as integer.
project_name=None #leave to None if project is provided with a *prj file

##### Construct filenames:
####1. parse python project from PRJ if project name is not provided
if project_name is None:
   plan_filename= glob.glob(input_dir+'/*.prj')[0]
   project_name=os.path.splitext(os.path.basename(plan_filename))[0]

geom_index = int(geom_index)
geom_index_str = '00{}'.format(geom_index)[-2:]
plan_index = int(plan_index)
plan_index_str = '00{}'.format(plan_index)[-2:]
# plan:
plan_h5_fname = '{}.p{}.hdf'.format(project_name, plan_index_str)
hdf_filename= input_dir+'/'+plan_h5_fname
b_fname = '{}.b{}'.format(project_name, plan_index_str)
#
# geometry:
x_fname = '{}.x{}'.format(project_name, geom_index_str)
g_hdf5 = '{}.g{}.hdf'.format(project_name, geom_index_str)
geom_filename=input_dir+'/'+g_hdf5


##get correspondence between bc and crest name
outnames = pd.read_csv(input_dir+'/boundary2CREST.csv')['OutName']
bcnames = pd.read_csv(input_dir+'/boundary2CREST.csv')['Name']


#get names of conditions
HRASf=h5py.File(hdf_filename,'r') # Read HEC-RAS 2D HDF output 
Bfiles=HRASf['Event Conditions']['Unsteady']['Boundary Conditions'] #this is where the boundary conditions are
Bfiles=list(Bfiles.keys()) #list all keys
HRASf.close()


fdest=createTempFile(hdf_filename) #create the .tmp.hdf file



Upstream=Bfiles[0]#the upstream conditions are by default the first group of conditions
keys=getB(hdf_filename,Upstream) #get their names

for id,item in enumerate(keys):
    BCcond=item.split('BCLine: ')[1]
    if sum(bcnames==BCcond)==1:
        OutN=outnames[bcnames==BCcond].astype(str).iloc[0] #find corresponding CREST name
        try:
            df=readCrestBASEFLOW(flow_dir+OutN+'.csv') 
            R=df['R'].round(2)
            dt=[df['Date'].iloc[0].strftime('%Y/%m/%d:%H'),df['Date'].iloc[-1].strftime('%Y/%m/%d:%H')]
            d1=np.array(list(zip([f*(float(1)/24) for f in range(0,len(R))],R)),dtype='float32')
            alterateKey(fdest,hdf_filename,d1,dt,Upstream,item)
        except:
            dt=[evST,evE]
            R=np.zeros(int(duration_in_h))
            d1=np.array(list(zip([f*(float(1)/24) for f in range(0,len(R))],R)),dtype='float32')
            alterateKey(fdest,hdf_filename,d1,dt,Upstream,item)
    else:
        dt=[evST,evE]
        R=np.zeros(int(duration_in_h))
        d1=np.array(list(zip([f*(float(1)/24) for f in range(0,len(R))],R)),dtype='float32')
        alterateKey(fdest,hdf_filename,d1,dt,Upstream,item)

#now embed start and end time in the b file
alterateBfile(input_dir,project_name,plan_index_str,dt)


#Now unfortunately, we need to convert the dos files to unix, so we will create a set of temporary files just in case
##convert dos to unix
job_file=input_dir+'/'+ x_fname #do it for the .x file
dos2unixlocal(job_file,input_dir)

job_file=input_dir+'/'+ b_fname #and now for the b file
dos2unixlocal(job_file,input_dir)


closeAllHDF()

hasupdates=runHEC(geom_index_str,plan_index_str,input_dir,hecPath,project_name,account,partition,ntasks,nnodes)
print('done with hec')  


##now do the postprocessing
#get the DEM
elevation,rastercoord,pixelcoord,header,fuseNumber,fuseLetter=getEE(hdf_filename,input_dir,DEMfile) #elevation in m, query points in utm

#get the name of the output file
pfileDone='{}/{}.p{}.hdf_done'.format(input_dir,project_name, plan_index_str)
print('start postproc')  

simtime=getsimtime(pfileDone)
#do the overall max for plotting
myDepth,td,a2= getResults_hourInterval(pfileDone,input_dir,DEMfile,'Depth',elevation,rastercoord,pixelcoord,0,simtime.shape[0])
myVelocity,td2,dd1= getResults_hourInterval(pfileDone,input_dir,DEMfile,'Velocity',elevation,rastercoord,pixelcoord,0,simtime.shape[0])

maxWW=HTMLforWarningEventsFast(myDepth,myVelocity,elevation,td,working_dir,project_name,header,rastercoord,fuseNumber,fuseLetter,a2,input_dir,1)
maxDD=HTMLforDepth(myDepth,elevation,td,working_dir,project_name,header,rastercoord,fuseNumber,fuseLetter,1)  

