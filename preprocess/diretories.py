import yaml

flying_dir = 'flying'
mesh_dir = 'mesh'
ext_msh = '.msh'
ext_h5m = '.h5m'
ext_out_initial_mesh = '_out_initial_mesh3D'

with open("inputs.yaml", 'r') as stream:
    data_loaded = yaml.load(stream)

def load_initial_mesh():
    global flying_dir
    name_out_mesh_file = flying_dir + '/' + 'name_out_initial_mesh.txt'
    names_tags_out_mesh_file = flying_dir + '/' + 'names_tags_out_initial_mesh.txt'
    entities_to_tags_file = flying_dir + '/' + 'entities_to_tags_initial_mesh.txt'
    tags_to_infos_file = flying_dir + '/' + 'tags_to_infos_initial_mesh.txt'

    return [name_out_mesh_file, names_tags_out_mesh_file, entities_to_tags_file, tags_to_infos_file]
