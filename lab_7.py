# 1
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Name: {self.name}, ID: {self.id}'

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
        self.projects = []

    def manage_projects(self, project_name):
        self.projects.append(project_name)
        return f'Manager {self.name} manages {project_name}'

    def get_info(self):
        return f'Name: {self.name}, ID: {self.id}, Department: {self.department}, Projects: {self.projects}'

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self, equipment):
        return f'{self.name} currently maintains {equipment}'

    def get_info(self):
        return f'Name: {self.name}, ID: {self.id}, Specialization: {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Technician.__init__(self, name, id, specialization)
        Manager.__init__(self, name, id, department)
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)
        return f'{self.name} added {employee.name}'

    def get_team_info(self):
        if not self.subordinates:
            return f'{self.name} has no subordinates'

        info = f'Team {self.name} ({len(self.subordinates)} employees)\n'
        for i, emp in enumerate(self.subordinates, 1):
            info += f'{i}. {emp.get_info()}\n'
        return info

    def get_info(self):
        return f'Name: {self.name}, ID: {self.id}, Department: {self.department}, Specialization: {self.specialization}'


# 2
emp1 = Employee("Sashka", 1488)

mgr1 = Manager("Vovka", 501, "DevOps")
print(mgr1.manage_projects('Website'))

tech1 = Technician("Grigory", 198, "Master")
print(tech1.perform_maintenance("Server1"))

tech_mgr1 = TechManager("vladimir", 777, "DevOps", "midle")
print(tech_mgr1.add_employee(emp1))
print(tech_mgr1.get_team_info())

employees = [
    emp1,
    mgr1,
    tech1,
    tech_mgr1,
    Employee("vika", 1004)
]

print("\nInformation about all employees:")
for emp in employees:
    print(f"- {emp.get_info()}")