'''
WHILE
With the while loop we can execute a set of statements as long as a condition is true.

'''
# BREAK
# With the break statement we can stop the loop even if the while condition is true:

# CONTINUE
# With the continue statement we can stop the current iteration, and continue with the next:

# WHILE ELSE
# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# FOR
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# FOR ELSE
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# PASS
# loop with no content, put in the pass statement to avoid getting an error.