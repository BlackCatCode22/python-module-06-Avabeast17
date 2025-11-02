# sampleClass.py
# A tiny sample class with an attribute and two methods.
# tell python were defining a blueprint for creating objects.
class Greeter:
    def __init__(self, name):
        self.name = name

    def set_name(self, new_name):
        self.name = new_name

    def greet(self):
        print(f"Hello, {self.name}!")
# assign
if __name__ == "__main__":
    g = Greeter("Caprice")
    g.greet()
    g.set_name("Ava")
    g.greet()

