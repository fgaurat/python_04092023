from pprint import pprint
import csv
import json

def main():
    with open("data.json",'r') as jsonfile:
        data = json.load(jsonfile)


    with open('data_fromjson.csv', 'w', newline='') as csvfile:
        fieldnames = data[0.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)





def main_read_json():

    with open("data.json",'r') as jsonfile:
        data = json.load(jsonfile)

        for d in data:
            print(d['first_name'])


def main_write_csv():
    with open('data.csv', 'r', newline='') as csvfile:
        data = list(csv.DictReader(csvfile,))

    with open("data.json",'w') as jsonfile:
        json.dump(data,jsonfile)        



        # for row in reader:
        #     print(row)


def main_01():

    with open("data.csv") as f:
        # s = f.read()
        l = [line.strip() for line in f.readlines()]
        # print(l[1])
        # for line in f:
        #     line = line.strip()
        #     print(line)

        # firstNames = set()
        header = l[0].split(',')
        for line in l[1:]:
            row = line.split(',')
            # print(header)
            # print(row)

            d = dict(zip(header,row))
            print(d)
            # firstNames.add(row[1])
        
        # pprint(len(firstNames))

if __name__=='__main__':
    main()
