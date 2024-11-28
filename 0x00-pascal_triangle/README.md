# Pascal Triangle

## Psuedocode
1. Prototype = `def pascal_triangle(n)`
you and assume that n will alway be an integer
2. If `n` is <= 0 return
3. Create an empty list which will represent the triangle
4. Set the first elemet of the list in every row which will always be 1
`row = [1]`
5. In a for loop using `n`, iterate of it
* Check if triangle empty or no, if empty append row and that will be the first row of the triangle.
* Get the last row of the triange `last_row = triangel[-1]`
* In a second loop using `len(last_row) - 1` as the range
* Use extend to add other members of the new row to row which has be declared as `row = [1]`
* `row.extend([last_row[j] + last_row[j + 1]])`
* Now append 1 to row to get the last element which will also be 1 row.append(1)
* Append row to triangle to update it `triangle.append(row)`
* Return triangle
