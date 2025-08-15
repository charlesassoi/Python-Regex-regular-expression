import re
s = 'NASA A computer science portal for geeks'

match=re.search(r'portal',s)
print('start index',match.start())
print('start index',match.end())

string = """Hello my Number is 123456789 and my friend's number is 987654321"""

regex='\d+'
match=re.findall(regex,string)
print(match)

p=re.compile('[a-e]')
print(p.findall(s))
print(re.findall('\W',s))
print(re.sub('Hello','Hi',string,count=1))
print(re.sub(r'\sand\s',' & ',string))

#extraction d'adresses mail

m= "Hello from shubhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"

print(re.findall('\S+@\S+',m))
