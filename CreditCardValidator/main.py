card_no = "5610591081018250"
odd_sum = 0
double_sum = 0
number = list(card_no)
for (idx,val) in enumerate(number):
    if idx%2==1:
        odd_sum += int(val)
    elif idx%2==0:
        val = int(val)
        val = val*2
        val = str(val)
        if len(val)>1:
            val = int(val)
            val = val%10 + int(val/10)
            double_sum += val
        else:
            double_sum += int(val)


net_sum = odd_sum + double_sum
if net_sum % 10 ==0:
    print("Valid card!")
else:
    print("Invalid card!")


