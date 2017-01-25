# Fight Against Injustice III
# Interactive Fiction
# Julian Rojas and Sasai Nakmee

import sys

print "Fight Against Injustice III"
print 
print "The world you once lived in has been overtaken by the notorius Injustice League, led by a mysterious figure who's code name is Dump. This is the story of your quest."
print "What is your name?"
user_name = raw_input()
print 
print "Welcome %s. You are the chosen one. Now it is your duty to protect the people of Hollywood." %(user_name)

def accept_quest():
	print "Do you accept this quest that you have been chosen for? (y/n)"
	question1 = raw_input()
	print
	if question1 == "n" or question1 == "N":
		print "Game over"
		sys.exit()
	elif question1 == "y" or question1 =="Y": 
		print "Word on the street is that the notorious Dump is hiding somewhere in Hollywood. You notice a tower with high security and suspicious looking pins of Dump."
		print
		fight_boss1()
	else:
		print "Invalid choice. Choose y or n"
		accept_quest()
		
def fight_boss1():
	print "As you approach the tower, a young looking girl with bright yellow hair gets close to you. She doesn't want you to gain access to the tower and challenges you to a fight. Do you accept the challenge? (y/n)"
	question2 = raw_input()
	print 
	if question2 == "n" or question2 == "N":
		print "You walked around the tower and there is no other entrance into the tower. You come back to the front extrance."
		fight_boss1()
	elif question2 == "y" or question2 =="Y": 
		print "The young looking girl turns out to be none other than Justin Bieber. He gives you the option of either fighting him or answering a question. You haven't had any lunch and would rather save your energy for the boss, so you choose to answer his question."
		print
		boss1()
	else:
		print "Invalid choice. Choose y or n"
		fight_boss1()

def boss1():
	print "He said 'This will determine whether you're a true Belieber. In what year did my hit single Baby come out?'"
	print "a) 2010" 
	print "b) 2011" 
	print "c) You slap him"
	boss1_answer = raw_input()
	print
	
	if boss1_answer == "a" or boss1_answer =="A":
		print "*Justin Bieber gasps*"
		print 
		print "Justin replies 'You really ARE a Belieber!!!!!'"
		print "I grant you 2 VIP passes to my next world tour. You may enter the gate"
		raw_input ("Press Enter to continue...")
		print 
		print "As you cross the gate you see a man stumbling accross the yard. As you make your way towards the door he approaches you. The man turns out to be Lil Jon."
		print
		boss2()
	elif boss1_answer == "b" or boss1_answer == "B":
		print "Try Again"
		boss1()
	elif boss1_answer == "c" or boss1_answer == "C":
		print "Justin Bieber calls for back up and you are taken to the dungeon. Your missions has failed and the Injustice League has taken over the world."
		print "Game Over"
		sys.exit()
	else:
		print "Invalid choice. Choose a, b, or c"
		boss1()
		
		
def boss2():
	print "Lil Jon asks 'What are you doing here?' What is your response?"
	print "a) Tell me where Dump is!" 
	print "b) Have you seen the boss?"
	print "c) Pretend to be a delivery person and say 'I'm delivering a very important package to Dump. I need to enter the building immediately.'"
	boss2_answer = raw_input()
	print 
		
	if boss2_answer == "a" or boss2_answer == "A":
		print "WHAT?!"
		boss2()
	elif boss2_answer == "b" or boss2_answer == "B":
		print "YEA!"
		boss2()
	elif boss2_answer == "c" or boss2_answer == "C":
		print "OKAY!"
		print "His office is located on the top floor...the Penthouse!"
		print 
		print"*Lil Jon opens the door and let's you inside the building.*"
		raw_input("Press Enter to continue...")
		print
		print"As you proceed to make your way inside the bulding, you hear an obnoxious sound which turns out to be coming from 3 women clearly obsessed over their looks. You try to make your way towards the elevator when one of the women notices you and the conversation ceases."
		raw_input ("Press Enter to continue...")
		print
		print "All three quickly make their way to you with the intent to stop you from your mission."
		boss3()
	else:
		print "Invalid choice. Choose a, b, or c"
		boss2()
		

		
def boss3():
	print "The oldest one takes charge and says 'My name is Kourtney. We are...like...the Kardashian Sisters. You look poor...Who are you? Are you a maintenance worker? (y/n)"
	boss3_answer = raw_input()
	print 
	if boss3_answer == "y" or boss3_answer == "Y":
		print "You are...like...totally a lifesaver! You can take the elevator to the basement to get the cleaning supplies. Just hurry up because my sisters and I have...like...been waiting for...like...an hour and we really to get a tan."
		print
		print "You walk in the elevator, and as the door closes, you immediately press the penthouse button."
		raw_input("Press Enter to continue...")
		print
		print "The elevator door opens and you see someone sitting in a big chair. It is then that you realize you have found Dump, who turns out to be none other than...Donald Trump. You approach the chair and make eye contact with the leader of the Injustice League."
		raw_input ("Press Enter to continue...")
		print
		boss4()
	elif boss3_answer == "n" or boss3_answer == "N":
		boss3_2()
	else:
		print "Invalid choice. Choose y or n"		
		boss3()
		
def boss3_2():
		print "Are you serious? This is...like...so annoying. Like seriously. If you're not with maintenance, then who are you and what are you doing here?"
		print "a) My mistake, I am with maintenance"
		print "b) Can you just shut up and stop wasting my time?! You are the most ridiculous, self-absorbed people I know. I'm going to see the Dump so let me through!"
		boss3_answer2 = raw_input()
		print 
			
		if boss3_answer2 == "a" or boss3_answer2 == "A":
			print "You are...like...totally a lifesaver! You can take the elevator to the basement to get the cleaning supplies. Just hurry up because my sisters and I have...like...been waiting for...like...an hour and we really to get a tan."
			print "You walk in the elevator, and as the door closes, you immediately press the penthouse button."
			raw_input("Press Enter to continue...")
			print 
			print "The elevator door opens and you see someone sitting in a big chair. It is then that you realized you have found Dump, who turns out to be none other than...Donald Trump. You approach the chair and make eye contact with the leader of the Injustice League."
			raw_input ("Press Enter to continue...")
			print
			boss4()
			
		elif boss3_answer2 == "b" or boss3_answer2 == "B":
			print "The youngest Kardashian, Khloe, tackles you in anger and you get knocked out cold."
			print "You wake up outside the building with Lil Jon"
			print
			boss2()
		else :
			print "Invalid choice. Choose a or b"
			boss3_2()
			
def boss4():
	print "Donald Trump stares you in the eye and says 'You have uncovered my secret hideout location. If you want to defeat the Injustice League, you must answer the following question."
	print 
	print "Who will you be voting for in the 2016 election?"
	print "a) Donald Trump"
	print "b) *scoffs* Hillary Clinton"
	boss4_answer = raw_input()
	print 
	if boss4_answer == "a" or boss4_answer == "A":
		print "Donald Trump says '%s, you and I will rule the world!'" %(user_name)
		print "You have failed your mission!"
		print "Game Over!"
		sys.exit()
	elif boss4_answer == "b" or boss4_answer == "B":
		print "I needed one more vote to become the next President and now my lifelong dream will never become a reality."
		print "*starts to cry*"
		print "I will run away and never return...NEVER!!!!!"
		raw_input ("Press Enter to continue...")
		print 
		print "*1 week later*"
		print
		print "Donald Trump and the Injustice League have left the Country and the world is back to being a peaceful place."
		print "Thank you %s!" %(user_name)
		print "Congratulations for completing your quest!"
		sys.exit()
	else :
		print "Invalid choice. Choose a or b"
		boss4()
		
accept_quest()
