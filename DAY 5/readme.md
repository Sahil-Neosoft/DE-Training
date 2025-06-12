
---

## 🔸 Flask Application Overview

### What Was Implemented

- A **home route (`/`)** displayed an "About" message.
- The **`/index` route** rendered an HTML page (`index.html`) from the templates directory.
- The **`/api/user` endpoint** returned static JSON user data.
- A **greeting endpoint (`/greet`)** responded with a personalized message using a `name` query parameter.
- The **`/employees` route** returned a list of all employees stored in memory.
- The **`/employee/<emp_id>` route** fetched a specific employee by ID.
- The **`/employee` route** accepted a POST request with JSON payload to add a new employee.
- A **search route (`/search`)** filtered employees by department via query parameters.


## ⚡ FastAPI Application Overview

### What Was Implemented

- A **welcome route (`/`)** returned a basic greeting.
- A **user creation endpoint (`/user/`)** accepted a JSON payload with name, age, and email, and returned a confirmation.
- The **`/employee/{emp_id}` route** accepted a path parameter and an optional department filter.
- A **POST endpoint (`/employees`)** registered new employees using Pydantic models to validate incoming data.
- A **GET route (`/employees`)** listed all employees, and also supported filtering by department using query parameters.
- The **`/employee/{emp_id}` route** returned a single employee by ID, with error handling for not found cases.

### Features

- Used **Pydantic** models for type-safe request and response handling.
- Included **automatic documentation** at `/docs` (Swagger UI) and `/redoc`.
- Managed employee data in-memory with an auto-incrementing employee ID.
- Handled errors using FastAPI’s built-in `HTTPException`.

---