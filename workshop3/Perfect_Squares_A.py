# PERFECT_SQUARES
# Author: Catherine Potts
# This code will read from a file and count perfect squares

fileLink = open("rmds_data.csv", 'r')

count_squares = [0]*45;

for line in fileLink:
    num = int(line)
    for i in range(0,len(count_squares)):
        if(i*i == num):
            count_squares[i] = count_squares[i]+1

fileLink.close()

for i in range(0,len(count_squares)):
    print("There are " + str(count_squares[i]) + " times that " + str(i*i) + " occurs in the file.")
