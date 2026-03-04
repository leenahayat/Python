for i in [2,3,4,5,6,8,0]:
    if (i%2 != 0):
        continue
    print(i)

#break means loop ko chorh k nikal jao
#continue means iteration ko chorh k nikal jao     


for num in range(1, 6):
  if num % 2 == 0:
    print(f"Skipping even number: {num}")
    continue  # Skip the rest of the loop body for this iteration
  print(f"Processing odd number: {
