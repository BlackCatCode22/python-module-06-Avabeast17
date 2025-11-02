# lifecycle.py
# define the class here
class Counter:
    def __init__(self):
        self.x = 0
        print("constructed starting x =", self.x)

    def bump(self):
        self.x += 1
        print("So far:", self.x)

    def __del__(self):
        # called automatically when the object is about to be destroyed
        print("Destructed with x =", self.x)

if __name__ == "__main__":
    a = Counter()
    a.bump()
    a.bump()
    # overwrite reference so object can be cleaned up
    a = 42
