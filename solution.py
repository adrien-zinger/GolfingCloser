def golf(): #pass with 132 char
  i,a,p=[input,abs,print]
  if i()=='0':p(0);return
  r=5526
  for t in map(int, i().split()):
    if a(t)==a(r) and t>r or a(t)<a(r):r=t
  p(r)