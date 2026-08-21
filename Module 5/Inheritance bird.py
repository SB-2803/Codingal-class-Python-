class Bird:
    def __init__(self):
        print("Bird is ready!!")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("Swim faster!!")

class Penguin(Bird):
    def __init__(self):
        print("Penguin is ready!!")
        super().__init__()
    def whoisthis(self):
        super().whoisthis()
        print("Penguin")
    def run(self):
        print("Run faster!!")

peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()