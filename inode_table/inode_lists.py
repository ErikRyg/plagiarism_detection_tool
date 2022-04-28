import json
# from tokenize import String
import numpy as np

student_answer = [["55", "d", "20,21,22", "|", "20", "\".\" id 55"], ["600", "d", "41,42,43,44", "|", "21", "\"..\" id 55"], ["700", "-", "31", "|", "22", "\"Schreibtisch\" id 600"], ["800", "-", "36", "|", "31", "Hirn"],
                  ["", "", "", "|", "36", "Petrus"], ["", "", "", "|", "41", "\".\" id 600"], ["", "", "", "|", "42", "\"..\" id 20"], ["", "", "", "|", "43", "\"Notitzen\" id 700"], ["", "", "", "|", "44", "\"Programmieren\" id 800"]]
solution = student_answer
given_fields = []
given_fields.append('55')
given_fields.append('600')
given_fields.append('20')
given_fields.append('Schreibtisch')
given_fields.append('Notitzen')
given_fields.append('Programmieren')
given_fields.append('Hirn')
given_fields.append('Petrus')


def print_out(got, comment, fraction):
    print(json.dumps({'got': got, 'comment': comment, 'fraction': fraction}))


def seperate_tables(data):
    n_coloum = len(data)
    inode = []
    datablock = []
    for x in range(n_coloum):
        inode.append(data[x][0:3])
        datablock.append(data[x][4:6])
    inode = remove_empty_coloums(inode)
    datablock = remove_empty_coloums(datablock)
    return inode, datablock


def remove_empty_coloums(matrix):
    removed = [x for x in matrix if not x[0] == '']
    return removed


def create_tables_string(inode, datablock):
    header_inode = ['Inode-ID', 'Dateityp',
                    'Speicheradressen']
    header_data = ['Speicheradresse', 'Inhalt']
    string = ''
    fill = ''

    # print header of the tables
    for elem in header_inode:
        string += elem.ljust(20)
    string += fill.ljust(20)
    for elem in header_data:
        string += elem.ljust(20)
    string += '\n'

    # print data of the tables
    for i, inode in enumerate(inode):
        string += f'{inode[0].ljust(20)}{inode[1].ljust(20)}{inode[2].ljust(40)}{datablock[i][0].ljust(20)}{datablock[i][1].ljust(20)}\n'
    for j in range(i+1, len(datablock)):
        string += f'{fill.ljust(80)}{datablock[j][0].ljust(20)}{datablock[j][1]}\n'
    return string


def remove_given_rows(inode, datablock):
    new_inode = [inode[x] for x in range(1, len(inode))]
    new_data = [datablock[x] for x in range(3, len(datablock))]
    return new_inode, new_data


def evaluate_inode(inode_stud, inode_must, score):
    for x, y in zip(inode_stud, inode_must):
        for i, j in zip(x, y):
            if i is j:
                score += 1
    return score
    # for y in inode_stud:
    #     if y[0] == given_fields[0]:
    #         score += 1
    #         if y[1] == 'd':
    #             score += 1
    # return score


def evaluate_datablock(datablock_stud, datablock_must, score):
    for x, y in zip(datablock_stud, datablock_must):
        for i, j in zip(x, y):
            if i is j:
                print(i, score)
                score += 1
    return score


def test_student_answer():
    #    got = "Hier in der Variable sollst du ausgeben, was der Student in etwa in die Tabelle eingegeben hat. Inodeliste und Datenblock bitte trennen und einfach in ASCII schön ausgeben. Erwähne auch dass die Zahlen flexibel sind"
    got = ''
    inode_stud, datablock_stud = seperate_tables(student_answer)
    inode_must, datablock_must = seperate_tables(solution)

    inode_stud, datablock_stud = remove_given_rows(inode_stud, datablock_stud)
    inode_must, datablock_must = remove_given_rows(inode_must, datablock_must)

    earned_score = 2
    total_score = 26
    earned_score += evaluate_inode(inode_stud, inode_must, earned_score)
    print(f'earned score: {earned_score}')
    earned_score += evaluate_datablock(datablock_stud,
                                       datablock_must, earned_score)
    print(f'earned score: {earned_score}')

    table_stud = create_tables_string(inode_stud, datablock_stud)

    # Wie viel Prozent der Gesamtpunktzahl du dem Studierenden gibst: von 0 bis 1
    fraction = earned_score / total_score
    got += f"Inode-Liste und Dateblock des Studenten:\n{table_stud}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Musterlösung unterscheiden"
    # got += f"Inode-Liste der Musterlösung:\n{inode_must}\nDateblock der Musterlösung:\n{datablock_must}"
    print(got)

    # comment = "hier sollen die Punkte kommentiert werden"

    table_must = create_tables_string(inode_must, datablock_must)
    comment = f"Inode-Liste und Dateblock der Musterlösung:\n{table_stud}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Studentenlösung unterscheiden"

    # Ganz viel Magie wie aus der Liste dann Punkte werden

    return print_out(got, comment, fraction)


if __name__ == '__main__':
    test_student_answer()
