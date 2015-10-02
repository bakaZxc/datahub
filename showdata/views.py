from django.shortcuts import render
from django.http import HttpResponse
import os
import os.path 
rootdir = "test"
files = []
def getnames(request):
    for filename in os.walk(rootdir):
	for a in range(len(filename)):
		files.append(filename[a])
	data = files[2]
	return render(request,'select.html',{'data':data})
