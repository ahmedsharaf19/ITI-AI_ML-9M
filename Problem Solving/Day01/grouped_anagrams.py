# Problem Link: https://leetcode.com/problems/group-anagrams/
# Submission Link: https://leetcode.com/problems/group-anagrams/submissions/1807375275/


from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}

        for element in strs:
            sortedElement = "".join(sorted(element))
            if sortedElement not in groupedAnagrams.keys():
                groupedAnagrams[sortedElement] = []
            
            groupedAnagrams[sortedElement].append(element)
        return list(groupedAnagrams.values())