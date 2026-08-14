THEME_COLOR = "#375362"
from tkinter import *
import os
from quiz_brain import QuizBrain


class QuizeInterFace:
    def __init__(self, quiz_brain: QuizBrain):
        self.windows = Tk()
        self.quiz = quiz_brain
        self.windows.title("Quizzler")
        self.windows.minsize(height=500, width=500)
        self.windows.config(padx=20, pady=20)
        self.windows.config(bg=THEME_COLOR)
        self.score_label = Label(
            text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=288,
            text="Some question",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)

        self.basepath1 = os.path.dirname(__file__)
        self.filepath1 = os.path.join(self.basepath1, "images", "true.png")
        self.true_image = PhotoImage(file=self.filepath1)
        self.true_button = Button(
            image=self.true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(column=0, row=3)
        self.basepath2 = os.path.dirname(__file__)
        self.filepath2 = os.path.join(self.basepath1, "images", "false.png")
        self.false_image = PhotoImage(file=self.filepath2)
        self.false_button = Button(
            image=self.false_image, highlightthickness=0, command=self.flase_pressed
        )
        self.false_button.grid(column=1, row=3)
        self.next_question()
        self.windows.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, Text="You have reached end of the questions"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def flase_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.next_question)
