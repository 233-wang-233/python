from abc import ABCMeta,abstractmethod
class Employee(metaclass=ABCMeta):
    '''员工（抽象类）'''
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def get_salary(self):
        '''结算月薪（抽象方法）'''
        pass
class Manger(Employee):
    '''部门经理'''
    def get_salary(self):
        return 15000.0
class Programmer(Employee):
    '''程序员'''
    def __init__(self,name,working_hours=0):
        self.working_hours=working_hours
        super().__init__(name)
    def get_salary(self):
        return 200.0*self.working_hours
class Salesman(Employee):
    '''销售员'''
    def __init__(self,name,sales=0.0):
        self.sales=sales
        super().__init__(name)
    def get_salary(self):
        return 1800.0+self.sales*0.05
class EmployeeFactory():
    '''创建员工工厂'''
    @staticmethod
    def create(emp_type,*arg,**kwargs):
        '''创建员工'''
        emp_type=emp_type.upper()#将小写字母转化为大写字母
        emp=None
        if emp_type=='M':
            emp=Manger(*arg,**kwargs)
        elif emp_type == 'P':
            emp = Programmer(*arg, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*arg, **kwargs)
        return emp
def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print('%s: %.2f元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()