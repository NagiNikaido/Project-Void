import os,sys,json

INF = 1000000

class problemset(object):
	name='nonamepro'
	def __init__(self,workDir='.'):
		self.dir=workDir
		a,b='',''
		try:
			a=open(workDir+"/dataconf.json","r")
		except IOError:
			self.problemList=json.loads('{ \"problems\": {} }')
		else:
			self.problemList=json.load(a)
			a.close()

	def export(self):
		a=open(self.dir+"/dataconf.json","w")
		json.dump(self.problemList,a,sort_keys=True,indent=4)
		a.close()
	
	def display(self):
		print(json.dumps(self.problemList,sort_keys=True,indent=4))
	
	def clear(self):
		self.problemList=json.loads("{ \"problems\": {} }")
	
	def getProblemList(self):
		return self.problemList
	def appeared(self,problemName):
		return problemName in self.problemList["problems"]
	
	def appendProblem(self,problemName,inputFileList=[],outputFileList=[],TimeLimit=INF,MemLimit=INF,checkerName=''):
		if self.appeared(problemName):
			print("The problem \""+problemName+"\" has appeared already. If you want to replace it with a new one, remove the old one first.")
			return -1
		tmp={"checker": checkerName,"testCases": []}
		
		for i in range(len(inputFileList)):
			tmp["testCases"].append({"in": inputFileList[i],"out": outputFileList[i],"timeLimit": TimeLimit,"memLimit": MemLimit})
		
		self.problemList["problems"][problemName]=tmp
		print("The problem \""+problemName+"\" has been added.")
		return 0
		
	def removeProblem(self,problemName):
		try:
			self.problemList["problems"].pop(problemName)
		except KeyError: print("The problem \""+problemName+"\" has not appeared yet.");return -1
		else: print("The problem \""+problemName+"\" has been removed.");return 0
	
	def appendTestCase(self,problemName,inputFileName,outputFileName,TimeLimit=INF,MemLimit=INF):
		if not self.appeared(problemName):
			print("The problem \""+problemName+"\" has not appeared yet.");return -1
		else:
			self.problemList["problems"][problemName]["testCases"].append({"in": inputFileName,"out": outputFileName,"timeLimit": TimeLimit,"memLimit": MemLimit})
			print("Appended successfully.")
			return 0

	def removeTestCase(self,problemName,CaseNo):
		if not self.appeared(problemName):
			print("The problem \""+problemName+"\" has not appeared yet.");return -1
		elif CaseNo>len(self.problemList["problems"][problemName]["testCases"]) or CaseNo<=0:
			print("The problem \""+problemName+"\" doesn't have such test case.");return -1;
		else:
			t=self.problemList["problems"][problemName]["testCases"]
			self.problemList["problems"][problemName]["testCases"]=t[:CaseNo-1]+t[CaseNo:]
			print("Removed successfully.")
			return 0

	def modifyTestCase(self,problemName,CaseNo,newTimeLimit=-1,newMemLimit=-1):
		if not self.appeared(problemName):
			print("The problem \""+problemName+"\" has not appeared yet.");return -1
		elif CaseNo>len(self.problemList["problems"][problemName]["testCases"]) or CaseNo<=0:
			print("The problem \""+problemName+"\" doesn't have such test case.");return -1;
		else:
			if newTimeLimit!=-1:
				self.problemList["problems"][problemName]["testCases"][CaseNo-1]["timeLimit"]=newTimeLimit;
			if newMemLimit!=-1:
				self.problemList["problems"][problemName]["testCases"][CaseNo-1]["memLimit"]=newMemLimit;
			print("Modified successfully.");
			return 0;

if __name__=="__main__":
		a=problemset()
		a.display()
		a.removeProblem("123")
		a.display()
		a.removeProblem("maze")
		a.display();
		a.appendProblem("123")
		a.display()
		a.appendProblem("maze",inputFileList=["1.in","2.in","3.in"],outputFileList=["1.out","2.out","3.out"])
		a.display();
		a.removeTestCase("maze",1)
		a.display();
		a.modifyTestCase("maze",1,newTimeLimit=128,newMemLimit=1000)
		a.display();
		a.appendTestCase("123","1.in","1.out")
		a.display();
