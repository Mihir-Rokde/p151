from tkinter import*
root=Tk()
root.title("Sales application")
root.configure(background="yellow")
root.geometry("500x500")

lm=Label(root)
lp=Label(root)
maxp=Label(root)
minp=Label(root)

month=("jan" ,"feb","march","april","may","june","july","aug","sep","oct","nov","dec")
profit=(20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)
lm["text"]="Months : "+str(month)
lp["text"]="profit : "+str(profit)
def maxprofit():
    max_profit=max(profit)
    max_profit_index=profit.index(max_profit)
    print(max_profit_index)
    max_profit_month = month[max_profit_index]
    print("The maximum profit of " + str(max_profit)+ " was recorded in the month of " + str(max_profit_month))
    maxp["text"]="maximum profit of : "+str(max_profit)+"was given in the month of "+str(max_profit_month)
def minprofit():
    min_profit = min(profit)
    min_profit_index = profit.index(min_profit)
    print(min_profit_index) 
    min_profit_month = month[min_profit_index]
    print( "The minimum profit of "+str(min_profit)+" was recorded in the month of " +str(min_profit_month))
    minp["text"]="The minimum profit of "+str(min_profit)+" was recorded in the month of " +str(min_profit_month)

lm.place(relx=0.5,rely=0.2,anchor=CENTER)
lp.place(relx=0.5,rely=0.3,anchor=CENTER)
btn_max=Button(root,text="show max profitable month",command=maxprofit,bg="red",fg="white")
btn_min=Button(root,text="show min profitable month",command=minprofit,bg="red",fg="white")
btn_max.place(relx=0.5,rely=0.4,anchor=CENTER)
btn_min.place(relx=0.5,rely=0.6,anchor=CENTER)
maxp.place(relx=0.5,rely=0.5,anchor=CENTER)
minp.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()