import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    
    def __init__(self, quiz_interface: QuizBrain):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz_interface_gestor = quiz_interface
        
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.set_score()
        
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=200,
            text="Some Question...",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.true_image = tk.PhotoImage(file="/Users/antonyferreira/Documents/Bootcamp_Python/Day34/true.png")
        self.true_button = tk.Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        
        self.false_image = tk.PhotoImage(file="/Users/antonyferreira/Documents/Bootcamp_Python/Day34/false.png")
        self.false_button = tk.Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)    

        self.get_next_question()
        
        self.window.mainloop()
          
    def answer_true(self, is_right):
        # desativa os botões logo que o usuário responde
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        # verifica resposta e mostra feedback
        self.get_feedback(is_right)
        
    def get_next_question(self):
        if self.quiz_interface_gestor.still_has_questions():
            q_text = self.quiz_interface_gestor.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")

        # reativa os botoes
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"Total Score: {self.quiz_interface_gestor.score}/{self.quiz_interface_gestor.total_questions}"
            )
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_pressed(self):
            is_right = self.quiz_interface_gestor.check_answer(user_answer="true")
            self.answer_true(is_right)
    
    def false_pressed(self):
            is_right = self.quiz_interface_gestor.check_answer(user_answer="false")
            self.answer_true(is_right)
        
    def get_feedback(self, is_right):
            if is_right:
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.window.after(800, self.get_next_question)
            self.set_score()

    def set_score(self):
        total_questions = self.quiz_interface_gestor.total_questions
        self.score_label.config(text=f"Score: {self.quiz_interface_gestor.score}/{total_questions}")

    