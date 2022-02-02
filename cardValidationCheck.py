
def cardValidCheck(card_number):

    # x="6763605504614728"
    # card_number=list(x.strip())
    # card_number=list(input("CardNumber:").strip())
    card_number=list(str(card_number).strip())

    card_number.reverse()
    card_length=len(card_number)
    card_digit=[]
    if card_length>=13 and card_length<=16:
        sumofeven=0
        sumofodd=0
        for index,digitincard in enumerate(card_number):
            if (index+1)%2==0:
                double_digit=int(digitincard)*2
                if double_digit>9:
                    double_digit-=9
                sumofeven+=double_digit
                card_digit.append(double_digit)
            else:
                sumofodd+=int(digitincard)
                card_digit.append(int(digitincard))
        if (sumofeven+sumofodd)%10==0:
            print("True")
        else:print("false")
        return((sumofeven+sumofodd)%10==0)
    else:
        raise ValueError("Card number is too short")
        return False
