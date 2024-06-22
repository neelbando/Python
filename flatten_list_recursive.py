# lstx = [[0,1],2,[3,4,[5,6,[7,8,9,[10,11]]]]]
lstx = [[0,1],2,[3,4,[5,6,[7,8,9,[10,11]]]]]

def flatten_list(lst):
    out_list = []
    
    def flatten(ls,olst):
        for itm in ls:
            if isinstance(itm,list):
                flatten(itm,olst)
            else:
                olst.append(itm)
                
        return out_list
                
    return flatten(lst,out_list)


cc = flatten_list(lstx)
print(cc)