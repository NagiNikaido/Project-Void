import os,sys,re

def getList(Dir,File,regexList):
	a,b,List=re.compile(r"<\d*>"),0,[]
	a=re.compile(a.sub(lambda m: regexList[File[m.start():m.end()]],File))
	for p in os.listdir(Dir):
		c=a.match(p)
		if c and c.end()==len(p):
			List.append(p)
	return List

def regexMatcher(srcName,inPattern,outPattern,regexList):
	inDir,inFile=os.path.split(inPattern)
	outDir,outFile=os.path.split(outPattern)
	
	inList=getList(inDir,inFile,regexList)
	outList=getList(outDir,outFile,regexList)
	inList.sort();outList.sort()
	for i in range(len(inList)):
		inList[i]=inDir+os.sep+inList[i]
		outList[i]=outDir+os.sep+outList[i]
	return inList,outList

