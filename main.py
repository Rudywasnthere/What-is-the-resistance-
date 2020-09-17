
print("Hi I am here to help calculate the resistance for you")
print("First I will need the colors on the resistor:\n either: black, brown, red, orange, yellow, green, blue, violet(purple), gold, silver, or transparent(none)")
## sets color values
first_color= input("first color (number one):\t")
second_color= input("second color (number two):\t")
third_color= input("third color (number three):\t")
fourth_color= input("fourth color (number four):\t")
print(f"\nyour colors are {first_color}, {second_color}, {third_color}, and {fourth_color}\n")
black=0
brown=1
red=2
orange=3
yellow=4
green=5
blue=6
violet=7
purple=7
grey=8
white=9
x= 0
x_2= 0
x_3= 0
x_4= 0
prefix= ""
prefix_1=""
if first_color=='black':
  first_color=black
  x+=1
if first_color=='brown':
  first_color=brown
  x+=1
if first_color=='red':
  first_color=red
  x+=1
if first_color=='orange':
  first_color=orange
  x+=1
if first_color=='yellow':
  first_color=yellow
  x+=1
if first_color=='green':
  first_color=green
  x+=1
if first_color=='blue':
  first_color=blue
  x+=1
if first_color=='purple' or first_color=='violet':
  first_color=purple
  x+=1
if first_color=="grey":
  first_color=grey
  x+=1
if first_color=='white':
  first_color=white
  x+=1
elif x== 'gold'or x=='silver'or x=='transparent'or x=='none':
  print("You have the resistor backwards, list the colors the other way around")
if x==0: 
  print("Error: color 1, insert a color that must be: black, brown, red, orange, yellow, green, blue, violet(purple), grey, or white")

if second_color=='black':
  second_color=black
  x_2+=1
if second_color=='brown':
  second_color=brown
  x_2+=1
if second_color=='red':
  second_color=red
  x_2+=1
if second_color=='orange':
  second_color=orange
  x_2+=1
if second_color=='yellow':
  second_color=yellow
  x_2+=1
if second_color=='green':
  second_color=green
  x_2+=1
if second_color=='blue':
  second_color=blue
  x_2+=1
if second_color=='purple' or second_color=='violet':
  second_color=purple
  x_2+=1
if second_color=="grey":
  second_color=grey
  x_2+=1
if second_color=='white':
  second_color=white
  x_2+=1
elif x_2==0:
  print("Error: color 2, insert a color that must be: black, brown, red, orange, yellow, green, blue, violet(purple), grey, or white")

if third_color=='black':
  third_color=black
  x_3+=1
if third_color=='brown':
  third_color=brown
  x_3+=1
if third_color=='red':
  third_color=red
  x_3+=1
if third_color=='orange':
  third_color=orange
  x_3+=1
if third_color=='yellow':
  third_color=yellow
  x_3+=1
if third_color=='green':
  third_color=green
  x_3+=1
if third_color=='blue':
  third_color=blue
  x_3+=1
if third_color=='purple' or third_color=='violet':
  third_color=purple
  x_3+=1
if third_color=="grey":
  third_color=grey
  x_3+=1
if third_color=='white':
  third_color=white
  x_3+=1
if third_color== 'silver':
  third_color= -2
  x_3+=1
if third_color=='gold':
  third_color=-1
  x_3+=1
elif x_3==0:
  print("Error: color 3, insert a color that must be: black, brown, red, orange, yellow, green, blue, violet(purple), grey, white, gold, silver, or transparent(none)")

if fourth_color=='gold':
  fourth_color= 0.05
  x_4+=1
if fourth_color== 'silver':
  fourth_color= 0.1
  x_4+=1
if fourth_color=='none' or fourth_color=='transparent':
  fourth_color=0.2
  x_4+=1
elif x_4==0:
  print("Error: color 4 , insert a color that is either: gold, silver, or transparent(none)")

##calculation time
if  0<=third_color<3:
  floor= third_color
  modulus= third_color-3
  if third_color==0:
    modulus=0
    prefix= ""
  if third_color ==1:
    modulus=1
    prefix= ""
  if third_color ==2:
    modulus= -1
    prefix= 'K'
    prefix_1= 'K'
  
else:
  floor= (third_color)//3
  if floor==-3:
    prefix= 'n'
    prefix_1='n'
  if floor== -2:
    prefix= 'µ'
    prefix_1= 'µ'
  if floor== -1:
    prefix= 'm'
    prefix_1= 'm'
  if floor==1:
    prefix= 'K'
    prefix_1= 'K'
  if floor==2:
    prefix= 'M'
    prefix_1= 'M'
  if floor==3:
    prefix= 'G'
    prefix_1='G'
  if floor==4:
    prefix= 'T'
    prefix_1='T'
  modulus= ((third_color)%3)

z= int(input("to how many places would you like to round the min and max values?\n"))
value=  ((10*first_color) + second_color) * (10**modulus) 
if value!=1:
  if third_color<0:
    if third_color==-1:
      modulus=-1
      value= value/1000
      prefix=""
      prefix_1=""
    if third_color==-2:
      modulus=2
      prefix="m"
      prefix_1="m"
      value=value
  if fourth_color==0.05:
    min= 0.95*value
    max= 1.05*value
  if fourth_color==0.1:
    min= 0.9*value
    max= 1.1*value
  if fourth_color== 0.2:
    min= 0.8*value
    max= 1.2*value
if value==1:
  if fourth_color==0.05:
    min= 0.95*value *1000
    max= 1.05*value
    if prefix =='n':
      prefix_1= 'p'
    if prefix =='µ':
      prefix_1 ='n'
    if prefix=='m':
      prefix_1='µ'
    if prefix=="":
      prefix_1='m'
    if prefix=='K':
      prefix_1=""
    if prefix=='M':
      prefix_1='K'
    if prefix=='G':
      prefix_1='M'
    if prefix=='T':
      prefix_1='G'

  if fourth_color==0.1:
    min= 0.9*value *1000
    max= 1.1*value
    if prefix =='n':
      prefix_1= 'p'
    if prefix =='µ':
      prefix_1 ='n'
    if prefix=='m':
      prefix_1='µ'
    if prefix=="":
      prefix_1='m'
    if prefix=='K':
      prefix_1=""
    if prefix=='M':
      prefix_1='K'
    if prefix=='G':
      prefix_1='M'
    if prefix=='T':
      prefix_1='G'
  if fourth_color== 0.2:
    min= 0.8*value *1000
    max= 1.2*value
    if prefix =='n':
      prefix_1= 'p'
    if prefix =='µ':
      prefix_1 ='n'
    if prefix=='m':
      prefix_1='µ'
    if prefix=="":
      prefix_1='m'
    if prefix=='K':
      prefix_1=""
    if prefix=='M':
      prefix_1='K'
    if prefix=='G':
      prefix_1='M'
    if prefix=='T':
      prefix_1='G'

round_min= round(min,z)
round_max= round(max,z)
print(f"\nnominal value= {value} {prefix} Ohms\n minimum= {round_min} {prefix_1} Ohms\n maximum= {round_max} {prefix} Ohms")

print("\n\n\nderp ☉ ‿ ⚆")
