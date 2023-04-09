ff = "ყველაზე დიდი გვერდი. კი ან არა:"
a = "კი"
b = "არა"
c = "შეიტანეთ პირველი გვერდი:"
d = "შეიტანეთ მეორე გვერდი:"
e = input(ff)
if e==a:
	g1 = float(input(c))
	g2 = float(input(d))
	g13 = g1 ** 2
	g23 = g2 ** 2
	g3 = g13 + g23
	n = g3**0.5
	n1 = "მესამე გვერდის სიგრძე არის"
	print(n1, n)
if e==b:
	a = "შეიტანეთ დიდი გვერდის სიგრძე:"
	b = "შეიტანეთ მეორე გვერდის სიგრძე:"
	c = float(input(a))
	ac = float(input(b))
	cd = c ** 2
	acc = ac ** 2
	acd = cd - acc
	acb = acd**0.5
	print(acb)
else:
	print("თქვენ უნდა შეიყვანოთ კი ან არა")