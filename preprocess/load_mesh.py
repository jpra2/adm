from .mesh_object import Mesh
from . import diretories
import pickle

class LoadMesh:

    def __init__(self, n):
        self.n = n

    def load_mesh(self, list_names_files):

        mesh = Mesh(list_names_files)

        return mesh

    def run(self):

        if self.n == 1:
            list_names_files = diretories.load_initial_mesh()
            mesh = self.load_mesh(list_names_files)
            import pdb; pdb.set_trace()

        return mesh
