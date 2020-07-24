import re

f = open('actualRegex.txt')
data = f.read()
print( sum( [ int(num) for num in re.findall('[0-9]+', data) ] ) )
