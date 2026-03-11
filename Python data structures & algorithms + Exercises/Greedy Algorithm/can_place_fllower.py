

#n a quantidade de flores
def can_place_flowers(flowerbed: list, n: int)-> bool:

  for i in range(len(flowerbed) - 1):
    if flowerbed[i -1] == 0 and flowerbed[i]== 0 and flowerbed[i + 1] == 0:
      flowerbed[i] = 1
      n -= 1
  
  return n <= 0