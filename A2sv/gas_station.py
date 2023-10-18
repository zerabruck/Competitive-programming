class Solution:
    def canCompleteCircuit(self, gas, cost):
        tank = 0
        start_gas = 0
        index = 0
        n = len(gas)
        i = 0
        
        while i < n:
            diff = gas[i] - cost[i]
            tank += diff
            start_gas += diff
            
            if tank < 0:
                tank = 0
                index = i + 1
            
            i += 1
        
        if start_gas >= 0 and index < n:
            return index
        else:
            return -1
