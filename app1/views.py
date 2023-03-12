from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.


# Function base view 
# def welcome(request):                   # requeset is reserved keyword
    # print(request.method)
    # print(request.user)
    # return HttpResponse("Welcome to the Django Application...!") #1st
    # # studs = Student.objects.get(id=1)
    # studs = list(Student.objects.values("name"))
    # print(studs)
    # final_stud = list(map(lambda x: x["name"], studs))
    # return HttpResponse(f"Welcome to Django Application...!, {final_stud }")


# Views are two types:
# 1. Class base Views
# 2. Function base Views


# Status code
# Status code is Http response  
# -- 1XX - 100 == informational
# -- 2XX - 200 -- Ok or success 
# -- 3XX - 301 -- redirect to other page   Ex :- Stackoverflow
# -- 4XX - 404 -- Client side error
# -- 5Xx - 500 -- server side error

# for not showing error on client side make debug equal to false in setting.py showing error massage only

# Queary params - Queary parameters :- it will use in urls for geting expected output if get more info then add after and 
#                                      you will get the all qyeary paramaters output


def welcome(request):
    return render(request,"home.html")

