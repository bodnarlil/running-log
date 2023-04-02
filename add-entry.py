# work on date and time assuming they logged in already
from datetime import date
day = date.today().day; month = date.today().month; year = date.today().year
if(month == 1): month = "January"
elif(month == 2): month = "February"
elif(month == 3): month = "March"
elif(month == 4): month = "April"
elif(month == 5): month = "May"
elif(month == 6): month = "June"
elif(month == 7): month = "July"
elif(month == 8): month = "August"
elif(month == 9): month = "September"
elif(month == 10): month = "October"
elif(month == 11): month = "November"
else: month = "December"

print("today's date:",month,day,year)

# work on basic run/ct info
def newEntry():
    # create a temporary list to hold the dates in the 
    milesRan = input("How many miles did you run? ")
    runTime = input("How long did it take you? (30 minutes, 20 minutes and 31 seconds, etc.): ")
    milesCrossTrained = input("How many running-equivalent miles did you cross train? ")
    typeCrossTrain = input("What type of cross training did you do? (biking, swimming, ellipticaling, etc.): ")
    crossTrainTime = input("How long did it take you? (30 minutes, 20 minutes and 31 seconds, etc.): ")
    workoutEffort = input("How did your workout feel? (good, too slow, too fast, etc.): ")
    workoutType = input("What type of workout did you complete? (easy run, long run, fartlek, etc.): ")
    weather = input("Describe the weather in 1-5 words: ")

    lifted = input("Did you lift? (yes/no): ")
    numSleep = input("How many hours of sleep did you get? ")
    numDrinks = input("How many alcoholic drinks did you have? ")
    numMeals = input("How many meals did you eat? ")

    classesAttended = input("How many classes did you attend? (0, 1, 2, etc.): ")
    classesSkipped = input("How many classes did you skip? (0, 1, 2, etc.): ")
    hoursStudyingOutsideOfClass = input("How many hours did you spend on school outside of class? (0, 1, 2, etc.): ")
    testsQuizesPresentations = input("How many presentations, tests, papers, or quizzes did you have? ")

    notes = input("Add any extra details here: ")

    print("")
    print("--------------------------------------")
    print("")

    print("this is what your entry will look like: ")
    print(milesRan,"miles of running in",runTime,"and",milesCrossTrained,"miles of cross training in",crossTrainTime,"by",typeCrossTrain,".")
    print("the",workoutType,"felt",workoutEffort,"and the weather was",weather,".")
    print("lifting?",lifted+". slept for",numSleep,"hours and had",numDrinks,"drinks and",numMeals,"meals.")
    print("attended",classesAttended,"classes today and skipped",classesSkipped,"classes. spent",hoursStudyingOutsideOfClass,"hours studying outside of class and had",testsQuizesPresentations,"tests, quizzes, presentations, or papers due today.")
    print("extra notes:",notes)
    addToLog = input("does this look correct? (y/n)").lower()

    if(addToLog == "y"):
        # save the log in database
        print("your log has been saved")
    else:
        print("log has not been saved. yes")


# create a place to hold log entries
entries = {"firstname" : "log entry as a list of seperated items"}
