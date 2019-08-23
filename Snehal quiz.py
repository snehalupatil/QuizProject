

import os
import json

FILENAMES = {'SPORT': 'sport.json', 'MATH': 'math.json'}
QUIZDATA = {1: 'MATH', 2:'SPORT'}

def __openFile(fileFlag):
    sourceJsonPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAMES[fileFlag])
    with open(sourceJsonPath, 'r') as f:
        distros_dict = json.load(f)
        return distros_dict

def quiz():
    print("Select quiz : \n 1. Math quiz \n 2. Sport quiz")
    choice = int(input("Enter your choice : "))
    cnt=0
    if choice in QUIZDATA.keys():
        quizData = __openFile(QUIZDATA[choice])
        for question in quizData.keys():
            print(quizData[question]['q'])
            for key, value in quizData[question]['opt'].items():
                print("{} : {}".format(key, value))

            a=int(input('Enter correct option:'))
            b=quizData[question]['answer']
            if a==int(b):
                print('Your answer is Correct')
                cnt+=1
            else:
                print('Entered option is wrong.....Correct option is',b)
            print('-------------------------------')
                
        print('**** Your Score is',cnt,' out of 5 ****')
                
        
                
                
    else:
        print("You entered wrong option")

def main():
    quiz()

if __name__ == '__main__':
    main()
