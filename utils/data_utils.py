import csv
import random
import re

def get_item_list(file):
    item_list = []
    with open(file, newline='') as csvfile:
        item_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in item_reader:
            item_list.append(line)

    return item_list

def get_random_element(w_list):
    return random.choice(w_list)

def get_random_item_num(min=1,max=30):
    return random.randint(min,max)

def get_product_id_from_href(href):
    print(href)
    reg=r"product/([\w]+)/ref"
    x=re.search(reg,href)
    return x[1]