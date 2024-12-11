# 0x02-minimum_operations

This can be done by taking advantange of factors of `n`
if the n is a prime number? then you would have to repeate the operation `n` times

eg: if `n=5` `1 copy AlL + 4 pastes = 5 operations`
Total operations = `p (1CopyAll + (p-1)Pastes`)

If you get the composite number, it can be broken into smaller factors to minimize operations.
eg `n=9` you can break it down to `3 x 3`
you construct 3 "H" characters then you copy paste the group to make 9

Psudo code
1. check if `n` is less or equal to 1
	if true return 0.
2. Declar operations variable as 0
3. Declear divisor to 2
4. Enter a while loop with `n > 1`
5. Enter a second while loop with n % divisor == 0
6. update operation to be divisor + operations
7. update n to `n = n //divisor
8. update divisor by + 1 outside the inner loop
9. Return operation in the outside loop
