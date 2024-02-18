class Stack:
    def __init__(self):          # 빈 스택 하나를 생성
        self.items = []
                
    def push(self, item):        # 스택에 데이터를 추가
        self.items.append(item)
                
    def empty(self):             # 스택이 비어있으면 True를 반환
        return not self.items
                
    def size(self):              # 스택에 있는 데이터 수를 반환
        return len(self.items)
        
    def pop(self):               # 스택의 가장 위에 있는 데이터를 반환
        if self.empty():
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):               # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]


s = Stack()          # 정수를 관리할 stack을 선언 => 빈 스택

n = int(input())
cmd_arr =  [input().split("\n") for _ in range(n)]

for i in cmd_arr:
    check_push = " " in i[0]
    if check_push:
        num = i[0].split()
        s.push(num[1])
    if i[0] == "size":
        print(s.size())
    elif i[0] == "empty":
        if s.empty():
            print(1)
        else:
            print(0)
    elif i[0] == "pop":
        print(s.pop())
    elif i[0] == 'top':
        print(s.top())