__author__ = 'rram'
import os
import random
import pickle
import sys
import itertools


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


def save_progress(qlist, current_index):
    with open('question_list.pickle', 'wb') as ques_list:
        pickle.dump(qlist, ques_list)
    with open('curr_index.pickle', 'wb') as ind:
        pickle.dump(current_index, ind)


def load_progress():
    with open('question_list.pickle', 'rb') as ques_list:
        qlist = pickle.load(ques_list)
    with open('curr_index.pickle', 'rb') as ind:
        current_index = pickle.load(ind)
    return qlist, current_index


def display_questions(question_list, starting_index):
    total_questions = len(question_list)
    completed_questions = starting_index
    for question in itertools.islice(question_list, starting_index, len(question_list)):
        clear_screen()
        print question + '\n\n'
        print str(completed_questions) + "/" + str(total_questions) + " completed."
        completed_questions += 1
        choice = raw_input("Press Enter for new question\n'S' to save current progress")
        if choice.lower() == 's':
            save_progress(question_list, completed_questions)
            raw_input("Progress Saved!\n")
        clear_screen()
    print 'Done!'


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "new":
            question_list = read_questions('question_list.txt')
            random.shuffle(question_list)
            display_questions(question_list, 0)
        elif sys.argv[1] == "load":
            question_list, curr_index = load_progress()
            display_questions(question_list, curr_index)
    else:
        question_list = read_questions('question_list.txt')
        random.shuffle(question_list)
        display_questions(question_list, 0)