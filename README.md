# stepper controls

This repository will contain the file for controlling stepper motors using a Raspberry pi GPIO and TB6560 drivers

|program|function|
|---|---|
|[clk_signal.py](https://github.com/kelvinutp/stepper-control/blob/main/clock_signal.py)|Generates a constant frequency clock signal (square wave)|
|[only_motors_control.py](https://github.com/kelvinutp/stepper-control/blob/main/only_motors_control.py)|Allows for controlling individual Enable (start/stop) and Direction (changes direction) pin on driver|
|[auto_moving.py](https://github.com/kelvinutp/stepper-control/blob/main/auto_moving.py)|Makes a motor moves repeteadly in prestablished timed sequences|
|[variador.py](https://github.com/kelvinutp/stepper-control/blob/main/variaddor.py)|enables the stepmotor for a soft start and a soft stop by gradually increasing and decreaseing th efrequency|
|[class.py](https://github.com/kelvinutp/stepper-control/blob/main/class.py)|A programmed class that provides all the functionalities for controlling a stepmotor|
|[Django files](https://github.com/kelvinutp/stepper-control/tree/main/django%20files)|a Django project created for providing a sort of UI capable of doing almost everything that is done by code|
