class person:
    def __init__(self,name,years):
        self.name = name
        self.years = years
    def apresentar(self):
        return f"Olá meu nome é {self.name}"