import json
import re

solution = [["55", "d", "20,21,22", "|", "20", "\".\" id 55"], ["600", "d", "41, 42,43,44", "|", "21", "\"..\" id 2"], ["700", "-", "31", "|", "22", "\"Schreibtisch\" id 600"], ["800", "-", "36", "|", "31", "Hirn"],
                  ["", "", "", "|", "36", "Petrus"], ["", "", "", "|", "41 ", " \".\" id 600 "], ["", "", "", "|", "42", "\"..\" id 55"], ["", "", "", "|", "43", "\"Notitzen\" id 700"], ["", "", "", "|", "44", "\"Programmieren\" id 800"]]
student_answer = []
for string in solution:
    student_answer.append(string.copy())
given_fields = []
given_fields.append('55')               #starting_id
given_fields.append('600')              #second_id
given_fields.append('20')               #starting_adress
given_fields.append('Schreibtisch')     #directory
given_fields.append('Notitzen')         #filename1
given_fields.append('Programmieren')    #filename2
given_fields.append('Hirn')             #content1
given_fields.append('Petrus')           #content2


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


def create_inode_string(inode):
    header = ['Inode-ID', 'Dateityp', 'Speicheradressen']
    string = ''
    for elem in header:
        string += elem.ljust(20)
    string += '\n'
    for inode in inode:
        string += f'{inode[0].ljust(20)}{inode[1].ljust(20)}{inode[2].ljust(40)}\n'
    return string


def create_datablock_string(datablock):
    header = ['Speicheradresse', 'Inhalt']
    string = ''
    for elem in header:
        string += elem.ljust(20)
    string += '\n'
    for data in datablock:
        string += f'{data[0].ljust(20)}{data[1]}\n'
    return string



#TODO should be more generic, maybe with locked cells? -> more complex to calculate points
def remove_given_rows(inode, datablock):
    new_inode = [inode[x] for x in range(1, len(inode))]
    new_data = [datablock[x] for x in range(3, len(datablock))]
    return new_inode, new_data


def remove_white_spaces(inode, datablock):
    new_inode = []
    for elem in inode:
        tmp = []
        for string in elem:
            tmp.append(string.strip(' '))
        new_inode.append(tmp)
    new_data = []
    for elem in datablock:
        tmp = []
        for string in elem:
            tmp.append(string.strip(' '))
        new_data.append(tmp)
    return new_inode, new_data


def evaluate_inode(inode_stud, inode_must, score):
    #TODO too much rows must give a penalty, negative point possible?!
    comment = ''
    if len(inode_stud) > len(inode_must):
        score -= 2
        comment += '- too much rows in inode table\n'
    elif len(inode_stud) == 0:
        comment += '- inode table is empty\n'
        return score, comment
    for y in inode_stud:
        if y[0].lower() == given_fields[1].lower():
            score += 1
            if y[1].lower() == 'd':
                score += 1
            else:
                comment += f'- "{given_fields[1]}" is a directory\n'
            n_adresses = len(y[2].split(","))
            score += 4 - abs(4-n_adresses)
        else:
            if y[0] != '':
                score += 1
            else:
                comment += '- first coloum cannot be empty\n'
            if y[1] == '-':
                score += 1
            else:
                comment += '- second coloum must be "-" when its not a directory\n'
            if y[2] != '':
                score += 1
            else:
                comment += '- third coloum cannot be empty\n'
    return score, comment


def find_elem_in_datablock(elem, datablock, score, comment):
    for row in datablock:
        if elem.lower() in row[1].lower() and row[0] != '':
            score += 1
            return score, comment
    comment += f'- could not find element {elem} in datablock\n'
    return score, comment


def evaluate_datablock(inode_stud, datablock_stud, datablock_must, score):
    inode_with_content = get_content_of_ids(inode_stud, datablock_stud)
    #TODO too much coloumns must give a penalty, negative point possible?!
    comment = ''
    if len(datablock_stud) > len(datablock_must):
        score -= 2
        comment += '- too much rows in datablock table\n'
    elif len(datablock_stud) == 0:
        comment += '- datablock table is empty\n'
        return score, comment
    index = get_index_of_directory(inode_stud)
    if index == -1:
        comment += '- could not find a directory in inode table\n'
    # simple check for entries in datablock
    score, comment = find_elem_in_datablock('"."', datablock_stud, score, comment)
    score, comment = find_elem_in_datablock('".."', datablock_stud, score, comment)
    for x in range(4, 8):
        score, comment = find_elem_in_datablock(given_fields[x], datablock_stud, score, comment)
    # more complex check for entries in inode with the corresponding content
    for row in inode_with_content:
        for j in range(3, len(row)):
            # check self and parent id
            if '"."' in row[j]:
                if given_fields[1] in row[j]:
                    score += 1
                else:
                    id = re.search('\d*', row[j]).group()
                    comment += f'- self-reference: "." id {id} is false; should be: "." id {given_fields[1]}\n'
            elif '".."' in row[j]:
                if given_fields[0] in row[j]:
                    score += 1
                else:
                    id = re.search('\d*', row[j]).group()
                    comment += f'- reference to parent_id: ".." id {id} is false; should be: ".." id {given_fields[0]}\n'
            # check file names and parent id
            elif given_fields[4].lower() in row[j].lower():
                if given_fields[1] is row[0]:
                    score += 1
                else:
                    comment += f'- file {given_fields[4]} has wrong memory address. This file belongs to the Inode-ID {row[0]}, but should belong to the Inode-ID {given_fields[1]}\n'
            elif given_fields[5].lower() in row[j].lower():
                if given_fields[1] is row[0]:
                    score += 1
                else:
                    comment += f'- file {given_fields[5]} has wrong memory address. This file belongs to the Inode-ID {row[0]}, but should belong to the Inode-ID {given_fields[1]}\n'
            # check content, corresponding inode_row and if the inode_row is in the right file
            elif index != -1:
                if given_fields[6].lower() in row[j].lower():
                    found_in_data = [True for i in inode_with_content[index] if row[0] in i and given_fields[4].lower() in i.lower()]
                    if found_in_data:
                        score += 1
                    else:
                        comment += f'- the content "{given_fields[6]}" belongs to the Inode-ID {row[0]}, which should belong to the file {given_fields[4]}\n'
                if given_fields[7].lower() in row[j].lower():
                    found_in_data = [True for i in inode_with_content[index] if row[0] in i and given_fields[5].lower() in i.lower()]
                    if found_in_data:
                        score += 1
                    else:
                        comment += f'- the content "{given_fields[7]}" belongs to the Inode-ID {row[0]}, which should belong to the file {given_fields[5]}\n'
    return score, comment


def get_content_of_ids(inode_stud, datablock_stud):
    complete_inode_stud = []
    for id_entry in inode_stud:
        adresses = id_entry[2].replace(' ', '').split(',')
        for adress in adresses:
            for data_entry in datablock_stud:
                if adress == data_entry[0]:
                    id_entry.append(data_entry[1])
                    break
        complete_inode_stud.append(id_entry)
    return complete_inode_stud


#TODO does not work with multiple directorys in task so far
def get_index_of_directory(inode_stud):
    index = -1
    for i, elem in enumerate(inode_stud):
        if elem[1] == 'd':
            index = i
    return index


def test_inode_table():
    """
    Gibt pro Eintrag in einer Zelle einen Punkt.
    Bei Ordner gibt es hingegen für jede richtige Speicheradresse einen Punkt.
    """
    got = ''
    inode_stud, datablock_stud = seperate_tables(student_answer)
    inode_must, datablock_must = seperate_tables(solution)

    inode_stud, datablock_stud = remove_given_rows(inode_stud, datablock_stud)
    inode_must, datablock_must = remove_given_rows(inode_must, datablock_must)

    #TODO get total_score generic
    total_score = 12
    score, comment = evaluate_inode(inode_stud, inode_must, score=0)
    if comment == '':
        comment += '- inode table is correct\n'

    table_stud = create_inode_string(inode_stud)

    fraction = score / total_score
    got += f"Inode-Liste des Studenten:\n{table_stud}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Musterlösung unterscheiden"
    comment += f'{score} / {total_score} = {round(fraction*100, 2)}%'

    table_must = create_inode_string(inode_must)
    expected = f"Inode-Liste der Musterlösung:\n{table_must}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Studentenlösung unterscheiden"

    return print_out(expected, got, comment, fraction)


def compute_total_points_for_datablock(datablock_must):
    return len(datablock_must) * 2


def test_datablock_table():
    """
    Gibt pro Zelle in der Spalte Inhalt zwei Punkte.
    Einen Punkt wenn die Zeile im Datenblock richtig ist.
    Zweiter Punkt wenn diese Adresse auch in der richtigen Inode Zeile steht.
    Jedoch gibt es Abzug, wenn keine Adresse zu dem Inhalt angegeben wird.
    """
    got = ''
    inode_stud, datablock_stud = seperate_tables(student_answer)
    inode_must, datablock_must = seperate_tables(solution)

    inode_stud, datablock_stud = remove_given_rows(inode_stud, datablock_stud)
    inode_must, datablock_must = remove_given_rows(inode_must, datablock_must)
    inode_stud, datablock_stud = remove_white_spaces(inode_stud, datablock_stud)

    total_score = compute_total_points_for_datablock(datablock_must)
    score, comment = evaluate_datablock(inode_stud, datablock_stud, datablock_must, score=0)
    if comment == '':
        comment += '- datablock table is correct\n'

    table_stud = create_datablock_string(datablock_stud)

    fraction = score / total_score
    got += f"Datenblock des Studenten:\n{table_stud}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Musterlösung unterscheiden"
    comment += f'{score} / {total_score} = {round(fraction*100, 2)}%'

    table_must = create_datablock_string(datablock_must)
    expected = f"Datenblock der Musterlösung:\n{table_must}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Studentenlösung unterscheiden"

    return print_out(expected, got, comment, fraction)


if __name__ == '__main__':
    test_inode_table()
    test_datablock_table()
