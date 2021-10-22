import csv


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
        print('You have been disqualified for answering bullshit')
        quit()

def getConfirmation():
    ans=input('Is this true (yes or no)?: ')
    if 'y' in ans.lower():
        return True
    elif 'n' in ans.lower():
        return False
    else:
        print('You have been disqualified for answering bullshit')
        quit()        



if __name__=="__main__":
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
    counter=0
    yescounter=0
    nocounter=0    
    for statement in data:                  ## loop over statements (statement is the combi of question,yes answer, and no answer. e.g. a line in the database file)
        counter+=1
        ans=getAnswer(statement['question'])
        if ans=='yes':                      ## if the answer to the question is yes
            nocounter=0
            yescounter+=1
            if yescounter<2:           ## as long as there are questions left to ask
                print('I see, let me ask another question.')
            else:                           ## when there are no more questions to ask
                print('I guess the animal is a', statement['yes'])
                check=getConfirmation()
                if check==True:                 ## the guessed animal was right
                    print('I am awesome, I knew you were thinking of a {}'.format(statement['yes']))
                    break
                else:                           ## the guessed animal was wrong so ask for help to improve
                    print('You got me! Please teach me what you know:')
                    yes=input('What animal was it?:\t')
                    question=input("What should I've asked?:\t")
                    if not yes=='' or not question=='':      ## check whether the inputs are not empty
                        data.append({'question':question, 'yes':yes, 'no':statement['no']})
                        updateData(filename, data)
                    break
        elif counter<len(data)-1:             ## if the answer to the initial question was 'no' and there are unasked questions left
            yescounter=0
            nocounter+=1
            print('I see, let me ask another question.')
        else:                               ## if the answer to the initial question was 'no' but there aren't any questions left
            print('You outplayed me, are you Freek Vonk?')
            break
    












