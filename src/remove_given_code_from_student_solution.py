import re
from bs4 import BeautifulSoup
PATH_TEMPLATE = "/home/erik/TU/ni/plagiate_labeltool/data/code_templates/"


def get_given_code(file):
    try:
        with open(file) as xmlstr:
            soup = BeautifulSoup(xmlstr, 'xml')
            answerpreload = soup.find('answerpreload').text
            questiontext = soup.find('questiontext').text
            return answerpreload, questiontext
    except FileNotFoundError:
        return "Keine Vorgabedatei im Repo gefunden", "Keine Vorgabedatei im Repo gefunden"


def remove_given_code(code, preload_file_path):
    answerpreload, _ = get_given_code(preload_file_path)
    # remove empty lines
    code = '\n'.join([s for s in code.splitlines() if s.strip() != ''])
    if answerpreload == 'Keine Vorgabedatei im Repo gefunden':
        return code
    answerpreload = answerpreload.replace('\t', '').replace('\r', '')
    answerpreload = '\n'.join(
        [s for s in answerpreload.splitlines() if s.strip() != ''])
    for ap_tmp in answerpreload.splitlines():
        ap_tmp = re.sub(r"  +", " ", ap_tmp)
        ap_tmp = re.escape(ap_tmp)
        ap_tmp = re.sub(r"\\ ", r"\\s*", ap_tmp)
        ap_tmp = '^' + ap_tmp + '$'
        # {{ cr_random.f1 }} --> \S*
        ap_tmp = re.sub(
            r"\\{\\{\\\s*\S+\s*\\}\\}", r"\\S*", ap_tmp)
        for code_tmp in code.splitlines():
            code_tmp = re.sub(r"  +", " ", code_tmp)
            if re.match(ap_tmp, code_tmp.replace('\t', '').replace('\r', '')):
                code = code.replace(code_tmp+'\n', '', 1)
                break
    return code


def remove_given_code_from_df(df):
    for i, (semester, ha, prog_lang, task, code1, code2) in enumerate(df[['semester', 'ha', 'prog_lang', 'task', 'code1', 'code2']].values):
        answerpreload_path = f'{PATH_TEMPLATE}PPR [{semester}]-{ha}. Hausaufgabe - Pflichttest {prog_lang}-Antworten_{task}.xml'
        df.loc[i, 'code1'] = remove_given_code(code1, answerpreload_path)
        df.loc[i, 'code2'] = remove_given_code(code2, answerpreload_path)
    return df
