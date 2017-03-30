person = input('Enter your name: ')
print('Hello', person,'\n')
print("choose any 1 model among the following")
print("----------------------------------------------------------------")
print("Economical order quantity(EOQ) :1\n")
print("phase model with shortage :2\n")
print("manufacturing model without shortage :3\n")
print("manufacturing model with shortage :4\n")
print("type 1,2,3 or 4 for the following models:\n")
print("----------------------------------------------------------------")
model=input('your answer is :')
if model is "1":
    print("----------------------------------------------------------")
    print ("you have choosen economical order quantity problem\n")
    print("enter the values of following:\n")
    D  = float(input('Annual Demand D<unit/year>:'))
    Co = float(input('ordering cost Co<rupees/order> :'))
    print("is your carrying cost is in % if yes press Y")
    ans =str(input("answer is:"))
    if ans is "Y":
       chi=float(input("percentage in term of item cost:"))
       Ci=float(input("item cost:"))
       Ch=(chi*Ci)/100
    else:
       Ch = float(input('carrying cost Ch<rupees/unit/year>:'))

    Q1=(2*D*Co)/Ch
    Q=Q1**(.5)
    TC = ((D / Q) * Co) + ((Q / 2) * Ch)
    N=D/Q
    T = Q / D
    print("----------------------------------------------------------")
    print('the required value of optimal order quantity is:',Q,'order/year')
    print('the required number of order is:                ',N,'orders')
    print('the required time of order  is:                 ',T,'years')
    print('the required value of total cost :              ',TC,'rupees')
    print("----------------------------------------------------------")
elif model is "2":
    print("----------------------------------------------------------")
    print("you have choosen phase model with shortage problem\n")
    print("enter the values of following:\n")
    D = float(input('Annual Demand D<unit/year>:'))
    Co = float(input('ordering cost Co<rupees/order> :'))
    print("is your carrying cost is in % if yes press Y")
    ans = str(input("answer is:"))
    if ans is "Y":
        chi = float(input("percentage in term of item cost:"))
        Ci = float(input("item cost:"))
        Ch = (chi * Ci) / 100
    else:
        Ch = float(input('carrying cost Ch<rupees/unit/year>:'))
    Cs = float(input('shortage cost Cs<rupees/unit/year>:'))
    Q1 = ((2*D*Co)/Ch)*((Cs + Ch)/Cs)
    Q  = (Q1**0.5)
    S=(Q*(Ch/(Ch+Cs)))
    Imax=Q-S
    N=D/Q
    T=Q/D
    t1=(Imax*T)
    t2=((S*T)/D)
    Th=Imax/(t1+t2)
    OC=((D/Q)*Co)
    HC=(((Q-S)**2)*Ch)/(2*Q)
    SC=(((S**2)*Cs)/(2*Q))
    TC=OC+HC+SC
    print("----------------------------------------------------------")
    print('the required value of optimal order quantity is   ', Q, 'order/year')
    print('the required maximum inventory is:                ',Imax,'rupees')
    print('the required optimal shortage:                    ',S,'rupees')
    print('the required time of being held is:               ',Th,'years')
    print('the required number of order is:                  ',N,'orders')
    print('the required time of order  is:                   ',T,'years')
    print('the required value of total cost:                 ',TC,'rupees')
    print("----------------------------------------------------------")
elif model is "3":
    print("----------------------------------------------------------")
    print("you have choosen manufacturing model without shortage problem\n")
    print("enter the values of following:\n")
    D = float(input('Annual Demand D<unit/year>:'))
    Co = float(input('ordering cost Co<rupees/order> :'))
    print("is your carrying cost is in % if yes press Y")
    ans = str(input("answer is:"))
    if ans is "Y":
        chi = float(input("percentage in term of item cost:"))
        Ci = float(input("item cost:"))
        Ch = (chi * Ci) / 100
    else:
        Ch = float(input('carrying cost Ch<rupees/unit/year>:'))
    P = float(input('production rate  P<unit/month>:'))
    w= int(input('working days  w<days>:'))
    Ci = float(input('item cost Ci<rupees/unit>:'))
    X=(D/w)
    Q1 = ((2 * D * Co) / Ch) * (P/(P-X))
    Q = (Q1 ** 0.5)
    Imax =((Q*(P-X))/P)
    N = D / Q
    T = Q / D
    t1=Q/P
    OC = ((D / Q) * Co)
    HC = (((P-X) * Ch)*Q) / (2 *P )
    PC = (Ci*X)
    TC = OC + HC + PC
    print("----------------------------------------------------------")
    print('the required value of optimal order quantity is: ', Q, 'order/year')
    print('the required maximum inventory is:               ',Imax,'rupees')
    print('the required time of manufacturing is:           ',t1,'years')
    print('the required number of order is:                 ',N,'orders')
    print('the required time of order  is:                  ',T,'years')
    print('the required value of total cost:                ',TC,'rupees')
    print("----------------------------------------------------------")
elif model is "4":
    print("----------------------------------------------------------")
    print("you have choosen manufacturing model with shortage problem\n")
    print("enter the values of following:\n")
    D = float(input('Annual Demand D<unit/year>:'))
    Co = float(input('ordering cost Co<rupees/order> :'))
    print("is your carrying cost is in % if yes press Y")
    ans = str(input("answer is:"))
    if ans is "Y":
        chi = float(input("percentage in term of item cost:"))
        Ci = float(input("item cost:"))
        Ch = (chi * Ci) / 100
    else:
        Ch = float(input('carrying cost Ch<rupees/unit/year>:'))
    P = float(input('production rate  P<unit/month>:'))
    w = int(input('working days  w<days>:'))
    Ci = float(input('item cost Ci<rupees/unit>:'))
    Cs = float(input('shortage cost Cs<rupees/unit/year>:'))
    Q1 = ((2 * D * Co) / Ch) * (P / (P - D))*((Ch+Cs)/Cs)
    Q = (Q1 ** 0.5)
    S=(Q*(Ch/(Ch+Cs)))*((P-D)/P)
    Imax = ((((P - D) / P)*Q)-S)
    N = D / Q
    T = Q / D
    t1 = (S/(P-D))
    t2=Imax/(P-D)
    t3=((P*Imax*T)/(Q*(P-D)))-t2
    t4=((P*S*T)/(Q*(P-D)))-t1
    a=t2+t3
    b=t1+t2
    c=t1+t4
    OC = ((D / Q) * Co)
    HC = ((((Q*(P-D))/P)-S)**2)*((P*Ch)/(2*Q*(P-D)))
    SC=(S/Q)*((t1+t4)/T)*Cs
    TC = OC + HC + SC
    print("----------------------------------------------------------")
    print('the required value of optimal order quantity is:', Q, 'order/year')
    print('the required maximum inventory is:                 ',Imax,'rupees')
    print('the required optimal shortage:                     ',S,'rupees')
    print('the required time of manufacturing is :            ',b,'years')
    print('the required depletion time is:                    ',t3,'years')
    print('the required shortage time is :                    ',c,'years')
    print('the required inventory time is :                   ',a,'years')
    print('the required number of order is:                   ',N,'orders')
    print('the required time of order  is:                    ',T,'years')
    print('the required value of total cost:                  ',TC,'rupees')
    print("----------------------------------------------------------")
else:
    print("......you have entered a wrong option.please try again..............")
print ("thank you")
print ("                                    AMIT KUMAR DAS(2014108002)")