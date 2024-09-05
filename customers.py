from db import customers, parse_json


def read_all():
    return parse_json(customers.find())


def create(customer):
  
    customers.insert_one(customer)

    return parse_json(customers.find()), 201
