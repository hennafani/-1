# *sort order*
# 1.sort sizes of boobs
boobs_lst=[85,85.5,8.05,0.75,8.5,75]
# lst.sort()
# print(boobs_lst)
print(sorted(boobs_lst))
# 2.sort sexy len
hot_lst=['kiss','spank','facesitting','doggy style','sack','licking','69','BDSM','creampie','nipple pulling','orgasm','cumshot','+18']
print(sorted(hot_lst,key=len))

# *management of bitchs*
# 1.creating dictionary
js=[33,100,0,87]
mk=[0,4,10,6]
at=[98,100,16,85]
lm=[100,100,88,92]
bitchName = {'Johnny Sins':js,
               'Mia Khalife':mk,
               'Alexis Texas':at,
               'Logan McCree':lm
               }
print(bitchName)
# 2.avrage score
bitchsName = input('enter your kiri name'+'\n')
if bitchsName=='Johnny':
    print('your RIDEMAN = '+ str(round(sum(js)/len(js),2)))
elif bitchsName== 'Mia':
    print('your RIDEMAN = '+ str(round(sum(mk)/len(mk),2)))
elif bitchsName == 'Alexis':
    print('your RIDEMAN = ' + str(round(sum(at) / len(at), 2)))
elif bitchsName == 'Logan':
    print('your RIDEMAN = ' + str(round(sum(lm) / len(lm), 2)))
else:
    print('you are a motherfucker')
# 3. statuses

bitchsName = input('enter your kiri name'+'\n')
if bitchsName =='Johnny':
    J =(round(sum(js)/len(js),2))
    if J > 60:
        print('BILAKH')
    else:
        print('RIDI')
elif bitchsName=='Mia':
    M =(round(sum(mk)/len(mk),2))
    if M > 60:
        print('BILAKH')
    else:
        print('RIDI')
elif bitchsName=='Alexis':
    A =(round(sum(at)/len(at),2))
    if A > 60:
        print('BILAKH')
    else:
        print('RIDI')
elif bitchsName=='Logan':
    L =(round(sum(lm)/len(lm),2))
    if L > 60:
        print('BILAKH')
    else:
      print('RIDI')
else:
    print(':/')

















