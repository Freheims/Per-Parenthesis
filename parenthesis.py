def matchParenthesis(string):
    parenthesis = 0
    brackets = 0
    curlyBrackets = 0
    for i in range(len(string)):
        l = string[i]
        if l == '(':
            parenthesis += 1
        elif l == '[':
            brackets += 1
        elif l == '{':
            curlyBrackets += 1
        elif l == ')':
            if i > 0:
                if not (string[i-1] == ':' or string[i-1] == ';'):
                    if i > 1:
                        if not string[i-2] == '-':
                            parenthesis -= 1
        elif l == '[':
            brackets -= 1
        elif l == '{':
            curlyBrackets -= 1
    fix = ""
    for i in range(parenthesis):
        fix += ")"
    for i in range(brackets):
        fix += "]"
    for i in range(curlyBrackets):
        fix += "}"

    return fix
