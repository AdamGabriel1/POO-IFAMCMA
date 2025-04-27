class Aluno:
    pass
    
class Curso:
    def __init__(self,aluno):
        self.aluno=aluno

class Casa:
    def contem(self,classe):
        print(f"{classe} contem")
        
class TabuleiroDeXadrez:
    def contem(self,classe):
        print(f"{classe} contem[64]")

class C1:
    pass

class C2:
    pass

class PropriedadesDaRelacao(C1, C2):
    pass
    
class School:
    pass
    
class Department:
    def has(self,classe):
        print(f"Department has {classe}")
        
class Student:
    def attends(self,classe):
        print(f"Student attends {classe}")
    
    def member(self,classe):
        print(f"Student member {classe}")

class Course:
    pass
    
class Instructor:
    def teaches(self,classe):
        print(f"Instructor teaches {classe}")
        
    def assignedTo(self,classe):
        print(f"Instructor assignedTo {classe}")