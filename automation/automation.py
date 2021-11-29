import re

content = ''
with open('automation/assets/potential-contacts.txt', 'r') as f:
    content = f.read()

phone_regex1  = r"[0-9]{3}-[0-9]{4}"
phone_regex2  = r"[0-9]{3}.[0-9]{3}.[0-9]{4}"
phone_regex3  = r"[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{4}"
phone_regex4  = r"[0-9]{10}"
phone_regex5  = r"\+1-[0-9]{3}-[0-9]{3}-[0-9]{4}"

phone_numbers = re.findall(phone_regex1, content)
phone_numbers+= re.findall(phone_regex2, content)
phone_numbers+= re.findall(phone_regex3, content)
phone_numbers+= re.findall(phone_regex4, content)
phone_numbers+= re.findall(phone_regex5, content)

output = []
for number in phone_numbers:
    if len(number) < 10:
        output.append(f'206-{number}')
    elif len(number) == 10:
        output.append(f'{number[0:3]}-{number[3:6]}-{number[6:]}')
    elif len(number) == 16:
        output.append(f'{number[4:]}')
    elif len(number) == 15:
        output.append(f'{number[3:]}')
    elif '.' in number:
        output.append(number.replace('.','-'))
    elif ')' in number:
        output.append(number.replace(')','-'))
    else:
       output.append(number) 
    pass

phone_numbers_remove_repetitions = []
for number in output:
    if number not in phone_numbers_remove_repetitions:
        phone_numbers_remove_repetitions.append(number)

all_emails = re.findall(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+',content)
emails = []
for email in all_emails:
    if email not in emails:
        emails.append(email)

with open ('emails.txt', 'w') as f:
    emails.sort()
    for email in emails:
        f.write(email+'\n')

with open ('phones.txt', 'w') as f:
    phone_numbers_remove_repetitions.sort()
    for number in phone_numbers_remove_repetitions:
        f.write(number+'\n')
