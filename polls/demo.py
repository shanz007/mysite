# Slicing

b = "Hello, World!"
print(b[2:5])

print(b[:5])  # slice from the start
print(b[2:])  # slice from the end
a = "Hello, World!"
print(a.upper())

print(a.strip()) # returns "Hello, World!"

print(a.replace("H", "J"))

print(a.split(",")) # returns ['Hello', ' World!']

# formatting
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# escape characters
txt = "We are the so-called \"Vikings\" from the north."

# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# evaluate  a boolean
  print(bool("Hello"))
  print(bool(15))


# function return a boolean values
  def myFunction():
      return True


  print(myFunction())


# to check instance type
  x = 200
  print(isinstance(x, int))