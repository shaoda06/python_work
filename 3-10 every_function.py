# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

languages = ['C++','Java','Php','Python','Javascript']
additional_language_1 = "C#"
additional_language_2 = "Ruby"
additional_language_3 = "Perl"
print("languages list: "+str(languages))
print("There are "+str(len(languages))+" programming languages in the list.")
languages.insert(0,additional_language_1)
languages.insert(2,additional_language_2)
languages.append(additional_language_3)
print("languages list: "+str(languages))
print("There are "+str(len(languages))+" programming languages in the list.")
print("Used [-1] to get the last element in the list: "+languages[-1])
print("Used [-2] to get the 2nd last element in the list: "+languages[-2])
print("I do not know "+languages.pop()+"! So, pop()!")
print("I do not know "+languages[2]+"! So, del()")
del(languages[2])
language_name = "C#"
print("I do not know "+language_name+" either! So, remove()")
languages.remove(language_name)
print("languages list: "+str(languages))
print("sorted(): "+str(sorted(languages)))
languages.reverse()
print("reverse(): "+str(languages))
languages.reverse()
languages.sort()
print("sort(): "+str(languages))
languages.sort(reverse=True)
print("sort(reverse=True): "+str(languages))
