import pandas as pd
import sys
import re
import random
from bs4 import BeautifulSoup
import argparse
import matplotlib.pyplot as plt
from pipeline import *
from model import *
from constants import *

TRAINING_SIZE = 40


"""
    1. dataframe mit texten ohne sonderzeichen ergänzen
    1.1 Kommentare in Codes entfernen
    2. dataframe mit PLOTtexten ohne sonderzeichen und ohne vorgabe ergänzen
    3. corr matrix mit lcs, n=1-gramm und n=6-gramm erstellen
    4. matrixen plotten
    5. pipeline so automatisieren, dass das alles nur mithilfe der eingabe der csv datei funktioniert
    6. siames network implementieren
    7. paare aus lösungen erstellen und labeln
    8. network mit paaren trainieren und vll ein zweites modell mit daten aus der challenge quora-question-pairs
    9. modelle evaluieren und miteinander und mit rudimentären lösungen vergleichen
"""

class DataCollector:
    # for interactive console
    # import importlib
    # import plagiate_maker
    # from plagiate_maker import *
    # importlib.reload(plagiate_maker)
    def __init__(self, csv_file_path="./data/unlabled/SoSe21/PPR [SoSe21]-9. Hausaufgabe - Pflichttest C-Antworten", column="Antwort 10"):
        df = dataframe_from_csv_for_training(csv_file_path, columns=['answer 1', 'answer 2'])
        self.pl = Pipeline(df, columns=['answer 1 text', 'answer 2 text'])
        text1, text2, self.label = (self.pl.df['tokend answer 1'], self.pl.df['tokend answer 2'], self.pl.df['label'])

        # select random train and test data
        # X_temp, X_test, y_temp, y_test = train_test_split(data[['clean_q1', 'clean_q2']], data['is_duplicate'], test_size=0.2, random_state=42)
        # X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.2, random_state=42)

        training_text1 = text1[0:TRAINING_SIZE]
        testint_text1 = text1[TRAINING_SIZE:]
        training_text2 = text2[0:TRAINING_SIZE]
        testint_text2 = text2[TRAINING_SIZE:]
        self.model = Model()
        self.texts = []
        for i, j in zip(training_text1, training_text2):
            self.texts.append(i+j)

        # print((type(self.texts), type(self.label)))
        # print((self.texts, type(self.label)))
        #TODO what is the datatype of each object
        #TODO! find out which format does model.fit need (which shape)
        #TODO how to reshape them
        self.model.model.fit(self.texts, self.label, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE)

        # df = dataframe_from_csv("./unlabled/SoSe22/PPR [SoSe22] -7. Hausaufgabe - Pflichttest C-Antworten")
        # self.semester = re.search("\[(\S+)\]", csv_file_path).group(1)
        # self.ha_number = re.search("-(\d{1,2})", csv_file_path).group(1)
        # matrix = create_lcs_matrix(df, column=column)
        # plot_correlation(matrix, f"{semester} - Aufgabe {ha_number}")


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


def dataframe_from_csv_for_training(file, columns):
    df = pd.read_csv(f'{file}.csv', delimiter=',')
    df = create_text_column_for_training(df, columns=columns)
    return df


def dataframe_from_csv_for_prediction(file):
    df = pd.read_csv(f'{file}.csv', delimiter=',')
    #TODO always 3 programming tasks?
    for j in range(0, 3):
        #TODO is task 16. in every homework first programming task?
        # file.write(row[15+j])
        df = create_text_column_for_predictions(df, index=(15+j))
    return df


def process_file(file):
    all_text = file.lower()

    # remove all non-alphanumeric chars
    #TODO sonderzeichen sind alle noch drinne
    all_text = re.sub(r"#", "", all_text)
    all_text = re.sub(r"[^a-zA-Z0-9]", " ", all_text)
    all_text = re.sub(r"\t", "", all_text)
    all_text = re.sub(r"\n", " ", all_text)
    all_text = re.sub("  ", " ", all_text)
    all_text = re.sub("   ", " ", all_text)
    all_text = re.sub("    ", " ", all_text)

    return all_text


def create_text_column_for_training(df, columns):
    '''Reads in the files, listed in a df and returns that df with an additional column, `Text`.
       :param df: A dataframe of file information including a column for `File`
       :param file_directory: the main directory where files are stored
       :return: A dataframe with processed text '''

    # # create copy to modify
    # text_df = df.copy()
    # store processed text
    text1 = []
    text2 = []
    # for each file (row) in the df, read in the file
    for row in df[columns[0]].values:
        if type(row) == float:
            text1.append("")
        else:
            code_text1 = process_file(row)
            text1.append(code_text1)
    for row in df[columns[1]].values:
        if type(row) == float:
            text2.append("")
        else:
            code_text2 = process_file(row)
            text2.append(code_text2)

    df[f'{columns[0]} text'] = text1
    df[f'{columns[1]} text'] = text2
    return df


def create_text_column_for_predictions(df, index):
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
        for column in source:
            plagiate.append(column.replace(i, random_function_names[count]))
    return plagiate


def create_plagiate_from_source(file):
    with open(file) as xmlstr:
        soup = BeautifulSoup(xmlstr.read, 'xml')
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
    parser.add_argument('-src', type=str, help='Source file', default='../data/labled/64_hand_labled_pairs')
    # parser.add_argument('-src', type=str, help='Source file', default='./unlabled/SoSe21/HA9C-0_0.c')
    parser.add_argument('-dest', type=str, help='Destination file', default='./unlabled/SoSe21/HA9C-0.xml')
    return parser.parse_args()


# Compute the normalized LCS given an answer text and a source text
def lcs_norm_word(answer_text, source_text):
    '''Computes the longest common subsequence of words in two texts; returns a normalized value.
       :param answer_text: The pre-processed text for an answer text
       :param source_text: The pre-processed text for an answer's associated source text
       :return: A normalized LCS value'''

    answer_list = answer_text.split()
    source_list = source_text.split()
    # return lcs(answer_list, source_list)/len(answer_list)
    rows = len(answer_list)
    columns = len(source_list)
    if rows == 0 or columns == 0:
        return 0
    matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]

    for i, a in enumerate(answer_list, start=1):
        for j, s in enumerate(source_list, start=1):
            if(a == s):
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    return matrix[rows][columns] / rows


def create_lcs_matrix(df, column):
    # matrix = [[lcs_norm_word(row_i, row_j) for row_i in df[column]] for row_j in df[column]]
    matrix = []
    for i, row_i in enumerate(df[column]):
        column = []
        for j, row_j in enumerate(df[column]):
            print((i,j))
            column.append(lcs_norm_word(row_i, row_j))
        matrix.append(column)
    return pd.DataFrame(matrix)


def plot_correlation(matrix, title):
    plt.matshow(matrix)
    plt.title(title)
    plt.show()



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
    dc = DataCollector(csv_file_path=args.src)

