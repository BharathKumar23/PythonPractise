#assigning value to types_of_people
types_of_people = 10

# inserting another variable value into the string using f"{}" formating type
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

#By using the f"{}" formating type insert binary and do_not value into the y string
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'") #placing "'" single quotes in the output for y value

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) # using .format(), to get the value of the valriables

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
