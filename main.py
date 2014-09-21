import os
from contest import *

nowContest=0
os.system('cd ~')
while True:
	print(os.getcwd())
	opt=''
	try:
		opt=input(">>> ")
	except EOFError:
		break
	if opt=='q':
		break
	if opt.split()[0] in ['open','new']:
		os.chdir(opt.split()[1])
		if opt.split()[0] == 'new':
			try:
				os.remove('dataconf.json')
			except FileNotFoundError:
				pass
		nowContest=contest()
		print(nowContest)
	elif opt.split()[0] == 'append':
		argv=opt.split();
		srcName,inPattern,outPattern=argv[1],argv[2],argv[3]
		checkerCmd=""

		regexList={}
		for pat in argv[4:]:
			t=pat.split("=")
			if t[0]=="checker_cmd":
				checkerCmd=t[1]
			else:
				regexList[t[0]]=t[1]
		nowContest.appendProblem(srcName,inPattern,outPattern,regexList,checkerName=checkerCmd)
	elif opt.split()[0] == 'test':
		nowContest.test()
	elif opt.split()[0] == 'display':
		nowContest.problemset.display()
	else:
		print("No such cmd.")
