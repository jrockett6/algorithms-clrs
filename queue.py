class QueueNode:
	def __init__(self, data):
		self.data = data
		self.tail = None

class Queue:
	def __init__(self):
		self.head = None
		self.end = None

	def enqueue(self, data):
		new_node = QueueNode(data)

		if self.head != None:
			self.end.tail = new_node
		else:
			self.head = new_node

		self.end = new_node

	def dequeue(self):
		if not self.is_empty():
			temp_node = self.head
			self.head = temp_node.tail
			return temp_node.data
		else:
			print('Cannot dequeue an empty queue')

	def is_empty(self):
		return self.head == None

	def __str__(self):
		queue_iterator = self.head
		queue_string = ''

		while queue_iterator != None:
			queue_string += str(queue_iterator.data) + ', '
			queue_iterator = queue_iterator.tail

		return queue_string
