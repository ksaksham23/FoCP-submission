import json
import signal
from sys import exit
from agent_names import agent_names as names
from greetings import greetings
from random import randint
from asking import asking_ques as ask_user
from termination_messages import terminate_msgs

def timeout_handler(signum, frame):
    print("\nNo input detected within the time limit. Exiting the application...")
    exit(0)

# set the timeout signal
signal.signal(signal.SIGALRM, timeout_handler)


def welcome_to_application():
    print("\t\t WELCOME TO UNIVERSITY OF POPPLETON VERY OWN INTERACTIVE CHAT APPLICATION \t\t")


def ask_user_name():
    try:

        signal.alarm(20)
        user_name = input("Please enter your name before we begin: ")
        return user_name
    except Exception:
        signal.alarm(0)  # Reset the alarm if an exception occurs
        raise

def get_agent_name():
    name = names[randint(0, len(names)-1)]
    return name

def display_greeting():
    get_greeting = greetings[randint(0, len(greetings)-1)]
    user_name = ask_user_name()
    agent_name = get_agent_name()
    print(f"{get_greeting} {user_name}\nMy name is {agent_name}. I will be your agent for today\n")

def get_user_question():
    signal.alarm(20)
    try:
        question = input(f"{ask_user[randint(0, len(ask_user)-1)]} ")
        signal.alarm(0)
        return question
    except Exception:
        signal.alarm(0)  # Reset the alarm if an exception occurs
        raise

def json_to_dictionary():
    f = open("prompts_and_response.json")
    keyword_response_dict = json.load(f)
    return keyword_response_dict

def analyze_user_question(prompt):
    data = json_to_dictionary() 
    # keywords_arr = [keyword for keyword in data['keywords']]
    prompt_arr = prompt.split(' ')
    found_keyword = None
    found_word = None

    for k, v in data['keywords'].items():
        if  k in prompt_arr:
            found_keyword = True
            found_response = v
            break
        else:
            random_arr = data['keywords']["random"]
            found_keyword = False
            found_response = random_arr[randint(0, len(random_arr) - 1)]

    if found_keyword:
        print(found_response)
    else:
        random_arr = data['keywords']["random"]
        print(random_arr[randint(0, len(random_arr) - 1)])
    
    return found_response

def create_log(file_name, question, answer):

        f = open(file_name, mode="a")
        question_answer_dict = {}
        question_answer_dict[question] = answer
        for k, v in question_answer_dict.items():
            string = f"{k}:\t{v}\n"
            f.write(string)
        f.close() 

welcome_to_application()
display_greeting()

def main_loop():
    while True:
        get_help = get_user_question()
        if get_help.lower() in terminate_msgs:
            print("THANK YOU FOR USING APP")
            break
        else:
            ans = analyze_user_question(get_help)
            create_log("log.txt", get_help, ans)
            continue

main_loop()
