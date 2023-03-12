from app1.models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# User = get_user_model()

# print(User.objects.all())

# command line argument to access data from the databases :-
# exec(open(r'D:\Python_Course\b8_django\first_project\app1\db_shell.py').read())

# obj = Person.objects.all() #-------- ORM object relational mapper
# print(obj.query)      SELECT "person"."id", "person"."name", "person"."age", "person"."mobile_num", "person"."address" FROM "person"
# print(list(obj))

# for Person in obj:
#     print(Person.__dict__)

# to get first record from databases
# first_record = Person.objects.first()
# print(first_record)


# to get record from database using id
# obj = Person.objects.get(id = 7)                # give only single record because of provide only one id given 
# print(obj)


# to get record does not exit 

# try:
#     obj = Person.objects.get(id = 12)
#     print(obj)
# except Person.DoesNotExist:
#     print("Record does not exit")


# To get multiple record by passing filename

# Person.objects.get(age = 25)  # in the database there two same record so don't use get


# obj = Person.objects.filter(age = 23, address = "dhule")
# print(obj.query)


# Modify existing data
# p1 = Person.objects.get(id = 1)
# print(p1.__dict__)
# p1.mobile_num = 2222     # -- To update or change in records
# print(p1.__dict__)
# p1.save()

# p1.delete()  -- deleting the particular record by using object p1 and providing which data have to delete


# 1st way to 
# creating the object 
# p1 = Person(name = "xyz", age = 20, mobile_num = 99, address = "jintur")
# p1.save()

# 2nd way to

# Person.objects.create(name = "Sham", age = 25, mobile_num = 66, address = "mumbai")

# print(dir(Person.objects))


# bulk_create               # To create bulk of recodes by using bulk_create and also we can create by using random function genarater
# p1 = Person(name = "A", age = 26, mobile_num = 77, address = "pune")
# p2 = Person(name = "B", age = 32, mobile_num = 88, address = "pune")
# p3 = Person(name = "C", age = 20, mobile_num = 99, address = "pune")
# p4 = Person(name = "D", age = 55, mobile_num = 111, address = "pune")

# Person.objects.bulk_create([p1, p2, p3, p4])

# Count :- If we want to count how many records are in database
# print(Person.objects.count())

# Delete :- To delete all record from the database use delete() and then all record are deleted by using filter we can delete particular records
# deleting all recordes
# Person.objects.all().delete()

# for delete multiple records
# Person.objects.filter(age = 25).delete()

# print(Person.objects.filter(name__startswith = "a"))
# print(Person.objects.filter(name__endswith = "m"))

# print(Person.objects.exclude(name__startswith = 'k'))
# print(Person.objects.filter(id = 1).exists())    # O/p :- True
# print(Person.objects.all().order_by("id")) # -id also use for descending order 
# print(Person.objects.all().order_by("-name"))

# Person.objects.get(id=3).show_details()    # by using function where we declare a doctring and apply a formating and we get all the info


# for per_obj in Person.objects.all():
#     per_obj.show_details()


# print(Person.get_data_above_age())

# print(Person.objects.filter(name__contains = "a"))



# data = Person.objects.filter(name__contains = "a")
# print(data)
# for i in data:
    # print(i, type(i))



# exec(open(r'D:\Python_Course\b8_django\first_project\app1\db_shell.py').read())
# print(Person.objects.all)

# print(Person.objects.filter(name__contains="a")) # Get the record by containg the word pass in function

# data = Person.objects.all().values("id", "name", "age") # For fetching all the data records from the database and we can pass the header and we get a particular data
# print(data)
# name_lst = []
# for i in data:
#     name_lst.append(i["name"])     # For accessing the from the data we can access too
# print(name_lst)
# print(data)
# print(list(map(lambda x: x['age'], list(data))))
# lst = list(map(lambda x: x['age'], list(data)))

# print(sum(lst)//len(lst))    # For calculating average age

# data = Person.objects.all().values_list()   # To get the data from the databases in the form of tuple we can convert it because of tuple is immutable 
# print(data)

# data = Person.objects.all().values_list("name")   # List of tuple name only 
# print(list(data))


# Here we change the database sqlite to mysql 
# User.objects.create_user(username="Rahul", password= "Python@123") # alway use create_user for encrypt the password 
# in above quary creating user for the admin login 


# data = list(Person.objects.all().values("id", "address", 'date_joins'))
# for i in data:
#     print(i)



# data = Person.objects.filter(id__in={6})    # for updating the data in database
# print(data)
# for i in data:
#     i.is_active = False           # is_active is True in databases but by using this we change it to false
#     i.save()

# or by using we can update the record like aboue quary
# data = Person.objects.filter(id__in=[5]).update(is_active = True)


# print(Person.objects.filter(is_active=True))


# print(Person.objects.filter(is_active=True))


# print(Person.get_active_data())    # print the data by using function form the models.py and we can say that calling the function 

# print(Person.get_inactive_data())     # print the inactive data



# objects is model manager for accessing the data from the database by using class(model) is called as model manager

# print(Person.activep.all())   # this is custom object for fetching data

# print(Person.inactivep.all())


# print(Person.all_data.all())


# clgs = College.objects.all()
# pric = Principle.objects.all()
# depts = Department.objects.all()
# studs = Student.objects.all()
# subjs = Subjects.objects.all()




# print(clg)
# print(pric)
# print(depts)
# print(studs)
# print(subjs)

# for dept in depts:
#     print(dept.__dict__)

# for subj in subjs:
#     print(subj.__dict__)

# for stud in studs:
#     print(stud.__dict__)

# for college in clg:
#     print(college.__dict__)

# for principle in pric:
#     print(principle.__dict__)


# clg = clgs[0]
# print(clg.principle.__dict__) # one to one relation for fatching the principle data using clg object

# obj = Principle.objects.first()
# print(obj.college.__dict__)


# print(clg.department_set.all())   # one to many Relation clg object and pass department_set attribute 


# dept = Department.objects.first()
# print(dept.college)                 # many to one for department in college using Department object is dept 

# print(dept.student_set.all())

# all_dept = Department.objects.all()
# d = {}
# for dept in all_dept:
    # print(f"Department Name:- {dept.name}, stud :- {list(dept.student_set.all())})")
    # d[dept.name] = list(dept.student_set.all())
# print(d)

# s1 = Student.objects.first()
# print(s1.dept)

# s1 = Student.objects.get(id=4)
# print(s1.dept)


# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.name

# print(stud_dept_dict)

# clg = College.objects.get(id=1)
# print(clg.principle)   # Giving related name that pass in models related_name = 'pri' like this and giving other too by respected tb_tabel name


# clg = College.objects.select_related('principle').all()
# print(clg)
# for i in clg:
    # print(i.__dict__)

# clg = College.objects.get(id=1)
# print(clg.principle.__dict__)
# print(clg.depts.all())


# dept = Department.objects.get(id=2)
# print(dept)
# print(dept.subjs.all())

# depts = Department.objects.all()
# for dept in depts:
    # print(dept.subjs.all())

# clg = College.objects.get(id=1)
# print(clg.depts.all())

# print([dept.subjs.all() for dept in Department.objects.all()]) # using list comprehension

# clg = College.objects.get(id=1)
# print(clg.depts.all()[0].studs.all()[0])
# stud_list = []
# all_depts = clg.depts.all()
# for dept in all_depts:
    # stud_list.extend(dept.studs.all())
# print(stud_list)

# s1 = Student.objects.get(id=5)
# print(s1.dept.college)


# ADDITION
# College.objects.create(name="MIT", adr='Aurangabad')
# c1 = College.objects.get(id=2)

# p1 = Principle(name="ABC", exp=20, qul="phd", college=c1)
# p1.save()

# other way for above code
# p1 = Principle(name="ABC", exp=20, qul="phd", college_id=2)
#p1.save()


# make sure that college id is present in table
# Department.objects.create(name= "production", dept_str=60, college = c1)

# Student.objects.create(name="AAA", marks=44, age=18)
# Student.objects.create(name="BBB", marks=50, age=19)
# Student.objects.create(name="CCC", marks=60, age= 20)



# s1, s2, s3 = Student.objects.filter(id__gt=9)
# print(s1, s2, s3)


# prod_dept = Department.objects.get(id=3)
# print(dir(prod_dept.studs))

# prod_dept.studs.add(s2, s3)
# print(dir(prod_dept.studs))


#---------------------------------------------------------------------------------------------------------------------------------------


# Select_Related

# studs = Student.objects.all()[:3]
# print(studs)

# studs = Student.objects.all()
# for stud in studs:
#     print(stud.dept)

# studs = Student.objects.select_related("dept")
# for stud in studs:
#     print(stud.dept.name)


# c100 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")
# print(CarModel.objects.all())

# gas = FuleType.objects.create(name="Gas")
# diesel = FuleType.objects.create(name="Diesel")
# hybrid = FuleType.objects.create(name="Hybrid")
# print(FuleType.objects.all())
c180 = CarModel.objects.get(name="C180")
c200 = CarModel.objects.get(name="C200")

gas = FuleType.objects.get(name="gas")
diesel = FuleType.objects.get(name="diesel")
hybrid = FuleType.objects.get(name="hybrid")

# c180.fuletype.add(diesel)
# print(c180.fuletype.all())

# c200.fuletype.add(diesel, hybrid)
# c200.fuletype.create(name="Bio Diesel")   # Create new fule record and also assgining it too 


# print(c180.fuletype.all())
# print(c200.fuletype.all())

# print(gas.carmodel_set.all()
# print(diesel.carmodel_set.all())
# print(hybrid.carmodel_set.all())

# print(gas.carmodels.all())    # using related name given in models.py 


# print(CarModel.objects.filter(fuletype__name__startswith="G"))


# print(FuleType.objects.filter(carmodels__name__startswith="C"))

# print(Student.objects.filter(dept__college__id=1))

#--------------------------------------------------------------------------------------------------------------------------
# ORM  django    Raw Quary of sql 

from django.db import connection

# cursor = connection.cursor()
# cursor.execute('''select * from student''')
# data = cursor.fetchmany(3)
# print(data)

# data = cursor.fetchmany(3)
# print(data)

# data = Student.objects.raw('select * from student')
# for i in data:
#     print(i.dept)


# Multiple databases
# Multi tenand 
# MySQL, SQLite3

# data = Student.objects.all()
# print(data)

# inserting data in second_db

SECOND_DATABASE = "second_db"
# data = Student.objects.using(SECOND_DATABASE).all()
# print(data)

# data = Student.objects.using(SECOND_DATABASE).create()

# c1 = College.objects.using(SECOND_DATABASE).create(name="IMSIT", adr="Aurangabad")
# d1 = Department.objects.using(SECOND_DATABASE).create(name="", dept_str=60, college=c1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name="Ganesh", marks=75, age=25, dept=d1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name="Amar", marks=55, age=26, dept=d1)
# d1 = Department.objects.using(SECOND_DATABASE).get(id=1)
# subj1 = Subjects.objects.using(SECOND_DATABASE).create(name="DAta Signal", is_practical=True, dept=d1)

# studs = Student.objects.using(SECOND_DATABASE).all()
# print(studs)

# clg = College.objects.using(SECOND_DATABASE).all()
# print(clg)

# dept = Subjects.objects.using(SECOND_DATABASE).all()
# print(dept)