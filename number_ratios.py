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

    positive_count_ratio = positive_counts/total_counts
    negative_count_ratio = negative_counts/total_counts
    zero_count_ratio = zero_counts/total_counts
    
    print (f"{positive_count_ratio:.6f}")
    print (f"{negative_count_ratio:.6f}")
    print (f"{zero_count_ratio:.6f}")


if __name__ == "__main__":
    n = int(input())  
    arr = list(map(int, input().split()))  

plusMinus(arr)
