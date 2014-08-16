import os
import sys
import xml.dom.minidom
import re

#def getDir(fileDir):
#	Dir=fileDir.path.split()
#	t=fileDir.split(os.sep)
#	Dir=""
#	for i in t[:-1]:
#		Dir+=i+os.sep
#	return (Dir,t[-1:][0])

def getList(Dir,File,regexList):
	a,b,List=re.compile(r"\<\d*\>"),0,[]
	a=re.compile(a.sub(lambda m: regexList[File[m.start():m.end()]],File))
	for p in os.listdir(Dir):
		c=a.match(p)
		if c and c.end()==len(p):
			List.append(p)
	return List

def initProblem(srcName,inPattern,outPattern,checkerCmd,regexList):
	dataConf=xml.dom.minidom.Document()
	root=dataConf.createElement("problem")
	if checkerCmd!="":
		root.setAttribute("checker_cmd",checkerCmd)
	root.setAttribute("name",srcName)
	dataConf.appendChild(root)

#	inDir,inFile=getDir(inPattern)
#	outDir,outFile=getDir(outPattern)
	inDir,inFile=os.path.split(inPattern)
	outDir,outFile=os.path.split(outPattern)
	
	inList=getList(inDir,inFile,regexList)
	outList=getList(outDir,outFile,regexList)
	inList.sort();outList.sort()
	for i in range(len(inList)):
		t=dataConf.createElement("data")
		t.setAttribute("in",inDir+os.sep+inList[i])
		t.setAttribute("out",outDir+os.sep+outList[i])
		root.appendChild(t)
	confFile=open("dataconf.xml","w")
	dataConf.writexml(confFile,"","\t","\n","utf-8")

if __name__=="__main__":
	if len(sys.argv)<4:
		print("Usage: python init_problem.py srcName inputFileNamePattern outputFileNamePattern [checker_cmd=\"...\" \"<1>=regex1\" \"<2>=regex2\" ...]")
		print("       python3 is ok.")
	else:
		srcName,inPattern,outPattern=sys.argv[1],sys.argv[2],sys.argv[3]
		checkerCmd=""

		regexList={}
		for pat in sys.argv[4:]:
			t=pat.split("=")
			if t[0]=="checker_cmd":
				checkerCmd=t[1]
			else:
				regexList[t[0]]=t[1]
		initProblem(srcName,inPattern,outPattern,checkerCmd,regexList)
