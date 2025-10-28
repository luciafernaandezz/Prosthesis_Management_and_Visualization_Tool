# Prosthesis_Management_and_Visualization_Tool
First project I completed as part of my bachelor’s degree in Biomedical Engineering

## Project Overview
This program assists in the fabrication of prostheses and features a menu displaying the main functions:

1. Add Prosthesis: The `nuevaProtesis` function allows the user to add new prostheses. The part, subpart, and measurements of required parameters are entered manually.
2. List Prostheses: Displays all prostheses with the required parameters and their measurements.
3. Inventory: Shows the number and types of prostheses to be fabricated.
4. Percentages: Illustrates the inventory data using a pie chart, showing the number of prostheses and their types.
5. Exit: The **program** function integrates all the above features and executes the main program workflow.
0. Introduction  

The **menu** function displays all the main program features, each associated with a number, and stores the selected number. This function has no output.  

The **read** function reads the `protesis.txt` file and creates a dictionary `protesis`, which contains the part, subpart, and measurements of specific parameters. It has no input or output.  

The **save** function stores the entered prosthesis data in the file. This function also has no input or output.

## How to run this program
To successfully run this program, make sure you have the **matplotlib.pyplot** library installed.  
Additionally, you must have the file `protesis.txt` available in the same directory as the program.
