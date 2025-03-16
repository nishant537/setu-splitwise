# Splitwise Clone

A FastAPI-based expense-sharing application that allows users to manage groups, add expenses, and track balances.

## Features

- User management: Create users, retrieve all users, and get user balances.
- Group management: Create groups, assign users to groups, and get group members.
- Expense management: Add expenses, assign expenses to users/groups, split expenses, and track payment statuses.
- Built using FastAPI, SQLAlchemy, and SQLite.

## How It Works

1. **User Management**:

   - Users are created with a `name`, `username`, and `password`.
   - User balances are calculated by tracking expenses paid and owed.

2. **Group Management**:

   - Groups are created with a `name` and marked as active by default.
   - Users can be assigned to groups, enabling group-based expense tracking.

3. **Expense Management**:

   - Expenses are created by specifying a `payee_id` (the person who paid), `amount`, and `split_type` (`equal`, `percentage`, or `manual`).
   - Expenses can be assigned to individual users or entire groups.
   - Each user’s share is recorded in the `UserExpense` table, and balances are calculated accordingly.

4. **Balance Calculation**:

   - A user’s balance is computed as the difference between what they paid (`credit`) and what they owe (`debit`).

5. **API Access**:

   - The app exposes RESTful endpoints for creating users, groups, expenses, and retrieving balances.
   - Swagger UI is available at `/docs` for easy API testing.

6. **Health Check**:

   - A health check endpoint verifies the database connection.

## Project Structure

```plaintext
.
├── app.py
├── app.db
├── db
│   └── database.py
├── model
│   ├── user_model.py
│   └── group_model.py
├── crud
│   ├── user_crud.py
│   └── group_crud.py
├── module
│   ├── users_module.py
│   ├── groups_module.py
│   └── expenses_module.py
└── html_response_codes.py
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd splitwise-clone
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the environment:
   - Create a `.env` file in the root directory and add the following content:
     ```plaintext
     TOKEN = "bzARDatkDXorjXpd3yiwhz6LAcpAnrGy3agckFpR"
     ```
4. Run the application:
   ```bash
   uvicorn app:app --reload
   ```
5. Access the API docs:
   ```
   http://127.0.0.1:8000/docs
   ```

## API Endpoints

### User Endpoints

- **GET /users/**: Retrieve all users.
- **POST /users/**: Create a new user.
  ```json
  {
    "name": "John Doe",
    "username": "johndoe",
    "password": "1234"
  }
  ```
- **GET /users/get_balance/{user_id}**: Get the balance of a specific user.

### Group Endpoints

- **GET /groups/**: Retrieve all groups.
- **POST /groups/**: Create a new group.
  ```json
  {
    "name": "Trip"
  }
  ```
- **POST /groups/assign_user**: Assign a user to a group.
  ```json
  {
    "user_id": 1,
    "group_id": 2
  }
  ```
- **GET /groups/get_users/{group_id}**: Get all users in a group.

### Expense Endpoints

- **GET /expenses/**: Retrieve all expenses.
- **POST /expenses/**: Create an expense.
  ```json
  {
    "group_id": 1,
    "payee_id": 1,
    "amount": 100,
    "split_type": "equal"
  }
  ```
- **POST /expenses/assign_user**: Assign an expense to a user.
  ```json
  {
    "expense_id": 1,
    "user_id": 2,
    "amount": 50
  }
  ```
- **POST /expenses/assign_group**: Assign an expense to a group.
  ```json
  {
    "expense_id": 1,
    "group_id": 1,
    "amount": 100
  }
  ```
- **PATCH /expenses/pay_expense**: Mark an expense as paid.
  ```json
  {
    "expense_id": 1,
    "user_id": 2
  }
  ```

## Database Schema

- **User**: `id`, `name`, `username`, `password`, `created_at`
- **Group**: `id`, `name`, `active`, `created_at`
- **UserGroup**: `id`, `user_id`, `group_id`, `created_at`
- **Expense**: `id`, `group_id`, `payee_id`, `amount`, `split_type`, `payment_status`, `created_at`
- **UserExpense**: `id`, `expense_id`, `user_id`, `amount`, `payment_status`, `created_at`
Using SQLAlchemy ORM with SQLite for in-repo db control

## Health Check

- **GET /health**: Checks the application's database connection.

## Future Improvements
- Can use Object Oriented Programming by using classes instead of crud apis for every entity
- Better response formatting by using return output functions in html_response_codes.py
- Added features to better clone splitwise
- Packaging application and Docker deployment.
- A BETTER DOCUMENTATION!!