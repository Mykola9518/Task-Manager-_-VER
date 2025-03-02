class task_manager():
    isnotcorrect = True
    while isnotcorrect:
        print ("TASK MANAGER")
        try:
            operation_desc = [
            'Select action:\n'
            '1 - Add a task \n'
            '2 - Show all tasks \n'
            '3 - Find a task \n'
            '4 - Task filter \n'
            '5 - Delete task \n'
            '6 - Mark as done \n'
            '7 - Quit \n' 
            ]
            operation = ['1', '2', '3', '4', '5', '6', '7']
            for item in operation_desc:
                print(item)
            print("Enter operation")
            select_action = str(input())
            if select_action in operation:
                if select_action == '1':
                    import Add_a_task
                    isnotcorrect = True
                elif select_action == '2':
                    print('Show all tasks')
                    isnotcorrect = True
                elif select_action == '3':
                    print('Finf a task')
                    isnotcorrect = True
                elif select_action == '4':
                    print('Task filter')
                    isnotcorrect = True
                elif select_action == '5':
                    print('Delete task')
                    isnotcorrect = True
                elif select_action == '6':
                    print('Mark as done')
                    isnotcorrect = True
                elif select_action == '7':
                    print('Quit the program')
                    isnotcorrect = False
                else:
                    raise ValueError('Not corrected operation')
        except:
            print('Error')
            isnotcorrect = True
Task = task_manager()



