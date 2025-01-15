# import signal
# from sys import exit

# def trap():
#     print("You've fallen into a trap,you have 10 seconds to type the word \"Get me out\"")
#     signal.signal(signal.SIGALRM, die)
#     signal.alarm(10)

#     user_input = input("> ")
#     right_choice = "Get me out"

#     if *SOME CODE*:
#         *MORE CODE*
#         signal.alarm(0)

# def die(signum, frame):
#     print "Try again"
#     signal.alarm(0)
#     exit(0)
