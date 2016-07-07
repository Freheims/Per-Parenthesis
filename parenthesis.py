def matchParenthesis(string):
    parenthesis = 0
    brackets = 0
    curlyBrackets = 0
    for i in range(len(string)):
        l = string[i]
        if l == '(':
            if i > 0:
                if not string[i-1] == ':' and not string[i-1] == ';':
                    parenthesis += 1
            else:
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
        elif l == ']':
            brackets -= 1
        elif l == '}':
            curlyBrackets -= 1

    fix = ""
    if parenthesis > 0:
        for i in range(parenthesis):
            fix += ")"
    else:
        for i in range(parenthesis * -1):
            fix += "("

    if brackets > 0:
        for i in range(brackets):
            fix += "]"
    else:
        for i in range(brackets * -1):
            fix += "["

    if curlyBrackets > 0:
        for i in range(curlyBrackets):
            fix += "}"
    else:
        for i in range(curlyBrackets * -1):
            fix += "{"

    return fix

