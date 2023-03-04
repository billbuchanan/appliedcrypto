
# Take in the upper limit for the range and store it in a variable
upper = int(input("Enter upper limit: "))

# Let the first for loop range from 2 to the upper limit
for num in range(2, upper + 1):

    # Initialize the count variable to 0
    count = 0

    # Let the second for loop range from 2 to half of the number (excluding 1 and the number itself)
    for i in range(2, (num//2 + 1)):

        # If any number between 2 and half of the number divides it completely then increment count by 1
        if(num % i == 0):
            count = count + 1
            break

    # If count is equal to zero then print that number as it is a prime number
    if (count == 0 and num != 1):
        print(" %d" %num, end = ' ')