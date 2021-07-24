print("\033[1;31m           Welcome To Health Management System")
def fun():
	import datetime
	return datetime.datetime.now()
	
	
	
vvv = fun()
	
with open("NishantaExacise.txt", "r") as v:
	a = v.read()
	
print("\033[1;32m1. To Open Nishanta Exacise list")
print("2.To Open Harry Exacise list")
print("3.To Open Rohan Exacise list")

N = (input("Choose The Name To Open  Exacise list:-"))
print(N)

if (N == "1"):
		print("\033[1;31m" + "The Exacise for Nishanta\n"+ a)
		
with open("Harryexacise.txt", "r") as r:
	e = r.read()
	
	
if (N == "2"):
		print("The Exasice Of Harry\n" + e)
		

with open("Rohanexacise.txt", "r") as z:
        o = z.read()
        
        
if (N == "3"):
	print("The Exasise Of Rohan\n" + o)
	
	
###Sec Path###
print("Choose Your Optional to Get the Value")

with open ("Na.txt", "r") as cc:
	a = cc.read()
	print("\033[1;32m" + a)
ii = input("Choose Numbers To Open Food List:-")	

with open("NishantaFood.txt", "r") as q:
	 w = q.read()
	 
with open("Harryfood.txt", "r") as qq:
	 ww = qq.read()
	 
with open("Rohan Food.txt", "r") as e:
	 s = e.read()
	 
if (ii == "1"):
		print("\033[1;31m", end=""+ str(fun()) + " Time to eat\n" +"The Food list Of Nishata\n" + w)
elif (ii == "2"):
		print("\033[1;31m", end="" + str(fun()) + " Time to eat\n" +"The Food list Of Nishata\n" + ww)
elif (ii == "3"):
		print("\033[1;31m", end="" + str(fun()) + " Time to eat\n" +"The Food list Of Nishata\n" + s)