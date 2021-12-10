class Stack:
    def __init__(self,size = 10):
        # 用序列来保存元素
        self.data = []
        # 栈的大小
        self.size = size
        # 栈的元素个数
        self.num = 0
        
    def push(self,n):
        if self.num < self.size:
            self.data.append(n)
            self.num = self.num + 1
        else:
            print("Stack Full!")
            
    def pop(self):
        if self.num > 0:
            self.num = self.num - 1
            return self.data.pop(-1)
        else:
            print("Stack is empty!")
    
    def isEmpty(self):
        return not self.data

    def Empty(self):
        self.data = []
        self.num = 0
        
    def Size(self):
        return self.num
    
    def maxlen(self):
        return self.size 
    
    def show(self):
        for i in range(len(self.data)):
            if i != len(self.data) - 1:
                print(self.data[i],end=' ')
            else:
                print(self.data[i])
                
if __name__ == '__main__':
    flag = 0
    while flag == 0:
        num = input()
        if ' ' in str(num):
            indata = num.split()
            if indata[0] == '1':
                st = Stack()
                for i in range(len(indata)-1):
                    st.push(indata[i+1])
                if len(indata) > 11:
                    st = Stack(len(indata)-1)
                    for i in range(len(indata)-1):
                        st.push(indata[i+1])
                flag = 1
            elif indata[0] == '2':
                print("data error")
            else:
                break;
        else:
            num = int(num)
            if num == 1:
                st.Empty()
                flag = 1
            elif num == 3:
                print("stack is not exist")
            elif num == 2:
                print("data error")
            elif num == 4:
                print("stack is not exist")
            elif num == 5:
                print("stack is not exist")
            else:
                break
            
    while flag == 1:
        num = input()
        if ' ' in num:
            indata = num.split()
            if indata[0] == '2':
                if st.Size() < st.maxlen():
                     for i in range(len(indata)-1):
                        st.push(indata[i+1])
                else:
                    print("The stack is full")
            else:
                break
        else :
            if num == '2':
                print("data error")
            elif num == '3':
                print(st.pop())
            elif num == '4':
                if st.isEmpty():
                    print("The stack is Empty")
                else:
                    st.show()
            elif num == '5':
                print(st.Size())
            else:
                break