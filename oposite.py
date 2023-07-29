import sqlite3

# Step 1: Connect to the SQLite database
db_path = 'Urdu_Db.db'


def Ner(word):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # a='O'
    # b=("DELETE FROM Ner WHERE NER = ?")
    #
    # cursor.execute(b, (a,))
    # conn.commit()
    query_select_with_param = "SELECT NER FROM Ner WHERE Word = ?;"
    cursor.execute(query_select_with_param, (word,))





    # Step 5: Fetch the data from the SELECT result
    result_set = cursor.fetchall()
    ner = [row[0] for row in result_set] if result_set else []
    ner_str = ', '.join(ner) if ner else "No کلاس found."
    print(ner_str)


    return ner_str


def get_synonyms_from_database(word):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query_select_with_param = "SELECT Synonym FROM same WHERE UrduWord = ?;"
    cursor.execute(query_select_with_param, (word,))
    result_set = cursor.fetchall()
    synonyms = [row[0] for row in result_set] if result_set else []
    synonyms_str = ', '.join(synonyms) if synonyms else "No مترادفات found."
    # print(synonyms_str)
    conn.close()
    return synonyms_str


def get_opposite_from_database(word):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query_select_with_param = "SELECT Word FROM oposite WHERE Opposite = ?;"
    query_select_with_param1 = "SELECT Opposite FROM oposite WHERE Word = ?;"

    # Execute the first query
    cursor.execute(query_select_with_param, (word,))
    result_set1 = cursor.fetchall()

    # Check if the first query returned any results
    if not result_set1:
        # Execute the second query
        cursor.execute(query_select_with_param1, (word,))
        result_set2 = cursor.fetchall()

        # Process the results from the second query
        opposites = [row[0] for row in result_set2] if result_set2 else []
        opposite_str = ', '.join(opposites) if opposites else "No متضاد found."
    else:
        # Process the results from the first query
        opposites = [row[0] for row in result_set1] if result_set1 else []
        opposite_str = ', '.join(opposites) if opposites else "No متضاد found."

    return opposite_str


def get_male_female_from_database(word):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query_select_with_param = "SELECT Male FROM mf WHERE Female = ?;"
    query_select_with_param1 = "SELECT Female FROM mf WHERE Male =?;"

    # Step 3: Execute the first query
    cursor.execute(query_select_with_param, (word, ))
    result_set1 = cursor.fetchall()

    # Step 4: Check if the first query returned any results
    if not result_set1:
        # Step 5: Execute the second query
        cursor.execute(query_select_with_param1, (word, ))
        result_set2 = cursor.fetchall()
        mf = [row[0] for row in result_set2] if result_set2 else []
        mf_str = ', '.join(mf) if mf else "No مذکر/مونث found."

    else:
        mf = [row[0] for row in result_set1] if result_set1 else []
        mf_str = ', '.join(mf) if mf else "No مذکر/مونث found."

    return mf_str


# Ner(user_input)
# same(user_input)
# oposite(user_input)
# mf(user_input)
# get_synonyms_from_database("طاقت")