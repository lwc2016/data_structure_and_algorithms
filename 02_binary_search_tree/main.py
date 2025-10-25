"""
二叉查找树
"""
from typing import Optional


class Node:
    """二叉查找树树的节点"""
    # 左节点
    left: Optional['Node'] = None
    # 右节点
    right: Optional['Node'] = None
    # 值
    value: int

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Node(value={self.value})"


class BinarySearchTree:
    """二叉查找树"""
    root: Optional[Node] = None
    _size: int = 0

    def add(self, value: int):
        """添加节点"""
        # 输入验证
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        
        if value is None:
            raise ValueError("Value cannot be None")

        # 没有节点情况下
        if self.root is None:
            self.root = Node(value)
            self._size += 1
            return

        current_node = self.root
        while current_node:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    self._size += 1
                    break
                else:
                    current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = Node(value)
                    self._size += 1
                    break
                else:
                    current_node = current_node.right
            else:
                # 如果节点存在则不插入
                break

    @staticmethod
    def get_info(value, root_node: Node):
        """获取节点信息
        返回信息：当前节点，父节点，位置
        """
        if root_node is None:
            return None, None, None

        parent_node = None
        current_node = root_node
        position = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
                position = 'left'
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
                position = 'right'
            else:
                return current_node, parent_node, position

        return None, None, None

    def get(self, value):
        """获取节点"""
        return self.get_info(value, self.root)[0]

    def delete(self, value):
        """删除节点"""
        if self.root is None:
            return
        # 目标节点的信息
        target_node, parent_node, position = self.get_info(value, self.root)

        # 目标节点为空
        if target_node is None:
            return

        # 目标节点的子节点都为空
        if target_node.left is None and target_node.right is None:
            # 说明是根节点
            if parent_node is None:
                self.root = None
            else:
                setattr(parent_node, position, None)
            self._size -= 1
            return

        # 目标节点同时有左右两个节点
        if target_node.left is not None and target_node.right is not None:
            # 找到左子树的最大节点作为替代节点
            max_node, max_parent = self.get_max_info(target_node.left)
            
            # 如果最大节点就是左子节点本身
            if max_node == target_node.left:
                # 直接用左子节点替代目标节点
                max_node.right = target_node.right
                if parent_node is None:
                    self.root = max_node
                else:
                    setattr(parent_node, position, max_node)
            else:
                # 最大节点不是左子节点，需要重新组织
                # 先断开最大节点与其父节点的连接
                if max_parent is not None:
                    max_parent.right = max_node.left
                
                # 用最大节点替代目标节点
                max_node.left = target_node.left
                max_node.right = target_node.right
                
                if parent_node is None:
                    self.root = max_node
                else:
                    setattr(parent_node, position, max_node)

            self._size -= 1
            return

        # 目标节点只有一个节点
        child_node = target_node.left or target_node.right
        if parent_node is None:
            self.root = child_node
        else:
            setattr(parent_node, position, child_node)
        self._size -= 1

    @staticmethod
    def _get_extreme_info(root_node: Node, direction: str):
        """获取极值节点信息（最小或最大）
        
        Args:
            root_node: 根节点
            direction: 'min' 或 'max'
        """
        if root_node is None:
            return None, None

        parent_node = None
        current_node = root_node
        child_attr = 'left' if direction == 'min' else 'right'
        
        while current_node:
            if getattr(current_node, child_attr) is None:
                return current_node, parent_node
            else:
                parent_node = current_node
                current_node = getattr(current_node, child_attr)

    @staticmethod
    def get_min_info(root_node: Node):
        """获取最小节点"""
        return BinarySearchTree._get_extreme_info(root_node, 'min')

    @staticmethod
    def get_max_info(root_node: Node):
        """获取最大节点"""
        return BinarySearchTree._get_extreme_info(root_node, 'max')

    @property
    def min(self):
        """最小节点"""
        return self.get_min_info(self.root)[0]

    @property
    def max(self):
        """最大节点"""
        return self.get_max_info(self.root)[0]

    @property
    def size(self):
        """节点数量"""
        return self._size

    def __repr__(self):
        if self.root is None:
            return ''

        lines: list[list[str]] = []

        def loop(current_node: Node | None, row_index: int):
            nonlocal lines
            if len(lines) < row_index + 1:
                lines.append([])

            if current_node is None:
                lines[row_index].append(' ')
            else:
                current_value = str(current_node.value)
                lines[row_index].append(str(current_value))
                loop(current_node.left, row_index + 1)
                loop(current_node.right, row_index + 1)

        loop(self.root, 0)

        for index, line in enumerate(lines):
            row = "".join([
                item.center(int(120 / (2 ** index)), ' ') for item in line
            ])
            print(row)
        return ''


if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.add(15)
    bst.add(9)
    bst.add(3)
    bst.add(12)
    bst.add(8)
    bst.add(23)
    bst.add(17)
    bst.add(28)
    print(bst)

    print('min:', bst.min)
    print('max:', bst.max)
    print('size:', bst.size)
    print('value:', bst.get(23))

    # 添加1
    bst.add(1)
    print(bst)
    print('-' * 200)

    # 添加4
    bst.add(4)
    print(bst)

    # 删除28
    bst.delete(28)
    print('删除28'.center(100, '-'))
    print(bst)

    # 删除8
    bst.delete(8)
    print('删除8'.center(100, '-'))
    print(bst)

    # 删除9
    bst.delete(9)
    print('删除9'.center(100, '-'))
    print(bst)

    # 删除15
    print('删除15'.center(100, '-'))
    bst.delete(15)
    print(bst)






