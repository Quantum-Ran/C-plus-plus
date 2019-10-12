from SingleNode import SingleNode


class SingleLinkedList():
    """
    节点和链表不是一回事，单个节点类没办法生成个单链表，
    因为在生成第一个节点时，没办法储存下个节点，因为第二个节点还没生成。

    链表是数据结构，节点是链表的元素。
    所以再写一个“单链表”的数据结构。
    """

    # 初始节点头部为 None
    def __init__(self, link_head=None):
        self.link_head = link_head

    # 增
    def add(self, data, index=None):
        """
        默认加入最后，如果有位置，就插入
        """
        # 创建节点实例，投入（数据，内存地址）
        node = SingleNode(data)
        # 如果是空的直接加
        if (self.is_empty()) or (index == 0):
            self.link_head = node
        elif (index is None) or (index == self.length()):
            # 创建节点实例，不能加 link_head 会出现头和尾巴连上
            # 因为只有一个头
            cursor = self.link_head
            # 当前 node 到没有下个节点为止
            while cursor.next_node is not None:
                cursor = cursor.next_node
            cursor.next_node = node
        elif 0 < index < self.length():
            cursor = self.link_head
            # 在 index 前添加
            # 到目标位置的前一个节点停止
            for i in range(index-1):
                cursor = cursor.next_node
            # 新节点的下个节点 = 当前节点的下个节点
            node.next_node = cursor.next_node
            cursor.next_node = node
        elif index > self.length():
            print('RangeOut')

    # 改
    def update(self, newdata, index):
        cursor = self.link_head
        for i in range(index-1):
            cursor = cursor.next_node
        cursor.node_data = newdata

    # 删
    def remove(self, index, offset=1):
        """
        根据索引和偏移量删除，默认偏移量为1
        """
        if self.length() >= index + offset - 1:
            cursor = self.link_head
            for i in range(index-1):
                cursor = cursor.next_node
            start_cursor = cursor
            for ii in range(offset+1):
                cursor = cursor.next_node
            start_cursor.next_node = cursor
        else:
            print('RangeOut')

    # 查
    def search(self):
        """
        要想展示还是要放到一个容器中
        首先获得所有节点头部
        """
        cursor = self.link_head
        SLL_list = []
        # 如果 游标的头部一直存放着上个节点的尾针，
        # 如果一直不为空，就添加到容器中。
        while cursor is not None:
            SLL_list.append(cursor.node_data)
            cursor = cursor.next_node
        return SLL_list

    # 长度
    def length(self):
        return len(self.search())

    # 为空
    def is_empty(self):
        return self.link_head is None


s = SingleLinkedList()
s.add(4)
s.add(54)
s.add(64)
s.add(45)
s.add(34)
s.add(89)
s.add(7, 1)
s.add(8, 7)
s.update(9, 3)
print(s.search())
s.remove(2, 5)
print(s.search())
print(s.length())
