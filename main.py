from ToDecimal import ToDecimal

user_input = str(input("Hex/Binary: ")).split(" ")

result_list = [str(ToDecimal(i).result) for i in user_input]

result = " ".join(result_list)

print(result)




