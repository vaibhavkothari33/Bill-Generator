# Bill-Generator
The Python script utilizes the Tkinter library to design a user-friendly bill generator application, streamlining the billing process for businesses such as restaurants or cafes. The graphical user interface (GUI) enhances user interaction by enabling them to input customer details and make selections from the menu .

Bill Generator using Tkinter

This Python script creates a simple bill generator application using the Tkinter library. The application provides a graphical user interface for a billing system commonly found in restaurants or cafes. It allows the user to input customer details, select items from different categories (burgers, pizzas, and shakes), and generates a bill summary.

Key Features

1. **Customer Details Section:**
   - Name, phone number, and a bill number entry fields are provided for the customer.
   - A search button allows users to find previous bills based on the bill number.

2. **Product Selection:**
   - The application includes sections for burgers, pizzas, and shakes, each with specific item entries and quantity input fields.

3. **Bill Area:**
   - A text area is dedicated to displaying the generated bill. It includes details such as the customer's name, phone number, bill number, selected items, quantities, prices, and total amounts.

4. **Tax Calculation:**
   - Taxes are automatically calculated for each category (burgers, pizzas, shakes) and displayed in the bill summary.

5. **Print and Save Functionality:**
   - Users can print the generated bill or save it for future reference.
   - Saved bills are stored in a "bills" directory.

6. **Email Sending:**
   - The application also has an option to send the generated bill via email. The user can input the recipient's email address and add a custom message.

**How to Use:**
   - Enter customer details in the provided fields.
   - Select items and specify quantities.
   - Click the "Total" button to calculate the bill.
   - Review the generated bill in the text area.
   - Optionally, send the bill via email, print it, or save it for record-keeping.

**Note:**
   - Ensure that the script is run in an environment with the required dependencies, particularly Tkinter for the graphical interface.
   - For the mailing button you have to generate a specific password from google via two step verification.
