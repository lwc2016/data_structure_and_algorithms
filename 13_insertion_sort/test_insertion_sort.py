"""
插入排序的pytest测试用例
"""

import pytest
from main import insertion_sort


class TestInsertionSort:
    """插入排序测试类"""
    
    def test_basic_sort(self):
        """测试基本排序功能"""
        data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 8]
        insertion_sort(data)
        assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def test_single_element(self):
        """测试单元素数组"""
        data = [1]
        insertion_sort(data)
        assert data == [1]
    
    def test_empty_array(self):
        """测试空数组"""
        data = []
        insertion_sort(data)
        assert data == []
    
    def test_two_elements(self):
        """测试两个元素"""
        data = [2, 1]
        insertion_sort(data)
        assert data == [1, 2]
    
    def test_already_sorted(self):
        """测试已排序数组"""
        data = [1, 2, 3, 4, 5]
        insertion_sort(data)
        assert data == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted(self):
        """测试逆序数组"""
        data = [5, 4, 3, 2, 1]
        insertion_sort(data)
        assert data == [1, 2, 3, 4, 5]
    
    def test_duplicate_elements(self):
        """测试重复元素"""
        data = [3, 1, 3, 1, 3]
        insertion_sort(data)
        assert data == [1, 1, 3, 3, 3]
    
    def test_negative_numbers(self):
        """测试负数"""
        data = [-3, -1, -4, -2, -5]
        insertion_sort(data)
        assert data == [-5, -4, -3, -2, -1]
    
    def test_mixed_positive_negative(self):
        """测试正负数混合"""
        data = [3, -1, 0, -4, 2]
        insertion_sort(data)
        assert data == [-4, -1, 0, 2, 3]
    
    def test_float_numbers(self):
        """测试浮点数"""
        data = [3.5, 1.2, 4.8, 2.1, 0.5]
        insertion_sort(data)
        assert data == [0.5, 1.2, 2.1, 3.5, 4.8]
    
    def test_mixed_int_float(self):
        """测试整数和浮点数混合"""
        data = [3, 1.5, 2, 4.2, 1]
        insertion_sort(data)
        assert data == [1, 1.5, 2, 3, 4.2]
    
    def test_zero_in_array(self):
        """测试包含0的数组"""
        data = [0, -1, 2, 0, 3]
        insertion_sort(data)
        assert data == [-1, 0, 0, 2, 3]
    
    def test_all_same_elements(self):
        """测试所有元素相同"""
        data = [3, 3, 3, 3, 3]
        insertion_sort(data)
        assert data == [3, 3, 3, 3, 3]
    
    def test_large_array(self):
        """测试大数组"""
        data = list(range(100, 0, -1))  # 100到1的逆序
        insertion_sort(data)
        assert data == list(range(1, 101))  # 1到100的正序
    
    def test_single_negative(self):
        """测试单个负数"""
        data = [-5]
        insertion_sort(data)
        assert data == [-5]
    
    def test_partially_sorted(self):
        """测试部分已排序的数组"""
        data = [1, 3, 2, 4, 6, 5, 7]
        insertion_sort(data)
        assert data == [1, 2, 3, 4, 5, 6, 7]
    
    def test_three_elements(self):
        """测试三个元素"""
        data = [3, 1, 2]
        insertion_sort(data)
        assert data == [1, 2, 3]
    
    def test_negative_zero_positive(self):
        """测试负数、零、正数混合"""
        data = [2, 0, -1, 3, -2]
        insertion_sort(data)
        assert data == [-2, -1, 0, 2, 3]
    
    def test_decimal_precision(self):
        """测试小数精度"""
        data = [0.1, 0.01, 0.001, 0.0001]
        insertion_sort(data)
        assert data == [0.0001, 0.001, 0.01, 0.1]
    
    def test_large_negative_numbers(self):
        """测试大负数"""
        data = [-100, -50, -200, -25]
        insertion_sort(data)
        assert data == [-200, -100, -50, -25]
    
    def test_alternating_pattern(self):
        """测试交替模式"""
        data = [1, 3, 2, 4, 3, 5, 4]
        insertion_sort(data)
        assert data == [1, 2, 3, 3, 4, 4, 5]


if __name__ == "__main__":
    pytest.main([__file__])
