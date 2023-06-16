balanced_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}

balanced = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]

unbalanced = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]

class Stack(list):

    def is_empty(self):
        return len(self) == 0
    
    def push(self, elem):
        self.append(elem)

    def pop(self):
        if not self.is_empty():
            elem = self[-1]
            self.__delitem__(-1)
            return elem
    
    def peek(self):
        if self.is_empty() is False:
            return self[-1]

    def size(self):
        stack_size = len(self.stack)
        return stack_size

# Задание №2    

def check_ballance(element):
    stack = Stack()
    for elem in element:
        if elem in balanced_dict:
            stack.push(elem)
        elif elem == balanced_dict.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()

if __name__ == '__main__':
    for element in balanced + unbalanced:
        print(f'{element:<30}{check_ballance(element)}')