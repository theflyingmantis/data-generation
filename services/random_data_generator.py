from random import shuffle
from math import ceil
import csv



def normalise(data):
    print "normalising"
    total = 0.0
    for i in range(0,len(data)):
        total= total+float(data[i])
    for i in range(0,len(data)):
        data[i] = data[i]/ float(total) 
    return data

def save_to_file(ans, OUTPUT_FILE):
    print "started writing to file"
    with open(OUTPUT_FILE, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for val in ans:
            spamwriter.writerow([val])
    print "written to file"

def generate_data(data, number):
    data = normalise(data)
    sum = 0
    for i in range(0,len(data)):
        sum+=data[i]
    ans = []
    for i in range(0,len(data)):
        j = [i] * int(ceil(data[i]*number))
        ans.extend(j)
    ans = ans[:number]
    shuffle(ans)
    return ans

if __name__=="__main__":
    data = [0.11,0.50,0.2,0.25,0.15,0.1,0,0.05,0.05,0.1, 0.4, 0.3, 0.1, 0.9]
    number = 90
    OUTPUT_FILE = "data_generated.csv"
    generate_data(data, number, OUTPUT_FILE)
