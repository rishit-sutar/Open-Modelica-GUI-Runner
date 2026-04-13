# Open-Modelica-GUI-Runner
 PyQt GUI to run OpenModelica simulations
 # OpenModelica GUI Runner

 📄 Detailed documentation is provided in the attached PDF file:  
`Open Modelica Project Readme.pdf`

A Python + PyQt6 desktop application that runs an OpenModelica-generated simulation from a simple GUI, accepts start and stop time inputs, and displays the simulation result as a graph inside the app.

## Overview

This project is based on the OpenModelica `TwoConnectedTanks` model. The model is compiled in OMEdit to generate simulation output files. A Python GUI is then used to launch the generated OpenModelica simulation from the desktop.

The application lets the user:

- select the generated OpenModelica simulation launcher
- enter start time and stop time
- run the simulation
- view the output graph inside the GUI

## Features

- Browse and select the OpenModelica-generated simulation file
- Enter start time and stop time
- Validate input before running the simulation
- Run the simulation from a desktop GUI
- Detect the generated `.mat` output file
- Plot the result inside the application window

## Technologies Used

- Python 3.6+
- PyQt6
- OpenModelica / OMEdit
- Matplotlib
- SciPy
- NumPy
- Windows 10/11

## Project Structure

```text
Open-Modelica-GUI-Runner/
├── main.py
├── README.md
├── model.zip
├── executables.zip
└── Open Modelica Project Readme.pdf

## Quick Run

```bash
py -3.14 main.py
