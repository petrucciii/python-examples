#by petrucciii

try_again = "si"

#try again
while try_again == "si" or try_again == "Si":

    #car quiz
    class CarQuiz():

        #title
        print("Quiz Sulle Auto")

        #questions
        class Questions():

            #first question
            def first_question():
                question_1 = input("1.Quando è stata messa in commercio la prima auto? ")

                #solution
                if question_1 == "1984" or question_1 == "Nel 1894":
                    print("Corretto")
                else:
                    print("Sbagliato")

            #second question
            def second_question():
                question_2 = input("2.Qual'è la macchina piú veloce al mondo(2020)? ")

                #solution
                if question_2 == "Koenigsegg Jesko Absolut" or question_2 == "Jesko Absolut":
                    print("Corretto")
                else:
                    print("Sbagliato")

            #third question
            def third_question():
                question_3 = input("3.Qual'è il cognome dei fondatori del famosissimo marchio di automobili FIAT? ")

                #solution
                if question_3 == "Agnelli":
                    print("Corretto")
                else:
                    print("Sbagliato")

            #fourth question
            def fourth_question():
                question_4 = input("4.Quale marchio italiano di macchine è in Formula 1? ")

                #solution
                if question_4 == "Ferrari" or question_4 == "La Ferrari":
                    print("Corretto")
                else:
                    print("Sbagliato")

            #fifth question
            def fifth_question():
                question_5 = input("5.In che anno è stata inventata la prima macchina a metano? ")

                #solution
                if question_5 == "1930" or question_5 == "Nel 1930":
                    print("Corretto")
                else:
                    print("Sbagliato")
        
            first_question()
            second_question()
            third_question()
            fourth_question()
            fifth_question()

        Questions()


    try_again = input("Vuoi riprovare? ")