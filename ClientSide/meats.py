import os

#mince
fivehundredgrambeef = 'ITEM ID: 1: 500g BEEF MINCE ' 'PRICE: $6.50'
fivehundredgrampork = 'ITEM ID: 2: 500g PORK MINCE ' 'PRICE: $6.50'
fivehundredgramhalfporkhalfbeef = 'ITEM ID: 3 ITEM: 500g 1/2 PORK 1/2 BEEF MINCE ' 'PRICE: $7'
onekgpork = 'ITEM ID: 4 ITEM: 1KG PORK MINCE ' 'PRICE: $13'
onekgbeef = 'ITEM ID: 5 ITEM: 1KG BEEF MINCE ' 'PRICE: $13'

#steaks
fivehundredsteak = 'ITEM ID: 6 ITEM: 500g STEAK ' 'PRICE: $15'
onekgsteak = 'ITEM ID: 7 ITEM: 1KG STEAK ' 'PRICE: $20'
porksteak = 'ITEM ID: 8 ITEM: 4 PORK STEAK ' 'PRICE: $20'
onekgporksteak = 'ITEM ID: 9 ITEM: 12 PORK STEAK ' 'PRICE: $27.50'

#SAUSSAGES/PATTIES
twelvebeefsaussage = 'ITEM ID: 10 ITEM: 12 BEEF SAUSSAGES ' 'PRICE: $10'
twentyfourbeefsaussage = 'ITEM ID: 11 ITEM: 24 BEEF SAUSSAGES ' 'PRICE: $17.50'
sixbeefhamburgerpatties = 'ITEM ID: 12 ITEM: 6 BEEF HAMBURGER PATTIES ' 'PRICE: $7.60'
twelvebeefhamburgerpatties = 'ITEM ID: 13 ITEM: 12 BEEF HAMBURGER PATTIES ' 'PRICE: $13'
twentyfourbeefhamburgerpatties = 'ITEM ID: 14 ITEM: 24 BEEF HAMBURGER PATTIES ' 'PRICE: $24'
sixchickenhamburgerpatties = 'ITEM ID: 15 ITEM: 6 CHICKEN HAMBURGER PATTIES ' 'PRICE: $8.60'
twelvehchickenhamburgerpatties = 'ITEM ID: 16 ITEM: 12 CHICKEN HAMBURGER PATTIES ' 'PRICE: $15'
twentyfourchickenhamburgerpatties = 'ITEM ID: 17 ITEM: 24 CHICKEN HAMBURGER PATTIES ' 'PRICE: $26'
twelvechickensaussage = 'ITEM ID: 18 ITEM: 12 CHICKEN SAUSSAGES ' 'PRICE: $12'
twentyfourchickensaussage = 'ITEM ID: 19 ITEM: 24 CHICKEN SAUSSAGES ' 'PRICE: $19.50'

#SEAFOOD
fivehundredgramprawns = 'ITEM ID: 20 ITEM: 500g PRAWNS ' 'PRICE: $20'
onekgprawns = 'ITEM ID: 21 ITEM: 1kg prawns ' 'PRICE: $28.75'

#OTHERMEATS
fivehundredchickenbreasts = 'ITEM ID: 22 ITEM: 500g CHICKEN BREASTS ' 'PRICE: $19.50'
onekgchickenbreast = 'ITEM ID: 23 ITEM: 1kg CHICKEN BREASTS ' 'PRICE: $24.50'


#MINCE
minces = fivehundredgrambeef + ' \n' + fivehundredgrampork + '\n' + fivehundredgramhalfporkhalfbeef + '\n' + onekgpork + '\n' + onekgbeef

#STEAKS
steaks = fivehundredsteak + '\n' + onekgsteak

#SAUSSAGES/PATTIES
sadnp = twelvebeefsaussage + '\n' + twentyfourbeefsaussage + '\n' + sixbeefhamburgerpatties + '\n' + twelvebeefhamburgerpatties + '\n' + sixchickenhamburgerpatties + '\n' + twelvehchickenhamburgerpatties + '\n' + twentyfourchickenhamburgerpatties + '\n' + twelvechickensaussage + '\n' + twentyfourchickensaussage

#SEAFOODS
seafoods = fivehundredgramprawns + '\n' + onekgprawns

#OTHER MEATS
othermeats = fivehundredchickenbreasts + '\n' + onekgchickenbreast


meatitems =  minces+ '\n' + steaks + '\n' + sadnp + '\n' + seafoods + '\n' + othermeats