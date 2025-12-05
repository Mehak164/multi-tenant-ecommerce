- Multi-Tenant E-Commerce Backend

This is a multi-tenant e-commerce backend system built using Django, Django REST Framework (DRF), and JWT Authentication.It allows multiple vendors (tenants) to run their stores on a shared backend infrastructure while keeping their data isolated. Each store owner (tenant) can manage their own products, orders, and staff, while customers can view and place orders independently.

1. Tech Stack:
| Layer                 | Technology             |
| --------------------- | ---------------------- |
| Backend               | Django 5.2             |
| API                   | Django REST Framework  |
| Authentication        | JWT (SimpleJWT)        |
| Database              | SQLite + PostgreSQL    |
| Language              | Python 3.11            |
| Deployment            | Render + WhiteNoise    |
| Live Hosting          | Render                 |

2. Roles & Permissions:
| Role         | Access                                           |
| ------------ | ------------------------------------------------ |
|   Owner      | Can manage everything (users, products, orders). |
|   Staff      | Can manage only products and orders.             |
|   Customer   | Can browse products and place orders.            |


3. Multi-Tenancy Implementation:
Each model — User, Product and Order — includes a reference to a Tenant. When users perform any action, the backend automatically filters data for their specific tenant.
queryset = Model.objects.filter(tenant=self.request.user.tenant)
This ensures data isolation between vendors.

4. Authentication System (JWT):
Login tokens are issued using SimpleJWT.
Each token includes:
(json)

{ 
  "tenant_id": 5,
  "role": "owner"
}

This allows the API to identify which tenant and role a user belongs to.

5. API Endpoints:
| Feature         | Method     | Endpoint              | Description                                         |
| --------------- | ---------- | --------------------- | --------------------------------------------------- |
|   Register      | POST       | `/api/auth/register/` | Register a new user and tenant                      |
|   Login         | POST       | `/api/auth/login/`    | Authenticate user & get JWT token                   |
|   Products      | GET / POST | `/api/products/`      | View or create tenant-specific products             |
|   Orders        | GET / POST | `/api/orders/`        | Create or view orders (auto-calculates total price) |
|   Admin Panel   | -          | `/admin/`             | Manage users, tenants, and data                     |

- Register a New User / Store
  POST → /api/auth/register/

Example Request

{
  "username": "rohan",
  "password": "rohan12345",
  "email": "rohan@dreamkart.com",
  "role": "owner",
  "tenant_name": "DreamKart"
}

Response

{
  "username": "rohan",
  "email": "rohan@dreamkart.com",
  "role": "owner"
}

- Login and Get JWT Tokens
  POST → /api/auth/login/

Example Request

{
  "username": "rohan",
  "password": "rohan12345"
}

Response

{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "tenant_id": 5,
  "role": "owner"
}

Use the access token in headers:
Authorization: Bearer <access_token>

- Products API
 GET /api/products/ → View products for your tenant
 POST /api/products/ → Add a new product

Example Request

{
  "name": "Red Saree",
  "description": "Beautiful silk saree with embroidery.",
  "price": 999.99
}

Response

{
  "id": 1,
  "name": "Red Saree",
  "description": "Beautiful silk saree with embroidery.",
  "price": "999.99",
  "tenant": 5,
  "created_by": 8,
  "created_at": "2025-12-05T07:42:00Z"
}

- Orders API
  GET /api/orders/ → List orders
  POST /api/orders/ → Place new order

Example Request

{
  "product": 1,
  "quantity": 2
}

Response

{
  "id": 1,
  "product": 1,
  "quantity": 2,
  "total_price": "1999.98",
  "tenant": 5,
  "customer": 8,
  "created_at": "2025-12-05T08:23:07Z"
}

6. Test Credentials:
|   Role	            |       Username	  |      Password	    |         Email            |
|-----------------------|---------------------|---------------------|--------------------------|
|  Superuser (Admin)	|       Ria	          |      ria12345       |     ria123@gmail.com     |
|  Owner	            |       rohan         |      rohan12345	    |     rohan@dreamkart.com  |
|  Staff	            |       priya	      |      priya12345	    |     priya@dreamkart.com  |
|  Customer	            |       rahul	      |      rahul12345	    |     rahul@dreamkart.com  |
|  owner                |       meena         |      meena12345     |     meena@styleaura.com  |
|  staff	            |       kriti         |      kriti12345     |     kriti@styleaura.com  |

7. Setup Instructions:
- Live Deployment
  Project is live at:https://multi-tenant-ecommerce-4a8e.onrender.com

1️. Clone Repository
   git clone https://github.com/Mehak164/multi-tenant-ecommerce
   cd multi-tenant-ecommerce

2️. Create Virtual Environment
   python -m venv venv
   venv\Scripts\activate

3️. Install Requirements
   pip install -r requirements.txt

4️. Apply Migrations
   python manage.py makemigrations
   python manage.py migrate

5️. Run Server
   python manage.py runserver

Visit: http://127.0.0.1:8000/admin/

8. Deployment Notes
 To deploy to Render:
 - Push all code to GitHub.
 - Connect your repository on Render.
 - Use:
    Build Command: pip install -r requirements.txt
    Start Command: gunicorn core.wsgi:application
 - Add your Render domain to ALLOWED_HOSTS in core/settings.py.

9. Summary of Implementation
- Multi-tenancy implemented using Tenant model
- Role-based user access (Owner, Staff, Customer)
- JWT authentication with tenant_id and role in tokens
- Data isolation by tenant
- CRUD APIs for products and orders
- Auto-calculated total price in orders
- Admin panel for all models

- Contact
  Developer: Mehak Taj
  phone number: 8123314862
  Email: mehaktaj8709@gmail.com

- Final Note
This project implements all assessment requirements using Django, DRF,JWT Authentication and Deployment.
Each tenant (store) operates independently and user roles control access securely.

For AskMeIdentity Backend Developer Assessment – 2025