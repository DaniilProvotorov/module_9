def apply_all_func(in_list, *functions):
    results = {}
    for i in functions:
        name = i.__name__
        results[name] = i(in_list)
    return results


print(apply_all_func([6,20,15,9], sorted))