"""
冒泡排序的pytest测试用例
"""
import pytest
from main import bubble_sort


class TestBubbleSort:
    """冒泡排序测试类"""
    
    def test_basic_sorting(self):
        """测试基本排序功能"""
        data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bubble_sort(data)
        assert data == expected
    
    def test_single_element(self):
        """测试单元素列表"""
        data = [1]
        expected = [1]
        bubble_sort(data)
        assert data == expected
    
    def test_empty_list(self):
        """测试空列表"""
        data = []
        expected = []
        bubble_sort(data)
        assert data == expected
    
    def test_two_elements(self):
        """测试两个元素"""
        data = [2, 1]
        expected = [1, 2]
        bubble_sort(data)
        assert data == expected
    
    def test_already_sorted(self):
        """测试已经排序的列表"""
        data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        bubble_sort(data)
        assert data == expected
    
    def test_reverse_sorted(self):
        """测试逆序列表"""
        data = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        bubble_sort(data)
        assert data == expected
    
    def test_duplicate_elements(self):
        """测试重复元素"""
        data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 9, 9, 10]
        bubble_sort(data)
        assert data == expected
    
    def test_all_same_elements(self):
        """测试所有元素相同"""
        data = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5]
        bubble_sort(data)
        assert data == expected
    
    def test_float_numbers(self):
        """测试浮点数"""
        data = [3.14, 2.71, 1.41, 1.73]
        expected = [1.41, 1.73, 2.71, 3.14]
        bubble_sort(data)
        assert data == expected
    
    def test_mixed_int_float(self):
        """测试整数和浮点数混合"""
        data = [3, 2.5, 1, 4.7, 2]
        expected = [1, 2, 2.5, 3, 4.7]
        bubble_sort(data)
        assert data == expected
    
    def test_negative_numbers(self):
        """测试负数"""
        data = [-3, -1, -4, -2, 0]
        expected = [-4, -3, -2, -1, 0]
        bubble_sort(data)
        assert data == expected
    
    def test_large_dataset(self):
        """测试大数据集"""
        data = list(range(100, 0, -1))  # 100到1的逆序
        expected = list(range(1, 101))  # 1到100的正序
        bubble_sort(data)
        assert data == expected
    
    def test_original_example(self):
        """测试原始示例"""
        data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 9, 9, 10]
        bubble_sort(data)
        assert data == expected


if __name__ == "__main__":
    pytest.main([__file__])
