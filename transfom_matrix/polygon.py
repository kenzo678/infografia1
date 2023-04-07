import arcade
import numpy as np

class Polygon:
 def __init__(self, vertices, color=arcade.color.RED_VIOLET):
  self.vertices = vertices
  self.color = color
  self.line_width = 4

 def draw(self):
  arcade.draw_polygon_outline(self.vertices, self.color, self.line_width)

 def move(self, dx: int, dy:int):
  for i, v in enumerate(self.vertices):
   self.vertices[i] = (v[0] + dx, v[1] + dy)

 def transform(self, t_matrix):
  #1. convertir vertices a matrices de 3,n
  vlist=[[v[0], v[1], 1] for v in self.vertices]
  vmatrix = np.transpose(np.array(vlist))
  #2. aplicar la matriz de transformacion
  newmatrix = np.dot(t_matrix, vmatrix)
  #for v in self.vertices:
  # vlist.append([v[0], v[1], 1])
  #3. convertir nuevos vertices al formato [(),(),...]
  newmatrix2 = np.transpose(newmatrix)
  newverts = [(nv[0], nv[1]) for nv in newmatrix2]
  #4. reasignar vertices
  self.vertices = newverts
  print(newverts)

 def translate(self, dx, dy):
  trf = np.array([
   [1, 0, dx],
   [0, 1, dy],
   [0, 0, 1]
  ])
  self.transform(trf)

 def rotate(self, theta):
  varray = np.array(self.vertices)
  center = np.sum(varray, axis = 0) / varray.shape[0]
  to_origin_trf = np.array([
   [1, 0, -center[0]],
   [0, 1, -center[1]],
   [0, 0, 1]
  ])
  from_origin_trf = np.array([
   [1, 0, center[0]],
   [0, 1, center[1]],
   [0, 0, 1]
  ])
  rotatetrf = np.array([
   [np.cos(np.radians(theta)), -np.sin(np.radians(theta)), 0],
   [np.sin(np.radians(theta)), np.cos(np.radians(theta)), 0],
   [0, 0, 1]
  ])
  self.transform(np.dot(from_origin_trf, np.dot(rotatetrf, to_origin_trf)))

 def scale(self, sx, sy):
  varray = np.array(self.vertices)
  center = np.sum(varray, axis = 0) / varray.shape[0]
  to_origin_trf = np.array([
   [1, 0, -center[0]],
   [0, 1, -center[1]],
   [0, 0, 1]
  ])
  from_origin_trf = np.array([
   [1, 0, center[0]],
   [0, 1, center[1]],
   [0, 0, 1]
  ])
  trf = np.array([
   [sx, 0, 0],
   [0, sy, 0],
   [0, 0, 1]
  ])
  self.transform(np.dot(from_origin_trf, np.dot(trf, to_origin_trf)))

if __name__ == "__main__":
 p=Polygon([(40,40),(200,40),(120,200)])
 Tr = np.array([1, 0 , 100], [0, 1, 100], [0, 0, 1])
 p.transform(Tr)
