invite_list=["john","H","moe"]
print(invite_list)
print("hello " + invite_list[0].title() + " you are invited to the party :D" )
print("hiiiii " + invite_list[1] + " 10/10")
print("hello\n" + invite_list[2].title() + "\nyou are invited to today's party :D")
print(invite_list[2].title() + " can't attend the dinner party")
invite_list.pop(2)
invite_list.append("jack")
print(invite_list[2].title() + " your are invited to our dinner party")
message=("a bigger dinner table was found and the guest list has been changed")
print(message)
invite_list.insert(0,"joe")
invite_list.insert(2,"seif")
invite_list.append("liz")
print(invite_list)
#after further thinking, instaed of makinng a unique meesage for everybody
#i decided to just put a generic message in varibale called "invite_message"
#and just print it for the addtional guests.
invite_message=(" You are invited to our dinner party on the 13th of april")
print(invite_list[0] + invite_message)
print(invite_list[2] + invite_message)
print(invite_list[3] + invite_message)
print("The mentioned dinner table was broken during shipping and sadly we won't be able to invite more than 2 guests")
cancelled_guests=[invite_list.pop(5),invite_list.pop(4),invite_list.pop(3),invite_list.pop(2)]
cancel_message=(" sorry as mentioned before, we won't be able to invite you.")
print(cancelled_guests[0] + cancel_message)
print(cancelled_guests[1] + cancel_message)
print(cancelled_guests[2] + cancel_message)
print(cancelled_guests[3] + cancel_message)
confirm_message=(" invitation still valid, see you at 9p.m")
print(invite_list[0] + confirm_message)
print(invite_list[1] + confirm_message)
print(invite_list)
del invite_list[0]
del invite_list[0]
print(invite_list)
