from words import words_list
import random

not_solved = True
expected_word = ["-","-","-","-","-"]
correct_letters_unplaced = []
correct_letters = []


def _solve_word(words_list):
    counter = 0
    status = 1
    while not_solved:

        counter +=1
        if counter > 6:
            print("Hard Luck...Better luck next time...")
            status = 0
            break
        if len(words_list)==0:
            print("Our Bad...Retry please")
            status = 0
            break
        
        print(f"Chance number {counter}")
        wrong_letters = []
        messed_word = ["-","-","-","-","-"]
        
        probability_to_hit = '{0:.2f}'.format((1/len(words_list)*100))
        print(f"The probability to hit the word is {probability_to_hit} %")
        
        random_word = random.choice(words_list)
        print(f"Try the word : {random_word}")
        response = input("Enter the response you got in order...\n y for yellow, g for green, w for white...\n")
        
        while len(response) != 5:
            print("Your response is not correct please repeat")
            response = input("Enter the response you got in order...\n y for yellow, g for green, w for white...\n")
        
        if 'wwwww' in response:
            for letter in random_word:
                wrong_letters.append(letter)
        elif 'ggggg' in response:
            break
        else:
            for res in range(len(response)):
                if response[res] == 'w':
                    wrong_letters.append(random_word[res])
                elif response[res] == 'g':
                    expected_word[res] = random_word[res]
                    correct_letters.append(random_word[res])
                elif response[res] == 'y':
                    correct_letters_unplaced.append(random_word[res])
                    messed_word[res] = random_word[res]

        for letter in correct_letters_unplaced:
            for elem in list(words_list):
                if letter not in elem:
                    words_list.remove(elem)

        for letter in range(len(expected_word)):
            for elem in list(words_list):
                if expected_word[letter] != "-":
                    if elem[letter] != expected_word[letter]:
                        words_list.remove(elem)
        
        for letter in range(len(messed_word)):
            for elem in list(words_list):
                if messed_word[letter] != "-":
                    if elem[letter] == messed_word[letter]:
                        words_list.remove(elem) 

        for letter in wrong_letters:
            for elem in list(words_list):
                if letter in elem and letter not in correct_letters_unplaced and letter not in correct_letters:
                    words_list.remove(elem)
        
        print("----------------------------------------------------")

        if expected_word != ["-","-","-","-","-"]:
            print("The expected word should be something like", *expected_word)

    if status != 0:
        print(f"GG Done! Solved in {counter} chances.")

_solve_word(words_list)