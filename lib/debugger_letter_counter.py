
class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        print(f"We start off with an empty counter dictionary: {counter}")
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            print(f"this is our counter before the .get: {counter}")
            counter[char] = counter.get(char, 0) + 1         # the issue was that you were returning 1 here if there was no key, you need to return 0
            print(f"this is our char {char}")
            #print(f"this is our updated counter: {counter}")
            if counter[char] > most_common_count:
                print(f"this is our counter: {counter}, this is our character: {char}, this is most common count: {most_common_count}, and most common letter: {most_common}")
                most_common = char
                most_common_count = counter[char]   # the + in the += doesn't make any sense. Why are you adding extra bits? that needs to be removed. 
                print(most_common_count)
                print(most_common)
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())

# Intended output:
# [2, "i"]
