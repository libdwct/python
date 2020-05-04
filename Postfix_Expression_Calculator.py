'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : SW Expert Academy 4874. https://swexpertacademy.com/

problem : calculate "postfix expression"

'''

def postfix_calculation(data):
    stack = []
    for i in range(len(data)):
        if data[i].isdecimal():
            stack.append(data[i])


        else:
            if len(stack) < 2: return "error"
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(eval(str(first) + data[i] + str(second)))

    if len(stack) == 1:
        return int(stack.pop())
    else: return "error"

# case 1:  10 2 + 3 4 + *
data_1 = ["10","2","+","3","4","+","*"]
print(postfix_calculation(data_1))

# case 2:  5 3 * +   (error case)
data_2 = ["5","3","*", "+"]
print(postfix_calculation(data_2))