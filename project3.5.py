def user_shift(user_input):
    x = user_input.find(";")
    shift = user_input[0:x]
    shift = int(shift)
    return shift

def user_secret_word(user_input):
    x = user_input.find(";")
    y = user_input.rfind(";")
    word = user_input[x + 1 :y]
    word_nospace = word.replace(" ","")
    return word_nospace

def user_message(user_input):
    x = user_input.rfind(";")
    message = user_input[x + 1:]
    message_nospace = message.replace(" ","")
    return message_nospace

alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
    }

def word_to_num(word, shift):
    num_word = []
    word = word.lower()
    for i in word:
        for x, y in alpha.items():
           if x == i:
               y = y + shift
               if y > 26:
                   y = y - 26
               num_word.append(y)
    return num_word


def message_to_num(message, shift):
    num_message = []
    message = message.lower()
    for i in message:
        for x, y in alpha.items():
            if x == i:
                y = y + shift
                if y > 26:
                    y = y - 26
                num_message.append(y)
    return num_message

def message_to_size(message, word):
    size_message = []
    while len(size_message) < len(message):
        for i in word:
            size_message.append(i)
    while len(size_message) > len(message):
        del size_message[-1]
    return size_message

def add_messages(message1, message2, shift):
    for x, y in alpha.items():
        y = y + shift
        if y > 26:
            y = y - 26
        alpha[x] = y

    total_message = []
    z = 0
    for i in message1:
        q = i + message2[z]
        if q > 26:
            q = q - 26
        total_message.append(q)
        z = z + 1

    return total_message

def convert_back(message):
    letter_message = []
    for i in message:
        for x, y in alpha.items():
            if y == i:
                letter_message.append(x)
    return letter_message

def library_reset(alpha, shift):
    for x, y in alpha.items():
        y = y - shift
        if y < 0:
            y = y + 26
        alpha[x] = y

def output_word(new_word):
    upper_word = []
    for x in new_word:
        x = x.upper()
        upper_word.append(x)
    return''.join(upper_word)

def main():
    while(True):

        user_input = input()

        if user_input[0] != "-":

            get_user_shift = user_shift(user_input)
            get_word = user_secret_word(user_input)
            get_message = user_message(user_input)

            convert_word = word_to_num(get_word, get_user_shift)

            convert_message = message_to_num(get_message, get_user_shift)

            message_size = message_to_size(convert_message, convert_word)

            message_total = add_messages(convert_message, message_size, get_user_shift)

            new_word = convert_back(message_total)

            get_library = library_reset(alpha, get_user_shift)

            get_new_word = output_word(new_word)
            print(get_new_word)
        else:
            break

main()

