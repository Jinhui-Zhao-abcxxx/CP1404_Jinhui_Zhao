import datetime

class Project:
    def __init__(self, name = "", start_date = datetime.datetime.strptime("1/1/2000", "%d/%m/%Y").date(),priority = 0, cost = 0.0, completion_percentage = 0.0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percent = completion_percentage

    def __str__(self):
        return f"{self.name}    {self.start_date}  {self.priority}  {self.cost} {self.percent} "

    def __lt__(self,other):
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.name},{self.start_date},{self.priority},{self.cost},{self.percent}"

    def show_project_info(self):
        print(f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost}, completion: {self.percent}%")

    def is_completed(self):
        if self.percent == 100:
            return True
        else:
            return False