def breakingRecords(scores):
    max_count = 0
    min_count = 0
    max_score = scores[0]
    min_score = scores[0]

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1

    return [max_count, min_count]

# Example usage
n = int(input("Enter number of games: "))
scores = list(map(int, input("Enter scores: ").split()))
result = breakingRecords(scores)
print(result)
