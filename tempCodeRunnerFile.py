 for index, line in enumerate(user_list):
                    temp = line.split(",")
                    # if total_task_per_user >= 1 :
                    total_task_per_user = (f"{temp[0]}, {names.count(temp[0])}")
                    print(total_task_per_user)
                        # print(f"{temp[0]}")
                        # print(f"{names.count(temp[0])}")