"""
选择排序的pytest测试用例
"""

import pytest
from main import select_sort


class TestSelectSort:
    """选择排序测试类"""
    
    def test_basic_sort(self):
        """测试基本排序功能"""
        data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 8]
        select_sort(data)
        assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def test_single_element(self):
        """测试单元素数组"""
        data = [1]
        select_sort(data)
        assert data == [1]
    
    def test_reverse_sorted(self):
        """测试逆序数组"""
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        select_sort(data)
        assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def test_already_sorted(self):
        """测试已排序数组"""
        data = [1, 2, 3, 4, 5]
        select_sort(data)
        assert data == [1, 2, 3, 4, 5]
    
    def test_two_elements(self):
        """测试两个元素"""
        data = [2, 1]
        select_sort(data)
        assert data == [1, 2]
    
    def test_duplicate_elements(self):
        """测试重复元素"""
        data = [3, 1, 3, 1, 3]
        select_sort(data)
        assert data == [1, 1, 3, 3, 3]
    
    def test_negative_numbers(self):
        """测试负数"""
        data = [-3, -1, -4, -2, -5]
        select_sort(data)
        assert data == [-5, -4, -3, -2, -1]
    
    def test_mixed_positive_negative(self):
        """测试正负数混合"""
        data = [3, -1, 0, -4, 2]
        select_sort(data)
        assert data == [-4, -1, 0, 2, 3]
    
    def test_float_numbers(self):
        """测试浮点数"""
        data = [3.5, 1.2, 4.8, 2.1, 0.5]
        select_sort(data)
        assert data == [0.5, 1.2, 2.1, 3.5, 4.8]
    
    def test_mixed_int_float(self):
        """测试整数和浮点数混合"""
        data = [3, 1.5, 2, 4.2, 1]
        select_sort(data)
        assert data == [1, 1.5, 2, 3, 4.2]
    
    def test_empty_array(self):
        """测试空数组"""
        data = []
        select_sort(data)
        assert data == []
    
    def test_single_negative(self):
        """测试单个负数"""
        data = [-5]
        select_sort(data)
        assert data == [-5]
    
    def test_all_same_elements(self):
        """测试所有元素相同"""
        data = [3, 3, 3, 3, 3]
        select_sort(data)
        assert data == [3, 3, 3, 3, 3]
    
    def test_large_array(self):
        """测试大数组"""
        data = list(range(100, 0, -1))  # 100到1的逆序
        select_sort(data)
        assert data == list(range(1, 101))  # 1到100的正序
    
    def test_zero_in_array(self):
        """测试包含0的数组"""
        data = [0, -1, 2, 0, 3]
        select_sort(data)
        assert data == [-1, 0, 0, 2, 3]


if __name__ == "__main__":
    pytest.main([__file__])
