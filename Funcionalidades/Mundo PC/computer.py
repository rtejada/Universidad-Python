from monitor import Monitor
from keyboard import Keyboard
from mouse import Mouse

class Computer:
    count = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.count += 1
        self.__id_computer = Computer.count
        self.__name = name
        self.__monitor = monitor
        self.__keyboard = keyboard
        self.__mouse = mouse

    def __str__(self):
        return (
            f"""
            {self.__name}: {self.__id_computer}
                Monitor: {self.__monitor}
                Keyboard: {self.__keyboard}
                Mouse: {self.__mouse}
             """
        )


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def monitor(self):
        return self.__monitor

    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor

    @property
    def keyboard(self):
        return self.__keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self.__keyboard = keyboard

    @property
    def mouse(self):
        return self.__mouse

    @mouse.setter
    def mouse(self, mouse):
        self.__mouse = mouse
        

#monitor = Monitor("HP", "20 Pulgadas")
#Keyboard = Keyboard("HP", "USB")
#mouse = Mouse("HP", "USB")
#computer = Computer('Hp', monitor, Keyboard, mouse)
#print(computer)
