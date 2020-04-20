import os

data='''
Select an option you want to run:
1) Port Scanning.
2) Network sniffing and store in pcap file.
3) Crack password using John the Ripper.
4) Collect Email/banner/urls from a URL.
5) Vulnerability scan.
6) Display running services on a host.
'''
print (data)
num = int(input("Enter your option: "))
if num == 1:
    print("What type of Scan you want to do?..")
    print("1) SYN   2) Xmas   3) Fin")
    option=int(input("Enter your choice: "))
    RHOST = input("Enter the RHOST: ")
    if option ==1:
        print(os.system("nmap -sS " + RHOST))
    elif option == 2:
        print(os.system("nmap -sX " + RHOST))
    elif option ==3:
        print(os.system("nmap -sF " + RHOST))
    else:
        print("Wrong input")        
elif num == 2:
    interface = input("Enter the interface: ")
    time = input("Enter the duration in seconds: ")
    filename = input("Enter the filename to save as: ")
    print(os.system("tshark -i " + interface + " -a duration:" + time + " -w " + filename + ".pcap"))
elif num == 3:
    wordlist = input("Enter the wordlist directory: ")
    md5_hashes_file = input("Enter the directory of the file containing the md5 hashes: ")
    print(os.system("john --format=raw-md5 --wordlist " + wordlist + " " + md5_hashes_file ))
elif num == 6:
    RHOST = input("Enter the RHOST: ")
    print(os.system("nmap -sV " + RHOST ))
elif num == 5:
    RHOST = input("Enter the RHOST: ")
    print(os.system("nmap -sV -script=vulners.nse " + RHOST ))
elif num == 4:
    url = input("Enter the url: ")
    print(os.system("theHarvester -d " + url + " -l 1000 -b all"))
else:
    Print("Wrong input")    

    
     
    
