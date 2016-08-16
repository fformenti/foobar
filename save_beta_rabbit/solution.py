def answer(food, grid):
    N = len(grid)
    ans_grid = [[set() for i in range(N)] for j in range(N)]
    ans_grid[0][0] = {grid[0][0]}
    for (row, row_val) in enumerate(grid):
        for (col, val) in enumerate(row_val):
            if row != 0:
            	for x in ans_grid[row-1][col]:
	            	if (val + x) <= food:
	            		new_val = val + x
	            		ans_grid[row][col].add(new_val)
            if col != 0:
            	for x in ans_grid[row][col-1]:
            		if (val + x) <= food:
            			new_val = val + x
            			ans_grid[row][col].add(new_val)

    all_ans = sorted(ans_grid[N-1][N-1], reverse=True)

    for el in all_ans:
        if el <= food:
            return food-el
    return - 1