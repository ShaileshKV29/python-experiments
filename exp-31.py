num_list = list({12,2324,334,45,55,65,776,87,8,99,2})
max_num = max(num_list)
min_num = min(num_list)
num_list.remove(max_num)
num_list.remove(min_num)
max_num2 = max(num_list)
min_num2 = min(num_list)

print(f"Second Max : {max_num2}, Second Min : {min_num2}")
