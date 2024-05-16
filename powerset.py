import math

def generatePowerSet(input_set):
    set_size = len(input_set)
    pow_set_size = int(math.pow(2, set_size))
    
    power_set = []
    
    for counter in range(0, pow_set_size):
        subset = set()
        for j in range(0, set_size):
            if counter & (1 << j):
                subset.add(list(input_set)[j])
        power_set.append(subset)
    
    return power_set

# Example usage:
input_set = ['a', 'b', 'c','d','e']
power_set = generatePowerSet(input_set)
print(power_set)

