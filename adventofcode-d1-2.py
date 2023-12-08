def calibration_document(input_filename):
    calibration_values_sum = 0

    digit_names_translation = {
        'one': 'on1e', 'two': 'tw2o', 'three': 'thr3ee', 'four': 'fo4ur', 'five': 'fi5ve', 'six': 'si6x', 'seven': 'se7ven', 'eight': 'eig8ht', 'nine': 'ni9ne', 'zero': 'ze0ro'
    }

    try:
        with open(input_filename, 'r') as file:
            for line in file: 
                #replace any occurence of digit name with a number
                for digit_name, digit_value in digit_names_translation.items():
                    line=line.replace(digit_name,str(digit_value))

                digits_list = []
                for char in line:
                    if char.isdigit(): 
                        digits_list.append(char)

                #add the digit to the sum
                calibration_values_sum += int(digits_list[0]+digits_list[-1])

    except FileNotFoundError:
        print(f"File not found: {input_filename}")
        return None
    
    return calibration_values_sum

print(calibration_document('input.txt'))