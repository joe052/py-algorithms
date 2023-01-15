"""
Monk recently taught Fredo about sorting. Now, he wants to check whether he understood the concept or not. So, he gave him the following algorithm and asked to implement it:

Assumptions:
We consider the rightmost digit of each number to be at index 1, second last at index 2 and so on till the leftmost digit of the number.
Meaning of 
 chunk: This chunk consists of digits from position  5  * i to 1 + 5 * (i-1) in the given number.If there is no digit at some position in the number, take the digit to be 0.

Initially, i is 1.

Construct the i th chunk, for all of the integers in the array. Let's call the value of this chunk to be the weight of respective integer in the array.
If weight of all the integers of the array is 0, then STOP
Sort the array according to the weights of integers. If two integers have same weight, then the one which appeared earlier should be positioned earlier after the sorting is done. The array changes to this sorted array.
Increment i by 1 and repeat from STEP 1
 

See the sample explanation for a better understanding.
So, Fredo understood the concept and coded it. Now, Monk asks you to write the code for the algorithm to verify Fredo's answer.

Video approach to solve this question: here

Input:
The first line of the input contains N denoting the number of elements in the array to be sorted.
The next line contains N single space separated integers denoting the array elements.

Output:
You need to print the new array in each step of the algorithm.

Constraints:

; A[] is the input array
Size of integers (number of digits in integer) in A may not be same.
 

Note

 

Use Fast I/O
Sample Input
3
213456789 167890 123456789
Sample Output
213456789 123456789 167890 
167890 123456789 213456789 
Explanation
Each line of output is the array after each transformation.
Here goes the explanation:
1st chunk of respective integers= 56789, 67890, 56789
weight of respective integers= 56789, 67890, 56789
So, sorted array according to weights is [213456789, 123456789, 167890] because 56789< 67890.
Note that the weight of 213456789 and 123456789 are the same, so we need to keep the given order.This becomes the new array.

The array now is [213456789, 123456789, 167890]
2nd chunk of respective integers in the array= 02134, 01234, 00001
weight of respective integers= 2134, 1234, 1
So, sorted array according to weights is [167890, 123456789, 213456789] because 1<1234<2134.
This becomes the new array.

The array now is [167890, 123456789, 213456789].
So, as the 3rd chunk would have no digits for any integer, so weights of all integers will be 0 and the algorithm would stop.
"""


def radix_sort(arr):
    i = 1
    while True:
        # construct the chunk for each number in the array
        chunks = [int(str(num)[-5*i+4:5*i-4]) if 5*i-4 <= len(str(num)) else 0 for num in arr]
        # if all chunks are 0, stop
        if all(val == 0 for val in chunks):
            break
        # sort the array based on the chunks
        arr = [x for _, x in sorted(zip(chunks, arr))]
        print(arr)
        i += 1
    return arr

n = int(input())
arr = list(map(int, input().split()))
print(radix_sort(arr))



def chunk(x, i):
    n = len(str(x))
    start = n - 5*i
    end = n - 5*i + 5
    if start >= 0:
        return int(str(x)[start:end])
    elif end < 0:
        return 0
    else:
        return int(str(x)[:end])
 
n = int(input())
x = list(map(int,input().strip().split()))[:n]
 
i = 1
while True:
    chunk_dic = {}
    for num in x:
        chunk_dic[num] = chunk(num, i)
    values = list(chunk_dic.values())
    if values == [0 for j in range(n)]:
        break
    values.sort()
    sort_arr = []
    for num in values:
        sort_arr.append(list(chunk_dic.keys())[list(chunk_dic.values()).index(num)])
        chunk_dic[list(chunk_dic.keys())[list(chunk_dic.values()).index(num)]] = -1
    print(*sort_arr)
    i += 1
 
