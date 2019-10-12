class DoubleNode:
    """
    先构造这样一个“节点”数据结构
    多出一個前节点 previous
    """

    def __init__(self, data, prev_node_address=None, next_node_address=None):
        # next_node 存放的是下个节点的内存地址
        self.previous_node = prev_node_address
        self.next_node = next_node_address
        self.node_data = data

    def __str__(self):
        return str(self.node_data)
