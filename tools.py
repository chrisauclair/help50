import re
import string

# extracts a single character above the ^
def char_extract(lines):
    if len(lines) < 2 or not re.search(r"\^", lines[1]):
        return
    index = lines[1].index("^")
    if len(lines[0]) < index + 1:
        return
    return lines[0][lines[1].index("^")]

# extracts all characters above the sequence of ~
# by default, assumes the return value is to the leftmost sequence of ~
# if first_group is set to False, returns all characters above tilde to the right of the ^
def tilde_extract(lines, first_group=True):
    if len(lines) < 2 or not re.search(r"~", lines[1]):
        return
    if first_group:
        start = lines[1].index("~")
    else:    
        start = lines[1].index("^") + 1
    length = 1
    while len(lines[1]) > start + length and lines[1][start + length] == "~":
        length += 1
    if len(lines[0]) < start + length:
        return
    return lines[0][start:start+length]

# extract the name of a variable above the ^
# by default, assumes that ^ is under the first character of the variable
# if left_aligned is set to False, ^ is under the next character after the variable
def var_extract(lines, left_aligned=True):
    if len(lines) < 2 or not re.search(r"\^", lines[1]):
        return
    permissibles = string.ascii_letters + string.digits + '_'
    index = lines[1].index("^")
    var = ""
    
    if left_aligned:
        while len(lines[0]) > index + 1 and lines[0][index] in permissibles:
            var += lines[0][index]
            index += 1
    elif len(lines[0]) > index + 1:
        index -= 1
        while index >= 0 and lines[0][index] in permissibles:
            var = lines[0][index] + var
            index -= 1
            
    if len(var) > 0:
        return var
        
    