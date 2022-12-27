# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
english_paper = set(map(int,input().split()))
input() 
french_paper = set(map(int,input().split()))
print(len(english_paper | french_paper))
