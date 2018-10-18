"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, firstname, lastname, email, password):
    	self.firstname = firstname
    	self.lastname = lastname
    	self.email = email
    	self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {}, {}, {}>".format(self.firstname, self.lastname, self.email)

def read_customerinfo_from_file(filepath):
	"""Read customers from text file and populate dictionary of customers

	Dictionary format is {email: Customer(....), etc.}
	"""

	customer_dictionary = {}

	with open(filepath) as file:
		for line in file:
			(firstname, lastname, email, password) = line.strip().split("|")

			customer_dictionary[email] = Customer(firstname, lastname, email, password)

	return customer_dictionary

def get_by_email(email):
	"""get the customer object via email"""

	return customer_dictionary[email] 

customer_dictionary = read_customerinfo_from_file("customers.txt")