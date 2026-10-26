import os

def greet(name):
    print(f"Hello, {name}!")

# Get the current directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# Greet the user
greet("World")

# Print all Python files in the current directory
for file in os.listdir(cwd):
    if file.endswith(".py"):
        print(f" - {file}")   
