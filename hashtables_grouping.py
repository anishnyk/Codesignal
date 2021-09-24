def groupingDishes(dishes):
    ings_dict = {}
    ings = set()
    for dish in dishes:
        for ing in dish[1:]:
            if ing in ings:
                ings_dict[ing].append(dish[0])
            else:
                ings_dict[ing] = [dish[0]]
                ings.add(ing)
            
    # print(ings_dict)
    # print(ings)
    
    ret = []
    for ing in sorted(list(ings)):
        if len(ings_dict[ing]) > 1:
            ret.append([ing] + sorted(ings_dict[ing]))
        
    return ret
        

