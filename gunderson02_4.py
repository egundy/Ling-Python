'''Semitic morphology involves intercalating vowels and consonants to express morphological 
categories. '''

'''How might you use the format method to describe this system? Write a script that shows how 
format( ) could be used to express different categories. Submit your script. '''


arab_base = "{0}k{1}t{2}b{3}"

def format_arab(a,b,c,d):
    formatted_arab_base = arab_base.format(a,b,c,d)
    print(formatted_arab_base)
    
format_arab("","aa","a","-a")