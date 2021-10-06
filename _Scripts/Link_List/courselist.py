class CourseList:
    def __init__(self):
        self.head = None
        self.cursor = None

    # inserts at the end currently
    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            for current_node in self:
                pass
            current_node.set_next(node)

    def remove(self, number):
        if self.head is None:
            return None
        else:
            for nodes in self:
                if nodes.get_next() is None:
                    return None
                else:
                    next_node = nodes.next
                    if next_node.course_number == number:
                        temp_node = next_node
                        pointer = next_node.get_next()
                        next_node.set_next(None)
                        nodes.set_next(pointer)
                        return temp_node

            # temp_node = self.head
            # self.head = self.head.next
            # return temp_node

    def remove_all(self, number):
        if self.head is None:
            return None
        else:
            for nodes in self:
                if nodes.get_next() is None:
                    return None
                else:
                    next_node = nodes.next
                    if next_node.course_number == number:
                        temp_node = next_node
                        pointer = next_node.get_next()
                        next_node.set_next(None)
                        nodes.set_next(pointer)

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
            nodes.join(str(node) + "\n")
            nodes.join("1")
        return nodes

    def __iter__(self):
        self.cursor = self.head

        return self

        # node = self.head
        # while node is not None:
        #     yield node
        #     node = node.next

    def __next__(self):
        if self.cursor is None:
            raise StopIteration

        node = self.cursor
        self.cursor = self.cursor.next

        return node
