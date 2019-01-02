def cel_to_kel(cel):
    return cel + 273

def kel_to_cel(kel):
    return kel - 273

if __name__ == '__main__':
    hist = []
    
    while True:
        ch = int(input("Enter a choice \n1: Celsius to Kelvin \n2:Kelvin to Celsius"))
        if ch == 1:
            cel = int (input("Enter temperature in celsius \n"))
            temp = cel_to_kel(cel)
            temp_tup = (cel, temp)
            hist.append(temp_tup)
            print (temp)
        elif ch == 2:
            kel = int (input("Enter temperature in kelvin\n"))
            temp = kel_to_cel(kel)
            temp_tup = (kel, temp)
            hist.append(temp_tup)
            temp = kel_to_cel(kel)
        else:
            exit(0)

