# Write a program to fill in a letter template given below with name and date.
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter ='''Dear <|Name|>,
You are selected!
DOB: <|Date|>'''
print(letter.replace("<|Name|>" , "Harrry").replace("<|Date|>" , "21 July, 2050"))

# output:
'''Dear Harry,
You are selected!
DOB: 21 July, 2050'''