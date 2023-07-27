pass_list = ['a', 'b', 'c']
for elem_1 in pass_list:
    for elem_2 in pass_list:
        if elem_2 not in [elem_1]:
            print(elem_1, elem_2)


'''for el1 in pass_list:
    for el2 in pass_list:
        if el2 != el1:
            for el3 in pass_list:
                if el1 != el3 != el2:
                    for el4 in pass_list:
                        if el4 != el1 and el4 != el2 and el4 != el3:
                            print(el1, el2, el3, el4)'''
'''for el1 in pass_list:
    for el2 in pass_list:
        if el2 != el1:
            for el3 in pass_list:
                if el3 not in [el1, el2]:
                    for el4 in pass_list:
                        if el4 not in [el1, el2, el3]:
                            print(el1, el2, el3, el4)'''
