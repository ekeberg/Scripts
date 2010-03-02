#! /usr/bin/python

import sys, os, re

l = os.popen('find /home/ekeberg/Scripts').readlines()
files = [f[:-1] for f in l]

expr = re.compile('.py$')
py_files = filter(expr.search,files)

#expr = re.compile('^(.(?!home/ekeberg/Scripts/global))*$')
expr = re.compile('^(.(?!home/ekeberg/Scripts/global))*$')
#expr = re.compile('(?!^/home/ekeberg/Scripts/global)')
py_files2 = filter(expr.search,py_files)

expr = re.compile('/\w+\.py')

names = []

for i in py_files2:
    m = expr.search(i)
    names.append(i[m.start()+1:m.end()-3])

for i in range(len(py_files2)):
    os.system("cp %s /home/ekeberg/Scripts/global/python_script_%s"
              % (py_files2[i],names[i]))

os.system("chmod 744 /home/ekeberg/Scripts/global/*")
