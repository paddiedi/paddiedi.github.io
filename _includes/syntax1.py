# Nimetään muuttuja
totuus = True
if totuus:
    print("Se on tosi!")

else:
    print("Se on epätosi!")
# Tuloste: Se on tosi!

# If-lauseita voidaan pistää sisäkkäin:
a = True
b = True

if a:
    if b:
        print("a ja b tosia!")
# Voidaan ilmaista toisinkin:
if a and b:
    print("a ja b!")
