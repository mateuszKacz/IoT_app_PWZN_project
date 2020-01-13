## "IoT Manager App"

### Objective

The purpose of this application is to create simple GUI for managing and gathering data from Internet of Things devices.
Main functionality:
1. Gathering temperature data for plugged devices
2. Exporting those data to csv files
3. Mock devices either from list of devices from given file, using GUI or script parameter
4. Live temperature graph animation - real-time data displayed in the application window - possibility to change scope betweenn devices.

### Installing

To use following package you need following packages with Python 3.7 installed:
_tkinter, pandas, random, datetime, os, numpy, matplotlib_

### Sample run

There are several different approaches:
1. python main.py -n {_int8_} -> initiates app with _n_ > 0 devices (e.g. _'python main.py -n 4'_)
2. python main.py -f {_path_} -> initiates app with devices from file in _path_ (e.g. _'python main.py -f file/devices.txt'_)
3. python main.py -> initiates app with one mock _Device_

