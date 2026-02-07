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

def main():
    question = is_correct_format("abc")
    print(question)

if __name__ == '__main__':
    main()