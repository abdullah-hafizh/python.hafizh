score = int(input('masukkan score kamu: '))

if score > 85 and score < 100:
  print('grade A')
elif score > 70 and score < 85:
  print('grade B')
elif score > 50 and score < 70:
  print('grade C')
elif score < 50:
  print('grade D')
else:
  print('Invalid Score')