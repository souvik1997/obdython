# pyobd - An OBD-II compliant car diagnostic tool

pyobd is designed to interface with low-cost ELM 32x OBD-II diagnostic interfaces. 

pyobd is written in Python, originally written by Donour Sizemore, maintained by SECONS Ltd., and forked and improved upon by Souvik Banerjee. 

## What's new in this fork?

pyobd has been rewritten to work as a Python module. You can now install pyobd and import it in your code. pyobd's GUI and capturing code has been removed and all code has been merged into one file to avoid complications. You can specify a sensor to read by its name instead of its index in the list, and everything has been updated to work with Python 3. 

Example:

    import pyobd
    port=pyobd.OBDPort("/dev/ttyS1")
    print(port.sensor('rpm'))
