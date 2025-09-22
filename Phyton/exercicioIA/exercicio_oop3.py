class products:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def totalValue(self):
        return self.price * self.quantity
    def add(self,increment):
        self.quantity += increment
    def remove(self,decrement):
        self.quantity += decrement


product = products(input("digite o nome do produto: ")
                   ,float(input("digite o preco: "))
                   ,int(input("digite a quantidade: ")))

print(product.totalValue())

        