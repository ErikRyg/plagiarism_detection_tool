from Levenshtein import distance
import numpy as np

import csv
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import argparse


def distance_percentage(string1, string2):
    return distance(string1, string2) / np.max([len(string1), len(string2)])


def get_similarity(string1, string2):


    distance1 = distance_percentage(string1, string2)

    string1_p = string1
    string1 = string1.split()
    string1_w = "".join(string1)
    string1_s = "".join(sorted(string1_w))

    string2_p = string2
    string2 = string2.split()
    string2_w = "".join(string2)
    string2_s = "".join(sorted(string2_w))

    distance2 = distance_percentage(string1_w, string2_w)
    distance3 = distance_percentage(string1_s, string2_s)


    return np.max([1 - distance1, 1 - distance2, 1 - distance3])


def initialize_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', type=str, help='Source file', default='./unlabled/SoSe21/HA9C-0_0.c')
    parser.add_argument('-dest', type=str, help='Destination file', default='./unlabled/SoSe21/HA9C-0.xml')
    return parser.parse_args()



if __name__ == '__main__':
    args = initialize_argparser()

    # print(get_similarity("aaabbb", "bbbaaa")) #1.0
    # print(get_similarity("aaaaaa", "vvvvvv")) #0.0
    # print(get_similarity("aaaaaa", "aaa      \t             aaa")) #1.0
    # print(get_similarity("a    b    c", "d    e    f")) #0.7272

    with open(f'{args.src}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        submissions = list()
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'{line_count}\t{row[15]}')
                submissions.append(row)
                line_count += 1
        # print(f'Processed {line_count} lines.')


        similarity_matrix = np.ones((len(submissions), len(submissions)))

        for i, row in enumerate(submissions):
            maximum = 0
            person = ""



            for j, row_other in enumerate(submissions):

                if i == j:
                    continue

                similarity = get_similarity(row[15], row_other[15])

                if similarity > maximum:
                    maximum = similarity
                    person = row_other[0]
                similarity_matrix[i,j] = similarity#similarity_matrix[j,i] = similarity

            print(row[0], maximum, person)

        print(similarity_matrix)





        fig, ax = plt.subplots(figsize=(10,10))
        cax = ax.matshow(similarity_matrix, interpolation='nearest')
        ax.grid(True)
        fig.colorbar(cax, ticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, .8,.90,1])
        plt.title('similarity matrix')
        plt.show()


        embedding = MDS(n_components=2)

        similarity_matrix = similarity_matrix + np.random.normal(0, 0.001, size = similarity_matrix.shape)

        X_transformed = embedding.fit_transform(similarity_matrix)


        fig = plt.figure(figsize=(10,10))
        plt.scatter(X_transformed[:,0], X_transformed[:,1])

        plt.scatter(X_transformed[-1,0], X_transformed[-1,1])
        plt.scatter(X_transformed[-2,0], X_transformed[-2,1])
        plt.scatter(X_transformed[-3,0], X_transformed[-3,1])

        for i in range(len(submissions)):

            plt.annotate(submissions[i][0], (X_transformed[i,0], X_transformed[i,1]))

        plt.title('X transformed')
        plt.show()
