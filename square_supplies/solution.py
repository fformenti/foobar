def answer(n):

	def aux_f(start, n, min_squares):
		count = 0
		while True:
			if n - start**2 > 0:
				n = n - start**2
				count += 1
			elif n - start**2 < 0:
				start = start - 1
			else:
				count += 1
				return count

			if count >= min_squares:
				return min_squares

	max_coins = n**0.5
	max_coins = int(round(max_coins - 0.5, 0))
	coins_list = reversed(range(1,max_coins+1))
	min_squares = n

	for coin_val in coins_list:
		if (coin_val**2)*min_squares <= n:
			break
		min_squares = aux_f(coin_val, n, min_squares)

	return min_squares


print 'answer: ', answer(200000561)


