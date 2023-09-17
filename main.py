class Node:
    """
    Класс Node определяет вершины бинарного дерева
    """

    
    def __init__(self, data):
        """
        Инициализация данных, которые храняться в вершине
        """
        self.data = data
        self.left = self.right = None


class Tree:
    """
    Класс Tree служит для работы с бинарным деревом
    """

    def __init__(self):
        """
        Инициализация данных, имеющая указатель root,
        по умолчанию он имеет значение None,
        сначало бинароное дерево создается пустым
        """
        self.root = None


    def __find(self, node, parent, value):
        """
        Рекурсивный метод __find, который ищет нужный узел
        """
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True
        
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
            
        return node, parent, False


    def append(self, obj):
        """
        Метод append служит для добавления вершин,
        - если добавляемое значение меньше значения в родительском узле,
        то новая вершина добавляет в левую ветвь, иначе - в правую;
        - если добавляемое значение уже присутствует в дереве,
        то оно игнориется (то есть, дубли отсутствуют).
        """
        if self.root is None:
            self.root = obj
            return obj
        
        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        
        return obj
    
    def show_tree(self, node):
        """
        Отображение бинарного дерева, через рекурсивную функцию
        """
        if node is None:
            return
        
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


    def show_wide_tree(self, node):
        """
        Отображение дерева в ширину
        """
        if node is None:
            return
        
        v = [node]

        while v:
            vn = []

            for x in v:
                print(x.data, end=" ")

                if x.left:
                    vn += [x.left]

                if x.right:
                    vn += [x.right]

            print()
            v = vn


    def __del_leaf(self, s, p):
        """
        Удаление листовой вершины
        """
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None


    def __del_one_child(self, s, p):
        """
        Удаление узла с одним потомком
        """
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left

        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left


    def __find_min(self, node, parent):
        """
        Поиск минимального значения в правом поддереве рекурсивно
        """
        if node.left:
            return self.__find_min(node.left, node)
        
        return node, parent

    def del_node(self, key):
        """
        Удаление вершин из бинарного дерева с определенным значением
        """
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None
        
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)

        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


def size(node):
    """
    Подсчет кол-ва элементов в дереве с помощью рекурсии
    """
    if node==None:
        return 0
    return(size(node.left) + 1 + size(node.right))

# список добовляемых значений
# v = [10, 5, 7, 16, 13, 2, 20]
v = [20, 5, 24, 2, 16, 11, 18]
# Объект бинарного дерева
t = Tree()
# Перебор значений в списке
for x in v:
    t.append(Node(x))

t.del_node(5)
t.show_wide_tree(t.root)

print("Кол-во элементов в дереве:", size(t.root))
