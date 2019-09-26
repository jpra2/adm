import numpy as np
from pymoab import core, types, rng, topo_util
import yaml
import time
import pickle
import os

class Mesh:

    def __init__(self, list_names_files):
        self.mesh_file = list_names_files[0]
        self.excluir = self.load_file(list_names_files)


    def load_file(self, list_names_files):
        self.mb = core.Core()
        self.root_set = self.mb.get_root_set()
        self.mtu = topo_util.MeshTopoUtil(self.mb)
        self.dimension = 3
        self.tags = dict()
        self.datas = dict()
        # self.excluir = []
        self.n_levels = 2

        mesh_file = list_names_files[0]
        entities_to_tags_file = list_names_files[2]
        tags_to_infos_file = list_names_files[3]

        self.mb.load_file(mesh_file)

        volumes = self.mb.get_entities_by_dimension(0, self.dimension)
        nodes = self.mb.get_entities_by_dimension(0, 0)
        self.mtu.construct_aentities(nodes)
        faces = self.mb.get_entities_by_dimension(0, 2)

        self.entities = dict()

        self.entities['volumes'] = volumes
        self.entities['faces'] = faces
        self.entities['nodes'] = nodes

        with open(entities_to_tags_file, 'rb') as handle:
            self.entities_to_tags = pickle.loads(handle.read())
        with open(tags_to_infos_file, 'rb') as handle:
            self.tags_to_infos = pickle.loads(handle.read())

        for name in self.tags_to_infos.keys():
            try:
                self.tags[name] = self.mb.tag_get_handle(name)
            except:
                raise NameError(f'A tag {name} nao esta no arquivo')

        boundary_faces = self.mb.tag_get_data(self.tags['BOUNDARY_FACES'], 0, flat=True)[0]
        boundary_faces = self.mb.get_entities_by_handle(boundary_faces)
        self.entities['boundary_faces'] = boundary_faces
        intern_faces = self.mb.tag_get_data(self.tags['INTERN_FACES'], 0, flat=True)[0]
        intern_faces = self.mb.get_entities_by_handle(intern_faces)
        self.entities['intern_faces'] = intern_faces
        self.entities['vols_viz_face'] = self.mb.tag_get_data(self.tags['VOLS_VIZ_FACE'], intern_faces)

        excluir_nomes = ['BOUNDARY_FACES', 'INTERN_FACES', 'VOLS_VIZ_FACE']

        return excluir_nomes
