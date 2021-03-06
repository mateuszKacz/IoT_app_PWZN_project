from pandas import DataFrame
from random import random
from datetime import datetime
from os import mkdir, chdir
import pathlib

BASE_T = 20.
RAND_MULT = 10.

ROOT_PATH = pathlib.Path(__file__).absolute().parent


class Data:
    """Class where IoT devices data are generated and stored. Also data files have implemented simple version system
    based on current date and time.

    :param devices: Devices class object
    :type devices: object
    """

    def __init__(self, devices):

        # data frames init
        self.devices = devices
        self.data = self.data_init()

        # data exporting
        self.start_recording_index = None
        self.stop_recording_index = None

        # data folder creation
        self.data_dir = 'data_' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        self.data_files_count = 0

    def data_init(self):
        """Initiates data frame with mock data"""

        data_init = {'Time': [1]}

        for device in self.devices.list_of_devices:
            data_init[device.data_name] = self.rand_temp()

        return DataFrame(data_init)

    @staticmethod
    def rand_temp():
        """Random temp generator (mock data)"""
        return BASE_T + random() * RAND_MULT

    def add_data(self):
        """Method adds new row to existing data frame (mock data)"""
        append_data = {'Time': len(self.data) + 1}
        for device in self.devices.list_of_devices:

            append_data[device.data_name] = self.rand_temp()

        self.data = self.data.append(append_data, ignore_index=True)

    def show_data(self):
        """Method prints whole dataframe"""
        print(self.data)

    def start_recording(self):
        """Method marks index when recording is started with button push"""
        self.start_recording_index = self.data.tail(1).index.tolist()[0]
        print('Data recording - started')

    def stop_recording(self):
        """Method marks index when recording is stopped by button push and exports specified slice of data to file"""

        if self.start_recording_index is None:
            print('You should start the recording first with -Start recording- button.')
        else:
            try:
                chdir(ROOT_PATH)
                chdir('Exported_data')
            except NotADirectoryError:
                mkdir('Exported_data')
                chdir('Exported_data')
            try:
                mkdir(self.data_dir)
            except FileExistsError:
                pass

            self.stop_recording_index = self.data.tail(1).index.tolist()[0]

            # create slice to export
            data_to_export = self.data.iloc[self.start_recording_index:self.stop_recording_index]

            # new data file
            data_file_path = self.data_dir + '/' + 'data_' + str(self.data_files_count)

            try:
                data_to_export.to_csv(data_file_path)
                self.data_files_count += 1
                print(f'Data recording - stopped ; exported to: {data_file_path}')

            except NotADirectoryError as err:
                print(err)

