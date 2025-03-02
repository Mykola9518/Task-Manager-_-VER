class add_title():
    def __init__(self):
        print('Add a task title')
        title_task = str(input())
        self.title=title_task
        print('Title task:' + self.title)
class add_description():
    def __init__(self):
        print('Add a task description')
        description_task = str(input())
        self.description = description_task
        print('Description task:' + self.description)
class deadline():
    def __init__(self):
        from datetime import datetime
        print('Add a deadline')
        print('Please enter the deadline in the following order: \nDate: date of year, date of month, date of day \nTime: time of hours, time of minutes')
        print('Example date and time: 2024-12-15 12:00')
        date_str = str(input())
        date_format = '%Y-%m-%d %H:%M'
        date_obj = datetime.strptime(date_str, date_format)
        self.result = date_obj
        print(f'Date and time of deadline: {self.result}')
add_title_task = add_title()
add_description_task = add_description()
add_deadline = deadline()






