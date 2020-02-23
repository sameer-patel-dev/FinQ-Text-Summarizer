from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
# import sys
# sys.path.append(r'/home/mittal/CodeBlooded_DJHack/BackEnd')
from . import mainn
# Create your views here.
def index(request):
	answer = 'wrong.'
	if request.method == "POST":
		# uploaded_file = request.FILES['document']
		# fs = FileSystemStorage()
		# fs.save(uploaded_file.name, uploaded_file)
		question = request.POST.get('srch-term', None)
		print(question)
		answer = mainn.challenge1(question)
	context = {'answer':answer}
	return render(request,'ask/home.html',context)

# def ans(request):
# 	return render(request,'ask/home.html')