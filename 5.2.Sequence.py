# Með því að slá inn töluna n á niðurstaðan að vera röð af n tölum sem uppfylla það
# að hver tala er summan af síðustu þremur tölum á undan, þ.e. fyrstu þrjár tölurnar eru
# 1, 2, 3. Næsta talan á eftir þessum er summan af næstu þremur tölunum á undan þessum.
# Þar sem vitað er að fyrstu þrjár tölur er 1, 2 og 3 þá bý ég til þrjár breytur:
# a = 1
# b = 2
# c = 3
# Í byrjun prenta ég gefnu tölurnar, þ.e. 1, 2 og 3, t.d. þegar n = 1 þá prentar út 1
# þegar n = 2 þá prentast út 2.
# Þegar n er stærra en 3 þá kemur inn formúlan þar sem næstu 3 tölur á undan eru lagðar saman
# og búa til nýja tölu, d. Þegar það er komið þá verður að breyta a í b, b í c og c í d og svo 
# koll af kolli þar til n er náð.


n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 1
b = 2
c = 3

d = 0

if n >= 1:
    print(a)

if n >= 2:
    print(b)

if n >= 3:
    print(c)

if n > 3:
    for seq in range(n-3):  # we have already used the first thre numbers and therefore we use n - 3 here

        d = a + b + c
        a = b
        b = c
        c = d

        print(d)