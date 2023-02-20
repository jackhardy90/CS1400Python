firstName = ''
lastName = ''
mothersMaidenName = ''
starWarsFirstName = ''

print ("What is your Star Wars name?")
firstName = input ("First Name: ")              #Gather user input
lastName = input ("Last Name: ")
mothersMaidenName = input ("Mother's Maiden Name: ")


starWarsFirstName = lastName[:3].capitalize() + firstName[:2]
starWarsLastName = mothersMaidenName[:3].capitalize()           #Print star wars name 
print (starWarsFirstName, starWarsLastName)