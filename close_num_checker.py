def containsCloseNums(nums, k):
    
    # # method1 - works
    # # worst case time complexity - O[n2]
    
    # for i in range(len(nums) - 1):
    #     j = i + 1
    #     while j < len(nums) and j-i <= k:
    #         # print(i, j)
    #         if nums[j] == nums[i]:
    #             return True
    #         j+=1
            
    # return False
    
    # method2
    in_map = {}
    num = set()
    found = False
    
    for i, n in enumerate(nums):
        if n in num:
            for ind in in_map[n]:
                if i - ind <= k:
                    return True 
            
            in_map[n].append(i)
        else:
            num.add(n)
            in_map[n] = [i]
        
    # print(in_map)
    return False
    
    
