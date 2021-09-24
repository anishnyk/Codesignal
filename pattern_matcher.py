def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns):
        return False
      
    string_map = {}
    pattern_map = {}
    pattern = set() 
    string = set() 
    for i in range(len(strings)):
        if patterns[i] not in pattern:
            pattern_map[patterns[i]] = strings[i]
            pattern.add(patterns[i])
        else:
            if pattern_map[patterns[i]] != strings[i]:
                return False
        
        if strings[i] not in string:
            string_map[strings[i]] = patterns[i]
            string.add(strings[i])
        else:
            if string_map[strings[i]] != patterns[i]:
                return False
    
    # print(pattern_map)
    # print(string_map)
    return True
