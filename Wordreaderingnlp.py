inp=input()
for line in open(inp):
         for word in line.split():
           if word.endswith('ing'):
             print (word)
