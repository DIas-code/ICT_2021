morseletters = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
         '-.': 'G',   '....': 'H',     '..': 'I',  
      '.---': 'J',    '-.-': 'K',   '.-..': 'L',
        '--': 'M',     '-.': 'N',    '---': 'O', 
      '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U', 
      '...-': 'V',    '.--': 'W',   '-..-': 'X',
      '-.--': 'Y',   '--..': 'Z',  '-----': '0', 
     '.----': '1',  '..---': '2',  '...--': '3',
     '....-': '4',  '.....': '5',  '-....': '6', 
     '--...': '7',  '---..': '8',  '----.': '9'}
a=''
word=input()
word=word.upper()
for i in range(0,len(word)):
    for x,y in morseletters.items():
        if word[i]==y:
            a+=x+" "

print(a)