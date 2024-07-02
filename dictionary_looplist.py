student=["Mohamed","Sara","Hussein","Iman"]
grades=[20,30,20,40]
new_dict=dict(zip(student,grades))
empty_list={}
print(empty_list)
print(new_dict)
for value in new_dict.values():
    if value == 40:
        value="A"
    if value == 30:
        value="B"
    if value == 20:
        value ="C"
    if value in empty_list:
        empty_list[value]+=1
    else:
        empty_list[value]=1
print(empty_list)
