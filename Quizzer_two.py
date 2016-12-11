from tkinter import *
from tkinter import ttk
from quizzer_oo import Quizzer


class Feedback():

    def __init__(self, master):

        self.master = master
        self.label_text = None
        self.blah = Quizzer()

        # so this is how you do the title
        master.title('Quizzer')
        master.resizable(False, False)

    def show_start(self):

        # self.label.config(text = "this is the second welcome screen")
        self.label = ttk.Label(
            self.master, text="Hello and welcome.\nThis is a small quiz app. \nThat will help you learn the capital cities of countries.")
        self.label.config(justify=CENTER)
        self.label.config(font=('Calibri', 18, 'bold'))

        self.label.grid(row=0, column=1, columnspan=4)
        self.label.grid(row=0, column=1, padx=20, pady=20)

        self.button_continue = ttk.Button(self.master, text='Continue', padding=(150, 100),
                                 command=self.show_questions)
        self.button_continue.grid(row=1, column=1, stick='nsew', columnspan=2)

        self.button_quit = ttk.Button(self.master, text='Quit', padding=(150, 100),
                                 command=self.master.destroy)
        self.button_quit.grid(row=1, column=3, stick='nsew', columnspan=2)

    def show_questions(self):
        self.label.destroy()
        self.button_continue.destroy()
        self.button_quit.destroy()

        # Set the questions up.
        whatis = self.blah.get_question_list()

        question_text = whatis[0]
        button_a_text = whatis[1][0]
        button_b_text = whatis[1][1]
        button_c_text = whatis[1][2]
        button_d_text = whatis[1][3]

        self.label = ttk.Label(self.master, text=question_text)
        self.label.config(justify=CENTER)
        self.label.config(font=('Calibri', 18, 'bold'))

        self.label.grid(row=0, column=1, columnspan=4)
        self.label.grid(row=0, column=1, padx=20, pady=40)

        self.button_a = ttk.Button(self.master, text=button_a_text, padding=(150, 50),
                                   command=lambda: self.check_win(button_a_text))
        self.button_a.grid(row=1, column=1, stick='nsew', columnspan=2)

        self.button_b = ttk.Button(self.master, text=button_b_text, padding=(150, 50),
                                   command=lambda: self.check_win(button_b_text))
        self.button_b.grid(row=1, column=3, stick='nsew', columnspan=2)

        self.button_c = ttk.Button(self.master, text=button_c_text, padding=(150, 50),
                                   command=lambda: self.check_win(button_c_text))
        self.button_c.grid(row=2, column=1, stick='nsew', columnspan=2)

        self.button_d = ttk.Button(self.master, text=button_d_text, padding=(150, 50),
                                   command=lambda: self.check_win(button_d_text))
        self.button_d.grid(row=2, column=3, stick='nsew', columnspan=2)

    def check_win(self, value):
        # print(value)
        if value == self.blah.country_capital[self.blah.target_country]:
            # print('yes?')
            self.show_win()
        else:
            # print('no?')
            self.show_lose()

    def show_win(self):
        self.button_a.destroy()
        self.button_b.destroy()
        self.button_c.destroy()
        self.button_d.destroy()

        self.label.destroy()
        self.label = ttk.Label(
            self.master, text='Well done!\n The capital of {} is {}!\n Do you want to continue?'.format(self.blah.target_country,
                self.blah.country_capital[self.blah.target_country]))
        self.label.config(justify=CENTER)
        self.label.config(font=('Calibri', 18, 'bold'))

        self.label.grid(row=0, column=1, columnspan=4)
        self.label.grid(row=0, column=1, padx=20, pady=20)

        self.button_continue = ttk.Button(self.master, text='Continue', padding=(150, 100),
                                 command=self.show_questions)
        self.button_continue.grid(row=1, column=1, stick='nsew', columnspan=2)

        self.button_quit = ttk.Button(self.master, text='Quit', padding=(150, 100), 
                                command=self.master.destroy)
        self.button_quit.grid(row=1, column=3, stick='nsew', columnspan=2)

    def show_lose(self):
        self.button_a.destroy()
        self.button_b.destroy()
        self.button_c.destroy()
        self.button_d.destroy()
        self.button_continue.destroy()
        self.button_quit.destroy()

        self.label.destroy()
        self.label = ttk.Label(
            self.master, text='That is incorrect.\nThe capital of {} is {}!\n Do you want to continue?'.format(self.blah.target_country,
                                                                                                                 self.blah.country_capital[self.blah.target_country]))
        self.label.config(justify=CENTER)
        self.label.config(font=('Calibri', 18, 'bold'))

        self.label.grid(row=0, column=1, columnspan=4)
        self.label.grid(row=0, column=1, padx=20, pady=20)

        self.button_continue = ttk.Button(self.master, text='Continue', padding=(150, 100),
                                 command=self.show_questions)
        self.button_continue.grid(row=1, column=1, stick='nsew', columnspan=2)

        self.button_quit = ttk.Button(self.master, text='Quit', padding=(150, 100),
                                 command=self.master.destroy)
        self.button_quit.grid(row=1, column=3, stick='nsew', columnspan=2)


def main():

    blah = Quizzer()
    root = Tk()
    feedback = Feedback(root)
    feedback.show_start()
    root.mainloop()

if __name__ == '__main__':
    main()
