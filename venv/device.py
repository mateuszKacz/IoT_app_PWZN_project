
from numpy import genfromtxt

# tworzenie i usuwanie urzadzen, dodanie zapisywania do pliku i zbierania (start, stop) danych.
# dodanie flag '-n 4' -> tworzenie 4 urzadzen fejkowych przy starcie
# dodanie flagi '-f <sciezka do pliku>' dodanie urzadzen z pliku
# Readme.md - cel, instruckja instalacji, przyklad uruchomienia

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
            file_data = genfromtxt(self.params['f'], delimeter=',')
            _list_of_devices = [Device(x, name=name) for x, name in file_data]
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
