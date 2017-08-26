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

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM question_1').fetchall()
            return len(result)

    def insert_answers(self, survey_id, *answers):
        """ Добавляем ответы в бд """
        with self.connection:
            self.cursor.execute('INSERT INTO question_5(survey_id, text) VALUES(%s, %s)', (survey_id, answers[0]))

    def get_datetime(self):
        with self.connection:
            return self.cursor.execute("SELECT datetime('now', 'localtime')")

    def close(self):
        """ Закрываем текущее соединение с бд """
        self.connection.close()