# for each line of the input file, find the first digit and the last digit and add them to form two digits
# transform the digits into an int
# add to a sum

def calibration_document(input_filename):

    #start the calculation of the calibration values
    calibration_values_sum = 0

    try:
        #open the file
        with open(input_filename, 'r') as file:
            #read each line as a string
            for line in file: 
                #initiate digit values
                first_digit = second_digit = None
                #enumerate through the characters in a line until finding the first digit, start form the beginning of the string
                for character in line:
                    if character.isdigit(): 
                        first_digit = character
                        break
                #find the last digit by enumerating starting from the end of the string
                for character in line[ : :-1]:
                    if character.isdigit():
                        second_digit = character
                        break
                    
                #add the digit to the sum
                calibration_values_sum += int(first_digit + second_digit)

    except FileNotFoundError:
        print(f"File not found: {input_filename}")
        return None
    
    return calibration_values_sum

print(calibration_document('input.txt'))

