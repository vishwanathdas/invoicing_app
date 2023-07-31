Invoicing App
The Invoicing App is a Django application built using Django Rest Framework to manage invoices and their associated details. It allows users to create, view, and manage invoices and invoice details through a RESTful API.

Features
Create new invoices with details in a single API call.
Retrieve a list of all invoices.
Retrieve details of a specific invoice.
Update existing invoices and their associated details.
Delete invoices.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/invoicing_app.git
Navigate to the project directory:
bash
Copy code
cd invoicing_app
Create and activate a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use "venv\Scripts\activate"
Install the required packages:
Copy code
pip install -r requirements.txt
Usage
Run the migrations to create the database tables:
Copy code
python manage.py migrate
Start the development server:
Copy code
python manage.py runserver
Access the API at http://localhost:8000/.
API Endpoints
GET /invoices/: Get a list of all invoices.
POST /invoices/: Create a new invoice with associated details.
GET /invoices/<invoice_id>/: Get details of a specific invoice.
PUT /invoices/<invoice_id>/: Update details of a specific invoice.
DELETE /invoices/<invoice_id>/: Delete a specific invoice.
JSON Payload Example for Creating an Invoice
json
Copy code
{
  "date": "2023-07-31",
  "invoice_no": "INV123",
  "customer_name": "John Doe",
  "invoice_details": [
    {
      "description": "Product A",
      "quantity": 2,
      "unit_price": 10.00,
      "price": 20.00
    },
    {
      "description": "Product B",
      "quantity": 1,
      "unit_price": 15.00,
      "price": 15.00
    }
  ]
}
Dependencies
Django
Django Rest Framework
Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.