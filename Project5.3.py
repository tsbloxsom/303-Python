# Morgan McKee
def thread_list(big_str):
    new_list = []
    x = 0
    while x < len(big_str)//2:
        new_list.append(big_str[x])
        new_list.append(big_str[len(big_str)//2 + x])
        x = x + 1
    return "".join(new_list)

def valid_DNA(string):
    if len(string) < 2:
        return ""
    if string[0] == string[1]:
        return valid_DNA(string[2:])
    if string[0] == "A" and string[1] == "G" or string[0] == "a" and string[1] == "g":
        return valid_DNA(string[2:])
    if string[0] == "A" and string[1] == "C" or string[0] == "a" and string[1] == "c":
        return valid_DNA(string[2:])
    if string[0] == "G" and string[1] == "A" or string[0] == "g" and string[1] == "a":
        return valid_DNA(string[2:])
    if string[0] == "G" and string[1] == "T" or string[0] == "g" and string[1] == "t":
        return valid_DNA(string[2:])
    if string[0] == "T" and string[1] == "G" or string[0] == "t" and string[1] == "g":
        return valid_DNA(string[2:])
    if string[0] == "T" and string[1] == "C" or string[0] == "t" and string[1] == "c":
        return valid_DNA(string[2:])
    if string[0] == "C" and string[1] == "A" or string[0] == "c" and string[1] == "a":
        return valid_DNA(string[2:])
    if string[0] == "C" and string[1] == "T" or string[0] == "c" and string[1] == "t":
        return valid_DNA(string[2:])
    if string[0] == "a" and string[1] == "G" or string[0] == "A" and string[1] == "g":
        return valid_DNA(string[2:])
    if string[0] == "A" and string[1] == "c" or string[0] == "a" and string[1] == "C":
        return valid_DNA(string[2:])
    if string[0] == "g" and string[1] == "A" or string[0] == "a" and string[1] == "G":
        return valid_DNA(string[2:])
    if string[0] == "g" and string[1] == "T" or string[0] == "G" and string[1] == "t":
        return valid_DNA(string[2:])
    if string[0] == "t" and string[1] == "G" or string[0] == "g" and string[1] == "T":
        return valid_DNA(string[2:])
    if string[0] == "T" and string[1] == "c" or string[0] == "C" and string[1] == "t":
        return valid_DNA(string[2:])
    if string[0] == "c" and string[1] == "A" or string[0] == "C" and string[1] == "a":
        return valid_DNA(string[2:])
    if string[0] == "c" and string[1] == "T" or string[0] == "C" and string[1] == "t":
        return valid_DNA(string[2:])
    else:
        return string[0:2] + valid_DNA(string[2:])

def longest_DNA(numberOfPairs, recursion_list, valid_dna_list):
    if len(valid_dna_list) < numberOfPairs * 2:
        return ""
    elif valid_dna_list[0:numberOfPairs*2] != recursion_list[0:numberOfPairs*2] and valid_dna_list[0:2] \
            == recursion_list[0:2]:
        return longest_DNA(numberOfPairs, recursion_list[2:], valid_dna_list[2:])
    elif valid_dna_list[0:numberOfPairs*2] != recursion_list[0:numberOfPairs*2]:
        return longest_DNA(numberOfPairs, recursion_list[2:], valid_dna_list[:])
    else:
        return valid_dna_list[0:numberOfPairs*2]

def format_strand(small_str):
    strand_list = []
    x = 0
    while x < len(small_str)//2 - 1:
        strand_list.append(small_str[x])
        strand_list.append(small_str[x+2])
        strand_list.append(small_str[x+4])
        x = x + 1
    return "".join(strand_list)

def main():
    with open('dna.txt') as fileToOpen:
        numberOfPairs = int(fileToOpen.readline())
        DNA_list = fileToOpen.readlines()
        """Used code from here for line below: https://bytes.com/topic/python/answers/801097-how-remove-n-list"""
        DNA_list[:] = [line.rstrip('\n') for line in DNA_list]
        # print(numberOfPairs)
    """Used code from here for line below: https://stackoverflow.com/questions/5850986/
    joining-pairs-of-elements-of-a-list-python"""

    # joining pairs of elements in the list
    paired_list = [DNA_list[i] + DNA_list[i + 1] for i in range(0, len(DNA_list), 2)]
    # print(paired_list)

    # put pairs of the two strings next to each other
    recursion_list = []
    for str in paired_list:
        recursion_list.append(thread_list(str))
    # print("every DNA pair side by side", recursion_list)

    # putting valid pairs next to each other,
    valid_dna_list = []
    for str in recursion_list:
        valid_dna_list.append(valid_DNA(str))
    # print("every valid DNA pair", valid_dna_list)

    # longest DNA pairs list
    longest_dna_list = []
    for long_str, short_str in zip(recursion_list, valid_dna_list):
        longest = longest_DNA(numberOfPairs, long_str, short_str)
        longest_dna_list.append(longest)
    # print("longest dna strand", longest_dna_list)

    # put back into separate strings
    new_dna_list = []
    for str in longest_dna_list:
        new_dna_list.append(format_strand(str))
    # print("dna for file output", new_dna_list)

    file2write = open("dnaresults.txt", "w")
    x = 0
    for str in new_dna_list:
        file2write.write("DNA sequence pair {0}:\n".format(x))
        if longest_dna_list[x] == '':
            file2write.write("No matches found")
            file2write.write(" \n")
            file2write.write(" \n")
        else:
            str1, str2 = longest_dna_list[x][::2], longest_dna_list[x][1::2]
            file2write.write(str1 + " \n")
            file2write.write(str2)
            file2write.write(" \n")
            file2write.write(" \n")
        x = x + 1

    file2write.close()

main()