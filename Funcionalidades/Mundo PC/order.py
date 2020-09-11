from computer import Computer


class Order:
    count = 1

    def __init__(self, computers):
        Order.count += 1
        self.__id_order = Order.count
        self.__computers = computers

    def add_computer(self, computer):

        self.__computers.append(computer)

    def __str__(self):
        computer_str = ''
        for computer in self.__computers:
            computer_str += computer.__str__()

        return (
            f"Order: {self.__id_order}, "
            f"Computers: {computer_str}"
        )

    @property
    def computers(self):
        return self.__computers

    @computers.setter
    def computers(self, computers):
        self.__computers = computers
