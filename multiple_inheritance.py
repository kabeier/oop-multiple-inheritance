# What is Multiple Inheritance?

# Multiple inheritance means a class can inherit from more than one parent class.
class ParentA:
    pass

class ParentB:
    pass


class Child(ParentA, ParentB):
    pass


# Basic Example
class Car:
    def drive(self):
        print("Driving on the road")

class Plane:
    def fly(self):
        print("Flying in the sky")

class FlyingCar(Car, Plane):
    pass


fc = FlyingCar()

fc.drive()  # from Car
fc.fly()    # from Plane


# The Problem: Method Conflicts

# What if both parents define the same method?

class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

class FlyingCar(Car, Plane):
    pass


fc = FlyingCar()
fc.move() #print Driving

# Why? (MRO — Method Resolution Order)

# Python follows a rule called MRO (Method Resolution Order)
# It checks classes left → right.

# So it looks:

# FlyingCar
# Car ✅ (finds move)
# Plane (never reached)

# You can see the order:

print(FlyingCar.__mro__) 
# (<class '__main__.FlyingCar'>, <class '__main__.Car'>, 
# <class '__main__.Plane'>, <class 'object'>)



# Fixing Conflicts (Explicit Override)

# If you want control, define it yourself:
class FlyingCar(Car, Plane):
    def move(self):
        print("Switching modes...")
        Car.move(self)
        Plane.move(self)


# Real World Example 

# Multiple inheritance is often used to compose behaviors, 
# not mix unrelated things.

class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")

class SaveToFile:
    def save(self, data):
        print(f"Saving {data} to file")

class App(Logger, SaveToFile):
    def process(self):
        self.log("Processing started")
        self.save("results")

# Why is this good
# One class = one responsibility
# Combine them in a child

# When NOT to Use It

# Avoid when:

# - Classes are not logically related
# - You get method name conflicts everywhere
# - It becomes confusing to track behavior

# In those cases, prefer composition (objects inside objects).

# Challenge for Students

#  Create a class SmartPhone that inherits from:

# Camera (method: take_photo)
# Phone (method: call)”

# Then call both methods.
class Camera:
    def take_photo(self):
        print("📸 Taking a photo")


class Phone:
    def call(self, number):
        print(f"📞 Calling {number}")

class SmartPhone(Camera, Phone):
    pass

my_phone = SmartPhone()

my_phone.take_photo()     # from Camera
my_phone.call("555-1234") # from Phone


# What if you want to modify the behavoir?
# We can OVERRIDE a method in the child class


class SmartPhone(Camera, Phone):
   
    # This runs FIRST instead of the parent version
    def call(self, number):
        print("📱 Smart dialing...")
        # super() calls the "next" method in the inheritance chain (MRO)
        # In this case, it will call Phone.call(...)
        super().call(number)

my_phone = SmartPhone()
my_phone.call("555-1234")

# ----------------------------------------
# What happens step-by-step:
# ----------------------------------------
# 1. Python looks for call() in SmartPhone → finds it ✅
# 2. Runs SmartPhone.call():
#       prints "📱 Smart dialing..."
# 3. super().call(number) → calls Phone.call()
#       prints "📞 Calling 555-1234"
#
# Final Output:
# 📱 Smart dialing...
# 📞 Calling 555-1234