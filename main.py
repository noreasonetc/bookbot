from collections import Counter


def main():

    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    with open("books/frankenstein.txt") as f:
        contents = f.read()

    wc = len(contents.split())

    def charcounter(text):
        res = {k: v for k, v in Counter(text.lower()).items() if k in contents}
        print(res)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    for k,v in Counter(sorted(contents.lower())).items():
        if k in alph:
            print(f"The '{k}' was found {v} times")
    print("--- End report ---")
main()