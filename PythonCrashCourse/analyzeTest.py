def count_words(filename):
    """Count approximate words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry the file " + filename + " does not exist."
        print(msg)
    else:
        # Count words in the file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'moby_dick.txt', 'the_bible.txt']
for filename in filenames:
    count_words(filename)

# Use 'pass' in an except block for a no-op to swallow the exception
