#!/usr/bin/env python
from subprocess import Popen, PIPE, STDOUT
from pytet import *
import os
import os.path
import shlex
from platform import python_version
import subprocess

""" 
###################################################################################

###################################################################################
"""

python_version_local=python_version().replace(".","")

def printStr(msg):
	if (str(python_version_local) >= "2713" and str(python_version_local) <= "2900"):
		print(str(msg))
	else:
		print ("{}".format(str(msg)))

def executeCMD(cmd,user1='SUPER.SUPER,password',option="cmd"):
    cmdExec=None
    cmdExec=None
    if "su" in option:
       cmd="su - "+str(os.environ[user1])+",password -c '"+str(cmd)+"'"
    if (str(python_version_local) >= "2713" and str(python_version_local) <= "2900"):

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

def writeToFile(str):
   fileName="output.file"
   with open(fileName,'w') as f:
       f.write(str)
   return fileName

def startup():
    printStr("Calling startup")

def cleanup():
    printStr ("Calling cleanup")
 
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


def test1():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --resolve HOST:PORT:ADDRESS  Force resolve of HOST:PORT to ADDRESS")
    tet_infoline ("Command     : /usr/bin/"+str("curl --resolve HOST:PORT:ADDRESS  http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --resolve "+str(current_ip)+":8080:"+str(current_ip)+"  http://"+str(current_ip)+"/dashboard/")+"> /tmp/output1.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output1.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output1.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test2():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --retry NUM   Retry request NUM times if transient problems occur")
    tet_infoline ("Command     : /usr/bin/"+str("curl --retry 10 http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --retry 10 http://"+str(current_ip)+"/dashboard/")+"> /tmp/output2.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output2.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output2.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test3():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --retry-delay SECONDS  Wait SECONDS between retries")
    tet_infoline ("Command     : /usr/bin/"+str("curl --retry-delay 10 http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --retry-delay 10 http://"+str(current_ip)+"/dashboard/")+"> /tmp/output3.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output3.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output3.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test4():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --retry-max-time SECONDS  Retry only within this period")
    tet_infoline ("Command     : /usr/bin/"+str("curl --retry-max-time 10 http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --retry-max-time 10 http://"+str(current_ip)+"/dashboard/")+"> /tmp/output4.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output4.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output4.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test5():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --sasl-ir  Enable initial response in SASL authentication")
    tet_infoline ("Command     : /usr/bin/"+str("curl --sasl-ir   http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --sasl-ir   http://"+str(current_ip)+"/dashboard/")+"> /tmp/output5.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output5.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output5.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test6():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : -S, --show-error Show error. With -s, make curl show errors when they occur")
    tet_infoline ("Command     : /usr/bin/"+str("curl -S http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl -S http://"+str(current_ip)+"/dashboard/")+"> /tmp/output6.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output6.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output6.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test7():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : -s, --silent   Silent mode (don't output anything)")
    tet_infoline ("Command     : /usr/bin/"+str("curl -s http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl -s http://"+str(current_ip)+"/dashboard/")+"> /tmp/output7.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output7.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output7.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test8():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --socks4 HOST[:PORT]  SOCKS4 proxy on given host + port")
    tet_infoline ("Command     : /usr/bin/"+str("curl --socks4 HOST[:PORT]   http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --socks4 "+str(current_ip)+":8080   http://"+str(current_ip)+"/dashboard/")+"> /tmp/output8.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output8.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output8.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test9():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --socks4a HOST[:PORT]  SOCKS4a proxy on given host + port")
    tet_infoline ("Command     : /usr/bin/"+str("curl --socks4a HOST[:PORT]  http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --socks4a "+str(current_ip)+":8080   http://"+str(current_ip)+"/dashboard/")+"> /tmp/output9.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output9.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["XAMPP is an easy to install Apache distribution containing MariaDB, PHP and Perl.","/tmp/output9.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test10():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --socks5 HOST[:PORT]  SOCKS5 proxy on given host + port")
    tet_infoline ("Command     : /usr/bin/"+str("curl --socks5 HOST[:PORT]   http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --socks5 "+str(current_ip)+":8080    http://"+str(current_ip)+"/dashboard/")+"> /tmp/output10.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output10.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output10.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test11():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --socks5-hostname HOST[:PORT]  SOCKS5 proxy, pass host name to proxy")
    tet_infoline ("Command     : /usr/bin/"+str("curl --socks5-hostname HOST[:PORT] http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --socks5-hostname "+str(current_ip)+":8080 http://"+str(current_ip)+"/dashboard/")+"> /tmp/output11.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output11.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output11.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test12():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --socks5-gssapi-service NAME  SOCKS5 proxy service name for GSS-API")
    tet_infoline ("Command     : /usr/bin/"+str("curl --socks5-gssapi-service NAME  http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --socks5-gssapi-service NAME  http://"+str(current_ip)+"/dashboard/")+"> /tmp/output12.file 2>&1",None)
    if process[-1] != 0:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output12.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["Welcome to XAMPP","Start the XAMPP Control Panel to check the server status.","/tmp/output12.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test13():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : --socks5-gssapi-nec  Compatibility with NEC SOCKS5 server")
    tet_infoline ("Command     : /usr/bin/"+str("curl --socks5-gssapi-nec   http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl --socks5-gssapi-nec   http://"+str(current_ip)+"/dashboard/")+"> /tmp/output13.file 2>&1",None)
    if process[-1] != 48:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output13.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["An unknown option","was passed in to libcurl","/tmp/output13.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)

def test14():
    current_ip=os.environ['CURRENT_IP_ADDRESS']
    tet_infoline ("Description : -Y, --speed-limit RATE  Stop transfers below RATE for 'speed-time' secs")
    tet_infoline ("Command     : /usr/bin/"+str("curl -Y 5 http://"+str(current_ip)+"/dashboard/")+"")
    process = executeCMD("/usr/bin/"+str("curl -Y http://"+str(current_ip)+"/dashboard/")+"> /tmp/output14.file 2>&1",None)
    if process[-1] != 2:
        tet_infoline("command failed with")
        tet_infoline_output("Execution Output ", process)
        tet_result(TET_FAIL)
        return
    process1 = executeCMD(("cat /tmp/output14.file")+"",None)
    process1[-1]=process[-1]
    tet_infoline_output("Curl Output ",process1)

    String=["expected a proper numerical parameter","for more information","/tmp/output14.file"]
    returnValue=CompareString(String)
    if returnValue[-1] != 0:
        tet_infoline("Verification failed ")
        tet_infoline(str(returnValue))
        tet_result(TET_FAIL)
        return

    tet_infoline("Verification successful ")
    tet_result(TET_PASS)


testlist = {1:test1,2:test2,3:test3,4:test4,5:test5,6:test6,7:test7,8:test8,9:test9,10:test10,11:test11,12:test12,13:test13,14:test14,}
pytet_init(testlist, startup, cleanup)
