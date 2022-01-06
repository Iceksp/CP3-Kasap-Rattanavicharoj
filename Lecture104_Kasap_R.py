class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Kasap"
customer1.lastName = "R"
customer1.age = 18
customer1.addCart()

customer2 = Customer()
customer2.name = "Gluy"
customer2.lastName = "A"
customer2.age = 16
customer2.addCart()

customer3 = Customer()
customer3.name = "Lucas"
customer3.lastName = "N"
customer3.age = 20
customer3.addCart()