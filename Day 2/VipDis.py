amount = float(input("Enter shopping amount: "))
vip = input("Are you a VIP customer? (Yes/No): ")

discount = 0

if amount > 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10

# Extra VIP Discount
if vip.lower() == "yes":
    discount += amount * 0.05

amount_after_discount = amount - discount

gst = amount_after_discount * 0.18

final_bill = amount_after_discount + gst

print("Original Amount =", amount)
print("Discount =", discount)
print("Amount After Discount =", amount_after_discount)
print("GST (18%) =", gst)
print("Final Bill =", final_bill)
