num=int(input("How many number:"))
total_sum=0;
for n in range(num):
    number=float(input("Enter a number:"))
    total_sum+=number;
avg=total_sum/num
print("avg=",avg)