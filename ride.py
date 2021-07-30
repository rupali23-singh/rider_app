
                        
name=input("Enter the name:")
print("Welcome to the spectacular ride:")
print("Have a great day")
print("Spectacular Ride Have Saftey Insurance For You")
import random
def book_my_ride():
    your_destination=["Ashok nagar","Dehli","Phase3","Laxmi Nagar","Sarjapur"]
    ride_drivers=[["Monu","Sonu"],["Raju","Rahul"],["Vicky","Nitin"]]
    for i in your_destination:
        print(i)
    print()
    ride_limits=input("How many rides you  want?")
    index=1
    d={}
    total=0
    your_transport=["Cab","Ola","Uber","Auto"]
    for i in your_transport:
        print(i)
    select_your_ride=input("Selecte_categorys:")
    print()
    your_booking=int(input("For booking click :1 and for cancleing option :2"))
    print()
    print("Thanku For Booking Or Cancelation___Happy Joureny")
    while index<=len(ride_limits):
        select_your_ride=input("Enter Your Destination:")
        print()
        i=0
        while i<len(your_destination):
            if select_your_ride == your_destination[i]:
                j=0
                while j<len(ride_drivers[i]):
                    a=random.choice(ride_drivers[j])
                    print("Avilable drivers are:",a)
                    j=j+1
                choose_your_ride=input("Enter your ride?:")
                print()
        
                if your_booking==1:
                    print("Thanku for confirming")
                    kilomeeter=int(input("Enter The Distence:"))
                    a=kilomeeter*5
                    d[choose_your_ride]=a
                    print(d)
                else:
                    print("Cancelation ")
                    break
                print("Again Book Your Cab Without Stress \n1.yes\n2.Quit")
                book_your_cab_again=input(" Yes or No:")
                print("Thank You For Response")
                
            i=i+1      
        index=index+1
book_my_ride()
                


