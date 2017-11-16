'''A Python script that calculates the Motivating Potential Score given a CSV file of scores'''

import csv
import sys

# Skill variety (SV) (items 2, 8, 11*, 14, 18*) = ___ /5 = ___
def skill_var(q_2, q_8, q_11, q_14, q_18):
    total = q_2 + q_8 + (5 - q_11) + q_14 + (5 - q_18)
    return total/5

# Task identity (TI) (items 3, 7*, 16*, 22) = ___ /4 = ___
def task_identity(q_3, q_7, q_16, q_22):
    total = q_3 + (5 - q_7) + (5 - q_16) + q_22
    return total/4

# Task significance (TS) (items 4, 13*, 20*, 23) = ___ /4 = ___
def task_significance(q_4, q_13, q_20, q_23):
    total = q_4 + (5 - q_13) + 5 - (q_20) + q_23
    return total/4

# Autonomy (AU) (items 1, 9*, 17*, 21) = ___ /4 = ___
def autonomy(q_1, q_9, q_17, q_21):
    total = q_1 + (5 - q_9) + (5 - q_17) + q_21
    return total/4

# Feedback (FB) (items 5, 6, 10, 12*, 15, 19*) = ___ /6 = ___
def feedback(q_5, q_6, q_10, q_12, q_15, q_19):
    total = q_5 + q_6 + q_10 + (5 - q_12) + q_15 + (5 - q_19)
    return total/6

if __name__ == "__main__":
    # get the CSV file to parse
    if len(sys.argv) < 2:
        print("Enter a CSV file")
        sys.exit(0)
    FILENAME = sys.argv[1]

    # there are 23 QUESTIONS, but we won't fill index 0 for simplicity
    QUESTIONS = [0]*24

    # calculate the # of rows in the file
    try:
        CR = csv.reader(open(FILENAME, "r"))
        next(CR)
        ROW_COUNT = sum(1 for row in CR)
    except:
        print(FILENAME, "does not exist")
        sys.exit(0)

    for i in range(1, len(QUESTIONS)):
        # the row header is in the form "Q1, Q2, etc"
        key = "Q" + str(i)
        reader = csv.DictReader(open(FILENAME, "r"))
        # sum all the values in that column
        QUESTIONS[i] = sum(int(row[key]) for row in reader) / ROW_COUNT
        print("The average for", key, "is", QUESTIONS[i])

    SV = skill_var(QUESTIONS[2], QUESTIONS[8], QUESTIONS[11], QUESTIONS[14], QUESTIONS[18])
    TI = task_identity(QUESTIONS[3], QUESTIONS[7], QUESTIONS[16], QUESTIONS[22])
    TS = task_significance(QUESTIONS[4], QUESTIONS[13], QUESTIONS[20], QUESTIONS[23])
    AU = autonomy(QUESTIONS[1], QUESTIONS[9], QUESTIONS[17], QUESTIONS[21])
    FB = feedback(QUESTIONS[5], QUESTIONS[6], QUESTIONS[10], QUESTIONS[12], QUESTIONS[15], QUESTIONS[19])

    MPS = ((SV + TI + TS) / 3) * AU * FB

    print("Motivating Potential Score is", MPS)

