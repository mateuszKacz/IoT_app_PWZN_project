## "IoT Manager App"

### Objective

The purpose of this application is to create simple GUI for managing and gathering data from Internet of Things devices.
Main functionality:
1. Gathering temperature data for plugged devices
2. Exporting those data to csv files
3. Mock devices either from list of devices from given file (sample file can be found in _test_files/test_iot_dev.txt_)
, using GUI or script parameter
4. Live temperature graph animation - real-time data displayed in the application window - possibility to change scope 
betweenn devices.

### Installing

To use this package there is a Python 3.7 required with libraries specified in _requirements.txt_.

### Sample run

There are several different approaches:
1. python main.py -n {_int8_} -> initiates app with _n_ > 0 devices (e.g. _'python main.py -n 4'_)
2. python main.py -f {_path_} -> initiates app with devices from file in _path_ (e.g. _'python main.py -f file/devices.txt'_)
3. python main.py -> initiates app with one mock _Device_

Then you can click buttons:
1. _Add device_ -> to add new device (up to 16)
2. _Start recording_ -> to start gathering data
3. _Stop recording_ -> to stop gathering data and to export to file - it is needed to click _Start recording_ button first
4. Stitch between charts using _radio buttons_ in the menu on the left pane.
5. close the app with cross in the corner of the frame. 

### Data

All the data from the simulation is saved in _Exported_data_ directory with version system implemented.

### Tests

There are several test implemented to check integrity of the functions:

_flags_test.py_ -> contains tests of script's parameters that are given by user

Tests performed by The Creator:
1. executing _python main.py_ command -> _add_device_ button click -> _Start recording_ button click -> 
_Stop recording_ button click -> _left pane_ radio button click (switching graph) -> closing the app
2. executing _python main.py -n 4_ command -> _add_device_ button click -> _Start recording_ button click -> 
_Stop recording_ button click -> _left pane_ radio button click (switching graph) -> closing the app
3. executing _python main.py -f test_files/test_iot_dev.txt_ command -> _add_device_ button click -> 
_Start recording_ button click -> _Stop recording_ button click -> _left pane_ radio button click (switching graph) 
-> closing the app
4. executing _python main.py_ command -> _add_device_ button click -> _Start recording_ button click -> 
_Stop recording_ button click -> _left pane_ radio button click (switching graph) -> closing the app
5. executing _python main.py_ command -> _add_device_ button click -> _Start recording_ button click -> 
_Stop recording_ button click -> _Start recording_ button click -> _Stop recording_ button click -> 
_left pane_ radio button click (switching graph) -> closing the app

Tests finished successfully as expected.