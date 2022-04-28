import json
import re
import difflib
import ast
from collections import namedtuple
from enum import Enum

q_a = {{QUESTION.answer}}

q_ap = {% if QUESTION.answerpreload is empty % }{{ "[[]]" }}{ % else % }{{ QUESTION.answerpreload }}{ % endif % }

s_a = {{STUDENT_ANSWER}}

occupancy = [[i, j] for i, row in enumerate(
    q_ap) for j, element in enumerate(row) if element]


def occupancyRows(column): return [o[0] for o in occupancy if o[1] == column]


def isOccupied(i, j):
    for o in occupancy:
        if o[0] == i and o[1] == j:
            return True
    return False


def matchingBlocks(expected, got, junk=None):
    return difflib.SequenceMatcher(junk, flatStringList(expected), flatStringList(got)).get_matching_blocks()


def printCellMatches(matches):
    print("\n".join([str([CMS[i] for i in m.cellMatches])
          for i, m in matches.items()]))


def exists(array, idx):
    return (len(array) > idx) and (array[idx] != "") and (array[idx] != None)


def lockedCells():
    print(str(occupancy))


def matchingBlocksStatsRate(matchingBlocksStats):
    return matchingBlocksStats.ratio * (1-matchingBlocksStats.entropy)


def matchingBlocksStats(matchingBlocks):
    # The length of the expected sequence. (Described by the dummy element at the end of the list.)
    expectedSize = matchingBlocks[-1].a

    # The total amount of matching entries.
    size = sum(m.size for m in matchingBlocks)

    # The percentual amount of matching entries.
    matchRatio = float(size)/float(expectedSize)

    # The amount of wrong entries.
    matchDiff = expectedSize - size

    # The entropy within the order of matches. (Mistakes are substracted to avoid double punishment.)
    entropy = 1
    if size > 0:
        entropy = float(max(len(matchingBlocks)-matchDiff-2, 0))/float(size)

    MatchingBlockStats = namedtuple("MatchingBlockStats", "ratio diff entropy")
    return MatchingBlockStats(matchRatio, matchDiff, entropy)


def unmatchingBlocks(expected, got, matchingBlocks):
    e = {i: x for i, x in enumerate(expected)}
    g = {i: x for i, x in enumerate(got)}
    for m in matchingBlocks:
        for i in list(range(m.a, m.a+m.size)):
            del e[i]
        for i in list(range(m.b, m.b+m.size)):
            del g[i]
    Unmatch = namedtuple("Unmatch", "expected got")
    return Unmatch(e, g)


def selectColumns(table, colIdxs):
    return [[row[idx] for idx in colIdxs] for row in table]


def flatStringList(table):
    return [str(row) for row in table]


def delete(list, idxs):
    l = list.copy()
    for i in sorted(idxs, reverse=True):
        del l[i]
    return l


def parseLineAndJump(s, linesFirst=True):
    line = ""
    jump = ""
    numbers = re.findall("[0-9]+", s)
    if numbers and len(numbers) >= 1:
        line = numbers[0]
        if len(numbers) >= 2:
            if linesFirst:
                jump = numbers[1]
            else:
                jump = line
                line = numbers[1]
    LineAndJump = namedtuple("LineAndJump", "line jump")
    return LineAndJump(line, jump)


def parseTable(list, linesFirst=True):
    table = []
    for row in list:
        lineAndJump = parseLineAndJump(row[0], linesFirst)
        table.append([lineAndJump.line.strip()] +
                     [lineAndJump.jump.strip()]+[r.strip() for r in row[1:]])
    return table


class CellMatch(Enum):
    NONE = 0
    EMPTY = 1
    NON_EMPTY = 2
    SIMILAR_TYPE = 4
    SAME_TYPE = 5
    EXACT = 6


CMR = {CellMatch.NONE: 0.0, CellMatch.EMPTY: 1.0, CellMatch.NON_EMPTY: 0.25,
       CellMatch.SIMILAR_TYPE: 0.25, CellMatch.SAME_TYPE: 0.5, CellMatch.EXACT: 1.0}
CMS = {CellMatch.NONE: "O", CellMatch.EMPTY: "E", CellMatch.NON_EMPTY: "U",
       CellMatch.SIMILAR_TYPE: "U", CellMatch.SAME_TYPE: "U", CellMatch.EXACT: "X"}


class RowMatch:
    def matchCell(expected, got):
        match = CellMatch.NONE
        if expected and got:
            match = CellMatch.NON_EMPTY
            try:
                e = ast.literal_eval(expected.strip().lower().capitalize())
                g = ast.literal_eval(got.strip().lower().capitalize())
                if type(e) == type(g):
                    match = CellMatch.SAME_TYPE
            except Exception as ex:
                pass
        if closeEnough(expected, got):
            if expected:
                match = CellMatch.EXACT
            else:
                match = CellMatch.EMPTY
        return match

    def matchRow(expected, got):
        return [RowMatch.matchCell(expected[i], g) for i, g in enumerate(got)]

    def __init__(self, idxExpected=-1, idxGot=-1, rowExpected=None, rowGot=None):
        self.hasExpectedLine = False
        self.hasExpectedJump = False
        self.cellMatches = None
        if rowExpected and rowGot:
            self.hasExpectedLine = (exists(rowExpected, 0) and exists(
                rowGot, 0) and (rowExpected[0] == rowGot[0]))
            self.hasExpectedJump = (exists(rowExpected, 1) and exists(
                rowGot, 1) and (rowExpected[1] == rowGot[1]))
            if len(rowExpected) > 2 and len(rowGot) > 2:
                self.cellMatches = RowMatch.matchRow(
                    rowExpected[2:], rowGot[2:])
        self.idxExpected = idxExpected
        self.idxGot = idxGot

    def __lt__(self, other):
        # Compare line number match.
        if self.hasExpectedLine != other.hasExpectedLine:
            if self.hasExpectedLine:
                return False
            else:
                return True
        # Compare jump adress match.
        if self.hasExpectedJump != other.hasExpectedJump:
            if self.hasExpectedJump:
                return False
            else:
                return True
        # Compare index distance if line numbers match.
        diffSelf = abs(self.idxExpected - self.idxGot)
        diffOther = abs(other.idxExpected - other.idxGot)
        if self.hasExpectedLine:
            if diffSelf != diffOther:
                return diffSelf > diffOther
        # Compare match value.
        selfValue = sum(CMR[w]/len(self.cellMatches) for w in self.cellMatches)
        otherValue = sum(CMR[w]/len(other.cellMatches)
                         for w in other.cellMatches)
        if selfValue == otherValue:
            return diffSelf > diffOther
        return selfValue < otherValue

    def __gt__(self, other):
        return (other < self)

    def __eq__(self, other):
        return (not (self < other)) and (not (other < self))

    def __ge__(self, other):
        return (self > other) or (other == self)

    def __le__(self, other):
        return (self < other) or (other == self)

    def __str__(self):
        return "idxExpected: "+str(self.idxExpected)+" idxGot: "+str(self.idxGot)+" matches:: line: "+str(self.hasExpectedLine)+" jump: "+str(self.hasExpectedJump)+" cell value: "+str(sum(CMR[w]/len(self.cellMatches) for w in self.cellMatches))


def matchRows(expected, got):

    # For every row in the "got" table create a "RowMatch" object with every row in the "expected" table.
    matchMatrix = dict.fromkeys([i for i, e in enumerate(got)])
    matchMatrix = {gIdx: [RowMatch(eIdx, gIdx, eRow, gRow) for eIdx, eRow in enumerate(
        expected)] for gIdx, gRow in enumerate(got)}
    [matchMatrix[gIdx].sort() for gIdx in matchMatrix]

    # Save all unmatched rows of the "got" table.
    unmatched = [gIdx for gIdx in matchMatrix]

    # Create an empty dictionary to hold the best match for every row of the "expected" table.
    matches = dict.fromkeys([i for i, e in enumerate(expected)])

    # As long as there are unmatched rows or a row has been updated.
    while unmatched:
        # For all unmatched rows.
        for gIdx in unmatched:
            # If there is no possible match left for the "got" row, consider it matched. This might be a problem!
            if not matchMatrix[gIdx]:
                unmatched.remove(gIdx)
                continue
            # Remove the last (best) RowMatch for the row of the "got" table.
            m = matchMatrix[gIdx].pop()
            # Get the respective index in the "expected" table.
            eIdx = m.idxExpected
            # If there is no match for the "expected" index or the current match is better, replace the entry.
            if (eIdx in matches) and ((not matches[eIdx]) or (m > matches[eIdx])):
                # If an existing entry is replaced, the according index of the "got" table becomes unmatched.
                if matches[eIdx]:
                    unmatched.append(matches[eIdx].idxGot)
                # The current match is not unmatched anymore.
                unmatched.remove(gIdx)
                matches[eIdx] = m
    return matches


def errorsToString(matches):
    s = "(Tabellenzeile|Tabellenspalte): Programmzeile: Wert: Kommentar\n"
    s += "-------------------------------------------------------------\n"
    for i, m in matches.items():
        for j, c in enumerate(m.cellMatches):
            if not isOccupied(m.idxExpected, j+1):
                tmp = "("+str(m.idxGot)+"|"+str(j)+"): "
                if exists(s_a, m.idxGot):
                    if exists(s_a[m.idxGot], 0):
                        tmp += s_a[m.idxGot][0]+": "
                    else:
                        tmp += "N/A: "
                    if exists(s_a[m.idxGot], j+1):
                        tmp += s_a[m.idxGot][j+1]+": "
                    else:
                        tmp += "N/A: "
                if c == CellMatch.NONE:
                    s += tmp
                    s += "falsch\n"
                if c == CellMatch.SIMILAR_TYPE or c == CellMatch.NON_EMPTY:
                    s += tmp
                    s += "nicht der gesuchte Wert\n"
                if c == CellMatch.SAME_TYPE:
                    s += tmp
                    s += "Rechenfehler\n"
    return s


def closeEnough(expected, got):
    if expected.strip().lower() == got.strip().lower():
        return True
    try:
        e = float(expected)
        g = float(got)
        if abs(e-g) <= 0.01:
            return True
    except ValueError as ex:
        pass
    return False


def gradeProgramSequence(expected, got):
    expectedTable = parseTable(expected)
    comment = ""
    penalty = 0

    gotTable = parseTable(got)
    gotInvTable = parseTable(got, False)

    gotMatches = matchingBlocks(delete(selectColumns(expectedTable, [0]), occupancyRows(
        0)), delete(selectColumns(gotTable, [0]), occupancyRows(0)))
    gotInvMatches = matchingBlocks(delete(selectColumns(expectedTable, [0]), occupancyRows(
        0)), delete(selectColumns(gotInvTable, [0]), occupancyRows(0)))

    stats = matchingBlocksStats(gotMatches)
    statsInv = matchingBlocksStats(gotInvMatches)

    if matchingBlocksStatsRate(statsInv) > matchingBlocksStatsRate(stats):
        stats = statsInv
        gotMatches = gotInvMatches
        gotTable = gotInvTable
        comment += "\nDie Reihenfolge von Programmzeile und Ruecksprungadresse wurde vertauscht.\n"
        penalty = 1

    jumpMatch = matchingBlocks(delete(selectColumns(expectedTable, [0, 1]), occupancyRows(
        0)), delete(selectColumns(gotTable, [0, 1]), occupancyRows(0)))
    statsJump = matchingBlocksStats(jumpMatch)
    if matchingBlocksStatsRate(stats) > matchingBlocksStatsRate(statsJump):
        comment += "Es existieren Fehler bei den Ruecksprungadressen.\n"
        penalty = 1

    unmatches = unmatchingBlocks(flatStringList(delete(selectColumns(expected, [0]), occupancyRows(
        0))), flatStringList(delete(selectColumns(got, [0]), occupancyRows(0))), gotMatches)
    if len(unmatches.got) > 0:
        comment += "Folgende erhaltene Programmablaufzeilen konnten nicht zugeordnet werden:\n\n"
        comment += "Tabellenzeile: [Inhalt]\n"
        comment += "-----------------------\n"
        comment += "\n".join([str(k+1)+": "+str(v)
                             for k, v in unmatches.got.items()])+"\n"

    if stats.entropy > 0.0:
        comment += "Die Reihenfolge der Programmzeilen ist nicht korrekt. (Entropiewert: "+str(
            stats.entropy)+")\n"
        if stats.entropy >= 0.8:
            penalty = 1

    if not comment:
        comment = "Gut! Der Programmablauf ist vollstaendig richtig!"

    if stats.ratio < 0.25:
        penalty = 1

    points = max(int(3*matchingBlocksStatsRate(stats))-penalty+1, 0)*0.25
    jsonObj = {"iscorrect": points >= 1, "got": "Programmablauf",
               "comment": comment, "fraction": points / 3, "awarded": points}
    return expectedTable, gotTable, jsonObj


def gradeMatches(expected, got):
    # Count all expected empty and non empty cells, if not "given" (occupied). Exclude the tables first 2 columns (line and jump).
    emptyCells = sum(1 for i, row in enumerate(expected) for j, cell in enumerate(
        row) if j > 1 and (not isOccupied(i, j-1)) and (not cell))
    valueCells = sum(1 for i, row in enumerate(expected) for j, cell in enumerate(
        row) if j > 1 and (not isOccupied(i, j-1)) and cell)

    # Get the best matches.
    matches = matchRows(expected, got)

    # Count the amount of matching empty cells and calculate the value of matching non-empty (value) cells.
    emptyMatches = sum(1 for idxM, row in matches.items() for j, m in enumerate(
        row.cellMatches) if m == CellMatch.EMPTY and not isOccupied(row.idxExpected, j+1))
    valueMatches = sum(CMR[m] for idxM, row in matches.items() for j, m in enumerate(
        row.cellMatches) if m != CellMatch.EMPTY and m != CellMatch.NONE and not isOccupied(row.idxExpected, j+1))

    emptyRatio = 1
    if emptyCells > 0:
        emptyRatio = emptyMatches/float(emptyCells)
    valueRatio = 1
    if valueCells > 0:
        valueRatio = valueMatches/float(valueCells)

    comment = ""
    if emptyMatches < emptyCells or valueMatches < valueCells:
        comment = "Es gibt Fehler bei den folgenden Eintraegen:\n\n"
        comment += errorsToString(matches)

    if not comment:
        comment = "Klasse! Alle Tabelleneintraege sind korrekt!\n"

    comment += "Leere Zellen: "+str(emptyMatches)+"/"+str(emptyCells)+"\n"
    comment += "Tabelleneintraege: " + \
        str(int(valueMatches))+"/"+str(valueCells)+"\n"

    if valueMatches <= 0:
        points = 0
    else:
        points = (0.1*(emptyRatio+0.000001)+0.9*(valueRatio+0.000001))
        points *= 8
        points = (int(points)/8.0)*2.0

    return {"iscorrect": points >= 2.0, "got": "Bewertung der Tabelleneintraege", "comment": comment, "fraction": points / 3, "awarded": points}


def testCase1():
    progSeqGrade = gradeProgramSequence(q_a, s_a)
    print(json.dumps(progSeqGrade[2]))


def testCase2():
    progSeqGrade = gradeProgramSequence(q_a, s_a)
    grade = gradeMatches(progSeqGrade[0], progSeqGrade[1])
    print(json.dumps(grade))


{{TEST.testcode}}
