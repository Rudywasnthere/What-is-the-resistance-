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
tolerance_values= {'gold':0.95,'silver':0.9,'transparent':0.8,'none':0.8}
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
  count= str(count)
  prefix= count_prefixes[f'{count}']
  prefixed_number = f"{non_prefixed_number} {prefix}"
  return prefixed_number, count, prefix, non_prefixed_number

def tolerance(fourth_color, count, nominal_value):
  variance = int(tolerance_values[f'{fourth_color}'])
  lower_nominal = variance*int(nominal_value)
  if lower_nominal <1:
    lower_nominal = 1000*lower_nominal
    count = int(count) - 1
    count= str(count)
    lower_prefix= count_prefixes[f'{count}']
  else:
    lower_prefix = ""
  upper_nominal= (1 + variance)*nominal_value
  return lower_prefix, lower_nominal, upper_nominal

def round_outputs(upper, lower, non_prefixed_number):
  round_places= input("to how many places would you like to round the min and max values? (hit enter for no rounding)\n")
  length_lower = len(str(non_prefixed_number))
  if round_places != "":
    round_places= int(round_places)
    round_place= int(round_places + length_lower)
    final_number= round(non_prefixed_number,round_place)
    final_lower= round(lower,round_place)
    final_upper= round(upper,round_place)
  else:
    final_number= non_prefixed_number
    final_lower= lower
    final_upper= upper
  return final_number, final_lower, final_upper
## gets the final outputs to give to the user

def final_output(prefixed_number, non_prefixed_number, final_lower, final_upper, low_prefix):    print(f"\nnominal value= {prefixed_number} Ohms\n minimum= {final_lower} {low_prefix} Ohms\n maximum=  {final_upper} {prefix} Ohms")


while restart!="done":
  first_color = correct_input("first_color")
  second_color = correct_input("second_color")
  third_color = correct_input("third_color")
  fourth_color = correct_input("fourth_color")
  non_prefixed_number = calculations(first_color, second_color, third_color)
  prefixed_number, count, prefix, simplified_number = prefix_calculator(non_prefixed_number)
  low_prefix, lower, upper = tolerance(fourth_color, count, simplified_number)
  final_number, final_lower, final_upper = round_outputs(upper, lower, non_prefixed_number)
  print(f"\nnominal value= {prefixed_number} Ohms\n minimum= {final_lower} {low_prefix} Ohms\n maximum=  {final_upper} {prefix} Ohms")

  restart= input("\n\n\nderp ☉ ‿ ⚆\n\n press any button to continue, enter \"done\" when your finished to close the file.\n")