def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
        row = len(image)
        col = len(image[0])
        
        for i in range(row):
          left = 0
          right = row - 1
          while left <= right:
            image[i][left], image[i][right] = image[i][right], image[i][left]
            left +=1
            right -= 1
        transformed = [[1 - num for num in row] for row in image]

        return transformed

        
                
if __name__ == '__main__':
    image = [[1,1,0],[1,0,1],[0,0,0]]
    print(flipAndInvertImage(image))
