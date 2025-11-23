● Problem Statement

The project aims to develop a Python-based Shipment Cost Calculator that accurately computes the total shipment cost based on multiple items' names, costs, and quantities. It incorporates additional parameters such as fixed handling charges, GST (tax), and conditional discounts, to provide a detailed and accurate billing summary

● Scope of the project

The project focuses on enabling users to input various shipment item details, configure extra charges and discounts, and obtain a comprehensive shipment bill. It is designed as a command-line tool emphasizing modularity, user input validation, and efficient numerical computation using libraries like NumPy. It does not include GUI or database features but can be extended for those in future versions.

● Target Users

- Small business owners and logistic coordinators needing quick shipment cost calculations.

- Beginners learning Python programming, especially modular programming and numerical operations.

- Developers looking for a sample project demonstrating best practices in input handling, data processing, and output formatting using Python

● High-level features

- Accepts multiple shipment items including name, unit cost, and quantity.

- Inputs fixed handling charge, GST percentage, discount thresholds from users.

- Validates and sanitizes all user inputs.

- Calculates subtotal, applies discount if conditions are met.

- Calculates GST on the post-discount subtotal plus handling.

- Produces a detailed, well-formatted shipment bill with costs per item and totals.

- Uses NumPy for efficient mathematical computations.

- Modular code structure separating input, processing, and output functionality.
