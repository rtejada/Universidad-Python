from input_device import InputDevice


class Mouse(InputDevice):

    count = 0

    def __init__(self, brand, entry_type):
        Mouse.count += 1
        super().__init__(brand, entry_type)
        self.__id_mouse = Mouse.count

    def __str__(self):
        return (
            f"ID: {self.__id_mouse}, "
            f"Brand: {self._brand}, "
            f"Entry_type: {self._entry_type}"
        )

#mouse = Mouse('hp', 'usb')
#print(mouse)


