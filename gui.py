from tkinter import Button, Radiobutton, Frame, StringVar, TOP, LEFT, RIGHT
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from styles import Styles
from random import choice

GRAPH_MEASURE = 'Temp_'


class GUI(Frame):
    """All the graphic interface connected gathered here

    :param root: Tkinter root object for the main window
    :type root: object
    :param data: Data class object
    :type data: object
    :param devices: Devices class object
    :type devices: object
    """

    def __init__(self, root, data, devices):
        """Method initiates GUI and all it's main components"""
        super().__init__(root)
        self.root = root
        self.root.geometry('500x400')
        self.styles = Styles()

        # make GUI
        self.main_frame = Frame(self.root, height=400, width=500)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack()
        self.left_frame = Frame(self.main_frame, relief='groove', bd=3, height=400, width=100)
        self.right_frame = Frame(self.main_frame, relief='groove', bd=3, height=400, width=500)
        self.right_top_frame = Frame(self.right_frame, relief='groove', bd=1, height=200, width=350)
        self.right_bottom_frame = Frame(self.right_frame, relief='groove', bd=1, height=200, width=350)
        self.left_frame.pack(anchor='n', side=LEFT, fill='x')
        self.right_frame.pack(anchor='n', side=RIGHT)
        self.right_top_frame.pack()
        self.right_bottom_frame.pack()
        self.button_add_device = Button(self.left_frame, text='Add Device', relief='groove',
                                        command=self.add_device).pack(side=TOP, expand=True, fill='x')
        # data export
        self.data = data
        self.start_recording_button = Button(self.right_bottom_frame, text='Start Recording', relief='groove',
                                             command=self.start_recording).pack(side=LEFT)
        self.stop_recording_button = Button(self.right_bottom_frame, text='Stop Recording', relief='groove',
                                            command=self.stop_recording).pack()

        # IoT devices - menu
        self.devices = devices
        self.iot_dev_name_var = StringVar()
        self.iot_dev_name_var.set(self.devices.list_of_devices[0].serial_number)
        self.iot_dev_name_var.trace('w', lambda *pargs: self.callback_iot_dev_name_var())
        self.radio_buttons_init()
        # other objects
        self.ani = None
        self.main_frame.pack_propagate(0)
        self.root.resizable(0, 0)

    def draw_graph(self):
        """Method draws a graph from data gathered in Data-type object"""
        self.figure = plt.Figure(figsize=(6,5), dpi=70)
        self.figure.suptitle('Real-time temperature')

        self.ax = self.figure.add_subplot(111)
        self.line = self.ax.plot(self.data.data['Time'], self.data.data[self.devices.list_of_devices[0].data_name])

        self.canvas = FigureCanvasTkAgg(self.figure, self.right_top_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=1)
        self.ax.set_ylim(0, 50.)

        self.start()

    def update_graph(self, i):
        """Method updates created graph"""
        self.data.add_data()

        self.ax.plot(self.data.data['Time'], self.data.data[GRAPH_MEASURE + self.iot_dev_name_var.get()],
                     color=self.styles.graph_color)
        self.ax.set_xlim(max(self.data.data['Time']) - 10, max(self.data.data['Time']) + 10)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Temperature [C]')

        return self.line

    def start(self):
        """Method starts animation of matplotlib's graph"""
        self.ani = animation.FuncAnimation(
            self.figure,
            self.update_graph,
            frames=10000,
            interval=200,
            repeat=False)

        self.ani._start()

        print('started animation')

    def add_device(self):
        """Method adds device to the list in Devices class and adds Radiobutton associated with it"""
        if self.devices.number_of_devices < 16:
            self.devices.add_device()
            Radiobutton(self.left_frame, text=self.devices.list_of_devices[-1].serial_number,
                        variable=self.iot_dev_name_var,
                        value=self.devices.list_of_devices[-1].serial_number).pack(fill='both')
        else:
            print('To many devices!')

    def radio_buttons_init(self):
        """Creates as many as class Devices contains in list_of_devices"""
        for dev in self.devices.list_of_devices:
            Radiobutton(self.left_frame, text=dev.serial_number, variable=self.iot_dev_name_var,
                        value=dev.serial_number).pack(fill='both')

    def start_recording(self):
        """Start recording data to export using Data class method"""
        self.data.start_recording()

    def stop_recording(self):
        """Stops recording data and exports using Data class method"""
        self.data.stop_recording()

    def callback_iot_dev_name_var(self):
        """Clears the graph and sets new color on Radiobutton(devices menu) value change"""
        self.styles.graph_color = choice(self.styles.colors)
        self.ax.clear()
