def isCryptSolution(crypt, solution):
    sol_dict = {el[0]:el[1] for el in solution}
    
    crypt_nums = []
    for word in crypt:
        num = ''
        for letter in word:
            num += sol_dict[letter]
        if num[0] == '0' and len(num)>1:
            return False
        crypt_nums.append(num)
        
    if int(crypt_nums[0]) + int(crypt_nums[1]) == int(crypt_nums[2]):
        return True
        
    return False
    
    
        
    
