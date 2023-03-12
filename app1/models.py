from django.db import models

# Create your models here.
# ORM :- Object relational mapper 


class ActivePersons(models.Manager):   # custom model manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)        # this give us like models.objects.all()


class InactivePerson(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)


class Person(models.Model):               # This is for tables
    # Django provide id by default 
    name = models.CharField(max_length=200) # we can also give databases or column by using db_column="nm"
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    date_joins = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default= True)
    activep = ActivePersons()             # this is object of model manage
    inactivep = InactivePerson()
    all_data = models.Manager()


    class Meta:
        db_table = "person"
 

    def __str__(self):
        return f"{self.name} -- {self.address}"
    

    def show_details(self):
        print(f"""---------------------------
        Pesron Name :- {self.name}
        Person age :- {self.age}
        Person Mobile :- {self.mobile_num}
        Person Address :- {self.address}
        """)
    @classmethod
    def get_data_above_age(cls):
        return cls.objects.filter(age__gte=25) # gt(>), gte(>=), lt(<), lte(<=), startswith(), endswith()


    @classmethod
    def get_avrg_age(cls):
        '''Avearge of all person age form the database'''
        data = cls.objects.all().values("id", "name", "age")
        lst = list(map(lambda x: x['age'], list(data)))
        return (sum(lst)//len(lst))

    @classmethod
    def get_active_data(cls):
        return cls.objects.filter(is_active = True)

    @classmethod
    def get_inactive_data(cls):
        return cls.objects.filter(is_active=False)


   
#----------------------------------------------------------------------------------------------------------------------------------------------

# Relation based
   
   
   
   
   
class CommonClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True          # by using at the time of hitting tha makemigartions quary not creating for this 

class College(CommonClass):
    adr = models.CharField(max_length=500)
    est_date = models.DateField(auto_now=True)
        
    class Meta:
        db_table = "college"
    

class Principle(CommonClass):
    exp = models.FloatField()
    qul = models.CharField(max_length=50)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name="principle")
       
    class Mets:
        db_table = "principle"

class Department(CommonClass):
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="depts")
    
    class Meta:
        db_table = "dept"
        # unique_together = (("name", "college"),)   # not exculte it is for database for dublicate element is not allowed 

class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="studs", null=True)

    class Meta:
        db_table = "student"

class Subjects(CommonClass):
    is_practical = models.BooleanField(default=True)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subjs")

    class Meta:
        db_table = "subject"




#----------------------------------------------------------------------------------------------------------------------------------------------

# Many to many different example

class FuleType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fuletype = models.ManyToManyField(FuleType, related_name="carmodels")

    def __str__(self):
        return self.name