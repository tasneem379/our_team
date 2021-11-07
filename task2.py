print("=" *80)
fnum =int(input("Enter your first number:"))
snum =int(input("Enter your second number:"))
operator=input("operation:")
if operator =="+":
   The_result =fnum+snum
   print(The_result)
elif operator =="-":
    The_result =fnum-snum
    print(The_result)
elif operator =="*":
   The_result =fnum*snum
   print(The_result)
elif operator =="%":
    The_result =fnum%snum
    print(The_result)
elif operator =="/":
    The_result=fnum/snum
    if  The_result==ZeroDivisionError():

                    # continue
    # print(str(The_result))
    # while The_result =fnum/snum:
     while The_result==ZeroDivisionError():
    #   The_result =fnum/snum
      print("TRY AGAIN")
      fnum =input("Enter your first number:")
      snam =input("Enter your second number:")
      operator=input("operation")
      The_result =fnum/snum 
      print(The_result)  
    else:
    #   The_result =fnum/snum
      print(The_result)
elif operator =="**":
   The_result =fnum**snum
   print(The_result)
else:
    fnum =input("Enter your first number:")
    snam =input("Enter your second number:")
    operator=input("operation")

























