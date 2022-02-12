sampleCandidateList1 = ["Joe", "Frank", "Steve", "Mariah"]
sampleCandidateList2 = ["Joe", "Frank"]
sampleCandidateList3 = ["Joe", "Frank", "Steve"]

def getIndividVote(candidatelist):

    firstsecondthirdlist = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth"]

    from os.path import exists
    from time import sleep
    from json import loads, dumps

    if not exists("tidemanresults.json"):
        filevar = open("tidemanresults.json", "w+")
        filevar.write("{}")
        filevar.close()
    filevar = open("tidemanresults.json", "r")
    jsonvar = loads(filevar.read())
    filevar.close()
    currentNumEntries = len(list(jsonvar.keys()))
    
    individvotedict = {}

    print("\nHello, and welcome to the Tideman Voting Machine!\n")
    sleep(3)
    nameinput = input("What's your name anyways?\n\n >>> ")
    print("\nAlright, thanks!\n")
    sleep(3)
    print("Here are the candidates you can vote for today:\n")
    sleep(3)
    print("\n".join(["Candidate #{}: {}".format(indexnum + 1, anycand) for indexnum, anycand in enumerate(candidatelist)]) + "\n")
    sleep(5)
    for indexnum, anycand in enumerate(candidatelist):
        userinput = input("Who is your {} choice candidate? Please type ONLY their ID number here: >>> ".format(firstsecondthirdlist[indexnum]))
        individvotedict[int(userinput)] = indexnum + 1
    print("\nThank you for using the Tideman Voting Machine, powered by Python!\n")
    sleep(3)
    
    filevar = open("tidemanresults.json", "w")
    jsonvar["Vote {}".format(currentNumEntries + 1)] = [{"Castor": nameinput}, {"Candidates": candidatelist}, {"Ballot": individvotedict}]
    filevar.write(dumps(jsonvar))
    filevar.close()

def calcElectionResults(filename):

    from json import loads

    filevar = open(filename, "r")
    jsonvar = loads(filevar.read())
    filevar.close()

    candtotals = {anycand: 0 for anycand in list(jsonvar["Vote 1"][2]["Ballot"].keys())}

    firstvoteballot = jsonvar["Vote 1"][2]["Ballot"]

    pairlist = []
    for anycand in firstvoteballot:
        for anysubcand in firstvoteballot:
            if anycand != anysubcand and {anycand, anysubcand} not in pairlist:
                pairlist += [{anycand, anysubcand}]

    for anyvote in list(jsonvar.keys()):

        for anypair in pairlist:
            
            pairtuple = tuple(anypair)
            if jsonvar[anyvote][2]["Ballot"][pairtuple[0]] < jsonvar[anyvote][2]["Ballot"][pairtuple[1]]:
                candtotals[pairtuple[0]] += 1
            elif jsonvar[anyvote][2]["Ballot"][pairtuple[0]] > jsonvar[anyvote][2]["Ballot"][pairtuple[1]]:
                candtotals[pairtuple[1]] += 1

    returnlist = [(jsonvar["Vote 1"][1]["Candidates"][int(anykey) - 1], candtotals[anykey]) for anykey in list(candtotals.keys())]
    returnlist = sorted(returnlist, key = lambda a: a[1], reverse = True)
    returnlist = [(anytuple[0], anytuple[1], indexnum + 1) for indexnum, anytuple in enumerate(returnlist)]

    return(returnlist)

def printElectionResults(returnedlist):

    from time import sleep

    print("\n{} came in with {} points. Remember, the higher the number of points, the better that candidate did in the election.\n".format(returnedlist[0][0], returnedlist[0][1]))
    sleep(3)

    for anycand in returnedlist[1:]:

        print("{} came in with {} points.\n".format(anycand[0], anycand[1]))
        sleep(1.5)

    sleep(1.5)
    print("Thanks again for using the Tideman Voting Machine, powered by Python!\n")