import time

def add_log(user_first_name):
    print(user_first_name)
    #text = "User: " + user_first_name + " " + user_last_name + " (" + str(user_id) + ") connected at " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    f = open('logs.txt', 'a')
    f.write(format(user_first_name))
    f.close()
    