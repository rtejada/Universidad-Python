from order import Order
from computer import Computer
from monitor import Monitor
from mouse import Mouse
from keyboard import Keyboard


keyboard_hp = Keyboard("HP", "USB")
mouse_hp = Mouse("HP", "USB")
monitor_hp = Monitor("HP", "50 pulgadas")
computer_hp = Computer("HP", monitor_hp, keyboard_hp, mouse_hp)

keyboard_acer = Keyboard("ACER", "USB")
mouse_acer = Mouse("ACER", "USB")
monitor_acer = Monitor("ACER", "27 pulgadas")
computer_acer = Computer("ACER", monitor_acer, keyboard_acer, mouse_acer)

keyboard_gamer = Keyboard("GAMER", "USB")
mouse_gamer = Mouse("GAMER", "USB")
monitor_gamer = Monitor("GAMER", "47 pulgadas")
computer_gamer = Computer("GAMER", monitor_gamer, keyboard_gamer, mouse_gamer)

computer = Computer("ARMADA", monitor_hp, keyboard_acer, mouse_gamer)

computers = [computer_acer, computer_hp]
order1 = Order(computers)
order1.add_computer(computer_gamer)
print(order1)
computers1 = [computer_gamer, computer, computer_acer]
order2 = Order(computers1)
order2.add_computer(computer_hp)

print(order2)