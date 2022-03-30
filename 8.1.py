dict1 = {0:'零',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖'}
dict2_ = {3:'仟',2:'佰',1:'拾'}

def four_to_str(four_str):
    result = ""
    num_len = len(four_str)
    for i in range(num_len):
        num = int(four_str[i])
        if i != num_len - 1:
            result = result + dict1[num] + dict2_[num_len - i - 1]
        else:
            result = result + dict1[num]
    return result

def change(num):
    str_num = str(num)
    str_len = len(str_num)
    if (str_len > 12):
        return
    elif(str_len > 8):
        return four_to_str(str_num[:-8]) + '亿' + four_to_str(str_num[-8:-4]) + '万' + four_to_str(str_num[-4:]) + '圆'             # 这里切片一定要注意要逆向切片来遍历字符串
    elif(str_len > 4):
        return four_to_str(str_num[-8:-4]) + '万' + four_to_str(str_num[-4:]) + '圆'
    else:
        return  four_to_str(str_num[-4:]) + '圆'
    
    
n = eval(input())
print(change(n))