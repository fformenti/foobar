def answer(population, x, y, strength):
	import itertools

	Z = {(x,y)}
	x_domain = range(0,len(population[0]))
	y_domain = range(len(population))
	domain = set(itertools.product(x_domain,y_domain))

	while len(Z) > 0:
		rabbit = Z.pop()
		x = rabbit[0]
		y = rabbit[1]
		domain.remove(rabbit)
		if strength >= population[y][x]:
			population[y][x] = -1
			neighboors = set([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
			neighboors = neighboors.intersection(domain)
			Z = Z.union(neighboors)

	return population