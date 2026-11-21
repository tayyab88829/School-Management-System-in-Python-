import json

class SchoolMgSys:
    def __init__(self):
        self.students_info = {}
        self.teachers_info = {}
        self.id_student = 1
        self.id_teacher = 0
        
        self.menu()

    def menu(self):
        while True:
            principle = input("""
            Select to Check Details!
            1. Students Name and Info
            2. Teachers Admission
            3. Number of Students in classes 
            4. For Admission
            5. Teacher's Info.
            6. Exit
    """)
            if principle == '1':
                self.student_name_info()
            elif principle == '2':
                self.admission_teacher()
            elif principle == '3':
                self.count_in_class()
            elif principle == '4':
                self.admission()
            elif principle == '5':
                self.teachers_inf()               
            elif principle == '6':
                break
            else:
                print('Invalid Option')

    def save(self):
        data = {
            "students" : self.students_info,
            "teachers" : self.teachers_info,
        }
        with open("names.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        def load(self):
        try:
            with open("names.json", "r", encoding= "utf-8") as f:
                data = json.load(f)
                self.students_info = data.get("students", {})
                self.teachers_info = data.get("teachers", {})
        except FileNotFoundError:
            self.students_info = {}
            self.teachers_info = {}


    def admission(self):
        data = input("Enter Student Name and Class (Name : Class) : ").strip()
        try:   
            name, year = data.split(':')
        except ValueError:
            print('Enter Correctly')
            return
        self.students_info[self.id_student] = {
            "name": name.strip(),
            "class": year.strip(),
            }
        print(f'Admission Added, Roll No: {self.id_student}')
        self.id_student += 1
        self.save()

    def admission_teacher(self):
        data = input("Enter Teacher's Details (Name : Teaching Class...) : ").strip()
        try:   
            name, year = data.split(':')
        except ValueError:
            print('Enter Correctly')
            return
        self.teachers_info[self.id_teacher] = {
            "name": name.strip(),
            "class": year.strip(),
            }
        print(f'Teacher Added!')
        self.id_teacher += 1
        self.save()


    def teachers_inf(self):
        for name , info in self.teachers_info.items():
            print(f'Teacher Name and Teaching Class: {info['name']}, {info['class']}')
        print(f'Total Number of Teachers in School : {self.id_teacher}')
    


    def student_name_info(self):
        for id , info in self.students_info.items():
            print(f'Student Name, Roll No and Class: {info['name']}, {id} (Class {info['class']})')
        print(f'Total Students = {self.id_student - 1}')
                  


    def count_in_class(self):
        class_name = input('Enter Class: ').strip()
        count = sum(1 for s in self.students_info.values() if s['class'] == class_name)

        print(f'Class {class_name} Has {count} Students!')

SchoolMgSys()
