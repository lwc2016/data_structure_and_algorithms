"""
二叉查找树的pytest测试用例
"""
import pytest
from main import BinarySearchTree, Node


class TestBinarySearchTree:
    """二叉查找树测试类"""
    
    def test_add_single_node(self):
        """测试添加单个节点"""
        bst = BinarySearchTree()
        bst.add(5)
        
        assert bst.root is not None
        assert bst.root.value == 5
        assert bst.root.left is None
        assert bst.root.right is None
    
    def test_add_multiple_nodes(self):
        """测试添加多个节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(9)
        
        assert bst.root.value == 5
        assert bst.root.left.value == 3
        assert bst.root.right.value == 7
        assert bst.root.left.left.value == 1
        assert bst.root.right.right.value == 9
    
    def test_add_duplicate_node(self):
        """测试添加重复节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(5)  # 重复节点
        
        assert bst.root.value == 5
        assert bst.root.left.value == 3
        assert bst.root.right is None
    
    def test_add_ordered_sequence(self):
        """测试添加有序序列"""
        bst = BinarySearchTree()
        for i in range(1, 6):
            bst.add(i)
        
        current = bst.root
        assert current.value == 1
        for i in range(2, 6):
            current = current.right
            assert current.value == i
            assert current.left is None
    
    def test_add_reverse_ordered_sequence(self):
        """测试添加逆序序列"""
        bst = BinarySearchTree()
        for i in range(5, 0, -1):
            bst.add(i)
        
        current = bst.root
        assert current.value == 5
        for i in range(4, 0, -1):
            current = current.left
            assert current.value == i
            assert current.right is None
    
    def test_get_existing_node(self):
        """测试获取存在的节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(9)
        
        node = bst.get(3)
        assert node is not None
        assert node.value == 3
        
        node = bst.get(9)
        assert node is not None
        assert node.value == 9
        
        node = bst.get(5)
        assert node is not None
        assert node.value == 5
    
    def test_get_nonexistent_node(self):
        """测试获取不存在的节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        
        node = bst.get(1)
        assert node is None
        
        node = bst.get(9)
        assert node is None
    
    def test_get_empty_tree(self):
        """测试在空树中获取节点"""
        bst = BinarySearchTree()
        node = bst.get(5)
        assert node is None
    
    def test_min_property(self):
        """测试最小节点属性"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(9)
        
        min_node = bst.min
        assert min_node is not None
        assert min_node.value == 1
    
    def test_min_empty_tree(self):
        """测试空树的最小节点"""
        bst = BinarySearchTree()
        min_node = bst.min
        assert min_node is None
    
    def test_min_single_node(self):
        """测试单节点树的最小节点"""
        bst = BinarySearchTree()
        bst.add(5)
        
        min_node = bst.min
        assert min_node is not None
        assert min_node.value == 5
    
    def test_max_property(self):
        """测试最大节点属性"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(9)
        
        max_node = bst.max
        assert max_node is not None
        assert max_node.value == 9
    
    def test_max_empty_tree(self):
        """测试空树的最大节点"""
        bst = BinarySearchTree()
        max_node = bst.max
        assert max_node is None
    
    def test_max_single_node(self):
        """测试单节点树的最大节点"""
        bst = BinarySearchTree()
        bst.add(5)
        
        max_node = bst.max
        assert max_node is not None
        assert max_node.value == 5
    
    def test_size_property(self):
        """测试节点数量属性"""
        bst = BinarySearchTree()
        assert bst.size == 0  # 空树返回0
        
        bst.add(5)
        assert bst.size == 1
        
        bst.add(3)
        assert bst.size == 2
        
        bst.add(7)
        assert bst.size == 3
        
        bst.add(1)
        assert bst.size == 4
        
        bst.add(9)
        assert bst.size == 5
    
    def test_delete_leaf_node(self):
        """测试删除叶子节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        
        # 删除叶子节点1
        bst.delete(1)
        assert bst.get(1) is None
        assert bst.root.left.left is None
        assert bst.size == 3
        
        # 删除叶子节点7
        bst.delete(7)
        assert bst.get(7) is None
        assert bst.root.right is None
        assert bst.size == 2
    
    def test_delete_node_with_one_child_left(self):
        """测试删除只有左子节点的节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(1)
        
        # 删除节点3，它有左子节点1
        bst.delete(3)
        assert bst.get(3) is None
        assert bst.root.left.value == 1
        assert bst.size == 2
    
    def test_delete_node_with_one_child_right(self):
        """测试删除只有右子节点的节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(7)
        bst.add(9)
        
        # 删除节点7，它有右子节点9
        bst.delete(7)
        assert bst.get(7) is None
        assert bst.root.right.value == 9
        assert bst.size == 2
    
    def test_delete_node_with_two_children_case1(self):
        """测试删除有两个子节点的节点 - 情况1：左子节点没有右子树"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)  # 左子节点没有右子树
        
        # 删除节点5，左子树最大节点就是3
        bst.delete(5)
        assert bst.get(5) is None
        assert bst.root.value == 3  # 3成为新的根节点
        assert bst.root.left.value == 1
        assert bst.root.right.value == 7
        assert bst.size == 3
    
    def test_delete_node_with_two_children_case2(self):
        """测试删除有两个子节点的节点 - 情况2：左子节点有右子树"""
        bst = BinarySearchTree()
        bst.add(10)
        bst.add(5)
        bst.add(15)
        bst.add(3)
        bst.add(7)  # 左子树有右子树
        bst.add(6)
        bst.add(8)
        
        # 删除节点10，左子树最大节点是8
        bst.delete(10)
        assert bst.get(10) is None
        assert bst.root.value == 8  # 8成为新的根节点
        assert bst.root.left.value == 5
        assert bst.root.right.value == 15
        assert bst.size == 6
        
        # 验证左子树结构正确
        assert bst.root.left.left.value == 3
        assert bst.root.left.right.value == 7
        assert bst.root.left.right.left.value == 6
        assert bst.root.left.right.right is None  # 8的右子树应该被移除
    
    def test_delete_root_node_single(self):
        """测试删除单节点根节点"""
        bst = BinarySearchTree()
        bst.add(5)
        
        bst.delete(5)
        assert bst.root is None
        assert bst.size == 0
    
    def test_delete_root_node_with_one_child(self):
        """测试删除只有一个子节点的根节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        
        bst.delete(5)
        assert bst.root.value == 3
        assert bst.size == 1
    
    def test_delete_root_node_with_two_children(self):
        """测试删除有两个子节点的根节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        
        bst.delete(5)
        assert bst.get(5) is None
        assert bst.root.value == 3  # 左子树最大节点成为新根
        assert bst.root.right.value == 7
        assert bst.size == 2
    
    def test_delete_nonexistent_node(self):
        """测试删除不存在的节点"""
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        
        original_size = bst.size
        bst.delete(10)  # 删除不存在的节点
        
        assert bst.size == original_size  # 大小不变
        assert bst.get(5) is not None
        assert bst.get(3) is not None
        assert bst.get(7) is not None
    
    def test_delete_empty_tree(self):
        """测试在空树中删除节点"""
        bst = BinarySearchTree()
        bst.delete(5)  # 在空树中删除
        
        assert bst.root is None
        assert bst.size == 0
    
    def test_complex_tree_operations(self):
        """测试复杂树的综合操作"""
        bst = BinarySearchTree()
        
        # 构建一个复杂的树
        values = [15, 9, 3, 12, 8, 23, 17, 28, 1, 4]
        for value in values:
            bst.add(value)
        
        assert bst.size == len(values)
        assert bst.min.value == 1
        assert bst.max.value == 28
        
        # 删除一些节点
        bst.delete(28)  # 删除叶子节点
        assert bst.get(28) is None
        assert bst.size == len(values) - 1
        
        bst.delete(8)  # 删除叶子节点
        assert bst.get(8) is None
        assert bst.size == len(values) - 2
        
        bst.delete(9)  # 删除有两个子节点的节点
        assert bst.get(9) is None
        assert bst.size == len(values) - 3
        
        # 验证剩余节点仍然可以正常访问
        assert bst.get(15) is not None
        assert bst.get(3) is not None
        assert bst.get(12) is not None
    
    def test_tree_properties_after_operations(self):
        """测试操作后树的属性"""
        bst = BinarySearchTree()
        
        # 添加节点
        bst.add(10)
        bst.add(5)
        bst.add(15)
        bst.add(3)
        bst.add(7)
        bst.add(12)
        bst.add(18)
        
        # 验证二叉搜索树性质
        def verify_bst_property(node):
            if node is None:
                return True
            
            if node.left is not None and node.left.value >= node.value:
                return False
            if node.right is not None and node.right.value <= node.value:
                return False
            
            return verify_bst_property(node.left) and verify_bst_property(node.right)
        
        assert verify_bst_property(bst.root)
        
        # 删除节点后再次验证
        bst.delete(5)
        assert verify_bst_property(bst.root)
        
        bst.delete(15)
        assert verify_bst_property(bst.root)
        
        bst.delete(10)
        assert verify_bst_property(bst.root)
    
    def test_node_repr(self):
        """测试节点的字符串表示"""
        node = Node(5)
        assert repr(node) == "Node(value=5)"
        
        node = Node(10)
        assert repr(node) == "Node(value=10)"
    
    def test_edge_cases_comprehensive(self):
        """测试各种边界情况的综合测试"""
        bst = BinarySearchTree()
        
        # 测试空树的所有操作
        assert bst.size == 0
        assert bst.min is None
        assert bst.max is None
        assert bst.get(5) is None
        bst.delete(5)  # 删除不存在的节点
        
        # 测试单节点树
        bst.add(10)
        assert bst.size == 1
        assert bst.min.value == 10
        assert bst.max.value == 10
        assert bst.get(10).value == 10
        assert bst.get(5) is None
        
        # 删除单节点
        bst.delete(10)
        assert bst.root is None
        assert bst.size == 0
        
        # 测试只有左子树的树
        bst.add(10)
        bst.add(5)
        bst.add(3)
        bst.add(1)
        
        assert bst.size == 4
        assert bst.min.value == 1
        assert bst.max.value == 10
        
        # 测试只有右子树的树
        bst2 = BinarySearchTree()
        bst2.add(10)
        bst2.add(15)
        bst2.add(20)
        bst2.add(25)
        
        assert bst2.size == 4
        assert bst2.min.value == 10
        assert bst2.max.value == 25
    
    def test_negative_values(self):
        """测试负数值"""
        bst = BinarySearchTree()
        bst.add(-5)
        bst.add(-10)
        bst.add(-1)
        bst.add(0)
        
        assert bst.size == 4
        assert bst.min.value == -10
        assert bst.max.value == 0
        
        # 测试删除负数值
        bst.delete(-5)
        assert bst.get(-5) is None
        assert bst.size == 3
    
    def test_large_numbers(self):
        """测试大数值"""
        bst = BinarySearchTree()
        large_values = [1000000, 500000, 1500000, 250000, 750000, 1250000, 1750000]
        
        for value in large_values:
            bst.add(value)
        
        assert bst.size == len(large_values)
        assert bst.min.value == 250000
        assert bst.max.value == 1750000
        
        bst.delete(1000000)
        assert bst.get(1000000) is None
        assert bst.size == len(large_values) - 1
    
    def test_zero_value(self):
        """测试零值"""
        bst = BinarySearchTree()
        bst.add(0)
        bst.add(-1)
        bst.add(1)
        
        assert bst.size == 3
        assert bst.min.value == -1
        assert bst.max.value == 1
        
        bst.delete(0)
        assert bst.get(0) is None
        assert bst.size == 2
        assert bst.root.value in [-1, 1]  # 根节点可能是-1或1
    
    def test_sequential_deletion(self):
        """测试顺序删除"""
        bst = BinarySearchTree()
        values = [5, 3, 7, 1, 4, 6, 8]
        
        for value in values:
            bst.add(value)
        
        # 按顺序删除所有节点
        for value in values:
            original_size = bst.size
            bst.delete(value)
            assert bst.get(value) is None
            assert bst.size == original_size - 1
            
            # 验证树仍然保持BST性质
            def verify_bst_property(node):
                if node is None:
                    return True
                if node.left is not None and node.left.value >= node.value:
                    return False
                if node.right is not None and node.right.value <= node.value:
                    return False
                return verify_bst_property(node.left) and verify_bst_property(node.right)
            
            if bst.root is not None:
                assert verify_bst_property(bst.root)
        
        # 最后树应该为空
        assert bst.root is None
        assert bst.size == 0
    
    def test_reverse_sequential_deletion(self):
        """测试逆序删除"""
        bst = BinarySearchTree()
        values = [5, 3, 7, 1, 4, 6, 8]
        
        for value in values:
            bst.add(value)
        
        # 逆序删除所有节点
        for value in reversed(values):
            original_size = bst.size
            bst.delete(value)
            assert bst.get(value) is None
            assert bst.size == original_size - 1
        
        # 最后树应该为空
        assert bst.root is None
        assert bst.size == 0
    
    def test_duplicate_operations(self):
        """测试重复操作"""
        bst = BinarySearchTree()
        
        # 重复添加相同的值
        for _ in range(5):
            bst.add(5)
        
        assert bst.size == 1  # 只有1个节点
        assert bst.root.value == 5
        
        # 重复删除不存在的值
        for _ in range(3):
            bst.delete(10)
        
        assert bst.size == 1  # 大小不变
    
    def test_tree_structure_after_operations(self):
        """测试操作后的树结构"""
        bst = BinarySearchTree()
        
        # 构建一个特定的树结构
        bst.add(10)
        bst.add(5)
        bst.add(15)
        bst.add(3)
        bst.add(7)
        bst.add(12)
        bst.add(18)
        bst.add(1)
        bst.add(4)
        bst.add(6)
        bst.add(8)
        
        # 验证初始结构
        assert bst.size == 11
        assert bst.root.value == 10
        assert bst.root.left.value == 5
        assert bst.root.right.value == 15
        
        # 删除中间节点
        bst.delete(5)
        assert bst.get(5) is None
        
        # 验证新的根节点结构
        assert bst.size == 10
        # 左子树应该被重新组织
        assert bst.root.left is not None
    
    def test_consecutive_same_values(self):
        """测试连续相同值的处理"""
        bst = BinarySearchTree()
        
        # 尝试添加连续相同的值
        values = [5, 5, 5, 5, 5]
        for value in values:
            bst.add(value)
        
        assert bst.size == 1
        assert bst.root.value == 5
        assert bst.root.left is None
        assert bst.root.right is None
    
    def test_alternating_add_delete(self):
        """测试交替添加删除操作"""
        bst = BinarySearchTree()
        
        # 交替进行添加和删除操作
        bst.add(5)
        bst.add(3)
        bst.delete(3)
        bst.add(7)
        bst.add(1)
        bst.delete(5)
        bst.add(9)
        
        assert bst.size == 3
        assert bst.get(3) is None
        assert bst.get(5) is None
        assert bst.get(7) is not None
        assert bst.get(1) is not None
        assert bst.get(9) is not None
    
    def test_deep_tree_operations(self):
        """测试深层树的操作"""
        bst = BinarySearchTree()
        
        # 构建一个很深的树（链式结构）
        for i in range(20):
            bst.add(i)
        
        assert bst.size == 20
        assert bst.min.value == 0
        assert bst.max.value == 19
        
        # 删除中间的节点
        bst.delete(10)
        assert bst.get(10) is None
        assert bst.size == 19
        
        # 删除根节点
        bst.delete(0)
        assert bst.get(0) is None
        assert bst.size == 18
        assert bst.min.value == 1
    
    def test_wide_tree_operations(self):
        """测试宽树的操作"""
        bst = BinarySearchTree()
        
        # 构建一个很宽的树（每个节点都有两个子节点）
        bst.add(50)
        bst.add(25)
        bst.add(75)
        bst.add(12)
        bst.add(37)
        bst.add(62)
        bst.add(87)
        bst.add(6)
        bst.add(18)
        bst.add(31)
        bst.add(43)
        bst.add(56)
        bst.add(68)
        bst.add(81)
        bst.add(93)
        
        assert bst.size == 15
        
        # 删除根节点
        bst.delete(50)
        assert bst.get(50) is None
        assert bst.size == 14
        
        # 验证树仍然完整
        assert bst.min is not None
        assert bst.max is not None
    
    def test_get_info_edge_cases(self):
        """测试get_info方法的边界情况"""
        bst = BinarySearchTree()
        
        # 空树
        node, parent, position = BinarySearchTree.get_info(5, None)
        assert node is None
        assert parent is None
        assert position is None
        
        # 单节点树
        bst.add(5)
        node, parent, position = BinarySearchTree.get_info(5, bst.root)
        assert node.value == 5
        assert parent is None
        assert position is None
        
        # 不存在的节点
        node, parent, position = BinarySearchTree.get_info(10, bst.root)
        assert node is None
        assert parent is None
        assert position is None
    
    def test_get_min_max_info_edge_cases(self):
        """测试get_min_info和get_max_info的边界情况"""
        bst = BinarySearchTree()
        
        # 空树
        min_node, min_parent = BinarySearchTree.get_min_info(None)
        assert min_node is None
        assert min_parent is None
        
        max_node, max_parent = BinarySearchTree.get_max_info(None)
        assert max_node is None
        assert max_parent is None
        
        # 单节点树
        bst.add(5)
        min_node, min_parent = BinarySearchTree.get_min_info(bst.root)
        assert min_node.value == 5
        assert min_parent is None
        
        max_node, max_parent = BinarySearchTree.get_max_info(bst.root)
        assert max_node.value == 5
        assert max_parent is None
    
    def test_property_consistency(self):
        """测试属性的一致性"""
        bst = BinarySearchTree()
        
        # 测试空树
        assert bst.min is None
        assert bst.max is None
        assert bst.size == 0
        
        # 添加节点后测试
        bst.add(5)
        assert bst.min.value == 5
        assert bst.max.value == 5
        assert bst.size == 1
        
        # 添加更多节点
        bst.add(3)
        bst.add(7)
        assert bst.min.value == 3
        assert bst.max.value == 7
        assert bst.size == 3
        
        # 删除节点后测试
        bst.delete(5)
        assert bst.min.value == 3
        assert bst.max.value == 7
        assert bst.size == 2
    
    def test_complex_deletion_scenarios(self):
        """测试复杂的删除场景"""
        bst = BinarySearchTree()
        
        # 构建复杂树
        values = [20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]
        for value in values:
            bst.add(value)
        
        # 场景1：删除有复杂左子树的节点
        bst.delete(10)
        assert bst.get(10) is None
        assert bst.size == len(values) - 1
        
        # 场景2：删除有复杂右子树的节点
        bst.delete(30)
        assert bst.get(30) is None
        assert bst.size == len(values) - 2
        
        # 场景3：删除根节点
        bst.delete(20)
        assert bst.get(20) is None
        assert bst.size == len(values) - 3
        
        # 验证树仍然有效
        assert bst.min is not None
        assert bst.max is not None
        
        # 验证BST性质
        def verify_bst_property(node):
            if node is None:
                return True
            if node.left is not None and node.left.value >= node.value:
                return False
            if node.right is not None and node.right.value <= node.value:
                return False
            return verify_bst_property(node.left) and verify_bst_property(node.right)
        
        assert verify_bst_property(bst.root)
    
    def test_memory_cleanup_after_deletion(self):
        """测试删除后的内存清理"""
        bst = BinarySearchTree()
        
        # 添加节点
        bst.add(5)
        bst.add(3)
        bst.add(7)
        
        # 获取节点引用
        node_5 = bst.get(5)
        node_3 = bst.get(3)
        node_7 = bst.get(7)
        
        # 删除节点
        bst.delete(5)
        
        # 验证删除的节点不再被引用
        assert bst.get(5) is None
        # 验证其他节点仍然存在
        assert bst.get(3) is not None
        assert bst.get(7) is not None
        
        # 删除所有节点
        bst.delete(3)
        bst.delete(7)
        
        # 验证树为空
        assert bst.root is None
        assert bst.size == 0
        assert bst.min is None
        assert bst.max is None
    
    def test_inorder_traversal_property(self):
        """测试中序遍历的有序性"""
        bst = BinarySearchTree()
        
        # 构建树
        values = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93]
        for value in values:
            bst.add(value)
        
        def inorder_traversal(node):
            if node is None:
                return []
            return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)
        
        # 验证中序遍历结果是有序的
        traversal_result = inorder_traversal(bst.root)
        assert traversal_result == sorted(values)
        
        # 删除一些节点后再次验证
        bst.delete(50)
        bst.delete(25)
        bst.delete(75)
        
        remaining_values = [v for v in values if v not in [50, 25, 75]]
        traversal_result_after_deletion = inorder_traversal(bst.root)
        assert traversal_result_after_deletion == sorted(remaining_values)
    
    def test_height_balance_after_operations(self):
        """测试操作后的高度平衡"""
        bst = BinarySearchTree()
        
        def get_height(node):
            if node is None:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        # 添加节点
        for i in range(1, 8):
            bst.add(i)
        
        height_before = get_height(bst.root)
        
        # 删除根节点
        bst.delete(4)
        
        height_after = get_height(bst.root)
        
        # 高度不应该增加太多
        assert height_after <= height_before + 1
    
    def test_random_operations_sequence(self):
        """测试随机操作序列"""
        import random
        
        bst = BinarySearchTree()
        added_values = set()
        
        # 随机添加和删除操作
        for _ in range(100):
            if random.random() < 0.6 and len(added_values) < 50:  # 60%概率添加
                value = random.randint(1, 100)
                bst.add(value)
                added_values.add(value)
            elif added_values:  # 40%概率删除（如果树不为空）
                value = random.choice(list(added_values))
                bst.delete(value)
                added_values.remove(value)
        
        # 验证最终状态
        assert bst.size == len(added_values)
        if added_values:
            assert bst.min.value == min(added_values)
            assert bst.max.value == max(added_values)
        
        # 验证BST性质
        def verify_bst_property(node):
            if node is None:
                return True
            if node.left is not None and node.left.value >= node.value:
                return False
            if node.right is not None and node.right.value <= node.value:
                return False
            return verify_bst_property(node.left) and verify_bst_property(node.right)
        
        assert verify_bst_property(bst.root)
    
    def test_duplicate_value_handling(self):
        """测试重复值处理的一致性"""
        bst = BinarySearchTree()
        
        # 多次添加相同值
        for _ in range(10):
            bst.add(42)
        
        # 应该只有一个节点
        assert bst.size == 1
        assert bst.root.value == 42
        
        # 删除一次
        bst.delete(42)
        assert bst.size == 0
        assert bst.root is None
        
        # 再次添加
        bst.add(42)
        assert bst.size == 1
        assert bst.root.value == 42
    
    def test_edge_case_empty_operations(self):
        """测试空操作的边界情况"""
        bst = BinarySearchTree()
        
        # 在空树上进行各种操作
        bst.delete(5)  # 删除不存在的值
        bst.add(5)
        bst.delete(5)  # 删除后树变空
        bst.delete(5)  # 再次删除
        
        # 验证树为空
        assert bst.root is None
        assert bst.size == 0
        assert bst.min is None
        assert bst.max is None
    
    def test_property_invariants(self):
        """测试属性不变式"""
        bst = BinarySearchTree()
        
        # 空树的不变式
        assert bst.size == 0
        assert bst.min is None
        assert bst.max is None
        
        # 添加节点后的不变式
        bst.add(5)
        assert bst.size == 1
        assert bst.min.value == 5
        assert bst.max.value == 5
        assert bst.min == bst.max  # 单节点时min和max应该相等
        
        # 添加更多节点后的不变式
        bst.add(3)
        bst.add(7)
        assert bst.size == 3
        assert bst.min.value == 3
        assert bst.max.value == 7
        assert bst.min.value < bst.max.value  # min应该小于max
        
        # 删除节点后的不变式
        bst.delete(5)
        assert bst.size == 2
        assert bst.min.value == 3
        assert bst.max.value == 7
        assert bst.min.value < bst.max.value
    
    def test_repr_method(self):
        """测试__repr__方法"""
        bst = BinarySearchTree()
        
        # 空树的字符串表示
        assert repr(bst) == ''
        
        # 添加节点后的字符串表示
        bst.add(5)
        bst.add(3)
        bst.add(7)
        
        # 由于__repr__方法会打印输出，我们主要测试它不会抛出异常
        result = repr(bst)
        assert isinstance(result, str)
        assert result == ''  # 根据实现，应该返回空字符串