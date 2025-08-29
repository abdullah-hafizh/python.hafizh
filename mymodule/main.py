from mathematic.circle.area import area_of_circle
from mathematic.square.area import area_of_square
from konversi_suhu.celcius import celcius_to_farenheit, celcius_to_kelvin
from konversi_suhu.farenheit import farenheit_to_celcius
from konversi_suhu.kelvin import kelvin_to_celcius

area_of_circle(7)
area_of_square(2)

print(f'25 C = {celcius_to_farenheit(25)} F')
print(f'25 C = {celcius_to_kelvin(25)} K')

print(f'50 F = {farenheit_to_celcius(50)} F')
print(f'50 K = {kelvin_to_celcius(50)} K')
