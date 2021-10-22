import json
from random import choice

## speel een tijdje met het spel
## analyseer en bereid de code uit met extra functionaliteit
## gebruik pickle of json module omm data op te slaan
## vraag om een vraag die leidt naar het juiste antwoord


def loadData(filename):
    file = open(filename, 'r')
    if filename.split('.')[-1]=='json':
        data = json.load(file)
    else:
        data=[]
        for row in file:
            if type(row)==type({}):
                data.append(row)
            else:
                data.append(file)
    file.close()
    return data

def writeData(filename, data):
    file = open(filename, 'w')
    if filename.split('.')[-1]=='json':
        json.dump(data, file)
    else:
        for row in data:
            file.write(row +'\n')
    file.close()

def newQuestion():
    animal = input("What animal was it actually? ")
    question = input("What should I've asked? ")

def askQuestion(row):
    ans = input(row['question']+': ')
    if 'y' in ans.lower():
        print(row["yes"])
        return True
    elif 'n' in ans.lower():
        print(row["no"])
        return False
    else:
        print("You're disqualified for answering bullshit")
        quit()

if __name__=="__main__":
    first_question={'question':'is it extinct?', 'yes':'dodo', 'no':'penguin'}
    filename = 'QnA.json'
    #filename = 'QnA'
    try:
        data = loadData(filename)
    except:
        writeData(filename, first_question)
        data=loadData(filename)
    if data==[]:
        writeData(filename, first_question)
        data=loadData(filename)
    print(data)

    for row in data:
        ans=askQuestion(row)
        if ans==True:
            print("BOY am I right!")
        if ans==False:
            respone=choice(["getting a sense", "getting closer", "reading your thoughts"])
            print(response)


    





    

    


