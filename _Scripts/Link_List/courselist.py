class CourseList:
    def __init__(self):
        self.head = None
        self.cursor = None

    # inserts at the end currently
    def insert(self, node):
        class_num = node.number()
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)
        # if self.head is None:
        #     self.head = node
        # else:
        #     # node_pointer = node.next
        #     # while node_pointer is None:
        #
        #     i = iter(self)
        #     while i is self:
        #         lyst_cursor = self.cursor
        #         if lyst_cursor is None:
        #             self.head.set_next(node)
        #             i.__next__()
        #         else:
        #             for current_node in self:
        #                 if lyst_cursor.next is None:
        #                     lyst_cursor.set_next(node)
        #                 else:
        #                     next_node = lyst_cursor.next
        #                     if next_node.number() > class_num:
        #                         pointer = lyst_cursor.get_next()
        #                         lyst_cursor.set_next(node)
        #                         node.set_next(pointer)
        #                     elif next_node.get_next() is None:
        #                         next_node.set_next(node)

    def remove(self, number):
        if self.head is None:
            return None
        else:
            for nodes in self:
                if nodes.number() == number:
                    if nodes is self.head:
                        self.head = nodes.next
                    elif nodes.get_next() is None:
                        return None
                    else:
                        next_node = nodes.next
                        if nodes.course_number == number:
                            temp_node = nodes
                            pointer = nodes.get_next()
                            nodes.set_next(None)
                            next_node.set_next(pointer)
                            return temp_node

            # temp_node = self.head
            # self.head = self.head.next
            # return temp_node

    def remove_all(self, number):
        if self.head is None:
            return None
        else:
            for nodes in self:
                if nodes.number() == number:
                    if nodes is self.head:
                        self.head = nodes.next
                    elif nodes.get_next() is None:
                        return None
                    else:
                        next_node = nodes.next
                        if nodes.course_number == number:
                            temp_node = nodes
                            pointer = nodes.get_next()
                            nodes.set_next(None)
                            next_node.set_next(pointer)
                            # return temp_node

    def find(self):
        pass

    def size(self):
        pass

    def calculate_gpa(self):
        # calculate gpa weighted with how many credit hours the course is.
        # so gpa per credit per amount of courses taken?
        pass

    def is_sorted(self):
        pass

    def __str__(self):
        nodes = ""
        for node in self:
            nodes += f"{str(node)}\n"
        return nodes

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

        # node = self.head
        # while node is not None:
        #     yield node
        #     node = node.next

    # def __next__(self):
    #     if self.cursor is None:
    #         raise StopIteration
    #
    #     node = self.cursor
    #     self.cursor = self.cursor.next
    #
    #     return node
