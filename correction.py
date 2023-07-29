import sys
import sqlite3
import _sqlite3


class correct:
    def __init__(self, name):
        conn = sqlite3.connect('Urdu_Db.db')
        self.c = conn.cursor()
        self.name = name

        # for whole line to convert into sigle word
        self.a = self.name.split(' ')
        # self.data_list=self.x.split()

    def search(self):
        m = self.name.split()  # whole line converted into words
        for i in m:  #
            first = i[0]  # to get starting character
            # print(first)
            list = [first, "%"]
            string = "".join(list)
            # qurey for extracting word starting with
            self.c.execute("SELECT * FROM Data WHERE Words LIKE (?) ", (string,))
            red = self.c.fetchall()
            # print(red)
            # converting tuple into list
            new_list = []
            for t in red:
                for element in t:
                    new_list.append(element)
            # print(new_list)
            if i in new_list:
                print("found", i)
            else:
                print("not found", i)

    def levenshtein(self, s1, s2):

        if len(s1) > len(s2):

            s1, s2 = s2, s1

        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(
                        1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    def find_closest_words(self, input_string, word_list):
        closest_words = []
        min_distance = 1  # sys.maxsize
        for word in word_list:
            distance = self.levenshtein(input_string, word)
            if distance < min_distance:
                min_distance = distance
                closest_words = [word]
            elif distance == min_distance:
                closest_words.append(word)
        return closest_words


# a=correct("گھروالوں نے اداکاری میں آنے سے کبھی منع نہیں کیا، سعود")
# a.search()
# print(a.levenshtein("wweeE"))
# print(a.find_closest_words())
# input_string = a.name
# closest_words = a.find_closest_words(input_string, word_list)
# print(closest_words)
# word_list=a.x.split()
# print(a.find_closest_words(input_string,word_list))
# print(a.search())
