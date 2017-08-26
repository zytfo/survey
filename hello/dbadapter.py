# -*- coding: utf-8 -*-
import psycopg2

class DBAdapter:

    def __init__(self):
        self.connection = psycopg2.connect(
                database="dcrer4f7hatr58",
                user="wngxswjyulxtwx",
                password="2b09bd90d6261888f0415ca2b3ae8eb11df089812f5354934e4ca696d31036c2",
                host="ec2-79-125-13-42.eu-west-1.compute.amazonaws.com",
                port="5432"
            )
        self.cursor = self.connection.cursor()

    def get_next_id(self):
        """ Находим id следующего опроса """
        with self.connection:
            self.cursor.execute('SELECT max(survey_id) FROM question_5')
            result = self.cursor.fetchone()[0]
            return 1 if result == None else result + 1

    def insert_answers(self, survey_id, *answers):
        """ Добавляем ответы в бд """
        with self.connection:
            question1 = [False for i in range(8)]
            for i in answers[0]:
                question1[int(i)] = True;
            self.cursor.execute('INSERT INTO question_1(survey_id, choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8)'
                ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (survey_id, *question1))
            self.cursor.execute('INSERT INTO question_2(survey_id, level) VALUES(%s, %s)', (survey_id, answers[1]))
            self.cursor.execute('INSERT INTO question_3(survey_id, choice_id) VALUES(%s, %s)', (survey_id, answers[2]))
            self.cursor.execute('INSERT INTO question_4(survey_id, choice_id) VALUES(%s, %s)', (survey_id, answers[3]))
            self.cursor.execute('INSERT INTO question_5(survey_id, text) VALUES(%s, %s)', (survey_id, answers[4]))

    def get_results(self):
        ''' Получаем данные опроса '''
        with self.connection:
            self.cursor.execute('SELECT * FROM question_1 ORDER BY survey_id')
            question1 = self.cursor.fetchall()
            self.cursor.execute('SELECT * FROM question_2 ORDER BY survey_id')
            question2 = self.cursor.fetchall()
            self.cursor.execute('SELECT * FROM question_3 ORDER BY survey_id')
            question3 = self.cursor.fetchall()
            self.cursor.execute('SELECT * FROM question_4 ORDER BY survey_id')
            question4 = self.cursor.fetchall()
            self.cursor.execute('SELECT * FROM question_5 ORDER BY survey_id')
            question5 = self.cursor.fetchall()
            return { 'question1': question1, 'question2': question2, 'question3': question3, 'question4': question4, 'question5': question5 }

    def get_datetime(self):
        with self.connection:
            return self.cursor.execute("SELECT datetime('now', 'localtime')")

    def close(self):
        """ Закрываем текущее соединение с бд """
        self.connection.close()