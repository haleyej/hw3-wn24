# Your name: 
# Your student id:
# Your email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import random

# create a magic 8 ball class
class MagicEightBall():

    # create the constructor (__init__) method 
    # ARGUMENTS: 
    #       self: the current object
    #       answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers):
        pass 

    # Create the __str__ method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a string with all of the questions in the questions_history_list separated by commas
    #        iIf no questions have been asked, return an empty string
    def __str__(self):
        pass

    # Creates the get_fortune method
    # ARGUMENTS:
    #       self: the current object
    #       question: the question the user wants to ask the magic 8 ball
    # RETURNS: a string with the answer
    def get_fortune(self, question):
        pass 


    # Creates play_game method
    # ARGUMENTS:
    #   self: the current object
    # RETURNS: None
    def play_game(self):
        pass


    # Create the print_answer_frequencies method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: dictionary that maps answers to frequencies
    #          if no answers have been given, return an empty dictionary
    def print_answer_frequencies(self):
        pass

def test():
    answers_list = ['yes', 'no', 'maybe']
    eight_ball = MagicEightBall(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {eight_ball.answers_history_list}")
    print(f"Question History List: Expected: {[]}, Actual: {eight_ball.questions_history_list}")
    print(" ")

    print("Test __str__:")
    eight_ball.questions_history_list = ['will it snow today?', 'should I make soup?']
    expected = "will it snow today?, should I make soup?"
    print(f"Expected: {expected}, Actual: {str(eight_ball)}")
    print(" ")


    print("Testing return value of get_fortune:")
    res = eight_ball.get_fortune('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")

    print("Testing get_fortune:")
    eight_ball.answers_list = ['yes']
    res = eight_ball.get_fortune('test question 2')
    print(f"Expected: {'yes'}, Actual: {res}")
    print(" ")

    print("Testing that get_fortune adds answer index to answer_history_list:")
    eight_ball.answers_list = ['yes']
    eight_ball.answers_history_list = []
    eight_ball.get_fortune('test question 2')
    expected = [0]
    res = eight_ball.answers_history_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that get_fortune does not add 'I've already answered this question' to answer_history_list:")
    eight_ball.answers_list = ['yes']
    eight_ball.answers_history_list = [0]
    eight_ball.questions_history_list = ['test question 3']
    eight_ball.get_fortune('test question 3')
    expected = [0]
    res = eight_ball.answers_history_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


    print("Testing return value print_answer_frequencies")
    eight_ball.answers_list = ['yes', 'no', 'maybe']
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = type(eight_ball.print_answer_frequencies())
    print(f"Expected: {dict}, Actual: {res}")
    print(" ")

    print("Testing return value print_answer_frequencies keys")
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = type(list(eight_ball.print_answer_frequencies().keys())[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing print_answer_frequencies")
    eight_ball.answers_history_list = [0, 0, 0, 1, 1, 2]
    res = eight_ball.print_answer_frequencies()
    expected = {'yes': 3, 'no': 2, 'maybe': 1}
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

def main():
    # defines the possible answers

    # creates a MagicEightBall object

    # initiates the game play using the play_game method

    # shows the output of print_answer_frequencies

    pass



# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    # test() #TODO: Uncomment if you do the extra credit