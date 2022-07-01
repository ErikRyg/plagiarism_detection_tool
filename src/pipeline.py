from ftplib import MAXLINE
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import sys
import re
import random
from bs4 import BeautifulSoup
import argparse
import matplotlib.pyplot as plt
import constants

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

class Pipeline:
    # for interactive console
    # import importlib
    # import plagiate_maker
    # from plagiate_maker import *
    # importlib.reload(plagiate_maker)
    def __init__(self, df, columns):
        self.df = df
        self.columns = columns
        tokenize_coloums(self=self)
        # matrix = create_lcs_matrix(df, coloum=coloum)
        # plot_correlation(matrix, f"{semester} - Aufgabe {ha_number}")


def tokenize_coloums(self):
    ans1 = []
    ans2 = []
    # add entry for every words
    tokenizer = Tokenizer(num_words=constants.VOCABULARY_SIZE, oov_token="<OOV>")
    #TODO fit_on_texts only with the trained data, not the test data
    for row in self.df[self.columns[0]].values:
        tokenizer.fit_on_texts([row])
        tokend = tokenizer.texts_to_sequences([row])
        ans1.append(pad_sequences(tokend, maxlen=constants.MAXLEN, padding=constants.PADDING_TYPE, truncating=constants.TRUNC_TYPE))
    for row in self.df[self.columns[1]].values:
        tokenizer.fit_on_texts([row])
        tokend = tokenizer.texts_to_sequences([row])
        ans2.append(pad_sequences(tokend, maxlen=constants.MAXLEN, padding=constants.PADDING_TYPE, truncating=constants.TRUNC_TYPE))
    # Tokenize all strings
    self.df['tokend answer 1'] = ans1
    self.df['tokend answer 2'] = ans2


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


def create_lcs_matrix(df, coloum):
    # matrix = [[lcs_norm_word(row_i, row_j) for row_i in df[coloum]] for row_j in df[coloum]]
    matrix = []
    for i, row_i in enumerate(df[coloum]):
        coloum = []
        for j, row_j in enumerate(df[coloum]):
            print((i,j))
            coloum.append(lcs_norm_word(row_i, row_j))
        matrix.append(coloum)
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

