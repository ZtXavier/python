def acronym(phrase):
    res = ""
    ls = phrase.split("  ")
    for i in ls:
        res = res + i[0]
    return res.upper()


# def acronym(phrase):
#     #str1用于存储
#     str1 = ""
#     str = list(phrase.split())#按照空格分隔，使其每一个元素都放到list集合当中;
#     for i in str:#临时变量i用于获取集合str中的元素对象;
#         for j in i:#i指的是集合中的第一个元素，j遍历元素对象i;
#             if(j.isupper()):#isupper()是用来判断这个字符是否是大写的英文字母;
#                 str1 =str1+j
#                 break#只取第一个字符;
#             elif(j.lower()):#islower()判断该字符是否是小写的英文字母;
#                 str1 = str1 +chr(ord(j)-32)
#                 break
#     return str1



phrase=input()
print(acronym(phrase))