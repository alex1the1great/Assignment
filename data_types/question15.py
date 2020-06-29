def insert_str_middle(string, str_middle):
    # get middle value
    get_middle_num = len(string) // 2
    # insert middle string in middle of 1st string
    new_string = string[:get_middle_num] + str_middle + string[get_middle_num:len(string)]

    print(new_string)


insert_str_middle('{[]}', 'random')