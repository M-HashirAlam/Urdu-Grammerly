import sqlite3

conn = sqlite3.connect('Urdu_Db.db')
c=conn.cursor()
f = open('wordlist.txt', "r+",encoding="utf-8")
x=f.read()
lst=x.split()
# print(lst)
#
#  c.execute("""CREATE TABLE Data1 (
#                 Words   TEXT
#                 )""")
#
# c . executemany ( """
# INSERT INTO Data (Words)
# VALUES (?)
# """ , zip(lst) )
# # c.execute("INSERT INTO Data1  VALUES ('Hashir Alam')")
# conn.commit()
# c.execute("Drop Table Data1 ")
# c.fetchall()

# name=input()


# c.execute("SELECT * FROM Data WHERE Words LIKE (?) ",(string,))
# c.execute("Select * from Data where Words %STARTSWITH 'p' ")
# print(c.fetchall())

# new_list = []
# for i in a:
#     for element in i:
#         new_list.append(element)
# print(new_list)

# for i in m:
#
#     c.execute("SELECT * FROM Data WHERE Words =? ",(i,))
#     a=(c.fetchall())
#     if a==[]:
#         print('foun',i)
#     new_list = []
#     for i in a:
#         for element in i:
#             new_list.append(element)
#     print(new_list)
# m=name.split() # whole line converted into words
# for i in m: #
#     first=i[0] # to get starting character
#     # print(first)
#     list = [first, "%"]
#     string = "".join(list)
#     c.execute("SELECT * FROM Data WHERE Words LIKE (?) ",(string,)) #qurey for extracting word starting with
#     red=c.fetchall()
#     #print(red)
#     # converting tuple into list
#     new_list = []
#     for t in red:
#         for element in t:
#             new_list.append(element)
#     # print(new_list)
#     if i in new_list:
#         print("found",i)
#     else:
#         print(" aanot found",i)
conn.commit()
conn.close()