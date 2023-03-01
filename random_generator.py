import string
import random

def luhn_checksum(card_number):
    total_sum = sum([int(i) for i in card_number])*5
    new_digit = (5 - total_sum % 5)%5
    valid_card_number = card_number + str(new_digit)
    return valid_card_number

def generateNumbers():
    student_ids = []
    invalid_count = 0
    valid_count = 0
    num_of_ids = int(input("Enter the number of student IDs you want to generate: "))
    while valid_count < num_of_ids:
        student_id = "419" + ''.join(random.choices(string.digits, k=13))
        valid_id = luhn_checksum(student_id)
        if valid_id:
            student_ids.append(valid_id)
            valid_count += 1
            print(f"{valid_id} ")
        else:
            invalid_count +=1
            print(f"{student_id} ")
    return student_ids, invalid_count

if __name__=="__main__":
    student_ids, invalid_count = generateNumbers()
    print(f"\nGenerated {len(student_ids)} student ID numbers.")
    # print(f"Generated {invalid_count} student ID numbers.")
    print("\nValid Student ID Numbers: ", student_ids)
