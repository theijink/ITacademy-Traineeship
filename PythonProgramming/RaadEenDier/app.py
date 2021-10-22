import csv
from random import choice

def loadData(filename):
    data=[]
    file=open(filename, 'r')
    reader=csv.DictReader(file, delimiter=',')
    for row in reader:
        data.append(row)
    file.close()
    return data

def updateData(filename, data):
    file=open(filename, mode='w')
    writer=csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    file.close()

def createFile(filename):
    statement={'question':'Is the animal extinct?', 'yes':'dodo', 'no':'horse'}
    file=open(filename, mode='w')
    writer=csv.DictWriter(file, fieldnames=statement.keys())
    writer.writeheader()
    writer.writerow(statement)
    file.close()

def getAnswer(question):
    ans=input(question+'\t')
    if 'y' in ans.lower():
        return 'yes'
    elif 'n' in ans.lower():
        return 'no'
    else:
        print(choice(not_yes_no))
        quit()

def getConfirmation():
    ans=input('Is this true (yes or no)?: ')
    if 'y' in ans.lower():
        return True
    elif 'n' in ans.lower():
        return False
    else:
        print(choice(not_yes_no))
        quit()        

def getIndex():
    try:
        questions.remove(Q)
    except UnboundLocalError:
        questions = [i for i in range(len(data))]
    Q = choice(questions)
    return questions, Q


if __name__=="__main__":
    ## answer options
    winning_answers = ["I knew it, I'm te best", "You lost! Wanna play again?", "Please, go take a lesson at the kinderboerderij"]
    losing_answers = ["Since you're so good at this, why don't play again?", "I think you beat me because you live in the zoo"]
    not_yes_no = ["You have been disqualified for answering bullshit", "You can answer with 'yes', 'y', 'no', or 'n'. Don't make your own rules!"]
    questionaires = ["Are you thinking of a {}", "Is {} the one you had in mind?", "I bet you're thinking of a {}. Am I right?"]

    ## database file
    filename="statements.csv"
    ## load
    try:                            ## if this works, there is a file. However, it might be empty
        data=loadData(filename)
    except FileNotFoundError:       ## this means there wasn't a file, but it's created now
        createFile(filename)
        data=loadData(filename)
    if data==[]:                    ## if the file was loaded, but empty: add the first question
        createFile(filename)
    else:                           ## file is loaded and has content
        pass 
    
    ## the real part:
    print('Let us play a game')
    print('Take any animal in mind')
    print('If you press [enter] I will ask you some questions')
    print("You're allowed to answer with yes (y) and no (n)")
    if input("Let's see who knows best...") =="":
        pass
    else:
        print("Come on man, just hit [enter], no other characters!")
        quit()


    treated_statements=[]
    guessed=False
    while len(treated_statements)<=len(data):
        questions, Q = getIndex()
        statement=data[Q]
        treated_statements.append(statement)
        ans = getAnswer(statement['question'])
        if len(treated_statements)==len(data):
            print('\nYou have outplayed me. Are you Freek Vonk?')
            animal = input('Just kidding. Whay animal did you have in mind?:\t')
            question = input("And what question should I've asked?:\t")
            data.append({'question':question, 'yes':animal, 'no':statement['yes' if cnf==True else 'no']})
            updateData(filename, data)
            break
        else:
            print(choice(questionaires).format(statement[ans]))
            cnf = getConfirmation()
            if cnf == True:
                print(choice(winning_answers))
                break
            else:
                continue

