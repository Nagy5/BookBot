from stats import get_text, char_count
import sys


def get_book_text(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error {filepath} not found")
        return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        words = get_book_text(sys.argv[1])
        if words:
            sol = char_count(words)
            sol = sorted(sol.items(), key=lambda x: x[1], reverse=True)
            res = "\n\n ============ BOOKBOT ============ \n\n"
            res += "Analyzing book found at ./books/frankenstien.txt...\n\n"
            res += "----------- Word Count ---------- \n\n"
            res += f"found {get_text(words)} Total words \n\n"
            res += "--------- Character Count ------- \n\n"
            for key, value in sol:
                res += f"{key}: {value}\n"
            res += "\n ============= END =============== \n"
            print(res)

main()
