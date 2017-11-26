import csv
from random import shuffle

names = []




def title_name(name):
    individual_names = name.split()
    final_name = ''
    for ind in individual_names:
        final_name=final_name+ind.title()+' '
    final_name = final_name[:-1]
    return final_name


def read_names(NAME_FILE):
    with open(NAME_FILE, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            name = str(row[0])
            name=title_name(name)
            names.append(name)
    return names

def output_names(OUTPUT_FILE):
    with open(OUTPUT_FILE, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for name in names:
            spamwriter.writerow([name])

def shuffler(NAME_FILE,OUTPUT_FILE):
        read_names(NAME_FILE)
        shuffle(names)
        output_names(OUTPUT_FILE)


if __name__ == "__main__":
    NAME_FILE = "names.csv"
    OUTPUT_FILE = "names.csv"
    shuffler(NAME_FILE,OUTPUT_FILE)
