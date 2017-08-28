from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 40)
	phone = models.CharField(max_length = 12) 
	class_name = models.CharField(max_length = 2) 
	address = models.TextField(max_length = 100,default = "not provided")

	def __str__(self):
	  return self.name

	@classmethod
	def create(cls,params):
		new_student = cls(name = params["name"],phone = params["phone"],class_name = params["class_name"],address = params["address"])
		return new_student
	
# first_student = Student.create({"name":"new_student_one","phone":"7894561230","class_name":"09"})