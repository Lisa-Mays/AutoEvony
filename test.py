class Variable:
    def __init__(self):
        self.shared_variable = 5
    
class SubclassA(Variable):
    def __init__(self):
        super().__init__()  # Gọi __init__() của lớp cha Variable
        Variable.shared_variable = 10  # Ghi đè giá trị trong lớp con
        
cha = Variable()

print("Initial shared_variable in cha:", cha.shared_variable)  # In ra: 5

con_a = SubclassA()

print("shared_variable in con_a after update:", con_a.shared_variable)  # In ra: 10
print("shared_variable in cha after update:", cha.shared_variable)  # In ra: 10
