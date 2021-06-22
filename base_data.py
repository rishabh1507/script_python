import subprocess
import os

day = subprocess.run('date "+%d"',shell=True,stdout=subprocess.PIPE)
month = subprocess.run('date "+%m"',shell=True,stdout=subprocess.PIPE)
year = subprocess.run('date "+%Y"',shell=True,stdout=subprocess.PIPE)


def space_util():
    temp = subprocess.run('df -kh /base/data',shell=True,stdout=subprocess.PIPE)
    print("Current space Util : \n", temp.stdout.decode())


def top_consumer():
    temp_result1 = subprocess.run('du -sh /base/data/* | sort -hr | head -n 5',shell=True,stdout=subprocess.PIPE)
    print("Top 5 File Consumers are : \n", temp_result1.stdout.decode())

def interval_logs():
    #'find /base/data -newermt '+"'"+str(int(year.stdout.decode()))+"-"+str(int(month.stdout.decode())-2)+"-"+str(day.stdout.decode())+"'"+' \! -newermt '+"'"+str(int(year.stdout.decode()))+"-"+str(int(month.stdout.decode()))+"-"+str(int(day.stdout.decode()))+"'",shell=True,stdout=subprocess.PIPE
    # find /base/data -type f -mtime +30 -mtime -60
    #1. for PIMCO System something like this could work well find 
    # find /base/logs/svc_core_np/*  maxdepth 0 -type d -ctime +30 -ctime -60
    temp_result2 = subprocess.run('find /base/data/* -type d,f,l -mtime -100',shell=True,stdout=subprocess.PIPE)
    print("Files Listed : \n", temp_result2.stdout.decode())
    return temp_result2



def log_view(temp_result3):
    li = temp_result3.stdout.decode().split('\n')
    return li

def delete_file(li):
    ip = input("Are you sure you want to delete above listed files ? (y/n)")
    if(ip=="y"):
        for i in range(len(li)-1):
            li[i]=li[i].strip()
            subprocess.run('sudo rm -r '+li[i],shell=True,stdout=subprocess.PIPE)
        print("deleted the files\ncurrent space :\n")
        space_util()

    else:
        print("process terminated")

if __name__ == "__main__":
    space_util()
    top_consumer()
    temp = interval_logs()
    li1 = log_view(temp)
    delete_file(li1)


