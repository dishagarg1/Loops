# Initialize variables
total = 0
count = 0

# ask user to enter a number continuously and enter -1 to stop 
while True:
    number = int(input("Enter a number (enter -1 to stop): "))
    
    # Check if the entered number is -1 and break the loop if -1 entered
    if number == -1:
        break  
    
    # Add the entered number to the rotal  
    total = total + number  
    # increment in count everytime a number entered
    count = count + 1 

# Calculate the average
# Ensure count is not zero to avoid division by zero error
if count != 0:  
    average = total / count
    print("Average of the numbers entered (excluding -1):", average)
else:
   print("No numbers entered (excluding -1)")
