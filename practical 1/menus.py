# Menus

name = input("Enter Name:")
choice = ''
while choice != "Q":
   print("(H)ello")
   print("(G)oodbye")
   print("(Q)uit")
   choice = input(">>>") .upper()
   if choice == "H":
       print("Hello", name)
   elif choice == "G":
       print("Goodbye", name)
   elif choice != "Q":
       print("Invalid message")
print("Finished.")

