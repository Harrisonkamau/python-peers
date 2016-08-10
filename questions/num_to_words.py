"""
Create a function num_to_words() that takes a integer as an argument and returns
its word. E.g num_to_words(2) should print "two" and num_to_words(20) should
return "two zero"
"""


NUM_WORDS = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11:"eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18:"eighteen", 19:"nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def num_to_words(n):
	if n < 0:
		return num_neg(n)
	if n <= 20:
		return NUM_WORDS.get(n)
	else:
		tens, ones = divmod(n, 10)
		return str(NUM_WORDS.get(tens * 10)) + " " +str(NUM_WORDS.get(ones))

# returns negative numbers
def num_neg(n):
	pos = -1 * n
	if pos <= 20:
		return "negative" + " " + NUM_WORDS.get(pos)
	else:
		tens, ones = divmod(pos, 10)
		return "negative"+ " " +str(NUM_WORDS.get(tens * 10)) + " " +str(NUM_WORDS.get(ones))

print(num_to_words(55)) # prints out fifty five
