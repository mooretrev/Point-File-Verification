import logging

class Log:
	def __init__(self):
		logging.basicConfig(filename='point.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

	def cont_person(self, person):
		logging.debug("Continuing with {}".format(person))

	def move_person(self, person):
		logging.debug("Move to {}".format(person))