today = 'cerah'

if today == 'cerah': 
  print('Hari cerah kamu bisa menjemur pakaian')
  print('ga usah jemur di rumah')

battery_level = 'low'

if battery_level == 'low':
  print('your battery is low..')
  print('please, charge..')
else:
  print('your battery is full')
  
grade = input('enter your grade (A/B/C): ')
grade = grade.upper()

if grade == 'A':
  print('Congratulation..')
elif grade == 'B':
  print('Good job!')
elif grade == 'C':
  print('Good luck next time..')
else:
  print('wrong input!!')

score = 70

if score >= 70 and score < 80:
  print('grade B')
elif score > 80 and score < 85:
  print('grade B+')
elif score > 85 and score < 90:
  print('grade A')
elif score > 90 and score < 100:
  print('grade A+')
else:
  print('grade C')

hari = 'sabtu'

if hari == 'sabtu' or hari == 'minggu':
  print('hari libur!')
else:
  print('hari kerja')

usia = int(input('masukkan usia kamu: '))
sim = input('Apakah anda punya sim? Y/N : ')

if usia >= 17 and sim == 'Y':
  print('Anda diizinkan mengendarai kendaraan')
else:
  print('Anda tidak diizinkan mengendarai kendaraan')

