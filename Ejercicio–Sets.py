numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
letters = ['A', 'B', 'C','D'] 
unique_combinations = set() 
for number in numbers:    
    for letter in letters:        
        unique_combinations.add("{}{}{}".format(number,number,number,number))
        unique_combinations.add("{}{}{}".format(number,number,number,letter))
        unique_combinations.add("{}{}{}".format(number,number,letter,number))
        unique_combinations.add("{}{}{}".format(number,number,letter,letter))
        unique_combinations.add("{}{}{}".format(number,letter,number,number))
        unique_combinations.add("{}{}{}".format(number,letter,number,letter))
        unique_combinations.add("{}{}{}".format(number,letter,letter,number))
        unique_combinations.add("{}{}{}".format(number,letter,letter,letter))
        unique_combinations.add("{}{}{}".format(letter,number,number,number))
        unique_combinations.add("{}{}{}".format(letter,number,number,letter))
        unique_combinations.add("{}{}{}".format(letter,number,letter,number))
        unique_combinations.add("{}{}{}".format(letter,number,letter,letter))
        unique_combinations.add("{}{}{}".format(letter,letter,number,number))
        unique_combinations.add("{}{}{}".format(letter,letter,number,letter))
        unique_combinations.add("{}{}{}".format(letter,letter,letter,number))
        unique_combinations.add("{}{}{}".format(letter,letter,letter,letter))
print(unique_combinations)