# plusMinus Function

## Description

The `plusMinus` function takes an array of integers and calculates the ratio of positive, negative, and zero values in the array. It prints these ratios, formatted to 6 decimal places.

## How It Works

1. **Initialize Counters**: 
   - Three counters are created to track the number of positive, negative, and zero numbers in the array.

2. **Counting Loop**: 
   - The function loops through each number in the array:
     - If the number is positive, the positive counter is increased.
     - If the number is negative, the negative counter is increased.
     - If the number is zero, the zero counter is increased.

3. **Calculate Ratios**: 
   - The ratio of each category (positive, negative, zero) is calculated by dividing the count by the total number of elements in the array.

4. **Print Results**: 
   - The ratios are printed, each formatted to 6 decimal places.

## Example Input/Output

### Input
```python
6
-4 3 -9 0 4 1
```
### Output
```python
0.500000
0.333333
0.166667
```



## Code

```python
def plusMinus(arr):

    positive_counts = 0
    negative_counts = 0
    zero_counts = 0
    
    total_counts = len(arr)
    
    for num in arr:
        if num > 0:
            positive_counts += 1
        if num < 0:
            negative_counts += 1
        if num == 0:
            zero_counts += 1

    positive_count_ratio = positive_counts / total_counts
    negative_count_ratio = negative_counts / total_counts
    zero_count_ratio = zero_counts / total_counts
    
    print(f"{positive_count_ratio:.6f}")
    print(f"{negative_count_ratio:.6f}")
    print(f"{zero_count_ratio:.6f}")


if __name__ == "__main__":
    n = int(input())  
    arr = list(map(int, input().split()))  

plusMinus(arr)
```
--------
----

# Camel Case Split and Combine

This Python program processes strings either by splitting camelCase into separate words or by combining words into camelCase for class names, method names, or variable names.

## Example Input/Output

### Input
```python
S;V;iPad
C;M;mouse pad
C;C;code swarm
S;C;OrangeHighlighter
```
### Output
```python
i pad
mousePad()
CodeSwarm
orange highlighter
```

## Code

```python
import re

def split_camel_case(text):
    return ' '.join(re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', text)).lower()

def combine_camel_case(words, type):
    words = words.split()
    if type == 'C':
        return ''.join(word.capitalize() for word in words)
    elif type == 'V':
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    elif type == 'M':
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:]) + '()'

def process_input(line):
    operation, type, data = line.split(';')
    
    if operation == 'S':
        if type == 'M':
            data = data[:-2]
        print(split_camel_case(data))
    
    elif operation == 'C':
        print(combine_camel_case(data, type))

def main():
    import sys
    inputs = sys.stdin.read().strip().splitlines()
    
    for line in inputs:
        process_input(line)

if __name__ == "__main__":
    main()
```

----
----

# Breaking Records

## Description

The `breakingRecords` function tracks the number of times a player breaks their personal record for the highest and lowest scores during a season. Given a list of scores from a series of games, the function returns the count of how many times the player sets new records for both maximum and minimum scores.
## Example Input/Output

### Input
```python
Enter number of games: 10
Enter scores: 10 5 20 20 4 5 2 25 1
```
### Output
```python
[2, 4]
```
## Code

```python
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
```
---
---
# Mini-Max Sum

## Description

The `miniMaxSum` function takes a list of 5 integers and calculates two sums:
1. The **minimum sum** is the sum of the four smallest integers.
2. The **maximum sum** is the sum of the four largest integers.

The function then prints both sums, the minimum sum first and the maximum sum second, separated by a space.

## Example Input/Output

### Input
```python
1 2 3 4 5
```
### Output
```python
10 14
```

## Code

```python
def miniMaxSum(arr):
    total_sum = sum(arr)
    
    min_val = min(arr)
    max_val = max(arr)
    
    min_sum = total_sum - max_val
    max_sum = total_sum - min_val
    
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
```
----
----

# Time Conversion

## Description

The `timeConversion` function converts a given time from 12-hour AM/PM format to 24-hour military time format. It takes a string input in the format `hh:mm:ssAM` or `hh:mm:ssPM` and returns the time in `HH:MM:SS` format.

## Example Input/Output

### Input
```python
07:05:45PM
```
### Output
```python
19:05:45
```

## Code

```python
def timeConversion(s: str) -> str:
    period = s[-2:]
    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]

    if hour > 12:
        return "Invalid hour value. Hour must be between 01 and 12."

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    military_time = f"{hour:02}:{minute}:{second}"
    return military_time

print(timeConversion("07:05:45PM"))
```
---
---
