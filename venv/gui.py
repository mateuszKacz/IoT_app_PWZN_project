from tkinter import Label, Button, Radiobutton, Canvas, Frame, StringVar, TOP, LEFT, RIGHT
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation


class GUI(Frame):
    """All the graphic interface gathered here"""

    def __init__(self, root, data, devices):
        super().__init__(root)
        self.root = root
        self.root.geometry('500x400')

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
        self.test_button = Button(self.right_bottom_frame, text='test', relief='groove').pack()

        # IoT devices - menu
        self.devices = devices
        self.iot_dev_name_var = StringVar()
        self.iot_dev_name_var.set(self.devices.list_of_devices[0].serial_number)
        self.radiobutton_iot_dev_1 = Radiobutton(self.left_frame, text=self.devices.list_of_devices[0].serial_number,
                                                 variable=self.iot_dev_name_var,
                                                 value=self.devices.list_of_devices[0].serial_number).pack(fill='both')

        # other objects
        self.data = data
        self.ani = None
        self.main_frame.pack_propagate(0)
        self.root.resizable(0, 0)

    def draw_graph(self):

        self.figure = plt.Figure(figsize=(6,5), dpi=70)
        self.figure.suptitle('Real-time temperature')

        self.ax = self.figure.add_subplot(111)
        self.line = self.ax.plot(self.data.data['Time'], self.data.data['Temp'])

        self.canvas = FigureCanvasTkAgg(self.figure, self.right_top_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=1)
        self.ax.set_ylim(0, 50.)

        self.start()

    def update_graph(self, i):

        self.data.add_data()
        self.ax.plot(self.data.data['Time'], self.data.data['Temp'], color='blue')
        self.ax.set_xlim(max(self.data.data['Time']) - 10, max(self.data.data['Time']) + 10)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Temperature [C]')

        return self.line

    def start(self):

        self.ani = animation.FuncAnimation(
            self.figure,
            self.update_graph,
            frames=1000,
            interval=200,
            repeat=False)

        self.ani._start()

        print('started animation')

    def add_device(self):

        print('Added new device')
        self.devices.add_device()
        Radiobutton(self.left_frame, text=self.devices.list_of_devices[-1].serial_number,
                    variable=self.iot_dev_name_var,
                    value=self.devices.list_of_devices[-1].serial_number).pack(fill='both')



