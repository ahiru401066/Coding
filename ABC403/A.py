def main():
   n = int(input())
   a = list(map(int, input().split()))
   ans = 0
   for i in range(len(a)):
       if(i % 2 == 0): ans += a[i]

   print(ans)
    

main()