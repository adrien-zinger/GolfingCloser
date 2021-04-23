def golf(): #pass with 132 char
  i,a,p=[input,abs,print]
  if i()=='0':p(0);return
  r=5526
  for t in map(int, i().split()):
    if a(t)==a(r) and t>r or a(t)<a(r):r=t
  p(r)

def golf2(): #Shorter but O(nlogn).... but shorter
  if input()=='0':print(0);exit()
  l=map(int,input().split())
  print(min(sorted(l)[::-1],key=abs))