# Hardware Acceleration for AI presentation
## OAK-D cam accelometer

To run this program you need Python version 3.

Install requirements using following command:

```
python3 install_requirements.py
```

Run program using following command:

```
python3 main.py
```

If you get any of these errors

- ```Failed to boot the device: 1.3-ma2480, err code 3```

- ```Failed to find device (ma2480), error message: X_LINK_DEVICE_NOT_FOUND```

-  ```[warning] skipping X_LINK_UNBOOTED device having name "<error>"```

- ```Insufficient permissions to communicate with X_LINK_UNBOOTED device with name "1.1". Make sure udev rules are set```


Use these commands:

1. echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
2. sudo udevadm control --reload-rules && sudo udevadm trigger

Source: https://docs.luxonis.com/en/latest/pages/troubleshooting/
