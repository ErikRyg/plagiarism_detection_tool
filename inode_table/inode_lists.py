import json

student_answer = [["55", "d", "20,21,22", "|", "20", "\".\" id 55"], ["600", "d", "41,42,43,44", "|", "21", "\"..\" id 55"], ["700", "-", "31", "|", "22", "\"Schreibtisch\" id 600"], ["800", "-", "36", "|", "31", "Hirn"],
                  ["", "", "", "|", "36", "Petrus"], ["", "", "", "|", "41", "\".\" id 600"], ["", "", "", "|", "42", "\"..\" id 20"], ["", "", "", "|", "43", "\"Notitzen\" id 700"], ["", "", "", "|", "44", "\"Programmieren\" id 800"]]
solution = student_answer
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


#TODO should be more generic, maybe with locked cells? -> more complex to calculate points
def remove_given_rows(inode, datablock):
    new_inode = [inode[x] for x in range(1, len(inode))]
    new_data = [datablock[x] for x in range(3, len(datablock))]
    return new_inode, new_data


def evaluate_inode(inode_stud, inode_must, score):
    #TODO too much rows must give a penalty, negative point possible?!
    comment = ''
    if len(inode_stud) > len(inode_must):
        score -= 2
        comment += '- too much rows in inode table\n'
    elif len(inode_stud) == 0:
        comment += '- inode table is empty\n'
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
                comment += '- first coloum cannot be empty\n'
            if y[2] != '':
                score += 1
            else:
                comment += '- first coloum cannot be empty\n'
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
    #TODO add comments for missing points
    index = get_index_of_directory(inode_stud)
    if index == -1:
        comment += '- could not find a directory in inode table\n'
    for row in inode_with_content:
        for j in range(3, len(row)):
            # check self and parent id
            if '"."' in row[j] and given_fields[1] in row[j]:
                score += 2
            elif '".."' in row[j] and given_fields[2] in row[j]:
                score += 2
            # check file names and parent id
            elif given_fields[4].lower() in row[j].lower() and given_fields[1] is row[0]:
                score += 2
            elif given_fields[5].lower() in row[j].lower() and given_fields[1] is row[0]:
                score += 2
            #TODO is not always inode_with_content[0] --> get parent row
            # check content, corresponding inode_row and if the inode_row is in the right file
            elif index != -1 and given_fields[6].lower() in row[j].lower():
                found_in_data1 = [True for i in inode_with_content[index] if row[0] in i and given_fields[4].lower() in i.lower()]
                if found_in_data1:
                    score += 2
            elif index != -1 and given_fields[7].lower() in row[j].lower():
                found_in_data2 = [True for i in inode_with_content[index] if row[0] in i and given_fields[5].lower() in i.lower()]
                if found_in_data2:
                    score += 2
    return score, comment


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

#TODO does not work with multiple directorys in task so far
def get_index_of_directory(inode_stud):
    index = -1
    for i, elem in enumerate(inode_stud):
        if elem[1] == 'd':
            index = i
    return index


def test_student_answer():
    got = ''
    inode_stud, datablock_stud = seperate_tables(student_answer)
    inode_must, datablock_must = seperate_tables(solution)

    inode_stud, datablock_stud = remove_given_rows(inode_stud, datablock_stud)
    inode_must, datablock_must = remove_given_rows(inode_must, datablock_must)

    print((len(inode_must), inode_must, len(datablock_must), datablock_must))
    #TODO get total_score generic
    total_score = 24
    score, comment = evaluate_inode(inode_stud, inode_must, score=0)
    if comment == '':
        comment += '- inode table is correct\n'
    score, comment_datablock = evaluate_datablock(inode_stud, datablock_stud, datablock_must, score)
    if comment_datablock == '':
        comment += '- datablock table is correct\n'
    else:
        comment += comment_datablock
    print(('comment_datablock', comment_datablock))

    table_stud = create_tables_string(inode_stud, datablock_stud)

    print(('comment', comment))
    fraction = score / total_score
    got += f"Inode-Liste und Datenblock des Studenten:\n{table_stud}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Musterlösung unterscheiden"
    #TODO Kommentare zur Bewertung schreiben
    comment += f'{score} / {total_score} = {fraction}'
    print(('comment', comment))

    table_must = create_tables_string(inode_must, datablock_must)
    expected = f"Inode-Liste und Dateblock der Musterlösung:\n{table_must}\n\nDie freigewählten Inode-IDs und Speicheradressen können sich von der Studentenlösung unterscheiden"

    return print_out(expected, got, comment, fraction)


if __name__ == '__main__':
    test_student_answer()
