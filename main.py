# tworzenie i usuwanie urzadzen, dodanie zapisywania do pliku i zbierania (start, stop) danych. - dodać usuwanie 
# dodanie flag '-n 4' -> tworzenie 4 urzadzen fejkowych przy starcie - Done
# dodanie flagi '-f <sciezka do pliku>' dodanie urzadzen z pliku - Done
# Readme.md - cel, instruckja instalacji, przyklad uruchomienia - Done

from tkinter import Tk
from gui import GUI
from data import Data
from device import Devices
from flags import read_flags


def main():

    # flags reading
    params = read_flags()
    # tkinter init
    root = Tk()
    root.geometry("600x400")
    root.title('IoT Manager')
    # devices init
    devices = Devices(params)

    # data gen
    data = Data(devices)

    # gui start
    gui = GUI(root, data, devices)
    gui.draw_graph()

    # main tkinter loop
    root.mainloop()


if __name__ == '__main__':
    main()
