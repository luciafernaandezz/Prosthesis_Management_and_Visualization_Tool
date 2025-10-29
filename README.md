# Prosthesis_Management_and_Visualization_Tool
This program is designed to assist in prosthesis fabrication planning, manage and visualize prostheses data.
This was the first project I developed during my undergraduate studies, combining programming logic, data structures, and data visualization using `matplotlib`

## Project Overview
This program helps organize and analyze information about different prostheses.
It provides a simple menu interface to:

- **Add Prosthesis**: The `nuevaProtesis` function allows the user to add new prostheses. The part, subpart, and measurements of required parameters are entered manually.
- **List Prostheses**: Displays all prostheses with the required parameters and their measurements.
- **Inventory**: Shows the number and types of prostheses to be fabricated.
- **Percentages**: Illustrates the inventory data using a pie chart, showing the number of prostheses and their types.
- **Exit**: The **program** function integrates all the above features and executes the main program workflow.

The **menu** function displays all the main program features, each associated with a number, and stores the selected number. This function has no output.  

The **read** function reads the `protesis.txt` file and creates a dictionary `protesis`, which contains the part, subpart, and measurements of specific parameters. It has no input or output.  

The **save** function stores the entered prosthesis data in the file. This function also has no input or output.

## How to run this program
- Install and import the library **matplotlib.pyplot**.
- Have the file `protesis.txt` available in the same directory as the program.
