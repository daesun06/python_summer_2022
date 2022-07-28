rainy = input("How's the weather? Is it raining? (yes/no)").lower()
cold = input("Is it cold outside? (yes/no)").lower()
if (rainy == 'yes' and cold == 'yes'):
    print("You'd better wear a raincoat.")
elif (rainy == 'yes' and cold == 'no'):
    print("Carry an umbrella with you.")
elif (rainy == 'no' and cold == 'yes'):
    print("Put on a jacket.")
elif (rainy == 'no' and cold == 'no'):
    print("Wear whatever you want, it's dry and warm outside.")