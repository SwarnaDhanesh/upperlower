sentence="The quick Brown Fox" 
print("The Given string is:",sentence)
lower=0
count=1
upper=0
count1=1
for i in sentence:
      if i in sentence:
         if(i.islower()):
            lower=lower+count
         else:
            if(i.isupper()):
             upper=upper+count1
print("The number of  Uppercase characters is:",upper)
print("The number of Lowercase characters is:",lower)


