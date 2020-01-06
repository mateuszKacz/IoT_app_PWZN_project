
DEVICE_SERIAL_CORE = 'iot-dev-'


class Devices:
    """Class contains main info about devices"""

    def __init__(self):

        self.list_of_devices = [Device((1))]
        self.number_of_devices = 1

    def show_devices(self):

        print(self.list_of_devices)

    def add_device(self):
        self.number_of_devices += 1
        self.list_of_devices.append(Device(self.number_of_devices))

        for device in self.list_of_devices:
            device.info()


class Device:
    """Class cointains info about single device"""

    def __init__(self, number):

        self.serial_number = DEVICE_SERIAL_CORE + str(number)
        self.type = 'Raspberry Pi'

    def info(self):

        print(self.type + '\t' + self.serial_number)
