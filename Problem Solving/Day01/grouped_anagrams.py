class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}

        for element in strs:
            sortedElement = "".join(sorted(element))
            if sortedElement not in groupedAnagrams.keys():
                groupedAnagrams[sortedElement] = []
            
            groupedAnagrams[sortedElement].append(element)
        return list(groupedAnagrams.values())