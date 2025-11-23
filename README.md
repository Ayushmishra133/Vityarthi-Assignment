# Vityarthi-Assignment

Overview

This project is a Python-based program designed to calculate the total shipment cost for multiple items. Users can input shipment item details such as name, cost, and quantity. The program also allows input of additional parameters including handling charges, GST (tax percentage), and discount rules. After processing all inputs, the program computes subtotals, applicable discounts, taxes, and prints a detailed shipment bill

Features

•	Interactive command-line interface to input shipment items (name, cost, quantity).

•	Customizable handling charge, GST percentage, discount thresholds, and discount rates.

•	Automatic calculation of subtotal, discount, GST, and final total cost.
	
•	Uses NumPy for efficient calculations involving multiple items.

•	Detailed summary bill output including per-item cost breakdown and overall totals.
	
•	Built with modular design using separate functions for input, calculations, and output.

Technologies/Tools Used

•	Python: Core programming language for implementing the calculator.

•	NumPy: Library for efficient numerical operations and array calculations.
	
•	datetime: Used to print the current date and time on the bill.
	
•	math: For financial rounding operations

Steps to Install & Run the Project

1.	Install Python (version 3.6 or above) 

2.	Install NumPy package using pip:

Text

3.	Download the source code files.

4.	Run the program from the command line or an IDE like Visual Studio Code

python shipment_calculator.py

5.	Follow the on-screen prompts to input shipment details and parameters

Instructions for Testing

•	Run the program several times with different item entries and quantity values.

•	Also test varying inputs for handling charge, GST percent, and discount rules (including edge cases like zero or negative values which get converted to positive).

•	Confirm that the subtotal, discounts, GST, and final shipment cost calculations are accurate.

•	Validate error handling by entering invalid inputs like non-numeric costs or quantities.

•	Ensure the printed bill details correspond to the inputs and calculations performed.




