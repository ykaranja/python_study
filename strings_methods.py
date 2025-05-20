#Accepts a sentence from the user
sentence=input("Enter a sentence: ")
print("Your input:",sentence)
#counts the number of words

words=len(sentence.split(' '))
print(words)
#capitalize the first letter of each word
print(sentence.title())
#reverse the whole sentence
print(sentence[::-1])
#convert text to "good habits are hard to break!"
text= " BAD habits are hard to break! "
text=text.strip()
text=text.replace('BAD', 'good')
print(text)
#clean email and extract domain
email=" John.Doe@GMAIL.com "
email=email.strip()
email=email.lower()
email=email.split('@')
domain=email[1]
print(domain)
#Clean names and create a formatted sentence " My name is Yvonne Wanjiku and l love Reading Books"
first="yvonne"
last="WANJIKU"
hobby=" Reading Books "
cleanfirst=first.capitalize()
cleanlast=last.capitalize()
cleanhobby=hobby.strip()
format_sentence=f"My name is {cleanfirst} {cleanlast} and {cleanhobby}"
print(format_sentence)
