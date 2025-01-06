<!-- Blockchain Supply Chain Management Application
This is a Flask-based application for managing a blockchain-powered supply chain system. It enables the registration of suppliers, manufacturers, buyers, and their relationships, along with transactions recorded on a blockchain for transparency and security.

Features
Blockchain Visualization:
View the blockchain, including details of transactions such as sender, receiver, amount, timestamp, remarks, and relationship type.

Supply Chain Management:

Add suppliers, manufacturers, and buyers.
Establish relationships between these entities (e.g., Supplier-Manufacturer, Manufacturer-Buyer).
Visualize the supply chain relationships.
Transactions:

Record transactions between entities based on their relationships.
Each transaction is securely stored on a blockchain.
Dynamic Menu:
A user-friendly menu interface to navigate between different functionalities.

Prerequisites
System Requirements:
Python 3.x
MySQL Server
Python Libraries:
Install the required Python packages using the following command:

bash
Copy code
pip install flask flask_sqlalchemy pymysql
Database Configuration:
Ensure that your MySQL server is running and create a database named smart_contract_db. Update the database credentials in main.py if necessary:

python
Copy code
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@127.0.0.1/<database_name>'
Setup and Installation
Clone the Repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Setup Database Tables: Run the application for the first time to create the necessary tables in the database:

bash
Copy code
python main.py
Run the Application: Start the Flask development server:

bash
Copy code
python main.py
Open your browser and navigate to http://127.0.0.1:5000/.

How to Use
1. Home Page (/):
The main menu (menu.html) provides navigation links to the different features of the application.

2. Add Entities:
Navigate to:
/add_suppliers to add suppliers.
/add_manufacturers to add manufacturers.
/add_buyers to add buyers.
Enter the name of the entity and click "Submit" to save it to the database.
3. Manage Relationships:
Navigate to /add_relationship to establish relationships between entities.
Select a source, target, and relationship type, and save the relationship.
4. Record Transactions:
Navigate to /add_transaction to record a transaction between related entities.
Select the relationship, specify the amount and remarks, and submit the transaction.
5. View Blockchain:
Navigate to /view_blockchain to view all transactions recorded on the blockchain.
6. View Supply Chain:
Navigate to /view_supply_chain to view all relationships in the supply chain.
Folder Structure
csharp
Copy code
project/
│
├── static/
│   ├── css/
│   │   └── styles.css       # Application styles
│   └── assets/              # Static assets (if any)
│
├── templates/
│   ├── menu.html            # Main menu
│   ├── view_blockchain.html # Blockchain visualization
│   ├── add_suppliers.html   # Add suppliers
│   ├── add_manufacturers.html # Add manufacturers
│   ├── add_buyers.html      # Add buyers
│   ├── add_relationship.html # Add relationships
│   └── add_transaction.html  # Add transactions
│
├── blockchain.py            # Blockchain logic
├── main.py                  # Flask application
└── README.md                # Documentation
Notes
Ensure the database server is running before starting the application.
All blockchain data is stored in memory (as part of the Blockchain class). For persistence, consider integrating a database or file-based storage.
This application is built for educational and demonstration purposes.
Future Enhancements
Authentication: Add user roles and secure login features.
Blockchain Persistence: Store blockchain data in a database or decentralized ledger.
Enhanced UI: Improve the front-end interface for better usability.
Credits
Developed by: Saad Bin Farrukh
With Gratitude to: Almighty Allah for His guidance and blessings.
License
This project is open-source and available under the MIT License.
 -->