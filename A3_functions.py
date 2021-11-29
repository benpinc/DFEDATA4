# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)

# def gradescore(inputscore1,inputscore2,inputscore3):
#     totalscorepercent = (inputscore1 + inputscore2 + inputscore3) / 175 * 100
#     return totalscorepercent


# stu = input("NAME: ")
# hws = int(input("HOMEWORK: "))
# ass = int(input("ASSESMENT: "))
# fin = int(input("FINAL EXAM: "))

# returnpercentscore = gradescore(hws, ass, fin)
# print(stu,returnpercentscore)

def score(input1,input2,input3):
    percentage = (input1 + input2 + input3) / 175 *100
    return percentage

name = input("Your Name: ")
score1 = int(input("Score 1"))
score2 = int(input("Score 2"))
score3 = int(input("Score 3"))


the_score = score(score1,score2,score3)
print (name,the_score)

# cool_cows = "Winnie the Moo", "Moolan", "Milkshake", "Mooana"
# print(cool_cows[0])
# print(cool_cows[1])
# print(cool_cows[2])
# print(cool_cows[3])
# #
# cool_cows = ["Winnie the Moo", "Daisy", "Boomer"]
# cool_sheep = ["Baa Baa", "Boo Boo", "Bee Bee"]

# cool_animals = [cool_cows, cool_sheep]
# print(cool_animals[1][2])
