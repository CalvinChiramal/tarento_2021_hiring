# - Accept a String input
# - Accept a search String to search in the above input
# - Verify if the search String is present in the input string and the position and number of occurrences
# Eg. If the String input is - I like reading about threading
# and the search String is read
# then the output should be as below
# Occurrences - 2
# Position - 8,24

string = input()
substr = input()
#Stores all the positions
positions = []
# start tells from which part of string to start searching from [starts with beginning i.e 0]
# count gives number of occurrences
start, count = 0, 0


while(start < len(string)):
    ind = string[ start:len(string) ].find(substr)
    # If substring not found break the loop
    if(ind == -1):
        break  
    # ind gives position of substr in the substring 'string[start:len(string)]'
    # to get the position with respect to original string we add the number of
    # characters we didn't include in substring i.e 'start' and add to positions
    positions.append(ind + start)
    # now modify 'start' to the substring after the occurrence was found to search
    # in remaining part of string. Once 'start' exceeds string length exit loop
    start = ind + start + 1
    count+=1

# prints the results
print("occurences:", count)
print("positions:", end = '')
for i in positions:
    print("",i, end = '')
print()