class Timer:
    def __init__(self,seconds):
      self.seconds = seconds

    def set_time(self,sec):
       self.seconds = sec

    def get_time(self):
       return f"{self.seconds//60}:{self.seconds%60}"

t = Timer(20)

print(t.get_time())
t.set_time(100)
print(t.get_time())
        