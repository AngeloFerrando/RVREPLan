# from difflib import Differ

plus = 0
minus = 0

# strings = [";","?"]

# with open('lama\\depot\\plans_injected_errors_1\\dictionary_plans.txt') as dict:
#     for line in dict:
#         print(line)

with open('lama\\depot\\plans_injected_errors_3\\replan_1') as file_1, open('lama\\depot\\plans_injected_errors_3\\replan_2') as file_2: 
    lines1 = list(file_1.readlines()[13:])
    lines2 = list(file_2.readlines())
    for line in lines1:
        if ";" not in line:
            if line not in lines2:
                plus+=1

    for line in lines2:
        if ";" not in line:
            if line not in lines1:
                minus+=1
            

    # differ = Differ()

    # file_1.seek(6)
    # print(file_1.readlines()[6:])

    # for line in differ.compare(file_1.readlines()[2:], file_2.readlines()): 
    #     if all(x not in line for x in strings):
    #         # print(line)
    #         if "+" in line:
    #             plus+=1
    #         elif "-" in line:
    #             minus+=1

print("Plus ",plus)
print("Minus ",minus)
print("Total: ",plus+minus)


# with open('lama\\depot\\plans_injected_errors_1\\original.txt') as file_1: 
#     file_1_text = file_1.readlines() 
  
# with open('lama\\depot\\plans_injected_errors_1\\replan_1.txt') as file_2: 
#     file_2_text = file_2.readlines() 
  
# # Find and print the diff: 
# for line in difflib.unified_diff( 
#         file_1_text, file_2_text, fromfile='lama\\depot\\plans_injected_errors_1\\original.txt',  
#         tofile='lama\\depot\\plans_injected_errors_1\\replan_1.txt', lineterm=''): 
#     print(line) 

