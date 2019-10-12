class SingleNode:
    """
    先构造这样一个“节点”数据结构
    没有 node_head
    只有 next_node 和 node_data
    """

    def __init__(self, data, node_address=None):
        # next_node 存放的是下个节点的内存地址
        self.next_node = node_address
        self.node_data = data

    def __str__(self):
        return str(self.node_data)
