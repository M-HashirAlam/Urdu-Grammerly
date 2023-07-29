import re
import joblib
import sqlite3

clf = joblib.load('urdu_tense_model.pkl')
vectorizer = joblib.load('urdu_tense_vectorizer.pkl')
classifier = joblib.load('no-noun-dis.joblib')
vectorizer1 = joblib.load('no-noun-disv.joblib')

def parese_sentence(sentence):
    tags = []
    res = re.findall(r"[^۔!?]+", sentence)

    def gender(sentence):
        feminine = ['بچی', 'لڑکی', 'امی', 'بہن', 'بیٹی', 'نانی', 'دادی', 'بیوی', 'دوست', 'بیٹیاں', 'بیٹیاں', 'بھابھی',
                    'خالہ',
                    'خیالی بہن', 'صاحبہ', 'نوکرانی', 'رفیقہ']
        masculine = ['ابو', 'لڑکا', 'بھائی', 'بیٹا', 'دادا', 'دادو', 'داماد', 'دوست', 'بیٹے', 'پوتر', 'شوہر', 'بچہ',
                     'عمو',
                     'خیالی بھائی', 'صاحب', 'نوکر', 'رفیق']

        # sentence = input("Enter a sentence: ")
        res = re.findall(r"[^۔!?]+", sentence)
        for sent in res:

            words = sent.split()
            for i in words:
                if i in feminine:
                    #         print('h')

                    pattern = r"(تی|رہی)"
                    #         pattern = r"(تی)"
                    match = re.search(pattern, sentence)

                    if not match:
                        tags.append(f'Grammatical Error -- Gender Disagreement: {sent}')
                        print(f'Grammatical Error -- Gender Disagreement: {sent}')
                    # else:
                    #     print(f"Gramatical Error: {sent}")
                elif i in masculine:
                    #         print('h')

                    pattern = r"( تا|رہا| رہے)"
                    #
                    match = re.search(pattern, sentence)

                    if not match:
                        tags.append(f"Grammatical Error -- Gender Disagreement: {sent}")
                        print(f"Grammatical Error -- Gender Disagreement: {sent}")
                    # else:
                    #     print(f"Gramatical Error: {sent}")

    def tense(sentence):
        res = re.findall(r"[^۔!?]+", sentence)
        for sent in res:
            # Predict the tense of a new sentence
            # new_sentence = input("Enter Sentence: ")
            tense_ = clf.predict(vectorizer.transform([sent]))[0]
            print(f"Tense of '{sent}' is {tense_}")
            tags.append('\n')
            tags.append("           Tense:\n               ")
            tags.append('\n')
            tags.append(f"Tense of '{sent}' is {tense_}\n")
    def no_noun(sentence):
        # input_sentence = input('Enter a sentence: ')
        res = re.findall(r"[^۔!?]+", sentence)
        for sent in res:

        # Check if the input contains any digits using regular expression
            if re.search(r'\d', sent):
                input_vec = vectorizer1.transform([sent])
                prediction = classifier.predict(input_vec)[0]
                if prediction == 'not correct':
                    prediction = 'Number-Noun Disagreement'
                    tags.append(f"Grammatical Error -- Number-Noun Disagreement: {sent}")
                print(prediction)







    class Node1:
        def __init__(self, label):
            self.label = label
            self.children = []

        def add_child(self, child):
            self.children.append(child)

        def __repr__(self):
            if not self.children:
                return f'{self.label}()'
            return f'{self.label}({", ".join(str(c) for c in self.children)})'

    class Data:
        def __init__(self):
            conn = sqlite3.connect('Urdu_Db.db')
            c = conn.cursor()

            c.execute('''SELECT *
    FROM (
    SELECT words
    FROM table_name
    WHERE tags = 'اسم نکرہ'
    UNION
    SELECT words
    FROM table_name
    WHERE tags ="اسم معرفہ "
    UNION
    SELECT words
    FROM table_name
    WHERE tags = "اسم ضمیر  "
    ) ''')
            results = c.fetchall()
            self.noun = [row[0] for row in results]
            self.noun.append('لڑکی')
            self.noun.append('لڑکا')
            self.noun.append('سائیکل')
            self.noun.append("کتاب")
            c.execute("SELECT * FROM 'table_name' where tags='اسم صفت ' ")
            result1 = c.fetchall()
            self.adjective = [row[0] for row in result1]
            # print(words_list)
            # c.execute("SELECT * FROM 'table_name' where tags='فعل ' ")
            c.execute('''Select * from(
                SELECT words,tags FROM 'table_name' WHERE tags='فعل '
                UNION
                SELECT words,tags FROM 'table_name' WHERE tags='معاون فعل '
                )
            ''')
            result2 = c.fetchall()
            self.verb = [row[0] for row in result2]
            self.verb.append('رو')
            self.verb.append('چلا')
            self.verb.append("پڑھتا")
            # print(verb)
            c.execute("SELECT * FROM 'table_name' where tags='حرف ربط ' ")
            result3 = c.fetchall()
            self.prep = [row[0] for row in result3]

    class Node:
        def __init__(self, label, children=None):
            self.label = label
            self.children = [] if children is None else children

        def __str__(self):
            return f'{self.label}({",".join(str(c) for c in self.children)})'

    class UrduParser(Data):
        def __init__(self):
            self.data = Data()

        def parse_sentence(self, sentence):
            words = sentence1.split()
            root = Node('S', [])

            i = 0

            while i < len(words):
                # if words[i] in ['میں', 'تم', 'وہ']:
                if words[i] in self.data.noun:

                    root.children.append(Node('NP', [Node(words[i])]))
                # elif words[i] in ['ایک', 'وہ', 'یہ']:
                elif words[i] in self.data.noun:
                    if root.children[-1].label != 'NP':
                        raise ValueError('Sentence does not follow SOV ')
                    root.children[-1].children.append(Node('Det', [Node(words[i])]))
                # elif words[i] in ['کتاب', 'کام', 'گھر']:
                elif words[i] in self.data.noun:
                    if root.children[-1].label != 'NP' or not root.children[-1].children:
                        raise ValueError('Sentence does not follow SOV')
                    n_node = Node('N', [Node(words[i])])
                    # check if there are any adjectives following the noun
                    j = i + 1
                    # while j < len(words) and words[j] in ['بڑی', 'چھوٹی', 'سفید', 'کالی']:
                    while j < len(words) and words[j] in self.data.adjective:
                        n_node.children.append(Node('Adj', [Node(words[j])]))
                        j += 1
                    root.children[-1].children.append(n_node)
                    i = j - 1
                # elif words[i] in ['پڑھتا', 'چلتی', 'آتا']:
                elif words[i] in self.data.verb:
                    root.children.append(Node('VP', [Node(words[i])]))
                # elif words[i] in ['بہت', 'جلدی', 'زیادہ']:
                elif words[i] in self.data.adjective:
                    if root.children[-1].label != 'VP' or not root.children[-1].children:
                        raise ValueError('Sentence does not follow SOV')
                    root.children[-1].children.append(Node('Adv', [Node(words[i])]))
                elif words[i] == 'ہوں':
                    if root.children[-1].label != 'VP' or not root.children[-1].children:
                        raise ValueError('Sentence does not follow SOV')
                    root.children[-1].children.append(Node('V', [Node(words[i])]))
                elif words[i] == 'ہے':
                    if root.children[-1].label != 'VP' or not root.children[-1].children:
                        raise ValueError('Sentence does not follow SOV')
                    root.children[-1].children.append(Node('V', [Node(words[i])]))
                elif words[i] == 'رہا':
                    if root.children[-1].label != 'V' or not root.children[-1].children:
                        raise ValueError('Sentence does not follow SOV')
                    root.children[-1].label = 'VP'
                    root.children[-1].children.append(Node(words[i]))
                elif words[i] == 'رہی':
                    if root.children[-1].label != 'V' or not root.children[-1].children:
                        raise ValueError('Sentence does not follow SOV')
                    root.children[-1].label = 'VP'
                    root.children[-1].children.append(Node(words[i]))
                # elif words[i] in ['نے', 'ساتھ', 'کے', 'پر']:
                elif words[i] in self.data.prep:
                    if root.children[-1].label != 'NP' or not root.children[-1].children:
                        raise ValueError('Sentence does not follow SOV')
                    pp = Node('PP', [Node(words[i])])
                    # if words[i + 1] in ['بڑی', 'چھوٹی', 'سفید', 'کالی']:
                    if words[i + 1] in data.adjective:
                        pp.children.append(Node('Adj', [Node(words[i + 1])]))
                        i += 1
                    root.children[-1].children.append(pp)
                else:
                    raise ValueError(f'Invalid word: {words[i]}')
                i += 1

            if not root.children or root.children[-1].label != 'VP':
                raise ValueError('Sentence does not follow SOV')
            return root

        def print_tree(self, node, level=0):
            print(' ' * level + str(node))

    def parse_1(sentence):
        sentence = sentence.strip()
        words = re.findall(r'\b\w+\b', sentence)
        tree = Node1('S')
        np = None
        vp1 = None
        vp2 = None
        for word in words:
            if word in data.noun:
                if np is not None:
                    tree.add_child(np)
                    np = None
                np = Node1('NP')
                np.add_child(Node1(word))
            elif word in data.noun:
                if np is None:
                    np = Node('NP')
                np.add_child(Node1(word))
            elif word in data.verb:
                if vp1 is None:
                    vp1 = Node1('VP')
                    tree.add_child(vp1)
                vp1.add_child(Node1(word))
            elif word == 'اور':
                vp2 = Node('VP')
                tree.add_child(vp2)
            else:
                # print('h')
                raise ValueError('Sentence does not follow SOV')

        if np is not None:
            tree.add_child(np)
        if vp2 is not None:
            tree.add_child(vp2)
        return tree

    data = Data()
    parser = UrduParser()
    for sentence1 in res:
        gender(sentence1)
        tense(sentence1)
        no_noun(sentence1)

        # print(sentence1)

        # print(tree)
        try:
            tree1 = parse_1(sentence1)
            # tags.append('ok')
            # tags.append(tree1)
            print(tree1)
        except ValueError:
            # tags.append(f'Sentence does not follow SOV: {sentence1}')

            try:
                tree = parser.parse_sentence(sentence1)
                parser.print_tree(tree)
            except ValueError as e:
                tags.append('\n')
                tags.append("                    Sov: \n             ")
                tags.append('\n')
                tags.append(f'Sentence does not follow SOV: {sentence1}\n')
                tags.append("\n")
                tags.append("           Part Of Speech: \n          ")
                tags.append("\n")
                print(f'Sentence does not follow SOV: {e}')


    conn = sqlite3.connect('Urdu_Db.db')
    c = conn.cursor()
    # input_sent = input("Enter a sentence: ")
    w = sentence.split()

    for i in w:
        c.execute("SELECT tags FROM table_name WHERE words=?", (i,))
        ans = c.fetchone()
        tags.append('\n')

        if ans is None:
            tags.append(" ")
        else:

            tags.append(f"{ans} is {i}")
        # tags.append(" ")



    conn.close()
    return tags


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(parese_sentence(sentence))
