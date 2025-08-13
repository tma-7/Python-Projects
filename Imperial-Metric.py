#Imperial-Metric Convertor
#Goal: Convert any imperial measurements (lbs, ft, in, miles, farenheit, etc.) into metric units and vice versa
# 8/12/2025 | 9:46 PM EST

ask_question = input("What unit are you giving me? | 'I' for Imperial | 'M' for  Metric': ")
#--------------------------------------------------------------------------------------------------------------------------------------
#COVERTING METRIC TO IMPERIAL
if ask_question == "M":
    get_metric = input("What are you converting? A = kg to lbs | B = m to ft | C = cm to in | D = km to mi | E = C to F: ")
    
    if get_metric == "A":
        kg = float(input("What is the weight?"))
        pound = kg * 2.20462
        print(f"The weight in pounds is {round(pound, 1)} lbs.")
    
    elif get_metric == "B":
        meter = float(input("What is the distance?: "))
        feet =  meter * 3.281
        print(f"The distance in feet is {round(feet, 1)} ft.")
    
    elif get_metric == "C":
        cm = float(input("What is the distance?: "))
        inches =  cm / 2.54
        print(f"The distance in inches is {round(inches, 1)} in.")
    
    elif get_metric == "D":
        km = float(input("What is the distance?: "))
        mile =  km / 1.609
        print(f"The distance in inches is {round(mile, 1)} mi.")
    
    elif get_metric == 'E':
        celcius = float(input("What is the temperature?: "))
        farenheit = (celcius * (9/5) + 32)
        print(f"The temperature in farenheit is {round(farenheit, 1)} F.")
    
    else:
        print(f"{get_metric} is Invalid.")

#--------------------------------------------------------------------------------------------------------------------------------------
#CONVERTING IMPERIAL TO METRIC
if ask_question == "I":
    get_imperial = input("What are you converting? A = lbs to kg | B = ft to m | C = in to cm | D = mi to km | E = F to C: ")
    
    if get_imperial == "A":
        pound_1 = float(input("What is the weight?"))
        kg_1 = pound_1 / 2.20462
        print(f"The weight in kilograms is {round(kg_1, 1)} kg.")
    
    elif get_imperial == "B":
        feet_1 = float(input("What is the distance?: "))
        meter_1 =  feet_1 / 3.281
        print(f"The distance in meters is {round(meter_1, 1)} m.")
        
    elif get_imperial == "C":
        in_1 = float(input("What is the distance?: "))
        cm_1 =  in_1 * 2.54
        print(f"The distance in centimeters is {round(cm_1, 1)} cm.")
        
    elif get_imperial == "D":
        mile_1 = float(input("What is the distance?: "))
        km_1 =  mile_1 * 1.609
        print(f"The distance in kilometers is {round(km_1, 1)} km.")

    elif get_imperial == 'E':
        farenheit_1 = float(input("What is the temperature?: "))
        celcius_1 = (farenheit_1 - 32) * (5/9)
        print(f"The temperature in celcius is {round(celcius_1, 1)} C.")

    else:
        print(f"{get_imperial} is Invalid.")

else:
    print("Invalid Option")
    
