import pandas as pd
import sys
import re
import random
from bs4 import BeautifulSoup
import argparse

def read_and_store_from_csv(file):
    df = pd.read_csv(f'{file}.csv', delimiter=',')
    semester = re.search("\[(\S+)\]", file).group(1)
    ha_number = re.search("-(\d{1,2})", file).group(1)
    for i, row in enumerate(df.values):
        for j in range(0, 3):
            # "unlabled/SoSe21/PPR [SoSe21]-9. Hausaufgabe - Pflichttest C-Antworten"
            with open(f'unlabled/{semester}/HA{ha_number}C-{j}_{i}.c', 'w') as file:
                file.write(row[15+j])


def find_functions(code):
    no_functions = ['if', 'else', 'while', 'for', 'main', 'printf', 'scanf']
    result = []
    for x in code:
        if x == '':
            continue
        tmp = re.search("(\w+)\s*\(", x)
        if tmp == None:
            continue
        function = tmp.group(1)
        tmp = check_similarity(function, no_functions)
        if tmp != '' and result.count(tmp) == 0:
            result.append(tmp)
    return result


def generate_random_string(len):
    random_string = ''
    # Considering only upper and lowercase letters
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
    # Convert to lowercase if the flip bit is on
    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
    # Keep appending random characters using chr(x)
    for _ in range(len):
        random_string += (chr(random_integer))
    return random_string


def rename_functions(source):
    functions = find_functions(source)
    plagiate = []
    random_function_names = []
    for _ in range(len(functions)):
        random_function_names.append(generate_random_string(10))
    for count, i in enumerate(functions):
        for coloum in source:
            plagiate.append(coloum.replace(i, random_function_names[count]))
    return plagiate


def create_plagiate_from_source(file):
    with open(file) as xmlstr:
        soup = BeautifulSoup(xmlstr, 'xml')
        answer_tmp = soup.find('answer').text.split('\n')
        answer = []
        for string in answer_tmp:
            answer.append(string.replace('\t', ''))
        return rename_functions(answer)



# def rename_variables():
# def shift_functions():

def get_given_code(file):
    with open(file) as xmlstr:
        soup = BeautifulSoup(xmlstr, 'xml')
        answerpreload_tmp = soup.find('answerpreload').text.split('\n')
        answerpreload = []
        for string in answerpreload_tmp:
            answerpreload.append(string.replace('\t', ''))
        return answerpreload


def get_student_code(answer_file=str):
    with open(answer_file, 'r') as code:
        result = [x.replace('\n', '').replace('\t', '') for x in code.readlines()]
        return result


def remove_given_code(answer_file, preload_file):
    code = get_student_code(answer_file)
    answerpreload = get_given_code(preload_file)
    result = []
    for i in code:
        similar = check_similarity(i, answerpreload)
        if similar != '':
            result.append(similar)
    return result


#TODO remove slightly adjusted printfs and given lines with random variable name ({{ cr_random.product }})
def check_similarity(elem, list):
    for j in list:
        # print((elem, j))
        if j == elem or elem=='':
            return ''
    return elem


def initialize_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', type=str, help='Source file')
    parser.add_argument('-dest', type=str, help='Destination file')
    return parser.parse_args()


if __name__ == "__main__":
    args = initialize_argparser()
    # print(args.src, args.dest)
    # read_and_store_from_csv(sys.argv[1])
    result = remove_given_code(args.src, args.dest)
    for i in result:
        print(i)
    plagiate = create_plagiate_from_source(args.dest)
    for i in plagiate:
        print(i)
