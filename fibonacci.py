import time

def fibonacci(numbers):
	'''
		Fibonacci sequence
		Use: fibonacci('1, 1, 2')
	'''
	# Splitting the numbers and converting them to integers
	numbers = numbers.split(', ')
	numbers = map(int, numbers)
	# Now print that list
	for sequence in numbers:
		print sequence
	# And create the first sequence
	sequence = numbers[-2] + numbers[-1]
	# Then, append and print!
	numbers.append(sequence)
	print sequence
	# Finally, loop and groove!
	while sequence >= numbers[-1]:
		sequence = numbers[-2] + numbers[-1]
		numbers.append(sequence)
		time.sleep(2)
		print sequence