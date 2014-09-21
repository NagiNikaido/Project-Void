Project-Void
================

***Project-Void***，一个（将来也许能够）用来代替Lemon、Cena、……的评测系统。暂时只具备在Linux下对一位选手进行评测的能力。（请不要吐槽这些）

~~实现基于python和xml，python2.7.6和python3.4.0均能正常运行。~~

实现基于python和json。这里只保证python3能够正常使用。

暂时支持：

open 打开一个旧有的比赛

new 新建一个比赛

append 添加一道题

test 进行测试

display 输出**dataconf.json**的内容

q 退出交互界面

Changelog
================
2014.9.20 重新了所有组件，并且实现了一个简陋的字符交互界面。

2014.8.16 修复了**init_problem.py**的bug。

2014.8.12 修复了使用checker时会崩溃的bug。

2014.8.9   添加了**init_problem.py**，支持使用正则表达式自动生成**dataconf.xml**文件。