import pyautogui
import time

class commands:
    def __init__(self):
        self.tryclick = []
        self.lmx = 0
        self.lmy = 0
    def input_commands(self):
        while True:
            try:
                self.tryclick.append(input())
            except EOFError:
                break
    def execute(self):
        while True:
            time.sleep(4)
            z = 0
            for i in self.tryclick:
                z+=1
                mousemovement = i.split()
                mx = int(mousemovement[0])
                my = int(mousemovement[1])
                time.sleep(1)
                if(mx != 0 and my != 0 and mx != self.lmx and my != self.lmy ):
                    pyautogui.click(mx,my)
                    print(z,mx,my)
                    self.lmx = mx
                    self.lmy = my

def test():
    test_commands = commands()
    test_commands.input_commands()
    test_commands.execute()
