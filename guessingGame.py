import random

def main():
    nums=generateNums()
    userAnswer =getuserInput()


    matchUserAnswer(userAnswer, nums)


def getuserInput():
    print('Welcome to the game \n guess 3 numbers')
    answer= input("Guess 3 numbers: ")
    answer = str(answer)
    userAnswer = []
    for i in range(len(str(answer))):
        userAnswer.append(str(answer[i]))
    return userAnswer


def generateNums():
    nums=[]
    while (len(nums) < 3):
        r= random.randint(0,9)
        nums.append(str(r))
    print(nums)
    return nums


def matchUserAnswer(userAnswer,nums):
    arrUser = userAnswer

    print(arrUser)

    for i in range(len(arrUser)):
        if nums[i]== arrUser[i]:
            print("correct in position " + str(i))
        elif nums[i] in arrUser:
            print("correct number + wrong position " + str(i))
        else:
            print('No correct nums  in position '  + str(i))


main()
