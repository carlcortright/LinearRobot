# LinearRobot
Gilroy Lab - University of Wisconsin Madison.

This robot is designed to be an cheap, agile, high-throughput platform for researchers to be able to automatically phenotype plants. 

## Building and Contributing

This project consists of various physical and software components. The design of the robot is largely complete, but there is still a significant amount of work to be completed on integrating the software with the design. 

### Physical design

The physical design consists of a linear platform that slowly moves to set positions where a camera sitting on the platform will take pictures of the target plant. 

All of the design files are in the SolidworksFiles folder along with a parts list.

### Software

The software consists of firmware running on an Arduino Uno with a host computer, running a graphical interface, controlling commanding the movements over a serial connection and communicating with the camera taking pictures of the plants. 

The firmware is written in C++ and the GUI is written in python using the Tkinter library. 

### Where we need contribution
-Python multithreading to prevent the user interface from freezing while the robot is moving
-Interfacing the cannon API with the camera (C#)

More information on both the GUI and firmware is in the readme's for those folders respectively. 



