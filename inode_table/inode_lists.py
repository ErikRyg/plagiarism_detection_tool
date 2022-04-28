import json

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


def print_out(expected, got, comment, fraction):
    print(json.dumps({'expected': expected, 'got': got, 'comment': comment, 'fraction': fraction}))


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


#TODO order of the rows should be unimportant
#TODO too much rows must give a penalty
def evaluate_inode(inode_stud, inode_must, score):
    for y in inode_stud:
        if y[0] == given_fields[1]:
            score += 1
            if y[1] == 'd':
                score += 1
            n_adresses = len(y[2].split(","))
            score += 4 - abs(4-n_adresses)
        else:
            if y[0] != '':
                score += 1
            if y[1] == '-':
                score += 1
            if y[2] != '':
                score += 1
    return score


#TODO order of the rows should be unimportant
def evaluate_datablock(inode_stud, datablock_stud, score):
    inode_with_content = get_content_of_ids(inode_stud, datablock_stud)
    for adress in inode_with_content:
        for j in range(3, len(adress)):
            if '"."' in adress[j] and given_fields[1] in adress[j]:
                score += 2
            if '".."' in adress[j] and given_fields[2] in adress[j]:
                score += 2
            if given_fields[4] in adress[j]:
                score += 2
            if given_fields[5] in adress[j]:
                score += 2
            found_in_data1 = [True for i in inode_with_content[0] if adress[0] in i and given_fields[4] in i]
            if given_fields[6] in adress[j] and found_in_data1:
                score += 2
            found_in_data2 = [True for i in inode_with_content[0] if adress[0] in i and given_fields[5] in i]
            if given_fields[7] in adress[j] and found_in_data2:
                score += 2
    return score


def get_content_of_ids(inode_stud, datablock_stud):
    complete_inode_stud = []
    for id_entry in inode_stud:
        adresses = id_entry[2].split(',')
        for adress in adresses:
            for data_entry in datablock_stud:
                if adress == data_entry[0]:
                    id_entry.append(data_entry[1])
                    break
        complete_inode_stud.append(id_entry)
    return complete_inode_stud


def test_student_answer():
    got = ''
    inode_stud, datablock_stud = seperate_tables(student_answer)
    inode_must, datablock_must = seperate_tables(solution)

    inode_stud, datablock_stud = remove_given_rows(inode_stud, datablock_stud)
    inode_must, datablock_must = remove_given_rows(inode_must, datablock_must)

    print((len(inode_must), inode_must, len(datablock_must), datablock_must))
    total_score = 24
    score = evaluate_inode(inode_stud, inode_must, score=0)
    score = evaluate_datablock(inode_stud, datablock_stud, score)

    table_stud = create_tables_string(inode_stud, datablock_stud)

    fraction = score / total_score
    got += f"Inode-Liste und Datenblock des Studenten:\n{table_stud}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Musterlösung unterscheiden"
    #TODO Kommentare zur Bewertung schreiben
    comment = f'{score} / {total_score} = {fraction}'

    table_must = create_tables_string(inode_must, datablock_must)
    expected = f"Inode-Liste und Dateblock der Musterlösung:\n{table_must}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Studentenlösung unterscheiden"

    return print_out(expected, got, comment, fraction)


if __name__ == '__main__':
    test_student_answer()
