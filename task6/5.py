code=input()
Not1Charcter='DFIOQUWZ'
if  len(code)!=7:
    print('No valid postal code')
    exit()    
if code[1] <'0' or code[1]>'9' or code[4] <'0' or code[4]>'9' or code[6] <'0' or code[6]>'9':
    print('No valid postal code')
    exit()
if code[0] <'A' or code[0]>'Z' or code[2] <'A' or code[2]>'Z' or code[5] <'A' or code[5]>'Z':
    print('No valid postal code')
    exit()
for i in range(len(Not1Charcter)):
    if code[0]==Not1Charcter[i]:
        print('No valid postal code')
        exit()
address = {"Newfoundland" : "A", "Nova Scotia" : "B", 'Prince Edward Island' : 'C', 'New Brunswick' : 'E', 'Quebec' : 'G',
'Quebec' : 'H', 'Quebec' : 'J', 'Ontario' : 'K', 'Ontario' : 'L', 'Ontario' : 'M', 'Ontario' : 'N', 'Ontario' : 'P',
'Manitoba' : 'R', 'Saskatchewan' : 'S', 'Alberta' : 'T', 'British Columbia' : 'V', 'Nunavut or Northwest Territories' : 'X',
'Yukon' : 'Y'}

for x,y in address.items():
    if code[0]==y and code[1]=='0':
        print('Postal code is for a rural address in',x)
    elif code[0]==y:
        print('Postal code is for a urban address in',x)