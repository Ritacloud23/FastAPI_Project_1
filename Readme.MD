# FastAPI Projects

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.1xx-009688?logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-black)
![REST API](https://img.shields.io/badge/API-REST-orange)

A collection of beginner-friendly **FastAPI REST API projects** built while learning backend development with Python.

The projects in this repository show my progression from basic API concepts to working with request bodies, Pydantic validation, query parameters, path parameters, filtering, business logic, error handling, and automated testing.

---

## About This Repository

This repository contains a series of FastAPI projects built step-by-step.

Instead of building one large application immediately, I created smaller APIs to understand individual backend concepts and then gradually combined those concepts.

### Learning Progression

```
User Registration
       ↓
Request Bodies + Pydantic
       ↓
Input Validation
       ↓
Product Search
       ↓
Query Parameters + Filtering
       ↓
Payment Processing
       ↓
Business Logic + Custom Validation
       ↓
Vehicle Inventory
       ↓
Path Parameters + Query Parameters
       ↓
Error Handling + Automated Testing
```

### Projects

| Project | Main Concepts |
|---|---|
| User Registration API | POST, Request Body, Pydantic, Validation |
| Product Search API | GET, Query Parameters, Filtering |
| Payment Processing API | Pydantic, Custom Validation, Business Logic |
| Vehicle Inventory API | Path Parameters, Query Parameters, HTTP Errors, Testing |

---

## 1. User Registration API

### Description

The User Registration API is my first FastAPI project.

The goal was to understand how an API receives information from a user and validates that information before processing it.

The API provides a registration endpoint where a user can submit:

- Username
- Email
- Password

The API checks whether the submitted information follows the required rules.

### Endpoint

```
POST /register
```

### Example Request

```json
{
    "username": "rita123",
    "email": "rita@example.com",
    "password": "Password@123"
}
```

### Example Response

```json
{
    "message": "User registered successfully",
    "username": "rita123",
    "email": "rita@example.com"
}
```

### Validation Rules

**Username** must:
- Be at least 3 characters
- Be no more than 20 characters

**Email** must be a valid email address.

**Password** must:
- Contain at least 8 characters
- Contain an uppercase letter
- Contain a lowercase letter
- Contain a number
- Contain a special character

For example, `Password@123` is valid, but `password` is invalid because it does not contain the required uppercase letter, number, and special character.

### Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- FastAPI TestClient

### What I Learned

- How to create a FastAPI application
- How to create POST endpoints
- How request bodies work
- How to create Pydantic models
- How to validate user input
- How to use `Field`
- How to use `EmailStr`
- How to create custom validation with `field_validator`
- How to test API endpoints

---

## 2. Product Search API

### Description

The Product Search API was created to understand GET requests and query parameters.

The API contains a list of products and allows users to search and filter those products.

A user can search by:
- Product name
- Category
- Minimum price
- Maximum price

### Endpoint

```
GET /products
```

**Example 1: Get All Products**
```
GET /products
```
The API returns the available products.

**Example 2: Search by Product Name**
```
GET /products?name=phone
```
The `name` query parameter tells the API which product name to search for.

**Example 3: Search by Category**
```
GET /products?category=electronics
```
This searches for products in the electronics category.

**Example 4: Search by Minimum Price**
```
GET /products?min_price=50000
```
This returns products whose price is greater than or equal to ₦50,000.

**Example 5: Search by Maximum Price**
```
GET /products?max_price=100000
```
This returns products whose price is less than or equal to ₦100,000.

**Example 6: Search Using Multiple Query Parameters**
```
GET /products?category=electronics&min_price=50000&max_price=200000
```
This allows the user to combine filters.

### Simple Explanation

Query parameters are information added to the URL after `?`. For example: `/products?category=electronics`

Here, `category=electronics` is a query parameter.

I understand query parameters as:
> "How do I want to search, filter, or customize the information I receive?"

### What I Learned

- How GET endpoints work
- How query parameters work
- How to validate query parameters
- How to filter data
- How to use optional parameters
- How to use numeric validation
- How multiple query parameters work together

---

## 3. Payment Processing API

### Description

The Payment Processing API was created to practice request validation and business logic.

The API receives payment information and performs validation before simulating payment processing. **This is a learning simulation, not a real payment system.**

### Endpoint

```
POST /payments
```

### Example Request

```json
{
    "amount": 50000,
    "currency": "NGN",
    "card_number": "4111111111111111",
    "expiry": "12/28",
    "cvc": "123"
}
```

### Example Response

```json
{
    "message": "Payment processed successfully",
    "amount": 50000,
    "currency": "NGN"
}
```

### Validation

The API validates information such as:
- Payment amount
- Currency
- Card number
- Expiry date
- CVC

The API rejects invalid information before processing the request.

### Business Logic

After the input passes validation, the application performs simulated payment processing.

```
Client sends payment
        ↓
FastAPI receives request
        ↓
Pydantic validates request
        ↓
Validation successful?
       / \
     Yes  No
      ↓    ↓
Process   Return error
payment
      ↓
Return response
```

###  Important Security Note

This project is only for learning. A real payment application should not store or return raw card details or CVC values. Production payment systems should use secure payment providers, tokenization, encryption, and proper payment security practices.

### What I Learned

- How to work with POST requests
- How to validate payment data
- How to use Pydantic models
- How custom validation works
- How business logic fits inside an API
- How validation protects an API from bad input

---

## 4. Vehicle Inventory API

### Description

The Vehicle Inventory API combines many of the concepts learned from the previous projects.

The API allows users to:
- Get a vehicle by ID
- Search vehicles by make
- Search vehicles by model
- Filter vehicles by minimum price
- Filter vehicles by maximum price
- Combine multiple filters

This project also introduces proper HTTP error handling.

### Vehicle Data

| ID | Make | Model | Price |
|---|---|---|---|
| 1 | Toyota | Camry | ₦20,000,000 |
| 2 | Honda | Accord | ₦18,000,000 |
| 3 | Mercedes | C300 | ₦35,000,000 |
| 4 | Toyota | Corolla | ₦15,000,000 |
| 5 | BMW | X5 | ₦40,000,000 |

### Get Vehicle by ID

**Endpoint**
```
GET /vehicles/{vehicle_id}
```

The `vehicle_id` is a path parameter.

**Example**
```
GET /vehicles/2
```

**Example Response**
```json
{
    "id": 2,
    "make": "Honda",
    "model": "Accord",
    "price": 18000000
}
```

**What is a Path Parameter?**

A path parameter is information placed directly inside the URL path. Example: `/vehicles/2` — here `2` is the vehicle ID.

I understand it as:
> "I want this specific resource."

### Search Vehicles

**Endpoint**
```
GET /vehicles
```

The endpoint uses query parameters to search and filter vehicles.

- **Search by Make:** `GET /vehicles?make=Toyota` — returns Toyota vehicles.
- **Search by Model:** `GET /vehicles?model=Camry` — returns the Toyota Camry.
- **Search by Minimum Price:** `GET /vehicles?min_price=20000000` — returns vehicles costing ₦20,000,000 or more.
- **Search by Maximum Price:** `GET /vehicles?max_price=20000000` — returns vehicles costing ₦20,000,000 or less.
- **Search by Price Range:** `GET /vehicles?min_price=15000000&max_price=20000000` — returns vehicles within the selected price range.
- **Combine Filters:** `GET /vehicles?make=Toyota&model=Camry` — searches for a Toyota Camry.

### Error Handling

If a vehicle does not exist, the API returns `404 Not Found`.

**Example**
```
GET /vehicles/100
```

**Response**
```json
{
    "detail": "Vehicle not found"
}
```

**Invalid Vehicle ID**

If someone sends `GET /vehicles/abc`, FastAPI rejects it because the API expects an integer. The response status will be `422 Unprocessable Entity`.

### Automated Testing

Automated tests were created for the API. The tests check things such as:

- Getting a vehicle successfully
- Vehicle not found
- Invalid vehicle ID
- Searching by make
- Searching by model
- Searching by price
- Multiple query parameters
- Invalid price

**Example Test**
```python
def test_get_vehicle_by_id():
    response = client.get("/vehicles/2")

    assert response.status_code == 200
    assert response.json()["make"] == "Honda"
    assert response.json()["model"] == "Accord"
```

This test checks that requesting vehicle ID 2 returns the expected Honda Accord.

---

## Project Structure

```
FastAPI_Project/
│
├── README.md
│
├── registration_API/
│   ├── main.py
│   └── test_main.py
│
├── product_search_API/
│   ├── main.py
│   └── test_main.py
│
├── payment_processing_API/
│   ├── main.py
│   └── test_main.py
│
└── vehicle_inventory_API/
    ├── main.py
    └── test_main.py
```

### Understanding the Files

Each project contains two main files.

**`main.py`** - This contains the actual FastAPI application. It contains:
- FastAPI app
- Routes
- Validation
- Business logic
- Responses

**`test_main.py`** — This contains automated tests. It checks whether the API behaves as expected.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ritacloud23/FastAPI_Project.git
cd FastAPI_Project
```

### 2. Create a Virtual Environment

If you are using `uv`:

```bash
uv venv
```

Activate it if needed. On Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. Install Dependencies

```bash
uv add fastapi[standard]
```

---

## Running the Projects

Each API can run on a different port. This makes it possible to run multiple APIs at the same time.

### User Registration API

```bash
cd registration_API
uv run uvicorn main:app --reload --port 8000
```

- Swagger: http://127.0.0.1:8000/docs
- OpenAPI: http://127.0.0.1:8000/openapi.json

### Product Search API

```bash
cd product_search_API
uv run uvicorn main:app --reload
```

- Swagger: http://127.0.0.1:8001/docs
- OpenAPI: http://127.0.0.1:8001/openapi.json

### Payment Processing API

```bash
cd payment_processing_API
uv run uvicorn main:app --reload --port 8002
```

- Swagger: http://127.0.0.1:8002/docs
- OpenAPI: http://127.0.0.1:8002/openapi.json

### Vehicle Inventory API

```bash
cd vehicle_inventory_API
uv run uvicorn main:app --reload --port 8003
```

- Swagger: http://127.0.0.1:8003/docs
- OpenAPI: http://127.0.0.1:8003/openapi.json

---

## Swagger UI

FastAPI automatically provides interactive API documentation through Swagger UI. Open `/docs` — for example, http://127.0.0.1:8003/docs

Swagger allows me to:
- See available endpoints
- See request parameters
- Send requests
- See responses
- Test validation
- Test different inputs

## OpenAPI JSON

FastAPI also automatically generates an OpenAPI specification. Open `/openapi.json` — for example, http://127.0.0.1:8003/openapi.json

The OpenAPI document describes the API structure in JSON format. It includes information such as:
- Routes
- HTTP methods
- Parameters
- Request bodies
- Response schemas
- Validation rules

---

## Testing

Tests can be run from inside each project folder.

```bash
pytest
```

or

```bash
uv run pytest
```

A successful test run should show that the tests passed, e.g. `7 passed`. The exact number may change as more tests are added.

---

## Beginner Quick Reference

**GET** - Used mainly for retrieving information.
```
GET /vehicles
```
Think: "Give me information."

**POST** - Used mainly for sending information to the server.
```
POST /register
```
Think: "Here is some information I want you to process."

**Path Parameter** - Information directly inside the URL path.
```
/vehicles/2
```
Think: "I want this specific item."

**Query Parameter** - Information added after `?`.
```
/vehicles?make=Toyota
```
Think: "Search or filter the information this way."

**Request Body** - Information sent inside the request.
```json
{
    "username": "rita123",
    "email": "rita@example.com",
    "password": "Password@123"
}
```
Think: "Here is the data I am sending to the API."

**Pydantic** — Helps FastAPI validate and structure incoming data.
Think: "Check that the information is in the correct format."

**Validation** - Checks whether the data follows the rules. Example: age must be greater than 0. If someone sends `age = -10`, the API rejects it.

### HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created |
| 404 | Resource not found |
| 422 | Validation error |
| 500 | Server error |

---

## Development Workflow

```
1. Understand the assignment
        ↓
2. Identify the endpoint
        ↓
3. Decide the HTTP method
        ↓
4. Identify path/query/body parameters
        ↓
5. Create validation rules
        ↓
6. Write the FastAPI route
        ↓
7. Add business logic
        ↓
8. Run the API
        ↓
9. Test using Swagger
        ↓
10. Write automated tests
        ↓
11. Run Pytest
        ↓
12. Fix errors
        ↓
13. Push the project to GitHub
```

---

## My Learning Journey

These projects represent my progression in backend development.

**Step 1 - User Registration:** POST, Request Body, Pydantic, Validation

**Step 2 - Product Search:** GET, Query Parameters, Filtering, Numeric Validation

**Step 3 - Payment Processing:** Pydantic, Validation, Custom Validation, Business Logic

**Step 4 - Vehicle Inventory:** Path Parameters, Query Parameters, HTTPException, 404 Errors, Automated Testing

---

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- Git
- GitHub
- Swagger UI
- OpenAPI

## Skills Demonstrated

**Backend Development**
- Building REST APIs
- Creating API endpoints
- Handling HTTP requests
- Returning JSON responses

**FastAPI**
- FastAPI application setup
- GET endpoints
- POST endpoints
- Path parameters
- Query parameters
- Request bodies
- HTTPException
- Automatic API documentation

**Pydantic**
- Data models
- Field validation
- Email validation
- Numeric validation
- String validation
- Custom validators

**Testing**
- Pytest
- FastAPI TestClient
- API endpoint testing
- Validation testing
- Error testing

**Development Tools**
- Git
- GitHub
- Uvicorn
- Swagger
- OpenAPI

---

## Limitations

These projects are intentionally simple because they were created as learning exercises. Currently:

- Data is stored in memory
- There is no database
- Authentication is not implemented
- Authorization is not implemented
- Payment processing is simulated
- There are no production payment integrations
- Secrets and environment variables are not required
- The APIs are designed mainly for learning FastAPI concepts

## Future Improvements

As I continue learning backend development, I plan to improve these projects by adding:

- PostgreSQL
- SQLAlchemy
- Database CRUD operations
- Authentication
- JWT
- User authorization
- Environment variables
- Docker
- API versioning
- Better error handling
- Logging
- CI/CD
- AWS deployment
- Monitoring
- Production-ready security

---

## What I Can Now Explain

After building these projects, I can explain the basics of:

- What is an API?
- What is REST?
- What is FastAPI?
- What is an endpoint?
- What is GET?
- What is POST?
- What is a request body?
- What is a path parameter?
- What is a query parameter?
- What is Pydantic?
- What is validation?
- What is HTTPException?
- What are HTTP status codes?
- What is Swagger?
- What is OpenAPI?
- What is automated testing?
- What is Pytest?

--
## Developer

**Rita Nnenna**
Cloud & DevOps | Backend Development | Python | FastAPI

GitHub: [https://github.com/Ritacloud23](https://github.com/Ritacloud23)

---

## Project Philosophy

The purpose of this repository is not just to have code that works. Each project was built to understand a specific backend concept.

```
Learn
  ↓
Build
  ↓
Test
  ↓
Break
  ↓
Debug
  ↓
Understand
  ↓
Improve
```

This repository will continue to grow as I learn more about backend engineering, cloud computing, DevOps, and software development.

## Status

 **Learning in Progress**

These projects are part of my ongoing journey into backend development with Python and FastAPI. More projects and improvements will be added as I continue learning.

## License

This project is licensed under the MIT License.

---

### Thank You

Thank you for taking the time to explore my FastAPI learning repository. I am continuously learning, building, testing, and improving my backend development skills.