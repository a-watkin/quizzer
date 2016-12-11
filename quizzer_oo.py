import sqlite3
import random
from tkinter import *
from tkinter import ttk

class Quizzer(object):

    def __init__(self):
        self.country_list = []
        self.capital_list = []
        self.country_capital = {}
        self.target_country = ''


        # set up the country and capital dict
        # country_list = []
        # capital_list = []
        # country_capital = {}
        # target_country = ''
        # question_list = []

        # connect to the database
        country_db="./country_database.db"
        connection=sqlite3.connect(country_db)
        cursor=connection.cursor()

        # query the database and return all matching values
        cursor.execute('select country_name from country where has_capital=1')
        rows=cursor.fetchall()


        # iterate over the rows and put them into a list
        for x in rows:
            x = str(x)
            x = x[2:-3]
            self.country_list.append(x)

        # query the database and return all matching values
        cursor.execute('select capital_city from country where has_capital=1')
        for x in cursor:
            x = str(x)
            x = x[2:-3]
            # print(x)
            self.capital_list.append(x)

        # create the dict
        for x in range(len(self.country_list)):
            self.country_capital[self.country_list[x]] = self.capital_list[x]

    def get_question_list(self):
        question_list = []
        country_capital = self.country_capital
        self.target_country = random.choice(list(country_capital.keys()))

        question_list.append(country_capital[self.target_country])

        x = random.choice(list(country_capital.values()))
        # print(len(question_list))
        while len(question_list) < 4:
            x = random.choice(list(country_capital.values()))
            if x in question_list:
                pass
            else:
                question_list.append(x)

        random.shuffle(question_list)

        question_string = 'What is the capital of {}?'.format(self.target_country)

        return question_string, question_list 

        # print('What is the capital of {}?'.format(self.target_country))
        # print( 'A. {} \nB. {} \nC. {} \nD. {} \n'.format(
        # question_list[0], question_list[1], question_list[2], question_list[3]) )
        
        # i think maybe the gui class should be responsible for the text.
        # def get_label():
        #     label = ttk.Label(root, text = 
        #     target_string)
        #     label.config(justify = CENTER)
        #     # label.config(font = ('Calibri', 18, 'bold'))

        #     label.grid(row = 0, column = 1, columnspan = 4)
        #     label.grid(row=0, column=1, padx=20, pady=20)


    # def get_result(self, value):
    #     if value == self.country_capital[self.target_country]:
    #         return True
    #     else:
    #         return False


def main():


    blah = Quizzer()
    blah.get_question_list()

    meh = Quizzer()
    # print(meh.get_question_list())

    # print(blah.target_country)
    # print(blah.get_question_list())
    # blah.get_question_list()

    whatis = blah.get_question_list()
    # print(whatis)
    # print('target country: {}\n'.format(whatis[0]))
    
    # print(whatis[0])

    # print(whatis[1][0])
    # print(whatis[1][1])
    # print(whatis[1][2])
    # print(whatis[1][3])





    

if __name__ == '__main__':
    main()
