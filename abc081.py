N = int(input()) #1行目のNを取得する
A = [int(input()) for i in range(N)] #複数行の数値の入力を取得
count=0   #割った回数
state=1   #状態

while(state):
  i=0
  while(i<N):
    if(A[i]%2):   #割り切れないとき
      state=0
    else:     #割り切れるとき
      A[i]=A[i]/2
    i+=1
  count+=1

count-=1

print(count)