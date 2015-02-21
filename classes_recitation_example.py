# NOTE TO THE TA: the main function is at the bottom of this page. It ties in 2 different classes and illustrates static vs non static methods, among other things
# imagine that UPenn has asked you to build a system to manage enrolled students in various departments of the university
class Student:
	numberOfStudentsCreated = 0
	
	def __init__(self, name, email, major, graduation_year, pennkey):
		self.name = name
		self.email = email
		self.major = major
		self.graduation_year = graduation_year
		self.pennkey = pennkey
		Student.numberOfStudentsCreated += 1
		
		

	def get_student_name(self):
		return self.name

	def print_student_email(self):
		print "Email: ", self.email

	def print_student_major(self):
		print "Major: ", self.major

	def print_graduation_year(self):
		print "Graduation Year: ",  self.graduation_year

	def print_pennkey(self):
		print "Pennkey: ", self.pennkey

	def change_major(self, new_major):
		self.major = new_major

	def change_graduation_year(self, new_graduation_year):
		self.graduation_year = new_graduation_year


class Department:
	university_building_codes = {"TOWN": "Towne Building", "COLL": "College Hall", "FAGN": "Fagin Hall", "JMHH": "Huntsman Hall", "MOOR": "Moore Building"}
	numberOfDepartments = 0

	def __init__(self, department_name, main_office_building_code):
		self.name = department_name
		self.main_office = Department.university_building_codes[main_office_building_code]
		self.student_list = []
		Department.numberOfDepartments += 1
				

	def print_department_name(self):
		print "Department Name:", self.name

	def print_main_office_building(self):
		print "Main Office Building:", self.main_office

	def add_new_student(self, Student):
		self.student_list.append(Student)

	def remove_student(self, Student):
		#you will have to ensure that the given argument is a student who is already in the deaprtment
		self.student_list.remove(Student)

	def list_all_student_names(self):
		 student_names = []
		for student in self.student_list:
			student_names.append(student.get_student_name())
		return student_names


def main():
	print "hello"
	print Student.numberOfStudentsCreated
	student1 = Student("Yao", "chuyao@seas.upenn.edu", "Mechanical Engineering", 2020, "chuyao")
	student2 = Student("Juntao", "juntao@amazingTA.com", "Hairstyle Sciences", 2015, "juntao")
	student3 = Student("Alex", "alex@nicesthuman.org", "Awesomenology", 2015, "alex")

	print Student.numberOfStudentsCreated # => 3
	
	#student2 finishes his coursework very quickly and wants to change his graduation date to 2020 instead:
	student1.change_graduation_year(2020)
	#make sure it has been changed
	student1.print_graduation_year() #=> 2020

	department1 = Department("Awesomenology", "TOWN")
	department1.add_new_student(student1)
	#check if student1 was added to department
	print department1.list_all_student_names() # => 'Yao'

	department2 = Department("Hairstyle Sciences", "MOOR")
	department2.add_new_student(student2)
	department2.add_new_student(student3) #we added student3 to the department of Hairstyle Sciences by mistake! let's correct it
	department2.remove_student(student3)
	#lets make sure the right students are in the department
	print department2.list_all_student_names() # => 'Juntao'

	print Department.numberOfDepartments # => 2




if __name__ == '__main__':
	main()

