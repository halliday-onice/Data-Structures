def flood_fill(image: list[list[int]], sr:int, sc: int, color: int):
  #image[i][j] represents the pixel value of the image
  #perform a flood fill on the image starting from image[sr][sc]
  #dfs
  #FLOOD FILL:
  # change color to color
  # perform the same process that is directly adjacent and share the same color as the starting pixel
  rows = len(image)
  cols = len(image[0])

  original_color = image[sr][sc]

  if original_color == color:
    return image

  def dfs(r,c):
    if 0 <= r < rows and 0 <= c < cols:
      if image[r][c] == original_color:
        image[r][c] = color

        dfs(r + 1, c)
        dfs(r, c+ 1)
        dfs(r -1, c)
        dfs(r, c- 1)
  dfs(sr,sc)
  return image