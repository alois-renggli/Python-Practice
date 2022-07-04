from HelloWorld import Student

student1 = Student("Alois", "Engineering", 3.64, False)
student2 = Student("Mike", "History", 2.6, True)
student3 = Student("Lucy", "Art", 2.0, True)


print(student1.name)
print(student2.gpa)
print(student3.major)


print(student1.honor_roll())
print(student2.honor_roll())
print(student3.honor_roll())