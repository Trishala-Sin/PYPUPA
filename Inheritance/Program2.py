import Employee as employees
import Productivity
import HR as HR

manager = employees.Manager(1,'Balbir',30000)

secretary = employees.Secretary(2,'Reena',2000)

sales_guy = employees.SalesPerson(3,'Jitin',40000,1000)

Factory_worker = employees.FactoryWorker(4,'Devdas',40,200)

employees = [ manager,secretary,sales_guy,Factory_worker]

productivity_system = Productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = HR.PayrollSystem()
payroll_system.calculate_payroll(employees)
