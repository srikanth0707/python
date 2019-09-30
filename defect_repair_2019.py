#!/usr/bin/env python
from subprocess import Popen , PIPE , STDOUT
from pytet import *
import shlex
import os
import sys
sys.path.append(os.environ['TET_ROOT'] + "/lib/python")
from common import * 

#################################################################################################
# Defect Repair Automation script for bash
# Author: Arnob Dey, Srikanth Peddini
#
#Added the new test cases to validate these CRs:
# 1) Case : 10-181203-2882, Solution: 10-190107-9027, CR :10-190304-7318
#	 Title : EN: HPE bash 4.4.19 missing process substitution feature
#	 test1 - test33
#
# 2) Case : 10-190412-4890, Solution: 10-190412-9866, CR : 10-190625-8334
#    Title : Provide /bin/bash and /usr/bin/bash symlinks to /usr/coreutils/bin/bash
#    test34 - test35
#
# 3) Case : 10-160309-1625, Solution: 10-160309-9274, CR : 10-171103-2290
#    Title :/usr/coreutils/bin/find throws error when the directory path length is more th
#    test36
#Modification History:
# 1. [Arnob Dey]: added new TCs w.r.t Bash Process Substitution feature
# 2. [Arnob Dey]: added new TCs w.r.t /bin/bash & /usr/bin/bash symlinks
#################################################################################################
def startup():
    print "Calling startup"

def cleanup():
    print "Calling cleanup"

def tet_infoline_output(output, return_code):
	tet_infoline("-------------------------------------")
	tet_infoline ("Return code "+str(return_code))
	tet_infoline("-------------------------------------")
	tet_infoline ("Output ")
	for i in output.split(os.linesep):
	  tet_infoline(str(i).strip())
	tet_infoline("-------------------------------------")


def test1():
	tet_infoline ("Test Case 1 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: grep pass <(echo 'Test pass without syntax errors')")
	process = executeCMD("echo \"grep pass <(echo 'Test pass without syntax errors')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test1_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Test pass without syntax errors","/tmp/test1_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test2():
	tet_infoline ("Test Case 2 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: grep pass < <(echo 'Test pass without syntax errors')")
	process = executeCMD("echo \"grep pass < <(echo 'Test pass without syntax errors')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test2_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Test pass without syntax errors","/tmp/test2_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test3():
	tet_infoline ("Test Case 3 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < <(echo 'Hello World')")
	process = executeCMD("echo \"cat < <(echo 'Hello World')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test3_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Hello World","/tmp/test3_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test4():
	tet_infoline ("Test Case 4 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < <(echo test)")
	process = executeCMD("echo \"cat < <(echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test4_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["test","/tmp/test4_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test5():
	tet_infoline ("Test Case 5 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < < (echo test)")
	process = executeCMD("echo \"cat < < (echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test5_bash.log 2>&1", None)
	if process[-1] != 2:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["syntax error","/tmp/test5_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test6():
	tet_infoline ("Test Case 6 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat >>(echo test)")
	process = executeCMD("echo \"cat >>(echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test6_bash.log 2>&1", None)
	if process[-1] != 2:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["syntax error","/tmp/test6_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test7():
	tet_infoline ("Test Case 7 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat >> (echo test)")
	process = executeCMD("echo \"cat >>(echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test7_bash.log 2>&1", None)
	if process[-1] != 2:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["syntax error","/tmp/test7_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test8():
	tet_infoline ("Test Case 8 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat <<(echo test)")
	process = executeCMD("echo \"cat <<(echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test8_bash.log 2>&1", None)
	if process[-1] != 2:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["syntax error","/tmp/test8_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test9():
	tet_infoline ("Test Case 9 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat <(echo test)")
	process = executeCMD("echo \"cat <(echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test9_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["test","/tmp/test9_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test10():
	tet_infoline ("Test Case 10 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < <(ls -l)")
	process = executeCMD("echo \"cat < <(ls -l)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test10_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["total","/tmp/test10_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test11():
	tet_infoline ("Test Case 11 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < < (ls -l)")
	process = executeCMD("echo \"cat < < (ls -l)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test11_bash.log 2>&1", None)
	if process[-1] != 2:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["syntax error","/tmp/test11_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test12():
	tet_infoline ("Test Case 12 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: /usr/coreutils/bin/cat < < (echo test)")
	process = executeCMD("echo \"/usr/coreutils/bin/cat < < (echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test12_bash.log 2>&1", None)
	if process[-1] != 2:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["syntax error","/tmp/test12_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test13():
	tet_infoline ("Test Case 13 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: /usr/coreutils/bin/cat < <(echo test)")
	process = executeCMD("echo \"/usr/coreutils/bin/cat < <(echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test13_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["test","/tmp/test13_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test14():
	tet_infoline ("Test Case 14 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: /usr/coreutils/bin/grep pass <(echo 'Test pass without syntax errors')")
	process = executeCMD("echo \"/usr/coreutils/bin/grep pass <(echo 'Test pass without syntax errors')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test14_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Test pass without syntax errors","/tmp/test14_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test15():
	tet_infoline ("Test Case 15 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: /usr/coreutils/bin/grep pass < <(echo 'Test pass without syntax errors')")
	process = executeCMD("echo \"/usr/coreutils/bin/grep pass < <(echo 'Test pass without syntax errors')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test15_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Test pass without syntax errors","/tmp/test15_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test16():
	tet_infoline ("Test Case 16 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: /usr/coreutils/bin/grep pass < <(/usr/coreutils/bin/echo 'Test pass without syntax errors')")
	process = executeCMD("echo \"/usr/coreutils/bin/grep pass < <(/usr/coreutils/bin/echo 'Test pass without syntax errors')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test16_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Test pass without syntax errors","/tmp/test16_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test17():
	tet_infoline ("Test Case 17 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: /usr/coreutils/bin/cat < <(/usr/coreutils/bin/echo test)")
	process = executeCMD("echo \"/usr/coreutils/bin/cat < <(/usr/coreutils/bin/echo test)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test17_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["test","/tmp/test17_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test18():
	tet_infoline ("Test Case 18 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < <(echo '')")
	process = executeCMD("echo \"cat < <(echo '')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test18_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["","/tmp/test18_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test19():
	tet_infoline ("Test Case 19 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < <(printf 'fff\n')")
	process = executeCMD("echo \"cat < <(printf 'fff\n')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test19_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["fff","/tmp/test19_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test20():
	tet_infoline ("Test Case 20 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < <(printf 'f1\nf2\nf3\nf4\n')")
	process = executeCMD("echo \"cat < <(printf 'f1\nf2\nf3\nf4\n')\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test20_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["f1","f2","f3","f4","/tmp/test20_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test21():
	tet_infoline ("Test Case 21 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: cat < <({ echo 'hello $$'; sleep 5 ; echo 'hello again $$' ; })")
	process = executeCMD("echo \"cat < <({ echo 'hello $$'; sleep 5 ; echo 'hello again $$' ; })\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test21_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["hello","/tmp/test21_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return

	tet_infoline("Verification successful")
	tet_infoline(str(returnValue))
	tet_result(TET_PASS)

def test22():
	tet_infoline ("Test Case 22 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo < <(true)")
	process = executeCMD("echo \"echo < <(true)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test22_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["","/tmp/test22_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test23():
	tet_infoline ("Test Case 23 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo > >(true)")
	process = executeCMD("echo \"echo > >(true)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test23_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return
	#tet_infoline_output("Bash Output ",process)
	#String=[" ","/tmp/test23_bash.log"]
	#returnValue=CompareString(String)
	#if returnValue[-1] != 0:
	#	tet_infoline("Verification failed ")
	#	tet_infoline(str(returnValue))
	#	tet_result(TET_FAIL)
	#	return
	#tet_infoline("Verification successful ")
	#tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test24():
	tet_infoline ("Test Case 24 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo < <(false)")
	process = executeCMD("echo \"echo < <(false)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test24_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["","/tmp/test24_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test25():
	tet_infoline ("Test Case 25 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo > >(false)")
	process = executeCMD("echo \"echo > >(false)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test25_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return
#	tet_infoline_output("Bash Output ",process)
#	String=[" ","/tmp/test25_bash.log"]
#	returnValue=CompareString(String)
#	if returnValue[-1] != 0:
#		tet_infoline("Verification failed ")
#		tet_infoline(str(returnValue))
#		tet_result(TET_FAIL)
#		return
#	tet_infoline("Verification successful ")
#	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test26():
	tet_infoline ("Test Case 26 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: wc <(cat /tmp/Arnob)")
	process = executeCMD("ls /tmp/Arnob", None)
	if process[-1] != 0:
		executeCMD("mkdir -p /tmp/Arnob", None)
	process = executeCMD("echo \"wc <(cat /tmp/Arnob)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/tes26_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Is a directory","/tmp/test26_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	#tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)
	
def test27():
	tet_infoline ("Test Case 27 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: /usr/coreutils/bin/diff -u <(ls /tmp/Arnob |sort) <(ls -a /tmp/Arnob |sort)")
#	process = executeCMD("ls /tmp/Arnob", None)
#	if process[-1] != 0:
#		executeCMD("mkdir -p /tmp/Arnob", None)
	executeCMD("echo a > /tmp/Arnob/a", None)
	executeCMD("echo b > /tmp/Arnob/b", None)
	executeCMD("mv /tmp/Arnob/b /tmp/Arnob/.b", None)	
	process = executeCMD("echo \"/usr/coreutils/bin/diff -u <(ls /tmp/Arnob |sort) <(ls -a /tmp/Arnob |sort)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test27_bash.log 2>&1", None)
	if process[-1] != 1:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["+.b","/tmp/test27_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	#tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test28():
	tet_infoline ("Test Case 28 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo <(true)")
	process = executeCMD("echo \"echo <(true)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test28_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Interrupted system call","/tmp/test28_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test29():
	tet_infoline ("Test Case 29 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo <(true)")
	process = executeCMD("echo \"echo <(true)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test29_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Interrupted system call","/tmp/test29_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test30():
	tet_infoline ("Test Case 30 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo <(false)")
	process = executeCMD("echo \"echo <(false)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test30_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Interrupted system call","/tmp/test30_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test31():
	tet_infoline ("Test Case 31 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo >(false)")
	process = executeCMD("echo \"echo >(false)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test31_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["Interrupted system call","/tmp/test31_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test32():
	tet_infoline ("Test Case 32 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo > >(true) < < (true)")
	process = executeCMD("echo \"echo > >(true) < < (true)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test32_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["","/tmp/test32_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test33():
	tet_infoline ("Test Case 33 for /usr/coreutils/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-181203-2882/10-190107-9027/10-190304-7318 ")
	tet_infoline ("Description from Solution Title: EN: HPE bash 4.4.19 missing process substitution feature")
	tet_infoline ("CMD: echo > >(false) < < (false)")
	process = executeCMD("echo \"echo > >(false) < < (false)\" > /tmp/check.sh", None)
	process = executeCMD("bash /tmp/check.sh > /tmp/test33_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["","/tmp/test33_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test34():
	tet_infoline ("Test Case 34: To check symlink for /bin/bash ")
	tet_infoline ("Case/Solution/CR-ID: 10-190412-4890/10-190412-9866/10-190625-8334 ")
	tet_infoline ("Description fron Solution Title: Provide /bin/bash and /usr/bin/bash symlinks to /usr/coreutils/bin/bash ")
	tet_infoline ("CMD: ls -tlr /bin/bash ")
	process = executeCMD("ls -ltr /bin/bash > /tmp/test34_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["/bin/bash -> /usr/coreutils/bin/bash","/tmp/test34_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)
	
def test35():
	tet_infoline ("Test Case 35:To check symlink for /usr/bin/bash")
	tet_infoline ("Case/Solution/CR-ID: 10-190412-4890/10-190412-9866/10-190625-8334 ")
	tet_infoline ("Description fron Solution Title: Provide /bin/bash and /usr/bin/bash symlinks to /usr/coreutils/bin/bash ")
	tet_infoline ("CMD: ls -ltr /usr/bin/bash ")
	process = executeCMD("ls -ltr /usr/bin/bash > /tmp/test35_bash.log 2>&1", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("Bash Output ",process)
	String=["/usr/bin/bash -> /usr/coreutils/bin/bash","/tmp/test35_bash.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	tet_infoline_output(returnValue[-2],returnValue[-1])
	tet_result(TET_PASS)

def test36():
	tet_infoline ("Test Case 36 for /usr/coreutils/bin/find")
	result=executeCMD("python "+os.environ['TET_ROOT']+"/TestWareFS/T1202OSSCORE/scripts/bash/cr_automation/setup.py")
	process = executeCMD("find /tmp/ -name FILE0 > /tmp/defect_repair_T1202.log 2>&1", None)
	process1 = executeCMD("cat /tmp/defect_repair_T1202.log", None)
	if process[-1] != 0:
		tet_infoline("command failed with")
		tet_infoline_output("Execution Output ", process)
		executeCMD("rm -rf /tmp/test0", None)
		tet_result(TET_FAIL)
		return

	tet_infoline_output("find output",process1)
	String=["FILE0","/tmp/defect_repair_T1202.log"]
	returnValue=CompareString(String)
	if returnValue[-1] != 0:
		tet_infoline("Verification failed ")
		tet_infoline(str(returnValue))
		executeCMD("rm -rf /tmp/test0", None)		
		tet_result(TET_FAIL)
		return
	tet_infoline("Verification successful ")
	executeCMD("rm -rf /tmp/test0", None)	
	tet_result(TET_PASS)
	
testlist = {1:test1,2:test2,3:test3,4:test4,5:test5,6:test6,7:test7,8:test8,9:test9,10:test10,11:test11,12:test12,13:test13,14:test14,15:test15,16:test16,17:test17,18:test18,19:test19,20:test20,21:test21,22:test22,23:test23,24:test24,25:test25,26:test26,27:test27,28:test28,29:test29,30:test30,31:test31,32:test32,33:test33,34:test34,35:test35,36:test36}
pytet_init(testlist, startup, cleanup)
