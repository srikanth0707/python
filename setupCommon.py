import os
import subprocess
import re
from platform import python_version
import random
import operator
import shutil
import sys

user="SUPER.SUPER"
password="fsqa123"
python_version_local=python_version().replace(".","")

diskMatch=re.compile("\$\S+\D+\d+\D+\d+.\d+\D+[0-9]{2}\D+\d+\D+\d+.\d+")
def createpool(disk):
    cmd = '''gtacl -s -c "purge \$SYSTEM.ZXOSSMON.ETEPOL" '''
#    printStr(cmd)
    executeCMD(cmd)
    cmd = '''gtacl -s -c "purge \$SYSTEM.ZXOSSMON.DAETOET" '''
#    printStr(cmd)
    executeCMD(cmd)
    cmd = '''echo '''+str(disk).replace("$","\$")+''' > "/G/SYSTEM/ZXOSSMON/DAETOET" '''
#    printStr(cmd)
    executeCMD(cmd)
    cmd = '''gtacl -s -c "ctoedit \$SYSTEM.ZXOSSMON.DAETOET,\$SYSTEM.ZXOSSMON.'''+str(disk).replace("$","")+'''" '''
#    printStr(cmd)
    executeCMD(cmd)
    cmd = '''gtacl -s -c "purge \\\$SYSTEM.ZXOSSMON.DAETOET" '''
#    printStr(cmd)
    executeCMD(cmd)

def printStr(msg):
    print (str(msg))

def contentFile(msg,file):
    executeCMD("echo "+str(msg)+"> "+str(file)+" 2>&1")

def localFile(fileName,msg):
    file1=open(fileName,"a")
    file1.write(msg)
    file1.close()

def cleanfile(localList):
    for line in localList:
#        printStr(line)
        if(os.path.exists(line)):
            if (os.path.isdir(line)):
#               os.rmdir(line)
                shutil.rmtree(line)
            elif (not os.path.isdir(line)):
                os.unlink(line)

def cleanDir(folder_path):
    try:
        for file_object in os.listdir(folder_path):
            file_object_path = os.path.join(folder_path, file_object)
            if os.path.isfile(file_object_path):
                os.unlink(file_object_path)
                print("cleandir"+file_object_path)
            else:
                shutil.rmtree(file_object_path)
    except OSError as e:
        printStr(e)

def dumDir(path1):
    os.system("/bin/mkdir -p "+str(path1)+"/dir1")
    os.system("/bin/mkdir -p "+str(path1)+"/dir2")
    os.system("/bin/mkdir -p "+str(path1)+"/dir3")
    os.system("/bin/mkdir -p "+str(path1)+"/dir4")
    os.system("/bin/mkdir -p "+str(path1)+"/dir4/dir5")
    os.system("/bin/mkdir -p "+str(path1)+"/dir4/dir6")
    os.system("/bin/mkdir -p "+str(path1)+"/dir8")
    os.system("/bin/mkdir -p "+str(path1)+"/dir10")
    os.system("/bin/mkdir -p "+str(path1)+"/dir10/dir11")
    os.system("/bin/mkdir -p "+str(path1)+"/dir10/dir12")
    os.system("/bin/mkdir -p "+str(path1)+"/dir13")
    os.system("/bin/mkdir -p "+str(path1)+"/dir13/dir11")
    os.system("/bin/mkdir -p "+str(path1)+"/dir13/dir12")

def executeCMD(cmd):
    cmdExec=None
    printStr(cmd)
#    if (str(python_version_local) >= "2713" and str(python_version_local) <= "2900"):
    process=subprocess.Popen(cmd,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    out,rcode=process.communicate()
    process.wait()
    return ([out,rcode,process.returncode])

#    else:
#        cmdExec=subprocess.run(cmd,
#                           shell=True,
#                           stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE)

class getGroup():
    def __init__(self,group="norFS",groupid=None):
        self.group=group
        self.groupid=groupid
        self.optionMsg=None

    def groupName(self,group):
        cmd= '''gtacl -s -c "safecom info group ''' + str(group) +''' " '''
        out=executeCMD(cmd)
        getGroup.__init__(self,group,str(out[0]).split()[-4])
        return (str(out[0]).split()[-4])

    def newGroupID(self):
        cmd= '''gtacl -s -c "safecom info group * " '''
        out=executeCMD(cmd)
#        print(out)
        avaGroup=[]
        listA=str(out).split("\\n")[1:-1]
        for line in listA:
            if not "LAST" in line and line:
                if "x00" not in line:
                    avaGroup.append(line.split()[1])
        for x in xrange(255):
            rand = random.randint(1,255)
            if rand not in avaGroup:
                return rand
            else:
                printStr("Number - %d found in the array" % rand)
                break
        return (self)

    def createGroup(selfs,group,no):
        cmd= '''gtacl -s -c "safecom add group name ''' + str(group) +''' number ''' + str(no) +''' " '''
#        printStr(cmd)
        out=executeCMD(cmd)
        if "requested" in out[0]:
            return False
        else:
            return True

    def deleteGroup(self):
        cmd= '''gtacl -s -c "safecom delete group name ''' + str(self.group) +''' " '''
#        printStr(cmd)
        out=executeCMD(cmd)
        if "has members" in out[0]:
            return False
        else:
            return True


class getUser():
    def __init__(self,user="norFS",userid=None,group=None,groupid=None):
        self.user=user
        self.userid=userid
        self.group=group
        self.groupid=groupid
        self.optionMsg=None

    def createUser(self,group,user,passwd="password"):
        userid=random.randint(1,255)
        grp1=getGroup()
        logid=grp1.groupName(group)
        getUser.__init__(self,user,userid,group,logid)
#        printStr(grp1.groupName(group))
        cmd= '''gtacl -s -c "safecom add user ''' + str(group) +'''.'''+str(user)+''','''\
             +str(logid)+''','''+str(userid)+''',password '''+str(passwd)+''',GUARDIAN SECURITY  \\"NUNU\\""'''
#        printStr(cmd)
        out=executeCMD(cmd)
        if "SOA" in user:
            cmd= '''gtacl -s -c "safecom alter security-group security-oss-admin, access ''' + str(group) +'''.'''+str(user)+''' * "'''
#            printStr(cmd)
            out=executeCMD(cmd)
#            printStr(out)
        if "SPA" in user:
            cmd= '''gtacl -s -c "safecom alter security-group security-prv-administrator, access ''' + str(group) +'''.'''+str(user)+''' * "'''
            out=executeCMD(cmd)
#            printStr(cmd)

        if "user ID" in out[0]:
            lgrp=getUser()
            lgrp.createUser(group,user,passwd)
        else:
           return True

    def deleteUser(self):
       cmd= '''gtacl -s -c "safecom delete user ''' + str(self.group) +'''.'''+str(self.user)+''' " '''
       out=executeCMD(cmd)

    def infoUser(self,group=None,user=None):
#        printStr(user)
#        printStr(group)
        if (user and group):
            cmd= '''gtacl -s -c "safecom info user ''' + str(group) +'''.'''+str(user)+''' " '''
        else:
            cmd= '''gtacl -s -c "safecom info user ''' + str(self.group) +'''.'''+str(self.user)+''' " '''
#        printStr(cmd)
        out=executeCMD(cmd)
        listA=str(out[0]).split("\n")
        for line in listA:
            if not "LAST" in line and line:
                line1=str(line).split()
                line2=str(line1[1]).split(",")
                if (user and group):
                    getUser.__init__(self,user,line2[1],group,line2[0])
                else:
                    getUser.__init__(self,self.user,line2[1],self.group,line2[0])

    def alterPassword(self,user,passwd="password"):
        cmd = '''gtacl -s -c "safecom alter user ''' + str(user) + ''',password  ''' +str(passwd)+''' " '''
#        printStr(cmd)
        out=executeCMD(cmd)

    def getUserName(self):
        return (self.user)

    def getUserID(self):
        return (self.userid)

    def getUserGroup(self):
        return (self.group)

    def getUserGroupID(self):
        return (self.groupid)

class fileSet:
    def __init__(self,disk=None,server=None,fileset=None,mnt=None):
        self.disk=disk
        self.server=server
        self.fileset=fileset
        self.mnt=mnt

    def newDisk(self):
        cmd = '''gtacl -s -c "fup vols " '''
        out=executeCMD(cmd)
#        printStr(out)
        listA=str(out).split("\\n")[1:-1]
        tdisk={}
        for line in listA:
            if diskMatch.match(line):
#                print(str(line).split())
                tdisk[str(line).split()[3]]=str(line).split()[0]

        sorted_d=sorted(tdisk.items(),key=operator.itemgetter(0),reverse=True)
        sorted_d1=sorted_d[0]
        fileSet.__init__(self,sorted_d1[1],self.server,self.fileset,self.mnt)
        createpool(sorted_d1[1])
        return(sorted_d1)

    def createFileset(self,option="None"):
        if (not os.path.exists(self.mnt)):
            print(self.mnt)
            os.mkdir(self.mnt)
        if (str(option).__contains__("None") or str(option).__contains__("CHG")):
            cmd1 = '''gtacl -s -c "scf assume \$zpmon; allow all; ADD SERVER $ZPMON.#'''+str(self.server)+''', TYPE NAME, CPU 1, BACKUPCPU 2" '''
            cmd2 = '''gtacl -s -c "scf assume \$ZPMON; ADD FILESET '''+str(self.fileset)+''', CATALOG '''+str(self.disk).replace("$","\$")+''', POOL '''+str(self.disk).replace("$","")+''', NAMESERVER #'''+str(self.server)+''', MNTPOINT \\"'''+str(self.mnt)+'''\\", AUDITENABLED ON"'''
        if str(option).__contains__("RES"):
            user="SUPER.SPA"
            password="password"
            cmd1 = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; allow all; ADD SERVER $ZPMON.#" + str(self.server) + ", TYPE NAME, CPU 1, BACKUPCPU 2\"\' "
            cmd2 = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; allow all; ADD FILESET " + str(self.fileset) + ", CATALOG "+str(self.disk).replace("$","\$")+",POOL "+str(self.disk).replace("$","")+", NAMESERVER #"+str(self.server)+", MNTPOINT \\\""+str(self.mnt)+"\\\", AUDITENABLED ON,RESTRICTEDACCESS ENABLED\"\' "
        if str(option).__contains__("SEE"):
            user="SUPER.SOA"
            password="password"
            cmd1 = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; allow all; ADD SERVER $ZPMON.#" + str(self.server) + ", TYPE NAME, CPU 1, BACKUPCPU 2,SEEPENABLED ON,SEEPRESPONSETIMEOUT 5,SEEPPRI 199 ,SEEPPROCESSNAME \$"+str(self.disk).replace("$","")+" ,SEEPCPU ANY ,SEEPPROGFILENAME \$SAS4.SEEPSVR.SERY ,SEEPPARAMTEXT CHECK \"\' "
            cmd2 = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; allow all; ADD FILESET " + str(self.fileset) + ", CATALOG "+str(self.disk).replace("$","\$")+",POOL "+str(self.disk).replace("$","")+", NAMESERVER #"+str(self.server)+", MNTPOINT \\\""+str(self.mnt)+"\\\", AUDITENABLED ON,SEEPPROTECTED ON\"\' "
        if str(option).__contains__("CHG"):
            cmd1 = '''gtacl -s -c "scf assume \$zpmon; allow all; ADD SERVER $ZPMON.#'''+str(self.server)+''', TYPE NAME, CPU 1, BACKUPCPU 2" '''
            cmd2 = '''gtacl -s -c "scf assume \$ZPMON; ADD FILESET '''+str(self.fileset)+''', CATALOG '''+str(self.disk).replace("$","\$")+''', POOL '''+str(self.disk).replace("$","")+''', NAMESERVER #'''+str(self.server)+''', MNTPOINT \\"'''+str(self.mnt)+'''\\", AUDITENABLED ON"'''
#        printStr(cmd1)
        executeCMD(cmd1)
#        printStr(cmd2)
        executeCMD(cmd2)

    def deleteFileset(self):
        cmd = '''gtacl -s -c "scf assume \$ZPMON; delete fileset '''+str(self.fileset)+'''''''"'''
#        printStr(cmd)
        out=executeCMD(cmd)

    def deleteServer(self):
        cmd = '''gtacl -c "scf assume \$ZPMON; delete server $ZPMON.#'''+str(self.server)+'''"'''
#        printStr(cmd)
        out=executeCMD(cmd)

    def infofileset(self):
        cmd = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; info fileset " + str(self.fileset) + "\"\' "
#        printStr(cmd)
        out=executeCMD(cmd)
#        printStr(out[0])

    def infoServer(self):
        cmd = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; info server #" + str(self.server) + "\"\' "
#        printStr(cmd)
        out=executeCMD(cmd)
#        printStr(out[0])

    def infofilesetD(self):
        cmd = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; info fileset " + str(self.fileset) + ",detail\"\' "
#        printStr(cmd)
        out=executeCMD(cmd)
#        printStr(out[0])

    def infoServerD(self):
        cmd = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; info server #" + str(self.server) + ",detail \"\' "
#        printStr(cmd)
        out=executeCMD(cmd)
#        printStr(out[0])

    def startFileset(self):
        cmd = '''gtacl -s -c "scf assume \$ZPMON; start fileset '''+str(self.fileset)+'''''''"'''
#        printStr(cmd)
        out=executeCMD(cmd)

    def stopFileset(self):
        cmd = '''gtacl -s -c "scf assume \$ZPMON; stop fileset '''+str(self.fileset)+'''''''"'''
#        printStr(cmd)
        out=executeCMD(cmd)

    def getDisk(self):
        return (self.disk)
    def getServer(self):
        return (self.server)
    def getFileset(self):
        return (self.fileset)
    def getMount(self):
        return (self.mnt)

    def filesetDowngrade(self):
        cmd = '''gtacl -s -c "scf assume \$ZPMON; DIAGNOSE  fileset '''+str(self.fileset)+''''''',downgrade"'''
#        printStr(cmd)
        out=executeCMD(cmd)

    def filesetUpgrade(self):
        cmd = '''gtacl -s -c "scf assume \$ZPMON; DIAGNOSE fileset '''+str(self.fileset)+''''''',upgrade"'''
#        printStr(cmd)
        out=executeCMD(cmd)

    def alterFileset(self,option):
        cmd = '''gtacl -s -c "scf assume \$ZPMON; stop fileset '''+str(self.fileset)+'''''''"'''
        out=executeCMD(cmd)
        if ("RES" in option):
            user="SUPER.SPA"
            password="password"
            cmd2 = "su - " + str(user) + "," + str(password) + " -c \'gtacl -c \"scf assume \$ZPMON; allow all; ALTER FILESET " + str(self.fileset) + ", RESTRICTEDACCESS ENABLED\"\' "
            executeCMD(cmd2)
        cmd = '''gtacl -s -c "scf assume \$ZPMON; start fileset '''+str(self.fileset)+'''''''"'''
        out=executeCMD(cmd)

class apollo():
    def __init__(self):
        self.dirname=None
        self.hash=[]

    def createDirectory(self,name,user,hash):
        self.dirname=name
        self.user=user
        self.hash=hash
        self.option="diff"
        if ("Normal" in hash):
            self.setNormal(self)
        if ("Optional" in hash):
            self.setOptionalACL(self,"dir1")
        if ("OwnedACL" in hash):
            self.setOwnedACL(self,"dir2")
        if ("Attribute" in hash):
            self.setAttributeLock(self,"dir3")
        if ("Inheritance" in hash):
            self.setInheritace(self,"dir4,dir5,dir6")
        if ("OptOwn" in hash):
            self.setOptionalACL(self,"dir8","OptOwn")
            self.setOwnedACL(self,"dir8","OptOwn")
        if ("AttInh" in hash):
            self.setAttributeLock(self,"dir10/dir11,dir10/dir12",option="AttInh")
            self.setInheritace(self,"dir10,dir11,dir12",option="AttInh")
        if ("Mix" in hash):
#            printStr("/bin/mkdir -p "+self.dirname+"/dir13")
            executeCMD("/bin/mkdir -p "+self.dirname+"/dir13")
            self.setNormal(self,"/dir13",option="Mix")
            self.setOptionalACL(self,"/dir13",option="Mix")
            self.setOwnedACL(self,"/dir13",option="Mix")
            self.setAttributeLock(self,"dir13/dir11,dir13/dir12",option="Mix")
            self.setInheritace(self,"dir13,dir11,dir12",option="Mix")
##            self.setAttributeLock(self,"dir13/dir11,dir13/dir12",option="Mix")
##            self.setInheritace(self,"dir13,dir11,dir12",option="Mix")

    @staticmethod
    def setNormal(self,dirName=None,option=None):
        if(dirName != None):
            dirName=self.dirname+""+dirName
        else:
            dirName= self.dirname
        executeCMD("/bin/chmod 777 "+str(dirName))
        count=1
        fileName=None
        userList=None
        if (("Normal" in hash)):
            userList=str(self.hash["Normal"]).split(",")
            fileName="Normal"
            cleanfile([dirName+"/"+str(fileName)+"file01",dirName+"/"+str(fileName)+"file02"])
        if (("Mix" in hash) and (option == "Mix")):
            userList=str(self.hash["Mix"]).split(",")
            fileName="NormalMix"
#            cleanfile([dirName+"/"+str(fileName)+"file01",dirName+"/"+str(fileName)+"file02"])
        for line in userList:
            executeCMD("su - "+str(line)+",password -c \"touch "+str(dirName)+"/"+str(fileName)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Normalfile0"+str(count)+" file content' > "+str(dirName)+"/"+str(fileName)+"file0"+str(count)+"")
            count = count + 1

    @staticmethod
    def setOptionalACL(self,dirName,option=None):
        if (("Optional" in hash) and (option == None)):
            userList=str(self.hash["Optional"]).split(",")
            LocalFile="Optional"
            cleanfile([self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file01",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file02",self.dirname+"/"+str(dirName)+""])
            localDir=self.dirname+"/"+str(dirName)+""
            os.makedirs(localDir)
        elif (("Mix" in hash) and (option == "Mix")):
            userList=str(self.hash["Mix"]).split(",")
            LocalFile="OptionalMix"
#            cleanfile([self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file01",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file02",self.dirname+"/"+str(dirName)+""])
            localDir=self.dirname+"/"+str(dirName)+""
#            os.makedirs(localDir)
#            executeCMD("/bin/chmod 777 "+str(localDir))
        elif (("OptOwn" in hash) and (option == "OptOwn")):
            userList=str(self.hash["OptOwn"]).split(",")
            LocalFile="OptOwn"
            localDir=self.dirname+"/"+str(dirName)+""
            try:
                os.makedirs(localDir)
            except OSError as e:
                printStr(e)
            executeCMD("/bin/chmod 777 "+str(localDir))
        count=1
        for line in userList:
            executeCMD("su - "+str(line)+",password -c \"touch "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Optionalfile0"+str(count)+" file content' > "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"")
            count = count + 1
        executeCMD("setacl -m u:SUPER.SUPER:r--,g:SUPER:rw- /"+str(localDir)+"/"+str(LocalFile)+"file01")
        executeCMD("setacl -m u:PCTS.SOA:r--,g:PCTS:rw- /"+str(localDir)+"/"+str(LocalFile)+"file02")
        if (("Optional" in hash)):
            executeCMD("setacl -m u:SUPER.SOA:r--,g:PCTS:rw-,d:u::rwx,d:g::rwx,d:c:rwx,d:o:rwx "+str(localDir))

    @staticmethod
    def setOwnedACL(self,dirName,option=None):
        localDir=self.dirname+"/"+str(dirName)+""
        if (("OwnedACL" in hash) and (option == None)):
            userList=str(self.hash["OwnedACL"]).split(",")
            LocalFile="Owned"
            cleanfile([self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file01",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file02",self.dirname+"/"+str(dirName)+""])
            os.makedirs(localDir)
            executeCMD("/bin/chmod 777 "+str(localDir))
        elif (("Mix" in hash) and (option=="Mix")):
            userList=str(self.hash["Mix"]).split(",")
            LocalFile="OwnedMix"
            executeCMD("/bin/chmod 777 "+str(localDir))
        elif (("OptOwn" in hash) and option== "OptOwn"):
            userList=str(self.hash["OptOwn"]).split(",")
            LocalFile="OptOwn"
 #           os.makedirs(localDir)
            executeCMD("/bin/chmod 777 "+str(localDir))
        count=1
        for line in userList:
            executeCMD("su - "+str(line)+",password -c \"touch "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Ownedfile0"+str(count)+" file content' > "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"")
            count = count + 1
        executeCMD("setacl -o O:SUPER:: /"+str(localDir)+"/"+str(LocalFile)+"file01")
        executeCMD("setacl -o O:PCTS:: /"+str(localDir)+"/"+str(LocalFile)+"file02")

    @staticmethod
    def setAttributeLock(self,dirName,option=None):
        localDir=localDir1=localDir2=None
        if (("Attribute" in hash) and (option == None)):
            LocalFile="Attribute"
            userList=str(self.hash["Attribute"]).split(",")
            localDir=self.dirname+"/"+str(dirName)+""
            cleanfile([self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file01",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file02",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file03",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file04",self.dirname+"/"+str(dirName)+""])
            os.makedirs(localDir)
            executeCMD("/bin/chmod 777 "+str(localDir))
        elif (("Mix" in hash) and (option == "Mix")):
            LocalFile="AttributeMix"
            userList=str(self.hash["Mix"]).split(",")
#            localDir=localDir1=localDir2=self.dirname+"/"+str(dirName)+""
            dirNames=str(dirName).split(",")
#            printStr(dirName)
            localDir1=self.dirname+"/"+str(dirNames[0])+""
            localDir2=self.dirname+"/"+str(dirNames[1])+""
            try:
                os.makedirs(localDir1)
            except OSError as e:
                printStr(e)
            try:
                os.makedirs(localDir2)
            except OSError as e:
                printStr(e)
#            cleanfile([self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file01",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file02",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file03",self.dirname+"/"+str(dirName)+"/"+str(LocalFile)+"file04",self.dirname+"/"+str(dirName)+""])
#            os.makedirs(localDir)
            executeCMD("/bin/chmod 777 "+str(localDir))
        elif (("AttInh" in hash) and (option == "AttInh")):
            LocalFile="AttInh"
            userList=str(self.hash["AttInh"]).split(",")
            dirNames=str(dirName).split(",")
            localDir1=self.dirname+"/"+str(dirNames[0])+""
            localDir2=self.dirname+"/"+str(dirNames[1])+""
            try:
                os.makedirs(localDir1)
            except OSError as e:
                printStr(e)
            try:
                os.makedirs(localDir2)
            except OSError as e:
                printStr(e)

            executeCMD("/bin/chmod 777 "+str(localDir1))
            executeCMD("/bin/chmod 777 "+str(localDir2))
        count=1
        for line in userList:
            if ((("AttInh" in hash) and (option == "AttInh")) or (("Mix" in hash) and (option == "Mix"))):
                localDir=localDir1
            executeCMD("su - "+str(line)+",password -c \"touch "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Attributefile0"+str(count)+" file content' > "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"")
            count = count + 1
            if ((("AttInh" in hash) and (option == "AttInh")) or (("Mix" in hash) and (option == "Mix"))):
                localDir=localDir2
            executeCMD("su - "+str(line)+",password -c \"touch "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Attributefile0"+str(count)+" file content' > "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"")
            count = count + 1

        if ((("AttInh" in hash) and (option == "AttInh")) or (("Mix" in hash) and (option == "Mix"))):
            localDir=localDir1
        executeCMD("setacl -o O:SUPER::on "+str(localDir)+"/"+str(LocalFile)+"file01")
        executeCMD("setacl -o O:PCTS::on "+str(localDir)+"/"+str(LocalFile)+"file03")
        if ((("AttInh" in hash) and (option == "AttInh")) or (("Mix" in hash) and (option == "Mix"))):
            localDir=localDir2
        executeCMD("setacl -o O:SUPER::off "+str(localDir)+"/"+str(LocalFile)+"file02")
        executeCMD("setacl -o O:PCTS::off "+str(localDir)+"/"+str(LocalFile)+"file04")

    @staticmethod
    def setInheritace(self,dirNames,option=None):
        if (("Inheritance" in hash) and (option == None)):
            dirName=str(dirNames).split(",")
            localDir0=self.dirname+"/"+str(dirName[0])+""
            localDir1 = "/"+str(dirName[1])
            localDir2 = "/"+str(dirName[2])
            LocalFile="Inheritance"
            cleanfile([self.dirname+"/"+str(localDir0)+"/"+str(localDir2)+"/"+str(LocalFile)+"file05",
                           self.dirname+"/"+str(localDir0)+"/"+str(localDir2)+"/"+str(LocalFile)+"file06",
                           self.dirname+"/"+str(localDir1)+""])
            cleanfile([self.dirname+"/"+str(localDir0)+"/"+str(localDir1)+"/"+str(LocalFile)+"file03",
                           self.dirname+"/"+str(localDir0)+"/"+str(localDir1)+"/"+str(LocalFile)+"file04",
                           self.dirname+"/"+str(localDir1)+""])
            cleanfile([self.dirname+"/"+str(localDir0)+"/"+str(LocalFile)+"file01",
                           self.dirname+"/"+str(localDir0)+"/"+str(LocalFile)+"file02",
                           self.dirname+"/"+str(localDir1)+""])
            try:
                os.makedirs(localDir0 + localDir1)
                os.makedirs(localDir0 + localDir2)
            except OSError as e:
                printStr(e)
            executeCMD("/bin/chmod 777 "+str(localDir0))
            userList=str(self.hash["Inheritance"]).split(",")
        elif (("Mix" in hash) and (option == "Mix")):
            dirName=str(dirNames).split(",")
            localDir0=self.dirname+"/"+str(dirName[0])+""
            localDir1 = "/"+str(dirName[1])
            localDir2 = "/"+str(dirName[2])
            LocalFile="InheritanceMix"
            userList=str(self.hash["Mix"]).split(",")
        elif (("AttInh" in hash) and (option == "AttInh")):
            dirName=str(dirNames).split(",")
            localDir0=self.dirname+"/"+str(dirName[0])+""
            localDir1 = "/"+str(dirName[1])
            localDir2 = "/"+str(dirName[2])
            LocalFile="AttInh"
            userList=str(self.hash["AttInh"]).split(",")
        localDir = localDir0
        count=1
        for line in userList:
            executeCMD("su - "+str(line)+",password -c \"touch "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Inheritancefile0"+str(count)+" file content' > "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"")
            count = count + 1
        localDir = localDir0 + localDir1
        if ((("AttInh" not in hash) and (option == None)) or ("Mix" not in hash) and (option == "Mix")):
            try:
                os.makedirs(localDir)
            except OSError as e:
                printStr(e)
        for line in userList:
            executeCMD("su - "+str(line)+",password -c \"touch "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Inheritancefile0"+str(count)+" file content' > "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"")
            count = count + 1
        executeCMD("setacl -m d:u::rwx,d:g::rwx,d:c:rwx,d:o:rwx -o O:SUPER:on: "+localDir+"")
        localDir = localDir0 + localDir2
        if ((("AttInh" not in hash) and (option == None)) or ("Mix" not in hash) and (option == "Mix")):
            try:
                os.makedirs(localDir)
            except OSError as e:
                printStr(e)
        for line in userList:
            executeCMD("su - "+str(line)+",password -c \"touch "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"\"")
            executeCMD("su - "+str(line)+",password -c \"echo 'Inheritancefile0"+str(count)+" file content' > "+str(localDir)+"/"+str(LocalFile)+"file0"+str(count)+"")
            count = count + 1
        executeCMD("setacl -m d:u::rwx,d:g::rwx,d:c:rwx,d:o:rwx -o O:SUPER:on: "+localDir+"")
"""
class getGroup()
"""

if __name__ == "__main__":
    optionList=None
    src=None
    des=None
    if "All" in str(sys.argv[1:]):
        optionList="All"
        src=sys.argv[2]
        des=sys.argv[3]
        if (os.path.exists("source")):
            os.unlink("source")
    if "clean" in str(sys.argv[1:]):
        optionList=sys.argv[1]+"::"+sys.argv[2]

    if "sync" in str(sys.argv[1:]):
        optionList=sys.argv[1]+"::"+sys.argv[2]+"::"+sys.argv[3]

    if (optionList == "All"):
        #working####SUPER.SUPER - Super user not part of SOA and AOG
        #working####SUPER.SOA 	- part of SOA group
        #working####FSQA.SOA    - A user part of SOA group
        #working####ACL.USER1   - A File owner not part of SOA and AOG
        #working####ACL.SOA   	- A File owner part of SOA
        #working####PCTS.AOG    - A user part of owning ACL group
        #working####PCTS.SOA    - A user part of owning ACL and SOA group
        #working####PCTS.USER1  - A file owner part of AOG group
        #working####PCTS.USER2  - A file owner part of SOA and AOG group
        #working####SUPER.USER1 - part of AOG group
        #working####SUPER.SOA - part of AOG and SOA group
        listUser=["SUPER.SUPER","SUPER.SOA","FSQA.SOA","ACL.USER1","ACL.SOA","PCTS.AOG",
              "PCTS.SOA","PCTS.USER1","PCTS.USER2","SUPER.USER1","SUPER.SOA"]
        grp=getGroup()
        usr=getUser()
        count=1
        for usr1 in listUser:
            print (usr1)
            suser=str(usr1).rstrip('\x00').split(".")
            if("SUPER".__contains__(suser[0])):
                grp.createGroup(suser[0],grp.newGroupID())
                usr.createUser(suser[0],suser[1])
            if("SUPER".__contains__(suser[1])):
                usr.alterPassword(suser[0],suser[1])
            usr.infoUser()
            localFile("source",'export %s=%s\n' % ("USER"+str(count)+"_NAME_"+"_".join(suser)+"", usr.getUserGroup()+'.'+usr.getUserName()))
            localFile("source",'export %s=%s\n' % ("USER"+str(count)+"_ID_"+"_".join(suser)+"", str(usr.getUserGroupID())+'.'+str(usr.getUserID())))
            count = count + 1
        #only source directory has the setup (/sor201)
        #Normal				Normal
        #/"+str(src)+"s1202			/adir01  	#empty version 4, on different fileset
        #Restricted 		Restricted
        #/"+str(src)+"s1203			/adir02		#empty version 4, on different fileset
        hash={"Normal":"SUPER.SUPER,PCTS.PCTSOPER",
          "Optional":"SUPER.SUPER,PCTS.PCTSOPER",
          "OwnedACL":"SUPER.SUPER,PCTS.PCTSOPER",
          "Attribute":"SUPER.SUPER,PCTS.PCTSOPER",
          "Inheritance":"SUPER.SUPER,PCTS.PCTSOPER",
          "OptOwn":"SUPER.SUPER,PCTS.PCTSOPER",
          "AttInh":"SUPER.SUPER,PCTS.PCTSOPER",
          "Mix":"SUPER.SUPER,PCTS.PCTSOPER"}

        emtpyDirectoryOtherFileset=["/"+str(des)+"d1204","/"+str(des)+"d1205"]
        count = 4
        cleanfile(emtpyDirectoryOtherFileset)
        dir1=apollo()
        for dirs in emtpyDirectoryOtherFileset:
            printStr(dirs)
            executeCMD("/bin/mkdir -p "+str(dirs))
            dumDir(dirs)
            localFile("source",'export %s=%s\n' % ("FILESET_"+str(dirs).upper().replace("/","")+"_"+str(count)+"", str(str(dirs))))
            count = count + 1

        createNoramlFileset=["/"+str(src)+"s1202","/"+str(src)+"s1203","/"+str(des)+"d1206","/"+str(des)+"d1207","/"+str(des)+"d1208","/"+str(des)+"d1209","/"+str(des)+"d1210","/"+str(des)+"d1211","/"+str(des)+"d1212",
                     "/"+str(des)+"d1213","/"+str(des)+"d1214","/"+str(des)+"d1215","/"+str(des)+"d1216","/"+str(des)+"d1217","/"+str(src)+"s1218","/"+str(src)+"s1219"]
        #remove des206, des207 it is empty directory
        createNoramlFileset=["/"+str(src)+"s1202","/"+str(src)+"s1203","/"+str(des)+"d1208","/"+str(des)+"d1209","/"+str(des)+"d1210","/"+str(des)+"d1211","/"+str(des)+"d1212",
                     "/"+str(des)+"d1213","/"+str(des)+"d1214","/"+str(des)+"d1215","/"+str(src)+"s1218","/"+str(src)+"s1219"]
        count=2
        for name in createNoramlFileset:
            fs1=fileSet(None,str(src)+"0"+str(count),str(src)+"f20"+str(count),name)
            fs1.stopFileset()
            fs1.deleteFileset()
            fs1.deleteServer()
            count = count + 1

        dir1=apollo()
        count=2
        for name in createNoramlFileset:
            print(name)
            fs1=fileSet(None,str(src)+"0"+str(count),str(src)+"f20"+str(count),name)
            fs1.newDisk()
            if name in ['/'+str(src)+'s1203',"/"+str(des)+"d1209","/"+str(des)+"d1211","/"+str(des)+"d1213","/"+str(src)+"s1215"]:
                print ("1--"+str(name))
                fs1.createFileset("RES")
            else:
                print ("2--"+str(name))
                fs1.createFileset()
            fs1.startFileset()
            #version 4, find ch* "/"+str(src)+"s1202","/"+str(src)+"s1203"
            if name in ["/"+str(src)+"s1202","/"+str(src)+"s1203","/"+str(des)+"d1210","/"+str(des)+"d1211","/"+str(des)+"d1212","/"+str(des)+"d1213","/"+str(src)+"s1218","/"+str(src)+"s1219"]:
                dir1.createDirectory(fs1.getMount(),None,hash)
            #versuion 3, find ch* "/"+str(src)+"s1204"
            if name in ["/"+str(des)+"d1210","/"+str(des)+"d1211","/"+str(des)+"d1212","/"+str(des)+"d1213""/"+str(src)+"s1218"]:
                fs1.filesetDowngrade()
            #version 2 fileset, find ch* "/"+str(src)+"s1205"
            if name in ["/"+str(des)+"d1214","/"+str(des)+"d1215","/"+str(src)+"s1219"]:
                fs1.filesetDowngrade()
                fs1.filesetDowngrade()
            fs1.infofileset()
            fs1.infoServer()
            if (name.__contains__("202") or name.__contains__("203") or name.__contains__("sou")):
                localFile("source",'export %s=%s\n' % ("FILESET_"+str(name).upper().replace("/","")+"_"+str(count)+"_LOCAL", str(str(name)+"/Local")))
                os.system("/bin/mkdir -p "+str(str(name)+"/Local"))
                dumDir(""+str(str(name)+"/Local"))

            localFile("source",'export %s=%s\n' % ("FILESET_"+str(name).upper().replace("/","")+"_"+str(count)+"", str(str(name))))
            count = count + 1

        fs1=fileSet(None,None,None,None)
        fs1.newDisk()
        printStr(fs1.getDisk())
        localFile("source",'export %s=%s\n' % ("LOCAL_VOLUME","/G/"+str(fs1.getDisk()).replace("$","")+"/APOLLO/"))
        localFile("source",'export %s=%s\n' % ("REMOTE_MACHINE","/E/BRANDY/tmp/"))
    elif (optionList != "All"):
        if (str(optionList).__contains__("clean")):
            emtpyDirectoryOtherFileset=["/"+str(des)+"d1204","/"+str(des)+"d1205","/"+str(des)+"d1206","/"+str(des)+"d1207","/de101","/"+str(src)+"s1202/Local","/"+str(src)+"s1203/Local"]
            if (str(optionList).split("::")[1] in emtpyDirectoryOtherFileset):
                cleanDir(str(optionList).split("::")[1])
                dumDir(str(optionList).split("::")[1])
            if "/"+str(src)+"s1202/Local" in optionList:
                os.system("rm -rf /"+str(src)+"s1202/Local/*")
                dumDir("/"+str(src)+"s1202/Local")
            if "/"+str(src)+"s1203/Local" in optionList:
                os.system("rm -rf /"+str(src)+"s1203/Local/*")
                dumDir("/"+str(src)+"s1203/Local")

        if (str(optionList).__contains__("sync")):
            printStr("1--------------")
            dir1=apollo()
            printStr(str(optionList).split("::")[1])
            if str(optionList).split("::")[1] in ["/"+str(src)+"s1202","/"+str(src)+"s1203","/"+str(des)+"d1208","/"+str(des)+"d1209","/"+str(des)+"d1212","/"+str(des)+"d1213","/"+str(des)+"d1216","/"+str(des)+"d1217","/"+str(src)+"s1218","/"+str(src)+"s1219","/de101"]:
                printStr("Version4")
                if ((optionList).split("::")[2] == "Normal"):
                    printStr("2--------------")
                    hash={"Normal":"SUPER.SUPER,PCTS.PCTSOPER"}
                    cleanDir(str(optionList).split("::")[1]+"/Normalfile01")
                    cleanDir(str(optionList).split("::")[1]+"/Normalfile02")
                if ((optionList).split("::")[2] == "Optional"):
                    printStr("3--------------")
                    hash={"Optional":"SUPER.SUPER,PCTS.PCTSOPER"}
                    cleanDir(str(optionList).split("::")[1]+"/dir1")
                if ((optionList).split("::")[2] == "OwnedACL"):
                    printStr("4--------------")
                    hash={"OwnedACL":"SUPER.SUPER,PCTS.PCTSOPER"}
                    cleanDir(str(optionList).split("::")[1]+"/dir3")
                if ((optionList).split("::")[2] == "Attribute"):
                    printStr("5--------------")
                    cleanDir(str(optionList).split("::")[1]+"/dir4")
                    hash={"Attribute":"SUPER.SUPER,PCTS.PCTSOPER"}
                if ((optionList).split("::")[2] == "Inheritance"):
                    printStr("6--------------")
                    hash={"Inheritance":"SUPER.SUPER,PCTS.PCTSOPER"}
                    cleanDir(str(optionList).split("::")[1]+"/dir4")
#                    cleanDir(str(optionList).split("::")[1]+"/dir4")
                if ((optionList).split("::")[2] == "OptOwn"):
                    printStr("7--------------")
                    cleanDir(str(optionList).split("::")[1]+"/dir8")
                    hash={"OptOwn":"SUPER.SUPER,PCTS.PCTSOPER"}
                if ((optionList).split("::")[2] == "AttInh"):
                    printStr("8--------------")
                    hash={"AttInh":"SUPER.SUPER,PCTS.PCTSOPER"}
                    cleanDir(str(optionList).split("::")[1]+"/dir10")
                if ((optionList).split("::")[2] == "Mix"):
                    printStr("9--------------")
                    hash={"Mix":"SUPER.SUPER,PCTS.PCTSOPER"}
                    cleanDir(str(optionList).split("::")[1]+"/dir13")
#                print(str(optionList).split("::")[1])
#                printStr(hash["OwnedACL"])
                dir1.createDirectory(str(optionList).split("::")[1],None,hash)
                dumDir(str(optionList).split("::")[1])
            #versuion 3, find ch* "/"+str(src)+"s1204"
            if str(optionList).split("::")[1] in ["/"+str(des)+"d1210","/"+str(des)+"d1211","/"+str(des)+"d1212","/"+str(des)+"d1213""/"+str(src)+"s1218"]:
                printStr("Version3")
                dumDir(str(optionList).split("::")[1])
            #version 2 fileset, find ch* "/"+str(src)+"s1205"
            if str(optionList).split("::")[1] in ["/"+str(des)+"d1214","/"+str(des)+"d1215","/"+str(des)+"d1216","/"+str(des)+"d1217","/"+str(src)+"s1219"]:
                printStr("Version2")
                dumDir(str(optionList).split("::")[1])
            if "/"+str(src)+"s1202/Local" in optionList:
                os.system("rm -rf /"+str(src)+"s1202/Local/*")
                dumDir("/"+str(src)+"s1202/Local")
            if "/"+str(src)+"s1203/Local" in optionList:
                os.system("rm -rf /"+str(src)+"s1203/Local/*")
                dumDir("/"+str(src)+"s1203/Local/")
        dir1=apollo()
        printStr(optionList)
#    dir1.createDirectory(fs1.getMount(),None,hash)
