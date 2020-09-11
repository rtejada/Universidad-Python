from input_device import InputDevice


class Keyboard(InputDevice):
    count = 0

    def __init__(self, brand, entry_type):
        Keyboard.count += 1
        super().__init__(brand, entry_type)
        self.__id_key = Keyboard.count

    def __str__(self):

        return (
            f"ID: {self.__id_key}, "
            f"Brand: {self._brand}, "
            f"Entry_type: {self._entry_type}"
        )


#keyboard = Keyboard('hp', 'usb')
#print(keyboard)