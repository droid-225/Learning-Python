text = "We be writing fr fr\n"

with open('test.txt', 'w') as f: # 'w' to overwrite current text in file, 'a' to append text to a file's current text
    f.write(text)