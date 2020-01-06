import pandas as pd
from datetime import datetime as dt
from random import random

BASE_T = 20.
RAND_MULT = 10.


class Data:
    """Class where IoT devices data are generated and stored"""

    def __init__(self):

        data_init = {'Time': [1], 'Temp': [self.rand_temp()]}
        self.data = pd.DataFrame(data_init)

    @staticmethod
    def rand_temp():

        return BASE_T + random() * RAND_MULT

    def add_data(self):

        self.data = self.data.append({'Time': len(self.data)+1, 'Temp': self.rand_temp()}, ignore_index=True)

    def show_data(self):

        print(self.data)








