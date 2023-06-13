# Document Tracking System

Prerequisites:
- Python
- mysql server running
- Venv activated
- `pip install -r requirements.txt`

## To run:
- export FLASK_APP=main.py  
- flask run


# Deliverables: 
- You will find the ERD diagram in the repo labeled `ERD.png`
- You will find the SQL code in the directory `./db/schema.sql`
- You will find the microservice implemented using flask, following a Clean Architcture consisting of (API, Domain, Repository) layers

# APIs Documentation:

#### Creating new customer

<details>
 <summary><code>POST</code> <code><b>/customers</b></code>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | name      |  required | object (JSON)           | N/A  |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `text/plain;charset=UTF-8`        | `Customer created successfully`                                |
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                            |
> | `405`         | `text/html;charset=utf-8`         | None                                                                |


#### Getting Customer by ID

<details>
 <summary><code>GET</code> <code><b>/customers/{customer_id}</b></code>

##### Parameters

> | name       |  type     | data type               | description                                                           |
> |------------|-----------|-------------------------|-----------------------------------------------------------------------|
> | customer_id|  required | URL Param               | N/A                                                                   |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `application/json`                | `{"customer_id": "968704d9-cc01-4c1c-9fd8-47d961","name":"Mohamed"}`|
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                            |
> | `405`         | `text/html;charset=utf-8`         | None                                                                |


#### Getting Customers

<details>
 <summary><code>GET</code> <code><b>/customers</b></code>

##### Parameters

> | name       |  type     | data type               | description                                                           |
> |------------|-----------|-------------------------|-----------------------------------------------------------------------|


##### Responses

> | http code     | content-type                      | response                                                              |
> |---------------|-----------------------------------|---------------------------------------------------------------------  |
> | `201`         | `application/json`                | `[{"customer_id": "968704d9-cc01-4c1c-9fd8-47d961","name":"Mohamed"}]`|
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                              |
> | `405`         | `text/html;charset=utf-8`         | None                                                                  |

#### Update customer by Id

<details>
 <summary><code>PUT</code> <code><b>/customers/{customer_id}</b></code>

##### Parameters

> | name       |  type     | data type               | description                                                           |
> |------------|-----------|-------------------------|-----------------------------------------------------------------------|
> | name       |  required | object (JSON)           | N/A                                                                   | 
> | customer_id|  required | URL Param               | N/A                                                                   |   


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `text/plain;charset=UTF-8`        | `Customer updated successfully`                                |
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                            |
> | `405`         | `text/html;charset=utf-8`         | None                                                                |


#### Deleting Customer by ID
<details>
 <summary><code>DELETE</code> <code><b>/customers/{customer_id}</b></code>

##### Parameters

> | name       |  type     | data type               | description                                                           |
> |------------|-----------|-------------------------|-----------------------------------------------------------------------|
> | customer_id|  required | URL Param               | N/A                                                                   |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `application/json`                | `Customer deleted successfully`|
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                            |
> | `405`         | `text/html;charset=utf-8`         | None                                                                |


