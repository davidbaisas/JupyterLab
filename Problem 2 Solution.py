fibonacci = [1,2]

while True:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
    if fibo[-1]>4000000:        
      break

print sum(filter(lambda x:x%2==0,fibonacci))
