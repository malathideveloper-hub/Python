# Task : 1 (Easy)

#Create a class name "Book"
# Create a constructor which will take 3 parameters (title, author, price )
# Add a method called apply discount which will take a percentage as input and apply the discount to the price of the book and return the discounted price.
# Craate few books objects and apply the discount method to see the discounted price.

class Book:
    
    #contructor
    def __init__(self,title, author, price):
        self.title=title
        self.author=author
        self.price=price
        
    def applyDiscount(self, percentage):
        discount_amount = (percentage / 100) * self.price
        discounted_price = self.price - discount_amount
        print(f"Original price of '{self.title}' by {self.author}: ${self.price}")
        print(f"Discounted price after applying {percentage}% discount: ${discounted_price}")
        
bkobj1=Book("HarryPotter","J. K. Rowling",500)
bkobj2=Book("sherlock holmes","Arthur",600)
bkobj1.applyDiscount(10)

# Output:
# -------
# Original price of 'HarryPotter' by J. K. Rowling: $500
# Discounted price after applying 10% discount: $450.0