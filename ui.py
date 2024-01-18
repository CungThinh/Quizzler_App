THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20 ,background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, background="white")
        self.score_lable = Label(text= f"Score: 0", fg="white", background=THEME_COLOR)
        self.score_lable.grid(row=0, column=1, columnspan=2)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text= "Question here", 
            fill= THEME_COLOR, 
            font=("Arial",20,"italic"),
            width= 280 # Near equal to canvas 
            )
        self.canvas.grid(row=1, columnspan=2, pady= 50)

        true_button_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_button_img, command= self.true_pressed)
        self.true_button.grid(row=3, column=0)

        false_button_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_button_img, command = self.false_pressed)
        self.false_button.grid(row=3, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question_text, text = self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text= "You reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.show_result(is_right)
    
    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.show_result(is_right)

    def show_result(self, is_right):
        if is_right: 
            self.update_score_lable()
            self.canvas.config(background= "green")
        else:
            self.canvas.config(background= "red")
        self.window.after(1000, self.next_question)

    def update_score_lable(self):
        self.score_lable.config(text= f"Score: {self.quiz_brain.score}")