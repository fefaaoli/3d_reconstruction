import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def orientation(center, radius):
    vertices = [
        [center[0] - radius, center[1] - radius, center[2]], #vértice esquerdo
        [center[0] + radius, center[1] - radius, center[2]],  #vértice direito
        [center[0], center[1] + radius, center[2]]  #vértice superior
    ]
    return np.array(vertices)

resolutionx = int(720 / 2)
resolutiony = int(220 / 2)

#C1
bola1 = pd.read_csv('c1.txt', sep='\s+', header=None, decimal='.')
bola1[1] = bola1[1] - -resolutionx
bola1[2] = -1 * (bola1[2] - resolutiony)
bola1 = np.asarray(bola1[[1, 2]])

#C2
bola2 = pd.read_csv('c2.txt', sep='\s+', header=None, decimal='.')
bola2[1] = bola2[1] - -resolutionx
bola2[2] = -1 * (bola2[2] - resolutiony)
bola2 = np.asarray(bola2[[1, 2]])

#----------------------------------------------------------------------------------------------------- CAMERA 1
#trajetória 3D - C1 
traj3d_c1 = np.column_stack((bola1[:, 0], bola2[:, 1], np.linspace(0, 1, len(bola1))))


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

#trajetória C1
ax.plot(traj3d_c1[:, 0], traj3d_c1[:, 1], traj3d_c1[:, 2], 'o-', label='Trajetória da bola - C1', color='blue')

for point in traj3d_c1:
    triangle = orientation(point, radius=2.5)
    tri = Poly3DCollection([triangle], alpha=1, facecolor='red', edgecolor='black')
    ax.add_collection3d(tri)

ax.set_xlabel('Coordenada X')
ax.set_ylabel('Coordenada Y')
ax.set_zlabel('Coordenada Z')
ax.set_title('Trajetória da Bola em 3D orientada - C1')

plt.savefig('3d_orientada_c1.png', dpi=300)
plt.show()

#----------------------------------------------------------------------------------------------------- CAMERA 2

#trajetória 3D - C2
traj3d_c2 = np.column_stack((bola1[:, 0], bola2[:, 1], np.linspace(0, 1, len(bola2))))


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

#trajetória C2
ax.plot(traj3d_c2[:, 0], traj3d_c2[:, 1], traj3d_c2[:, 2], 'o-', label='Trajetória da bola - Câmera 2', color='green')

for point in traj3d_c2:
    triangle = orientation(point, radius=2.5)
    tri = Poly3DCollection([triangle], alpha=1, facecolor='yellow', edgecolor='black')
    ax.add_collection3d(tri)

ax.set_xlabel('Coordenada X')
ax.set_ylabel('Coordenada Y')
ax.set_zlabel('Coordenada Z')
ax.set_title('Trajetória da Bola em 3D orientada - C2')

plt.savefig('3d_orientada_c1.png', dpi=300)
plt.show()
