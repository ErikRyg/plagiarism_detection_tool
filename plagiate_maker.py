import pandas as pd
import sys
import re
import random
from bs4 import BeautifulSoup
import argparse

"""
    1. dataframe mit texten ohne sonderzeichen ergänzen
    2. dataframe mit texten ohne sonderzeichen und ohne vorgabe ergänzen
    3. corr matrix mit lcs, n=1-gramm und n=6-gramm erstellen
    4. matrixen plotten
    5. pipeline so automatisieren, dass das alles nur mithilfe der eingabe der csv datei funktioniert
    6. thomas eine mail schreiben, wegen der funktion des neuronalen netztes --> gibt es neuronale netzte mit 2 eingabe (texte)?
        --> aws projekt trainiert das model nur auf die wiki texte und arbeitet dann nur mit einem input und label
"""



def read_and_store_from_csv(file):
    df = pd.read_csv(f'{file}.csv', delimiter=',')
    semester = re.search("\[(\S+)\]", file).group(1)
    ha_number = re.search("-(\d{1,2})", file).group(1)
    for i, row in enumerate(df.values):
        #TODO always 3 programming tasks?
        for j in range(0, 3):
            # "unlabled/SoSe21/PPR [SoSe21]-9. Hausaufgabe - Pflichttest C-Antworten"
            with open(f'unlabled/{semester}/HA{ha_number}C-{j}_{i}.c', 'w') as file:
                #TODO is task 16. in every homework first programming task?
                file.write(row[15+j])


def dataframe_from_csv(file):
    df = pd.read_csv(f'{file}.csv', delimiter=',')
    #TODO always 3 programming tasks?
    for j in range(0, 3):
        #TODO is task 16. in every homework first programming task?
        # file.write(row[15+j])
        df = create_text_column(df, (15+j))
    return df


def process_file(file):
    all_text = file.lower()

    # remove all non-alphanumeric chars
    #TODO sonderzeichen sind alle noch drinne
    all_text = re.sub(r"[^a-zA-Z0-9]", " ", all_text)
    all_text = re.sub(r"\t", " ", all_text)
    all_text = re.sub(r"\n", " ", all_text)
    all_text = re.sub("  ", " ", all_text)
    all_text = re.sub("   ", " ", all_text)

    return all_text


def create_text_column(df, index):
    '''Reads in the files, listed in a df and returns that df with an additional column, `Text`.
       :param df: A dataframe of file information including a column for `File`
       :param file_directory: the main directory where files are stored
       :return: A dataframe with processed text '''

    # create copy to modify
    text_df = df.copy()
    # store processed text
    text = []
    # for each file (row) in the df, read in the file
    for row in df.values:
        if type(row[index]) == float:
            text.append("")
        else:
            code_text = process_file(row[index])
            text.append(code_text)

    # add column to the copied dataframe
    text_df[f'Aufgabe {15+index} Text'] = text
    return text_df


#TODO catboost anschauen
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
    parser.add_argument('-src', type=str, help='Source file', default='./unlabled/SoSe21/HA9C-0_0.c')
    parser.add_argument('-dest', type=str, help='Destination file', default='./unlabled/SoSe21/HA9C-0.xml')
    return parser.parse_args()


if __name__ == "__main__":
    args = initialize_argparser()
    # print(args.src, args.dest)
    # read_and_store_from_csv(sys.argv[1])

    # result = remove_given_code(args.src, args.dest)
    # for i in result:
    #     print(i)
    # plagiate = create_plagiate_from_source(args.dest)
    # for i in plagiate:
    #     print(i)
    df = dataframe_from_csv("./unlabled/SoSe22/PPR [SoSe22] -7. Hausaufgabe - Pflichttest C-Antworten")
    for i in range(0,3):
        # print(df.values[i][15])
        # print(df.values[i][16])
        # print(df.values[i][17])
        print(df.values[i][18])
        print(df.values[i][19])
        print(df.values[i][20])
