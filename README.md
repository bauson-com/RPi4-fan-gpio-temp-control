# RPi4-fan-gpio-temp-control

##### Requirements: 
- 1 x Generic USB fan (I bought one from shopee, those ones that says mobile fan)
- 1 x 2N2222 Diode
- 1 x resistor (depending on your fan)

##### Installation:
Clone this repository and execute `install.sh`
```sh
$> git clone https://github.com/RPi4-fan-gpio-temp-control/RPi4-fan-gpio-temp-control.git auto-fan
$> cd auto-fan && ./install.sh && cd .. && rm auto-fan -fr
```

##### Notes
You can update the settings on top of the `fan.py` file if you decided to use a different GPIO/Pin or target temperatures.
````code
pin=12  # this is the Pin12 or GPIO18
max=42  # if the temp is higher than what you have defined here, it will turn on the fan.
min=35  # after reaching this temp, the fan will be turned off.
````

# Diagram
![N|Solid](https://raw.githubusercontent.com/bauson-com/RPi4-fan-gpio-temp-control/master/FAN-TempControl.png)
