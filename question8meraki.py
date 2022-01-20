name=int(input('enter number:'))
i=1
l={}
for i in range (name):
    #while i<=name:
    k=(input('enter name:'))
    v=input('enter number:')
    l.update({k:v})
    #i=i+1
print(l)
# output
#{
#'sonu':85,
# 'Kartik':90,
#'Deepak':96,
#'Aman':76,
#'Somesh':60,
#'Umesh':85,
#'Amarpal':70,
#'Roshan':57,
#'Riyaz':98,
#'Shabid':56
#}
