#by petrucciii

import tkinter as tk 

#window settings
root = tk.Tk()
root.geometry("850x420")
root.resizable(False,False)
root.configure(bg="gray12")
root.title("Quiz")

#car quiz
class CarQuiz():

    #title
    tk.Label(root, text="Quiz Sulle Auto", fg="cyan1", bg="gray12", font=("",20)).pack()

    #questions
    class Questions():

        #first question
        def first_question():
            question_1 = tk.Label(root, text="1.Quando è stata messa in commercio la prima auto? ", fg="cyan1", bg="gray12", font=("",10)).place(x=10,y=70)
            first_solution = tk.StringVar()
            answer_1 = tk.Entry(root, textvar=first_solution, fg="white", bg="gray12", font=("",10)).place(x=330,y=72)

            #second question
            def second_question():
                question_2 = tk.Label(root, text="2.Qual'è la macchina piú veloce al mondo?", fg="cyan1", bg="gray12", font=("",10)).place(x=10,y=130)
                second_solution = tk.StringVar()
                answer_2 = tk.Entry(root, textvar=second_solution, fg="white", bg="gray12", font=("",10)).place(x=300,y=132)

                #third_password
                def third_question():
                    question_3 = tk.Label(root, text="3.Qual'è il cognome dei fondatori del famosissimo marchio di automobili FIAT?", fg="cyan1", bg="gray12", font=("",10)).place(x=10,y=190)
                    third_solution = tk.StringVar()
                    answer_3 = tk.Entry(root, textvar=third_solution, fg="white", bg="gray12", font=("",10)).place(x=490,y=192)

                    #fourth_password
                    def fourth_question():
                        question_4 = tk.Label(root, text="4.Quale marchio italiano di macchine è in Formula 1?", fg="cyan1", bg="gray12", font=("",10)).place(x=10,y=250)
                        fourth_solution = tk.StringVar()
                        answer_4 = tk.Entry(root, textvar=fourth_solution, fg="white", bg="gray12", font=("",10)).place(x=360,y=252)

                        #fifth question
                        def fifth_question():
                            question_5 = tk.Label(root, text="5.In che anno è stata inventata la prima macchina a metano?", fg="cyan1", bg="gray12", font=("",10)).place(x=10,y=310)
                            fifth_solution = tk.StringVar()
                            answer_5 = tk.Entry(root, textvar=fifth_solution, fg="white", bg="gray12", font=("",10)).place(x=400,y=312)            

                            #enter button settings
                            def but_enter():

                                #first solution
                                if first_solution.get() == "1894" or first_solution.get() == "Nel 1894":
                                    tk.Label(root, text="Corretto  ", fg="green", bg="gray12", font=("",10)).place(x=480,y=72)
                                    p_1 = 1
                                else:
                                    tk.Label(root, text="Sbagliato", fg="red", bg="gray12", font=("",10)).place(x=480,y=72)
                                    p_1 = 0

                                #second solution
                                if second_solution.get() == "Koenigsegg Jesko Absolut" or second_solution.get() == "Jesko Absolut":
                                    tk.Label(root, text="Corretto  ", fg="green", bg="gray12", font=("",10)).place(x=450,y=132)
                                    p_2 = 1
                                else:
                                    tk.Label(root, text="Sbagliato", fg="red", bg="gray12", font=("",10)).place(x=450,y=132)
                                    p_2 = 0

                                #third solution
                                if third_solution.get() == "Agnelli":
                                    tk.Label(root, text="Corretto  ", fg="green", bg="gray12", font=("",10)).place(x=660,y=192)
                                    p_3 = 1
                                else:
                                    tk.Label(root, text="Sbagliato", fg="red", bg="gray12", font=("",10)).place(x=660,y=192)
                                    p_3 = 0

                                #fourth solution
                                if fourth_solution.get() == "Ferrari" or fourth_solution.get() == "La Ferrari":
                                    tk.Label(root, text="Corretto  ", fg="green", bg="gray12", font=("",10)).place(x=530,y=252)
                                    p_4 = 1
                                else:
                                    tk.Label(root, text="Sbagliato", fg="red", bg="gray12", font=("",10)).place(x=530,y=252)
                                    p_4 = 0

                                #fifth solution
                                if fifth_solution.get() == "1930" or fifth_solution.get() == "Nel 1930":
                                    tk.Label(root, text="Corretto  ", fg="green", bg="gray12", font=("",10)).place(x=560,y=312)
                                    p_5 = 1
                                else:
                                    tk.Label(root, text="Sbagliato", fg="red", bg="gray12", font=("",10)).place(x=560,y=312)
                                    p_5 = 0
                        
                                #score
                                def score():
                                    score = p_1+p_2+p_3+p_4+p_5
                                    
                                    if score == 5:
                                        tk.Label(root, text=f"Punteggio: {score}/5", fg="green", bg="gray12", font=("",10)).place(x=380,y=340)
                                    elif score == 4:
                                        tk.Label(root, text=f"Punteggio: {score}/5", fg="green", bg="gray12", font=("",10)).place(x=380,y=340)
                                    elif score == 3:
                                        tk.Label(root, text=f"Punteggio: {score}/5", fg="orange", bg="gray12", font=("",10)).place(x=380,y=340)
                                    elif score == 2:
                                        tk.Label(root, text=f"Punteggio: {score}/5", fg="orange", bg="gray12", font=("",10)).place(x=380,y=340)
                                    elif score == 1:
                                        tk.Label(root, text=f"Punteggio: {score}/5", fg="red", bg="gray12", font=("",10)).place(x=380,y=340)
                                    elif score == 0:
                                        tk.Label(root, text=f"Punteggio: {score}/5", fg="red", bg="gray12", font=("",10)).place(x=380,y=340)
                                    else:
                                        tk.Label(root, text=f"Punteggio: {score}/5", fg="cyan1", bg="gray12", font=("",10)).place(x=380,y=340)
                                          
                                score()
                        
                            but_1 = tk.Button(root, text="Invia", fg="gray", bg="black", command=but_enter).place(x=400,y=380)

                        fifth_question()

                    fourth_question()

                third_question()
            
            second_question()

        first_question()
    
    Questions()

if __name__ == "__main__":
    CarQuiz()
    root.mainloop()
