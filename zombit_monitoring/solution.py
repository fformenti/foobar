def answer(intervals):
	
	watching_hours = 0
	set_of_intervals = set([(intervals[0][0],intervals[0][1])])
	
	for new_interval in intervals[1:len(intervals)]:
		set_to_remove = set()
		change_set_bool = True

		for my_interval in set_of_intervals:
			if (new_interval[0] >= my_interval[0]) and (new_interval[1] <= my_interval[1]):
				change_set_bool = False
				break
			if (new_interval[0] <= my_interval[0]) and (new_interval[1] >= my_interval[1]):
				set_to_remove.add((my_interval[0],my_interval[1]))
			if (new_interval[0] < my_interval[0]) and (new_interval[1] > my_interval[0] and new_interval[1] < my_interval[1]):
				new_interval = [new_interval[0],my_interval[0]]
			if (new_interval[0] > my_interval[0]) and (new_interval[0] < my_interval[1] and new_interval[1] > my_interval[1]):
				new_interval = [my_interval[1],new_interval[1]]

		if change_set_bool:
			# Adding trimmed interval
			set_of_intervals.add((new_interval[0],new_interval[1]))
			# Removing subset intervals
			set_of_intervals = set_of_intervals.difference(set_to_remove)

	for my_interval in set_of_intervals:
		watching_hours += my_interval[1] - my_interval[0]

	return watching_hours