import re

content = ''
with open('automation/assets/potential-contacts.txt', 'r') as f:
    content = f.read()

print (re.match('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$','509-234-5018').group(0))
print ( (re.findall('(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?',content)[0]))

# for char in content.split(' '):
#      if re.match('(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?',char).group(0) != '':
#          print (re.search('(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?',char).group(0))