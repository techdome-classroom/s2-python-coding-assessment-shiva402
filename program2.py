class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Loop through each character in the string
        for i in range(n):
            # Get the value of the current symbol
            current_val = roman_map[s[i]]
            
            # Check if the next symbol exists and is larger than the current symbol
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                # Subtract the current value
                total -= current_val
            else:
                # Add the current value
                total += current_val
        
        return total
