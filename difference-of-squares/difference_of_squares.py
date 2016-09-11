def square_of_sum(n):
	
	a = sum(range(1, n+1)) ** 2
	return a


def sum_of_squares(n):
	
	a = sum([i**2 for i in range(1, n+1)])
	return a


def difference(n):

	a = square_of_sum(n) - sum_of_squares(n)
	return a
