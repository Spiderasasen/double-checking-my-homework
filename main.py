from typing import List


#checks if the message is only a's or b's
def is_correct_format(message: str):
    #checks if it has numbers
    if  message.isalpha():
        message = message.lower()
        #turns the its into a list and will check if it only has a or b
        string_list = []
        for char in message:
            if char == "a" or char == "b":
                string_list.append(char)

        #returns the list with a's and b's
        return string_list

    else:
        return "Please enter a valid message"

#orginazes the letters
def orginize(message: List[str]):
    # making 2 catigories
    a = []
    b = []

    # adds all the letters into the correct system
    for char in message:
        if char == "a":
            a.append(char)
        elif char == "b":
            b.append(char)

    return a, b

#checks if the message has an even amount of a's and a odd amount of b's
def even_odd(message: List[str]):
    print("Even and Odd characters problem")
    a, b = orginize(message)
    print(f"A: {a}\nB: {b}")
    if a == b:
        return False
    else:
        if len(a) % 2 == 0:
            if len(b) % 2 == 1:
                return True
            else:
                return False
        else:
            return False

#question 2, has a min length of 3, and even a's
def question2(message: List[str]):
    print("Question 2 problem, mas a minimum length of 3 and an even number of a's in the langague")
    a, b = orginize(message)
    print(f"A: {a}\nB: {b}")

    #actual code
    if len(message) >= 3:
        if len(a) % 2 == 0:
            return True
        else:
            return False
    else:
        return False

def main():
    message_input = input("Please enter a message: \n")
    message = is_correct_format(message_input)
    print(even_odd(message))
    print(question2(message))

if __name__ == '__main__':
    main()