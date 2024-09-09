import csv
import json
import requests
import pandas as pd
from tabulate import tabulate
import pprint
# https://data.lacity.org/resource/2nrs-mtv8.json?area=07

def print_geographic_codes():
    f = open("division_codes.csv")
    csv_f = csv.reader(f)
    print(tabulate(csv_f, headers='firstrow'))
    
def check_area_code(area_code):
    area_code = int(area_code)
    if area_code < 10:
        area_code = str(area_code)
        area_code = '0' + area_code
    return area_code

def get_info(area_code):
    base_url = 'https://data.lacity.org/resource/2nrs-mtv8.json'
    url = base_url + '?area=' + area_code
    response = requests.get(url)
    answer = json.loads(response.text)
    return answer
    
def pretty_print_answer(json_answer, sort=True, indents=4):
    if type(json_answer) is str:
        print(json.dumps(json.loads(json_answer), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_answer, sort_keys=sort, indent=indents))
    return None

def panadas_print():
    with open('data.json', 'r') as file:
        df = pd.DataFrame(json.load(file))
    print(df)
    
def write_json(answer):
    with open('data.json', 'w') as file:
        file.write(json.dumps(answer)) 

def check_choice(choice, function_call):
    choice = choice.lower()
    if choice == 'y':
        write_json()
    else:
        return
    
    
def main():
    
    print_geographic_codes()
    area_code = input("\nArea Code in LA to see crimes in the area (PREC Column): ")
    area_code = check_area_code(area_code)
    answer = get_info(area_code)
    # pretty_print_answer(answer)
    write_json(answer)
    panadas_print()
    
if __name__ == main():
    main();