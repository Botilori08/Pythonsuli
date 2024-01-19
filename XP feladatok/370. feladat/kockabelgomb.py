print("Ez a program kiszámolja a kocka oldalhosszából a kockába írható gömb sugarát.")
a = int(input("Mennyi legyen az első kocka oldala? "))

R= a/2
text = "Az első kockába beírható kör sugara: {R}"

print(text.format(R= a/2))

a = int(input("Mennyi legyen a második kocka oldala? "))

R= a/2
text = "A második kocklába beírható kör sugara: {R}"

print(text.format(R= a/2))