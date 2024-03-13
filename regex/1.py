import re 

s = 'rafsan'

match = re.search(r'fs', s) 

print('Start Index:', match.start()) 
print('End Index:', match.end()-1) 
