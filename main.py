##Rudy Garcia

import math, sys
import random, sys
import time, sys

non_prefixed_number= 0
##introdcution
print("Hi I am here to help calculate the resistance for you")
print("First I will need the colors on the resistor:\n either: black, brown, red, orange, yellow, green, blue, violet(purple), gold, silver, or transparent(none)")
## dictionaries for reference in my functions
possible_first_colors = ["black","brown","red","orange","yellow","green","blue","violet","purple",""]
possible_fourth_colors = ["gold","silver","transparent","none"]
restart= ""
color_values= {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'purple':7,'violet':7,'gold':-1,'silver':-2}
tolerance_values= {'gold':0.05,'silver':0.1,'transparent':0.2,'none':0.2}
tolerance_percents = {'gold':5, 'silver':10, 'transparent':20, 'none':20}
count_prefixes= {'0':"", '1':'K','2':'M','3':'G','4':'T','5':'P','6':'E'}
##funcitons that sorts inputs, and calculate based on them
## calculates upper and lower tolerance values based on fourth color band, and the nominal value
def correct_input(name_check):
  position = name_check.split("_")
  true_position = position.pop(0)
  name= input(f"{true_position} color:\t")
  name= name.lower()
  if name_check != "fourth_color":
    while name not in possible_first_colors:
      name = str(input(f"Please input a correct {true_position} color: "))
  if name_check == "fourth_color":
    while name not in possible_fourth_colors:
      name = str(input("Please input a correct fourth color: "))
  return name

def calculations(first_color, second_color, third_color): 
  first_digit= int(color_values[f'{first_color}'])*10 + int(color_values[f'{second_color}'])
  non_Prefixed_number= int(first_digit)*(10**int(color_values[f'{third_color}']))
  return non_Prefixed_number

def prefix_calculator(non_prefixed_number):
  count= 0 
  while non_prefixed_number>=1000:
      non_prefixed_number= non_prefixed_number/1000
      count +=1
  simplified_number= float(non_prefixed_number)
  count= str(count)
  prefix= count_prefixes[f'{count}']
  prefixed_number = f"{non_prefixed_number} {prefix}"
  return prefixed_number, count, prefix, simplified_number

def tolerance(fourth_color, count, nominal_value):
  variance = tolerance_values[f'{fourth_color}']
  variance_percent = variance*100
  number_variance= float(variance*nominal_value)
  lower_nominal = float(nominal_value - number_variance)
  if lower_nominal <1:
    lower_nominal = 1000*lower_nominal
    count = int(count) - 1
    count= str(count)
    lower_prefix= count_prefixes[f'{count}']
  else:
    lower_prefix = ""
  upper_nominal= float(nominal_value + number_variance)
  return lower_prefix, lower_nominal, upper_nominal, variance_percent

def round_outputs(upper, lower, non_prefixed_number):
  length_lower = len(str(non_prefixed_number))
  f= False
  round_places= input("how many places would you like to round to? \n(hit enter for no rounding):\t ")
  if round_places=="":
    final_number= non_prefixed_number
    final_lower= round(lower,5)
    final_upper= upper
    round_places= "no"
  else: 
    while f == False:
      try: 
        int(round_places)
        round_places= int(round_places)
        f= True
      except ValueError:
        print('Value Error')
        round_places= input("Please input an integer: ")
        f= False
    if round_places >0 :
      round_places= int(round_places)
      round_place= int(round_places + length_lower)
      final_number= round(non_prefixed_number,round_place)
      final_lower= round(lower,round_place)
      final_upper= round(upper,round_place)
  return final_number, final_lower, final_upper, round_places
## gets the final outputs to give to the user

def final_output(prefixed_number, non_prefixed_number, final_lower, final_upper, low_prefix, prefix):   
  if low_prefix =="":
   return f"\nnominal value= {prefixed_number} Ohms\n minimum= {final_lower} {prefix} Ohms\n maximum=  {final_upper} {prefix} Ohms"
  if low_prefix !="":
    return f"\nnominal value= {prefixed_number} Ohms\n minimum= {final_lower} {low_prefix} Ohms\n maximum=  {final_upper} {prefix} Ohms"

def main():
  first_color = correct_input("first_color")
  second_color = correct_input("second_color")
  third_color = correct_input("third_color")
  fourth_color = correct_input("fourth_color")

  non_prefixed_number = calculations(first_color, second_color, third_color)

  prefixed_number, count, prefix, simplified_number = prefix_calculator(non_prefixed_number)

  low_prefix, lower, upper, variance_percent = tolerance(fourth_color, count, simplified_number)

  final_number, final_lower, final_upper, round_places = round_outputs(upper, lower, non_prefixed_number)
  print(F"Your color inputs are {first_color}, {second_color}, {third_color} ({non_prefixed_number}) and your tolerance is ±{variance_percent}% and you rounded to {round_places} places ")
  print(final_output(prefixed_number, non_prefixed_number, final_lower, final_upper, low_prefix, prefix))

restart= ""
while restart!="done":
  main()
  restart = input("\nderp ☉ ‿ ⚆\n\n press any button to continue, enter \"done\" when your finished to close the file.\n")