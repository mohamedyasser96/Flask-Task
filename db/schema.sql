CREATE TABLE Customers (
    customer_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Employees (
    employee_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Receipt (
    receipt_id VARCHAR(255) PRIMARY KEY,
    receipt_date DATE,
    receipt_number VARCHAR(255)
);

CREATE TABLE Document_type_Lookups (
    type_id VARCHAR(255) PRIMARY KEY,
    type VARCHAR(255) NOT NULL
);

CREATE TABLE Document (
    document_id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    author VARCHAR(255),
    creation_date DATE NOT NULL,
    type_id VARCHAR(255) NOT NULL,
    receipt_id VARCHAR(255),
    customer_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (receipt_id) REFERENCES Receipt(receipt_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
  FOREIGN KEY (type_id) REFERENCES Document_type_Lookups(type_id)
);



CREATE TABLE Status (
    status_id VARCHAR(255) PRIMARY KEY,
  	document_id VARCHAR(255),
    employee_id VARCHAR(255),
    mailing_address VARCHAR(255),
    FOREIGN KEY (document_id) REFERENCES Document(document_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)

);


CREATE TABLE Draft (
    draft_id VARCHAR(255) PRIMARY KEY,
    document_id VARCHAR(255) NOT NULL,
  	description TEXT,
    author VARCHAR(255),
    creation_date DATE NOT NULL,
    FOREIGN KEY (document_id) REFERENCES Document(document_id)
);

CREATE TABLE Copy (
    copy_id VARCHAR(255) PRIMARY KEY,
    draft_id VARCHAR(255) NOT NULL,
  	employee_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (draft_id) REFERENCES Draft(draft_id),
  FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

CREATE TABLE CirculationHistory (
  	id VARCHAR(255) PRIMARY KEY,
    document_id VARCHAR(255),
    employee_id VARCHAR(255),
  	circulation_date DATETIME NOT NULL,
    FOREIGN KEY (document_id) REFERENCES Document(document_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

CREATE TABLE DocumentChange (
    change_id VARCHAR(255) PRIMARY KEY,
    document_id VARCHAR(255) NOT NULL,
    employee_id VARCHAR(255) NOT NULL,
    change_date DATETIME NOT NULL,
  	description text,
    FOREIGN KEY (document_id) REFERENCES Document(document_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);


