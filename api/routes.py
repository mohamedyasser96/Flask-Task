from flask import request, jsonify
from repositories.repositories import CustomersRepository
from domain.models.customer import Customer
import uuid


def register_routes(app, conn):
    customers_repo = CustomersRepository(conn)
    @app.route('/customers', methods=['GET'])
    def get_customers():
        try:
            customers = customers_repo.get_all_customers()
            customers_data = [customer.__dict__ for customer in customers]
            return jsonify(customers_data)
        except Exception as e:
            return jsonify({'error': str(e)})

    @app.route('/customers/<string:customer_id>', methods=['GET'])
    def get_customer_by_id(customer_id):
        try:
            customer = customers_repo.get_customer_by_id(customer_id)
            if customer:
                return jsonify(customer.__dict__), 200
            else:
                return jsonify({'error': 'Customer not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    @app.route('/customers', methods=['POST'])
    def create_customer():
        try:
            customer_id = str(uuid.uuid4())
            name = request.json['name']
            if name == "":
                return jsonify({'error': str("Missing customer name")}), 400
            customer = Customer(customer_id, name)
            customers_repo.create_customer(customer)
            return jsonify({'message': 'Customer created successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/customers/<string:customer_id>', methods=['PUT'])
    def update_customer(customer_id):
        try:
            name = request.json['name']
            if name == "":
                return jsonify({'error': str("Missing customer name to be updated")}), 400
            customers_repo.update_customer(customer_id, name)
            return jsonify({'message': 'Customer updated successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})

    @app.route('/customers/<string:customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        try:
            customers_repo.delete_customer(customer_id)
            return jsonify({'message': 'Customer deleted successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})
