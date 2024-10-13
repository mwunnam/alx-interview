# 0x09-island_perimeter

## Things to Understand about this question
1. You are given a grid which has these properties
	* 0 Represents water
	* 1 Represents land
	* Cells are connected horizontally and vertical not diagonal
	* You are to find the perimeter of an island which is a group of 1 connected together horizontally or vertically
	* Each land cell(1) has a perimeter of 4 becasue it is a sqare and it has 4 sides.
	* If a cell share boarder with another 2 is subtracted from the cell(adjacent cell is the top and the left side)
	* Only the top and the left will be checked because the bottom and right will be checked in the subsequent iteration.
	* Only land cell at the boarder will be considered meaning if aland cell is surrounded by other land cell it won't be counted as part of the perimeter
