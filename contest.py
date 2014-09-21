import os,sys
from problemset import *
from regexMatcher import *

class contest(object):
	name='noname'
	def __init__(self,workDir='.'):
		self.problemset=problemset(workDir)
		self.dir=workDir
#		try:
#			os.mkdir(self.dir+"/data")
#		except FileExistsError:
#			pass
#		try:
#			os.mkdir(self.dir+"/source")
#		except FileExistsError:
#			pass

	def appendProblem(self,problemName,inPattern,outPattern,regexList,TimeLimit=INF,MemLimit=INF,checkerName=''):
		inList,outList=regexMatcher(problemName,inPattern,outPattern,regexList);
		self.problemset.appendProblem(problemName,inList,outList,TimeLimit,MemLimit,checkerName='')
		self.problemset.export()
	
	def test(self):
		problemList=self.problemset.getProblemList()["problems"]
		for srcName in problemList:
			print("Now testing problem \""+srcName+"\" ...")
			opt="diff "+srcName+".out "+srcName+".ans -Z -B > .nil"
			if problemList[srcName]["checker"]:
				opt=problemList[srcName]["checker"]+" "+srcName+".in "+srcName+".out "+srcName+".ans > .nil"
			cnt=0
			for j in problemList[srcName]["testCases"]:
				inName,ansName=j["in"],j["out"]
				cnt+=1
				os.system("cp "+inName+" "+srcName+".in")
				os.system("cp "+ansName+" "+srcName+".ans")
				print("Test Case #"+str(cnt))
				os.system("./"+srcName)
				if os.system(opt)==0:
					print("Correct!")
				else:
					print("Wrong answer!")
				os.remove(srcName+".in")
				os.remove(srcName+".ans")
				os.remove(srcName+".out")
			print("")
