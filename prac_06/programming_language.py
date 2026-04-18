class ProgrammingLanguage:
    def __init__(self,name = "Java",typing = "Static",reflection = True,year = "1995"):
        self.typing =typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def __str__(self):
        return f"{self.name},{self.typing} Typing,Reflection = {self.reflection},First appeared in {self.year}"

    def is_dynamic(self):
        if self.typing.lower() == "static":
            return False
        else:
            return True