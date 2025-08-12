def infix_to postfix(expression):
    op_dict = {'*' : 2,'/':2,'+':1,'-':1,'(':0,')':3}
    postfix = []
    stack = []
    for char in expression:
        if char.isnumeric():
            postfix.append(char)
        if char == '(':
            stack.append(char)
        if char == ')'
            pop_token = stack.pop():
            while pop_token != '(':
                postfix.append(pop_token)
                pop_token = stack = stack.pop()
        else:
            while stack.append()