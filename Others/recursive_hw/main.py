import random
# def task_one():
#     number = int(input("Input number: "))
#     number_step = int(input("Input step: "))
#     print(number ** number_step)
#     return task_one()
#
# task_one()
#
#
# def task_two():
#     a = int(input("Input first num: "))
#     b = int(input("Input second num: "))
#     n = 0
#     for i in range(a, b+1):
#         n += i
#     print(n)
#     return task_two()
#
#
# task_two()
#
#
# def task_three():
#     n = int(input("Enter number of stars: "))
#     print("*" * n)
#     return task_three()
#
#
# task_three()
#
#
# def task_six():
#     print("Date format: dd-mm-yyyy")
#     fd = (input("Enter first date: "))
#     sd = (input("Enter second date: "))
#     fd_list = fd.split("-")
#     sd_list = sd.split("-")
#
#     if (fd_list[0] > "31" or fd_list[1] > "12" or len(fd_list[2]) != 4) or (sd_list[0] > "31" or sd_list[1] > "12" or len(sd_list[2]) != 4):
#         print("Wrong date format")
#     else:
#         if fd_list[2] > sd_list[2]:
#             print("First date is bigger!")
#         elif fd_list[2] < sd_list[2]:
#             print("Second date is bigger!")
#         elif fd_list[2] == sd_list[2]:
#             if fd_list[1] > sd_list[1]:
#                 print("First date is bigger!")
#             elif fd_list[1] < sd_list[1]:
#                 print("Second date is bigger!")
#             elif fd_list[1] == sd_list[1]:
#                 if fd_list[0] > sd_list[0]:
#                     print("First date is bigger!")
#                 elif fd_list[0] < sd_list[0]:
#                     print("Second date is bigger!")
#                 elif fd_list[0] == sd_list[0]:
#                     print("Dates are the same!")
#
#     return task_six()
#
#
# task_six()
