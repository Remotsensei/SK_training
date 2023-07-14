
import glob,os,re,shutil,h5py,subprocess,re,datetime
import warnings
import numpy as np
import pandas as pd
import gc
from time import sleep

####Functions
#replace specific line in file
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    
#close all open hdf
def closeAllHDF():
    for obj in gc.get_objects():   # Browse through ALL objects
        if isinstance(obj, h5py.File):   # Just HDF5 files
            try:
                obj.close()
            except:
                pass # Was already closed
                
# get the boundaries keys from the hdf file
def getB(hdf_filename,type):
    hf = h5py.File(hdf_filename,'r') 
    Ky=hf['Event Conditions']['Unsteady']['Boundary Conditions'][type].keys()
    return Ky
    
    
def createTempFile(hdf_filename):
    closeAllHDF()
    #remove existing temp file
    if os.path.exists(os.path.splitext(hdf_filename)[0]+'.tmp.hdf'):
            os.remove(os.path.splitext(hdf_filename)[0]+'.tmp.hdf')            
    #read the input 'original' hdf, and remove the results
    if not os.path.exists(os.path.splitext(hdf_filename)[0]+'.tmp.hdf'):
            fsource=h5py.File(hdf_filename,'r')
            fdest=h5py.File(os.path.splitext(hdf_filename)[0]+'.tmp.hdf','w')
            for fattr in fsource.attrs.keys():
                fdest.attrs[fattr]=fsource.attrs.get(fattr)
            for fg in fsource.keys():
                if fg !='Results' :
                    fsource.copy(fg,fdest)        
            fdest.close()
            fsource.close()
    fdest=os.path.splitext(hdf_filename)[0]+'.tmp.hdf'
    return fdest
            
#function to read the CSV files from CREST.
def readCrestBASEFLOW(filename):
    datetimeFormat='%Y/%m/%d:%H'
    upstream = pd.read_csv(filename)
    upstream['Date'] = pd.to_datetime(upstream['Date'], format=datetimeFormat) 
    return upstream

##write flows into HDF from hecras
#fdest = destination file
#fsource = source hdf to duplicate
#d1= touple of flows and time interval 
#dt time interval to get start and end
#actual key= key to read in the HDF
#item subkey indicating which boundary condition to write
def alterateKey(fdest,fsource,d1,dt,actualKey,item):
        time2write1=np.array(datetime.datetime.strptime(dt[0],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H%M')).astype('S')
        time2write2=np.array(datetime.datetime.strptime(dt[-1],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H%M')).astype('S')
        time2write3=np.array(datetime.datetime.strptime(dt[0],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H:%M:%S')).astype('S')
        time2write4=np.array(datetime.datetime.strptime(dt[-1],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H:%M:%S')).astype('S')
        t4=np.array(datetime.datetime.strptime(dt[0],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H:%M:%S') +' to ' + datetime.datetime.strptime(dt[-1],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H:%M:%S')).astype('S')
        fs=h5py.File(fsource,'r')
        ds= h5py.File(fdest,'r+')
        try:
                  del ds['Event Conditions']['Unsteady']['Boundary Conditions'][actualKey][item] # delete old, differently sized dataset
        except:
                  None
        try:
                  ds.create_dataset('Event Conditions/Unsteady/Boundary Conditions/'+actualKey+'/'+item, data=d1,shape=d1.shape)
        except:
                  ds.create_dataset('Event Conditions/Unsteady/Boundary Conditions/'+actualKey+'/'+item, data=d1)
        for fattr in fs['Event Conditions']['Unsteady']['Boundary Conditions'][actualKey][item].attrs.keys():
            if fattr=='Start Date':
                ds['Event Conditions']['Unsteady']['Boundary Conditions'][actualKey][item].attrs[fattr]=time2write1
            elif fattr=='End Date':
                ds['Event Conditions']['Unsteady']['Boundary Conditions'][actualKey][item].attrs[fattr]=time2write2
            else:
                try:
                    ds['Event Conditions']['Unsteady']['Boundary Conditions'][actualKey][item].attrs[fattr]=fs['Event Conditions']['Unsteady']['Boundary Conditions'][actualKey][item].attrs.get(fattr)
                except:
                    ds['Event Conditions']['Unsteady']['Boundary Conditions'][actualKey][item].attrs[fattr]=''
        for fattr in fs['Plan Data']['Plan Information'].attrs.keys():
            if fattr=='Simulation Start Time':
                ds['Plan Data']['Plan Information'].attrs[fattr]=time2write3
            elif fattr=='Simulation End Time':
                ds['Plan Data']['Plan Information'].attrs[fattr]=time2write4
            elif fattr=='Time Window':
                ds['Plan Data']['Plan Information'].attrs[fattr]=t4           
        fs.close()
        ds.close()


##fix B01 file
def alterateBfile(folder,project_name,plan_index_str,dt):
        planFile=folder+'/'+'{}.b{}'.format(project_name, plan_index_str)
        time2write1=datetime.datetime.strptime(dt[0],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H%M')
        time2write2=datetime.datetime.strptime(dt[-1],'%Y/%m/%d:%H').replace(tzinfo=datetime.timezone.utc).strftime('%d%b%Y %H%M')
        replace_line(planFile, 46, '  Start Date/Time       = '+time2write1+'\n')
        replace_line(planFile, 47, '  End Date/Time         = '+time2write2+'\n')
        

##workaround to convert dos to unix
def dos2unixlocal(job_file,input_dir):
    pipe = subprocess.Popen("tr -d '\r' < %s >  plan.x" %job_file,shell=True,cwd=input_dir)
    pipe.wait()
    while True:
        doesItExist=os.path.exists('{}/{}'.format(input_dir,'plan.x'))
        if doesItExist:
            break
        else:
            sleep(30)
    pipe = subprocess.Popen("mv plan.x %s" %job_file,shell=True,cwd=input_dir)
    pipe.wait()
    while True:
        doesItExist=os.path.exists(job_file)
        if doesItExist:
            break
        else:
            sleep(30)

##function to launch hec rasUnsteady64

#function to run hecras in linux
def runHEC(geom_index_str,plan_index_str,folder,hecPath,project_name,account,partition,ntasks,nnodes):
    if os.path.exists('{}/{}.p{}.hdf_done'.format(folder,project_name, plan_index_str)):
            os.remove('{}/{}.p{}.hdf_done'.format(folder,project_name, plan_index_str))
    fileforsh = ''.join([c for c in project_name if c not in "aeiouAEIOU"])
    job_file=folder+'/'+fileforsh+'.sh'
    if os.path.exists(job_file):
            os.remove(job_file)
    print('launching job'+fileforsh)
    str1=hecPath+'{}.c{} b{}\n'.format(project_name,geom_index_str,geom_index_str)
    str2='mv '+'{}/{}.p{}.tmp.hdf '.format(folder,project_name, plan_index_str)+'{}/{}.p{}.hdf_done\n'.format(folder,project_name, plan_index_str)
    str3='module load gcc/5.4.0\n'
    str4='RAS_BIN_PATH='+os.path.dirname(hecPath)+'\n'
    str5='export LD_LIBRARY_PATH=$RAS_BIN_PATH:$LD_LIBRARY_PATH\n'
    with open(job_file,'w') as fh:
            fh.writelines("#!/bin/bash -l\n")
            if account=='':
                pass
            else:
                fh.writelines("#SBATCH --account=%s\n" % account)
            fh.writelines("#SBATCH --partition=%s\n" % partition)
            fh.writelines("#SBATCH --nodes=%s\n" % nnodes)
            #fh.writelines("#SBATCH --mem=64G\n")
            #fh.writelines("#SBATCH --ntasks=%s\n" % ntasks)
            fh.writelines("#SBATCH --output=%s.HECout\n" % project_name)
            fh.writelines("#SBATCH --error=%s.HECerr\n" % project_name)
            fh.writelines(str4)
            fh.writelines(str5)
            #fh.writelines(str3)
            fh.writelines(str1)
            fh.writelines(str2)
    ##convert dos to unix
    pipe = subprocess.Popen("tr -d '\r' < %s >  job.sh" %job_file,shell=True,cwd=folder)
    pipe.wait()
    pipe = subprocess.Popen("mv job.sh %s" %job_file,shell=True,cwd=folder)
    pipe.wait()       
    
    # Call RasMapper to generate tif
    pipe = subprocess.Popen("sbatch %s" %job_file,shell=True,cwd=folder)
    pipe.wait()
    while True:
    	doesItExist=os.path.exists('{}/{}.p{}.hdf_done'.format(folder,project_name, plan_index_str))
    	if doesItExist:
    		break
    	else:
    		sleep(30)
    return doesItExist
    
#####
warnings.filterwarnings('ignore')

###construct all the directory parameters
input_dir='/home/giulia/Training/Project_folder'
flow_dir=input_dir+'/input_flows/'

#hecras
hecPath='/home/giulia/Training/bin_ras/rasUnsteady64 '


#account info for HPC
account=''
partition='postproc'
ntasks=24 #number of cores for parallel processing
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
