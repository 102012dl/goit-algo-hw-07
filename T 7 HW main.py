\Завдання 1 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val
# Приклад використання
if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    # Знайти найбільше значення
    max_value = find_max(root)
    print(f"Найбільше значення у дереві: {max_value}") 




\Завдання 2 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val
# Приклад використання
if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    # Знаходження найменшого значення
    min_value = find_min(root)
    print(f"Найменше значення в дереві: {min_value}") 




\Завдання 3 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current
def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root
def sum_values(root):
    if root is None:
        return 0
    return root.val + sum_values(root.left) + sum_values(root.right)
# Test
if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    # Знаходження суми всіх значень у дереві
    total_sum = sum_values(root)
    print(f"Сума всіх значень у дереві: {total_sum}") 




\Завдання 4 (необовʼязкове) 

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False
    def add_reply(self, reply):
        self.replies.append(reply)
    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True
    def display(self, level=0):
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)
# Тестування
if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)
    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)
    reply1.remove_reply()
    root_comment.display() 
