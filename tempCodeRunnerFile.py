
seats=350
total_bookings=0
rejections=0
total_tickets_sold=0
remaining=350

while  remaining>0 :
    tickets=int(input("enter number of tickets"))
    if tickets==0 :
        break
    elif tickets >= 1 and  tickets<=15 :
        print("valid booking")
    else:
        print("invalid booking")
        rejections+=1
        continue
    if tickets > remaining :
        print("housefull")
        rejections+=1
        continue
    verfication = True
    for i in range(tickets):
        age = int(input("enter age :"))
        if age<12 :
            verfication =False
            print("age restriction")
            rejections+=1
            break
    if verfication==True:
        print("booking comfirned")
        total_bookings+=1
        total_tickets_sold+=tickets
        remaining-= tickets
print(f"Final Report : total bookings: {total_bookings},"
      f"Total tickets sold :{total_tickets_sold},"
      f"Rejected bookings: {rejections},"
      f"Remaining seats :{remaining}")