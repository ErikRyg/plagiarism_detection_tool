import pandas as pd
import sys
import re
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
        if tmp != '':
            result.append(tmp)
    return result


# def rename_function():
# def rename_variables():
# def shift_functions():

def get_given_code(file):
    with open(file) as xmlstr:
        soup = BeautifulSoup(xmlstr, 'xml')
        answerpreload = soup.find('answerpreload').text
        return answerpreload.split('\n')


def get_student_code(answer_file=str):
    with open(answer_file, 'r') as code:
        result = [x.replace('\n', '') for x in code.readlines()]
        return result


def remove_given_code(answer_file, preload_file):
    code = get_student_code(answer_file)
    answerpreload = get_given_code(preload_file)
    functions = find_functions(code)
    for i in functions:
        print(('i = ',i))
    result = []
    for i in code:
        result.append(check_similarity(i, answerpreload))
    return result


def check_similarity(elem, list):
    for j in list:
        if j == elem:
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
