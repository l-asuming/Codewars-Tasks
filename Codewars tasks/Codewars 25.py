def cartesian_neighbor(x, y):
    x_coords = [x-1,x,x+1]
    y_coords = [y-1,y,y+1]
    neighbours = [(i,j) for i in x_coords for j in y_coords]
    neighbours.remove((x,y))
    return neighbours

print(cartesian_neighbor(0,0))