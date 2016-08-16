
def answer(x):
	if isinstance(x, int):
		x_string = str(x)
		if len(x_string) > 1:
			result = 0
			for c in x_string:
				result +=  int(c)
			return answer(result)
		else:
			return x
	else:
		print 'input error'