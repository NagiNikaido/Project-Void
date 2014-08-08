import os
import sys
import xml.dom.minidom

def Run(srcName,dataList,checkOpt):
	os.system("g++ "+srcName+".cpp -o "+srcName)
	cnt=0
	for i in dataList:
		inName,ansName=i;cnt+=1
		os.system("cp "+inName+" "+srcName+".in")
		os.system("cp "+ansName+" "+srcName+".ans")
		print("Test Case #"+str(cnt))
		os.system("./"+srcName)
		if os.system(checkOpt)==0:
			print("Correct!")
		else:
			print("Wrong answer!")
		os.remove(srcName+".in")
		os.remove(srcName+".ans")
		os.remove(srcName+".out")
	os.system("rm .nil")
	os.system("rm ./"+srcName)

dataConf=xml.dom.minidom.parse("dataconf.xml")
root=dataConf.documentElement;
srcName,checker_cmd=root.getAttribute("name"),root.getAttribute("checker_cmd")

opt="diff "+srcName+".out "+srcName+".ans -Z -B > .nil"
if checker_cmd!="":
	opt=checker_cmd+" "+srcName+".in "+srcName+".out"+srcName+".ans > .nil"

dataList=[]
for i in root.getElementsByTagName("data"):
	dataList.append((i.getAttribute("in"),i.getAttribute("out")))

Run(srcName,dataList,opt)

