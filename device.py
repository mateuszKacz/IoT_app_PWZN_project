from numpy import genfromtxt

DEVICE_SERIAL_CORE = 'iot-dev-'


class Devices:
    """Class contains main info about devices"""

    def __init__(self, params):
        # imported script parameters
        self.params = params
        # class attributes
        self.list_of_devices = self.create_dev_list()
        self.number_of_devices = len(self.list_of_devices)

    def create_dev_list(self):

        if 'n' in self.params.keys():
            _list_of_devices = [Device(x) for x in range(1, self.params['n'] + 1)]
        elif 'f' in self.params.keys():
            try:
                file_data = genfromtxt(self.params['f'], dtype=[('myint','i8'), ('mystring','S25')], delimiter=',')
                _list_of_devices = [Device(x, name=None) for x, name in file_data]
            except ValueError as err:
                print(err)
                print('Initiating with sample Device')
                _list_of_devices = [Device(1)]
        else:
            _list_of_devices = [Device(1)]

        return _list_of_devices

    def show_devices(self):

        print(self.list_of_devices)

    def add_device(self):

        self.number_of_devices += 1
        new_device = Device(self.number_of_devices)
        self.list_of_devices.append(new_device)

        for device in self.list_of_devices:
            device.info()


class Device:
    """Class cointains info about single device"""

    def __init__(self, number, name=None):

        self.type = 'Raspberry Pi'
        self.serial_number = self.name(number, name)

    @staticmethod
    def name(number, name):

        if name is None:
            serial_number = DEVICE_SERIAL_CORE + str(number)
        else:
            serial_number = name

        return serial_number

    def info(self):

        print(self.type + '\t' + self.serial_number)
