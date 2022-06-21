#전역변수
str = "Not Class Member"

#클래스 정의
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)

g = GString()
g.set("First Message")
g.print()
