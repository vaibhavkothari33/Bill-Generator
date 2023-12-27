
<body>

  <h1>Bill Generator using Tkinter</h1>

  <p>The Python script utilizes the Tkinter library to design a user-friendly bill generator application, streamlining the billing process for businesses such as restaurants or cafes. The graphical user interface (GUI) enhances user interaction by enabling them to input customer details and make selections from the menu.</p>

  <h2>Key Features</h2>

  <ol>
    <li><strong>Customer Details Section:</strong>
      <ul>
        <li>Name, phone number, and a bill number entry fields are provided for the customer.</li>
        <li>A search button allows users to find previous bills based on the bill number.</li>
      </ul>
    </li>
    <li><strong>Product Selection:</strong>
      <ul>
        <li>The application includes sections for burgers, pizzas, and shakes, each with specific item entries and quantity input fields.</li>
      </ul>
    </li>
    <li><strong>Bill Area:</strong>
      <ul>
        <li>A text area is dedicated to displaying the generated bill. It includes details such as the customer's name, phone number, bill number, selected items, quantities, prices, and total amounts.</li>
      </ul>
    </li>
    <li><strong>Tax Calculation:</strong>
      <ul>
        <li>Taxes are automatically calculated for each category (burgers, pizzas, shakes) and displayed in the bill summary.</li>
      </ul>
    </li>
    <li><strong>Print and Save Functionality:</strong>
      <ul>
        <li>Users can print the generated bill or save it for future reference.</li>
        <li>Saved bills are stored in a "bills" directory.</li>
      </ul>
    </li>
    <li><strong>Email Sending:</strong>
      <ul>
        <li>The application also has an option to send the generated bill via email. The user can input the recipient's email address and add a custom message.</li>
      </ul>
    </li>
  </ol>

  <h2>How to Use</h2>

  <ol>
    <li>Enter customer details in the provided fields.</li>
    <li>Select items and specify quantities.</li>
    <li>Click the "Total" button to calculate the bill.</li>
    <li>Review the generated bill in the text area.</li>
    <li>Optionally, send the bill via email, print it, or save it for record-keeping.</li>
  </ol>

  <h2>Note</h2>

  <ul>
    <li>Ensure that the script is run in an environment with the required dependencies, particularly Tkinter for the graphical interface.</li>
    <li>For the mailing button, you have to generate a specific password from Google via two-step verification.</li>
  </ul>

</body>
</html>
