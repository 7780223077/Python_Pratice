class Student:
    def __init__(self, id, name, stream, fee):
        self._id= id
        self._name= name
        self._stream = stream
        self._fee = fee

    @property
    def name(self):
        return self._name
    
    @property
    def stream(self):
        return self._stream
    
    @property
    def fee(self):
        return self._fee
    
    @name.setter
    def name(self, name):
        self._name = name 

    @stream.setter
    def stream(self, stream):
        self._stream = stream 

    @fee.setter
    def fee(self, fee):
        self._fee = fee   

    def __str__(self) -> str:
        return f"id : {self._id}, name : {self._name}, stream : {self._stream}, fee : {self._fee}"
    

class StudentManagement:
    def __init__(self) -> None:
        self._students = []

    def add_student(self):
        print("enter student details to add : ")
        id = input('enter student id : ')
        name = input('enter student name : ')
        stream = input('enter student stream : ')
        fee = input('enter student fee : ')
        student = Student(int(id), name, stream, float(fee))
        self._students.append(student)

    def print_students(self):
        for student in self._students:
            print(student)