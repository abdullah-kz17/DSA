
def miniMaxSum(arr):
    # Write your code here
    total_sum = sum(arr)
    
    min_val = min(arr)
    max_val = max(arr)
    
    min_sum = total_sum-max_val
    max_sum = total_sum-min_val
    
    print(min_sum,max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
