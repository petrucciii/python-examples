#by petrucciii

#try again
try_again = "Yes"

while try_again == "Yes":

    class PythonQuiz():

        #title
        print("Python Quiz")

        #first question
        def first_question():
            print("First Question")
            question_1 = input("Who made python? ")

            if question_1 == "Guido Van Rossum" or question_1 == "Guido Rossum":

                print("Correct")
        
            else:

                print("Incorrect")


        #second question
        def second_question():
            print("Second Question")
            question_2 = input("When was the first version of python published? ")

            if question_2 == "1991" or question_2 == "In 1991":

                print("Correct")

            else:

                print("Incorrect")
        

        #third question
        def third_question():
            print("Third Question")
            question_3 = input("In which programming language was python written? ")

            if question_3 == "C" or question_3 == "In C":

                print("Correct")

            else:

                print("Incorrect")


        #fourth question
        def fourth_question():
            print("Fourth Question")
            question_4 = input("What are the two most famous modules for web development in python? ")

            if question_4 == "Django Flask" or question_4 == "Django and Flask":

                print("Correct")

            else:

                print("Incorrect")
    

        first_question()

        second_question()

        third_question()

        fourth_question()


    #run the program
    PythonQuiz()

    try_again = input("Do you want try again? ")


