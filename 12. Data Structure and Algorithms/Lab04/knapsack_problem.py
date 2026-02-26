class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

def knapsack(items, capacity):
        sorted_items = sorted(items, key = lambda item: item.cost, reverse=True)
        """
        for i in items:
            print(i.weight, i.value, i.cost)
        """
        remain = capacity
        result = 0
        for i in range(len(sorted_items)):
            if sorted_items[i].weight <= remain:
                remain -= sorted_items[i].weight
                result += sorted_items[i].value
                print(f"item {i} - Weight {sorted_items[i].weight} - value {sorted_items[i].value}")
            elif remain > 0:
                fraction = remain / sorted_items[i].weight
                result += (sorted_items[i].cost * remain)
                print(f"item {i} - Weight {fraction * sorted_items[i].weight} - value {sorted_items[i].value}")
                break
            else :
                break

        return result


if __name__ == "__main__":
    w = [1, 3, 5, 4, 1, 3, 2]
    v = [5, 10, 15, 7, 8, 9, 4]
    items = []
    for i in range(len(w)):
        items.append(item(w[i], v[i]))
    print(f"Max Result = {knapsack(items, 15)}")   
    print(f"Max Result = {knapsack(items, 14)}")  
