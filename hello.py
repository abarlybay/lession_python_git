#print("Helloworld!")

#print(2+2)

#a = 2
#print(a + 3)

#b = 6
#a = b
#print(a)

#a = 2
#a = a + 1
#print(a)

# Function VAT
def get_vat(payment):
	try:
		payment = float(payment)
		vat = payment / 100 * 20
		vat = round(vat, 2)
		return "Sum VAT: {}".format(vat)
	except TypeError:
		return "Can't count. Check data format!"

result = get_vat(4.1563)
print(result)