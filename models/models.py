from framework.models import Model

class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    @classmethod
    def get_by_id(cls, id):
        plant_dict = super().get_by_id(id)
        cls.print_object([plant_dict])
        get_employees_by_plant = Employee.get_data()
        print('The following workers work at this plant: ')
        for gebp in get_employees_by_plant:
            if gebp['type_of_work'] == 'plant' and gebp['object_id'] == str(plant_dict['id']):
                print(gebp['name'])
                break

    @classmethod
    def get_by_id_site(cls, id):
        plant_dict = super().get_by_id(id)
        get_employees_by_plant = Employee.get_data()
        new_list = []
        for gebp in get_employees_by_plant:
            if gebp['type_of_work'] == 'plant' and gebp['object_id'] == str(plant_dict['id']):
                new_list.append(gebp['name'])
        return new_list

    @classmethod
    def get_plant_by_id_site(cls, id):
        plant_dict = super().get_by_id(id)
        return plant_dict


    def _protected_example(self):
        return 'protected'

    def __private_example(self):
        return 'private'

class Employee(Model):

    file = "employees.json"

    def __init__(self, name, object_id, type_of_work):
        self.name = name
        self.object_id = object_id
        self.type_of_work = type_of_work

    def get_work(self):
        # Витягуєм данні про роботу
        if self.type_of_work == 'plant':
            return Plant.get_by_id(self.object_id)
        elif self.type_of_work == 'salon':
            return Salon.get_by_id(self.object_id)
        else:
            return {}

    @classmethod
    def get_by_id(cls, id):
        # Викликаєм батьківський метод get_by_id (get_by_id з класу Model)
        employee_dict = super().get_by_id(id)
        employee = Employee(employee_dict['name'], int(employee_dict['object_id']), employee_dict['type_of_work'])
        work_of_employee = employee.get_work()
        cls.print_object([employee_dict])
        # try:
        #     cls.print_object([employee_dict])
        # except:
        #     print('Ops, thomething is wrong...')
        print('Employee work: ')
        cls.print_object([work_of_employee])

    # @classmethod
    # def get_all_employee_ps(cls, temp):
    #     data = cls.get_data()
    #     if len(data) > 0:
    #         flag = 0
    #         for el in data:
    #             if el['type_of_work'] == temp:
    #                 flag += 1
    #                 print(el['name'])
    #         if flag == 0:
    #             print('Nobody work in ' + temp)
    #     else:
    #         print('Sorry, but we do not have employees :(')

class Salon(Model):
    file = 'salon.json'

    def __init__(self, name, address, size):
        self.name = name
        self.address = address
        self.size = size

    @classmethod
    def get_by_id(cls, id):
        salon_dict = super().get_by_id(id)
        cls.print_object([salon_dict])
        get_employees_by_salon = Employee.get_data()
        print('The following workers work at this salon: ')
        for gebs in get_employees_by_salon:
            if gebs['type_of_work'] == 'salon' and gebs['object_id'] == str(salon_dict['id']):
                print(gebs['name'])
                break
#<----------------------------------------------------------->
    # @classmethod
    # def get_data(cls):
    #     file = open('database/' + cls.file, 'r')
    #     data_in_json = file.read()
    #     data = json.loads(data_in_json)
    #     file.close()
    #     return data
    #
    # @classmethod
    # def get_all_employees(cls):
    #     data = cls.get_data()
    #     for employee in data:
    #         print(employee['name'])
    #         print(employee['plant_id'])
    #
    # @classmethod
    # def get_by_id(cls, id):
    #     data = cls.get_data()
    #     count = 0
    #     for employee in data:
    #         if id == employee['id']:
    #             print(employee['name'])
    #             print(employee['plant_id'])
    #             break
    #         count += 1
    #         if count == len(data):
    #             print('Not found employee with this Id')
    #
    # def save(self):
    #     data = self.get_data()
    #     new_employee = {'name': self.name, 'plant_id': self.plant_id}
    #     if len(data) > 0:
    #         new_employee['id'] = data[-1]['id'] + 1
    #     else:
    #         new_employee['id'] = 1
    #     data.append(new_employee)
    #     file = open('database/' + self.file, 'w')
    #     data_in_json = json.dumps(data)
    #     file.write(data_in_json)



