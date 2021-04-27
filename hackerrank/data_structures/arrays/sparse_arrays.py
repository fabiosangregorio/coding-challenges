def matchingStrings(strings, queries):
    matches = []

    for query in queries:
        curr_matches = 0
        for string in strings:
            if query == string:
                curr_matches += 1
        matches.append(curr_matches)

    return matches


if __name__ == "__main__":
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]
    print(matchingStrings(strings, queries))
