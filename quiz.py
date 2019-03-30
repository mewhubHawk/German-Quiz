score = 0
print("Hallo Milla :D")
print("translate from german to english and vice versa.")
print("PLEASE NOTE THIS IS CASE SENSITIVE!")
print("THIS IS MADE FOR GERMAN PEOPLE TO LEARN ENGLISH AND VICE VERSA DON'T CHEAT!")
questions=\
  {
    "müde(mooder)":"tired",
    "you are(informal)":"du bist",
    "glücklich":"happy",
    "she is(informal)":"sie ist",
    "hello":"hallo",
    "Katze":"cat",
    "es ist(informal)":"it is",
    "Freund":"friend",
    "blue":"Blau",
    "New Zealand":"Neuseeland",
    "Schwester":"sister",
    "ich habe eine Katze":"I have a cat"
    #add more Qs here
}

for question, answer in questions.items():
    response = input("What is '%s' translated to?\n--->" % question)
    if response != answer:
        print("No, '%s' is  translated to '%s'." % (question, answer))
    else:
        print("Yes, that's correct!")
        score += 1

print("You got %d out of %d!" % (score, len(questions)))

if score < len(questions)/3:
   print("better luck next time")
else:
 print("Well Done!")
