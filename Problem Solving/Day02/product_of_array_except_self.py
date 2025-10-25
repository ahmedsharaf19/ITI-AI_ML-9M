# Problem Link: https://leetcode.com/problems/product-of-array-except-self/
# Submission Link: https://leetcode.com/problems/product-of-array-except-self/submissions/1808305762/

from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
        result = []
        prefix_product = [1]
        for element in nums:
            prefix_product.append(prefix_product[-1] * element)
        suffix_product = [1]
        for element in nums[::-1]:
            suffix_product.append(suffix_product[-1] * element)
        suffix_product = suffix_product[::-1]

        for i in range(len(nums)):
            result.append(prefix_product[i] * suffix_product[i+1])
        return result