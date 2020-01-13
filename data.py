from pandas import DataFrame
from random import random
from datetime import datetime
from os import mkdir

BASE_T = 20.
RAND_MULT = 10.


class Data:
    """Class where IoT devices data are generated and stored"""

    def __init__(self):

        data_init = {'Time': [1], 'Temp': [self.rand_temp()]}
        self.data = DataFrame(data_init)

        # data exporting
        self.start_recording_index = None
        self.stop_recording_index = None

        # data folder creation
        self.data_dir = 'data_' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        mkdir(self.data_dir)
        self.data_files_count = 0

    @staticmethod
    def rand_temp():

        return BASE_T + random() * RAND_MULT

    def add_data(self):

        self.data = self.data.append({'Time': len(self.data)+1, 'Temp': self.rand_temp()}, ignore_index=True)

    def show_data(self):

        print(self.data)

    def start_recording(self):

        self.start_recording_index = self.data.tail(1).index.tolist()[0]
        print('Data recording - started')

    def stop_recording(self):

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

