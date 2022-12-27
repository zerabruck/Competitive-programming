import textwrap

def wrap(string, max_width):
    init = 0
    newstring = ''
    for i in range(max_width,len(string),max_width):
        newstring += string[init:i] + '\n' 
        init=i
        
    newstring+=string[init:]
        
        
    return newstring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)