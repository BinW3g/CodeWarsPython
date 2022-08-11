# codewars challenge link
# https://www.codewars.com/kata/537e18b6147aa838f600001b

def justify(text, width):
    words = text.split(" ")
    text_out = ""
    current_words = []
    current_with = 0
    while len(words) > 0:
        word = words.pop(0)
        if current_with + len(word) > width:
            if len(current_words) > 1:
                current_with -= len(current_words)
                spaces = int((width - current_with) / (len(current_words)-1))
                left_spaces = (width - current_with) % (len(current_words)-1)
                for w in current_words[:-1]:
                    text_out += w + " " * spaces + " " * (1 if left_spaces > 0 else 0)
                    left_spaces -= 1
            text_out += current_words[-1] + "\n"
            current_words.clear()
            current_with = 0
        current_words.append(word)
        current_with += len(word) + 1
    for w in current_words[:-1]:
        text_out += w + " "
    text_out += current_words[-1]
    return text_out


if __name__ == '__main__':
    print(justify('123 45 6', 7) == '123  45\n6')
    print(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, '
                  'at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet '
                  'felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt '
                  'suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. '
                  'Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec '
                  'lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis '
                  'rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque '
                  'commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et '
                  'dolor.', 20))
