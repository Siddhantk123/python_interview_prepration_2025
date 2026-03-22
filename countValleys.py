'''
https://www.hackerrank.com/challenges/counting-valleys/problem
'''
def count_valleys(steps, string_path):
    # Write your code here
    alt=0
    num_of_valley=0
    valley_flag = False
    for step in string_path:  
        if step == "U":
            alt+=1
        elif step == "D":
            alt -= 1
            
        if alt < 0:
            valley_flag = True
        if alt > 0:
            valley_flag = False
       
        if alt == 0 and valley_flag == True: #meaning once cycle completed for valley
            num_of_valley +=1 
    print(num_of_valley)

count_valleys(8, "UDDDUDUU") #1
count_valleys(12, "DDUUDDUDUUUD") #2

def cout_valley_mountain(steps, string_path):
    alt=0
    mount_flag, valley_flag = False, False
    count_mount, count_valley = 0,0
    for step in string_path:
        if step == "U":
            alt+=1
        elif step == "D":
            alt-=1
        
        if alt > 0:
            mount_flag, valley_flag = True, False
        if alt < 0:
            valley_flag, mount_flag = True, False
        
        # import pdb;pdb.set_trace()
        if alt == 0 and mount_flag == True:
            count_mount +=1
        if alt == 0 and valley_flag == True:
            count_valley +=1
    print(count_mount,count_valley)

cout_valley_mountain(8, "UDDDUDUU")
cout_valley_mountain(12, "DDUUDDUDUUUD")






