#!/usr/bin/env python3
from department import Department
from employee import Employee

def reset_database():
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

def seed():
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create("Human Resources", "Building C, East Wing")
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)

if __name__ == "__main__":
    reset_database()
    seed()
    try:
        import ipdb; ipdb.set_trace()
    except Exception:
        print("Departments:", Department.get_all())
        print("Employees:", Employee.get_all())
