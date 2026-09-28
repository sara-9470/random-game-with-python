import random
Pin_code=random.randint(1000,9999)
user_input=int(input('enter 4 dighits to pin code'))
if len(str(user_input))!=4:
 print("please enter 4 dighits")
elif Pin_code==user_input :
 print("success!pin code matched")
else:
print("falier! Pin code did not match")
print(f"computer generated this PIN:{Pin_code}")

