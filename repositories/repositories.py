from flask import jsonify
from mysql.connector import Error
from domain.models.customer import Customer


class CustomersRepository:
    def __init__(self, conn):
        self.conn = conn
        
    def get_all_customers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Customers")
            customers = cursor.fetchall()
            cursor.close()
            return [self._create_customer_object(customer) for customer in customers]

        except Error as e:
            raise Exception(f'Error getting customers: {e}')

    def get_customer_by_id(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Customers WHERE customer_id = %s", (customer_id,))
        customer = cursor.fetchone()
        cursor.close()
        return self._create_customer_object(customer) if customer else None

    def create_customer(self, customer):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Customers (customer_id, name) VALUES (%s, %s)",
                        (customer.customer_id, customer.name))
            cursor.close()
        except Error as e:
            raise Exception(f'Error creating customer: {e}')

    def update_customer(self, customer_id, name):
        try:
            customer = self.get_customer_by_id(customer_id)
            if not customer:
                raise Exception(f'Customer does not exist')
            cursor = self.conn.cursor()
            cursor.execute('UPDATE Customers SET name = %s WHERE customer_id = %s', (name, customer_id))
            self.conn.commit()
        except Error as e:
            raise Exception(f'Error updating customer: {e}')

    def delete_customer(self, customer_id):
        try:
            customer = self.get_customer_by_id(customer_id)
            if not customer:
                raise Exception(f'Customer does not exist')
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM Customers WHERE customer_id = %s', (customer_id,))
            self.conn.commit()
        except Error as e:
            raise Exception(f'Error deleting customer: {e}')
        

    def _create_customer_object(self, customer):
        if customer:
            return Customer(customer[0], customer[1])
        return None
        
    
