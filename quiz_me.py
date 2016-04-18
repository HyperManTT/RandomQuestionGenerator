__author__ = 'rram'
import os
import random
# Change directories to scripts being run
scriptPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptPath)


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def read_questions(file_name):
    questions = []
    with open(file_name, 'r') as question_file:
        for each_question in question_file:
            each_question = each_question.replace('\n', '')
            questions.append(each_question)
    return questions

if __name__ == "__main__":
    question_list = read_questions('question_list.txt')
    random.shuffle(question_list)
    for question in question_list:
        clear_screen()
        print question + '\n'
        raw_input('Press Enter for new question')
    clear_screen()
    print 'Done!'