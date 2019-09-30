import os
import subprocess
import re
from platform import python_version
from pytet import *


python_version_local=python_version().replace(".","")
nums=list()
groupID=list()

def execCommand():
    return
    
def executeCMD(cmd,user1='SUPER.SUPER,fsqa123',option="cmd"):
    cmdExec=None
    cmdExec=None
    if "su" in option:
       cmd="su - "+str(os.environ[user1])+",password -c '"+str(cmd)+"'"
    if (str(python_version_local) >= "2713" and str(python_version_local) <= "2900"):
        #print("Here...if",str(python_version_local),"CMD:",cmd)
        process=subprocess.Popen(cmd,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        out,rcode=process.communicate()
        process.wait()
        return ([out,rcode,process.returncode])

    else:
        cmdExec=subprocess.run(cmd,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        return ([cmdExec.stdout,cmdExec.returncode,cmdExec.stderr]) 

def NonStopSUTVersion():
    cmd = [ 'gtacl -c sutver' ]
    output = subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
    sutver = "".join(((output.split(" ")[0]).split("."))[:2])
    Version = re.sub("[^0-9]", "",sutver)
    Series = re.sub("[0-9]", "",sutver)

    return Series + "::" + Version

def printStr(msg):
    if (str(python_version_local) >= "2713" and str(python_version_local) <= "2900"):
        print(str(msg))
    else:
        print ("{}".format(str(msg)))

def CompareString(aList):
    found=False
    lMessage=[]
    if os.path.exists(aList[-1].strip()):
        lMessage.append("File exists "+str(aList[-1].strip()))
        if os.path.isfile(aList[-1].strip()):
            lMessage.append("isFile "+str(os.path.isfile(aList[-1].strip())))
            lFile=open(aList[-1].strip(),"r").readlines()
            for aListcontent in aList[:-1]:
                found1=True
                for lFile1 in lFile:
                    if aListcontent in lFile1.strip():
                        lMessage.append(lFile1.strip()+str("::")+str(True))
                        found1=False
                        break
                if found1:
                    lMessage.append(aListcontent.strip()+str("::")+str(False))
    else:
        found=False
    if any("::False" in s for s in lMessage):
        lMessage.append(1)
    else:
        lMessage.append(0)
    return lMessage

def writeToFile(str,fileName):
   with open(fileName,'w') as f:
       f.write(str)
   return fileName

def tet_infoline_output(name,output):
  tet_infoline("-------------------------------------")
  tet_infoline(""+str(name))
  tet_infoline("Return code : "+str(output[2]))
  tet_infoline("-------------------------------------")
  localOut=output[1]
  if (output[0]):
      localOut=output[0]

  for i in localOut.split("\n"):
      if (i):
        tet_infoline(str(i).strip())
  tet_infoline("-------------------------------------")
  
def newGroupID():
    for num in range(256):
        nums.append(num)    
    cmd= '''gtacl -c "safecom info group *" '''
    out=executeCMD(cmd)
    listA=str(out).split("\\n")[1:-1]
    for i in listA:
        for index in range(256):
            if str(index) in i.split():
                groupID.append(index)
                break
def group_ID():
    newGroupID()
    for i in range(255):
        if i not in groupID:
            return i
            break  
