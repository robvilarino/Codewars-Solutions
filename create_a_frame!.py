'''
Kata URL: https://www.codewars.com/kata/5672f4e3404d0609ec00000a
'''
def frame(text, char):
    frame = []
    
    width = len(max(text, key=len))+4
    height = len(text) + 2
    
    for i in range(height):
        if i == 0 or i == height-1:
            frame.append(char*(width))
        else:
            padding = (width - 4) - len(text[i-1])
            frame.append(f"{char} {text[i-1]}" + " "*padding + f" {char}")
        
    return "\n".join(frame)