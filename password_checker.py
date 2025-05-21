from collections import Counter
import re

def analyze_string(string):
    # Most frequent character
    char_counter = Counter(string)
    most_frequent_char = max(char_counter.items(), key=lambda x: x[1])

    # Word analysis
    words = re.findall(r'\b\w+\b', string)
    word_count = len(words)
    average_word_length = round(sum(len(word) for word in words) / word_count, 2) if word_count > 0 else 0

    # Palindrome check
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
    is_palindrome = cleaned == cleaned[::-1]

    # Output
    print(f"🔤 Most Frequent Character: '{most_frequent_char[0]}' occurred {most_frequent_char[1]} times")
    print(f"📝 Number of Words: {word_count}")
    print(f"📏 Average Word Length: {average_word_length}")
    print(f"🪞 Is Palindrome? {'Yes' if is_palindrome else 'No'}")

# Run
user_input = input("Enter a string to analyze: ")
analyze_string(user_input)

