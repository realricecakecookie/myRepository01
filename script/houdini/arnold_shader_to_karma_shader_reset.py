#arnold_shader_to_karma_shader_reset.py

import hou

def find_image_node(node, materiallibrary, principled_shader, input_path=[]):
    for idx, node_input in enumerate(node.inputs()):
        if node_input is not None:
            new_input_path = input_path + [idx]
            if node_input.type().name() == "arnold::image":
                if new_input_path[0] == 0: # base
                    texture = materiallibrary.createNode("texture::2.0", node_input.name())
                elif new_input_path[0] == 1: # base_color
                    texture_path = node_input.parm("filename").eval()
                    texture = materiallibrary.createNode("texture::2.0", node_input.name())
                    texture.parm("map").set(texture_path)
                    principled_shader.setInput(1, texture)
                elif new_input_path[0] == 2: # diffuse_roughness
                    texture = materiallibrary.createNode("texture::2.0", node_input.name())
                elif new_input_path[0] == 3: # metalness
                    texture = materiallibrary.createNode("texture::2.0", node_input.name())
                elif new_input_path[0] == 4: # specular
                    texture = materiallibrary.createNode("texture::2.0", node_input.name())
                elif new_input_path[0] == 5: # specular_color
                    texture = materiallibrary.createNode("texture::2.0", node_input.name())
                elif new_input_path[0] == 6: # specular_roughness
                    texture_path = node_input.parm("filename").eval()
                    texture = materiallibrary.createNode("texture::2.0", node_input.name())
                    texture.parm("map").set(texture_path)
                    principled_shader.setInput(7, texture)
                materiallibrary.layoutChildren()
            else:
                image_input_path = find_image_node(node_input, materiallibrary, principled_shader, new_input_path)
                if image_input_path is not None:
                    if new_input_path[0] == 0: # base
                        texture = materiallibrary.createNode("texture::2.0", node_input.name())
                    elif new_input_path[0] == 1: # base_color
                        texture_path = node_input.parm("filename").eval()
                        texture = materiallibrary.createNode("texture::2.0", node_input.name())
                        texture.parm("map").set(texture_path)
                        principled_shader.setInput(1, texture)
                    elif new_input_path[0] == 2: # diffuse_roughness
                        texture = materiallibrary.createNode("texture::2.0", node_input.name())
                    elif new_input_path[0] == 3: # metalness
                        texture = materiallibrary.createNode("texture::2.0", node_input.name())
                    elif new_input_path[0] == 4: # specular
                        texture = materiallibrary.createNode("texture::2.0", node_input.name())
                    elif new_input_path[0] == 5: # specular_color
                        texture = materiallibrary.createNode("texture::2.0", node_input.name())
                    elif new_input_path[0] == 6: # specular_roughness
                        texture_path = node_input.parm("filename").eval()
                        texture = materiallibrary.createNode("texture::2.0", node_input.name())
                        texture.parm("map").set(texture_path)
                        principled_shader.setInput(7, texture)
                    materiallibrary.layoutChildren()
    return None

selected_arnold_materialbuilders = hou.selectedNodes()
stage_network = hou.node("/stage")
materiallibrary = stage_network.createNode("materiallibrary")

for selected_arnold_materialbuilder in selected_arnold_materialbuilders:
	selected_arnold_materialbuilder_name = selected_arnold_materialbuilder.name()
	principled_shader = materiallibrary.createNode("principledshader::2.0", selected_arnold_materialbuilder_name)
	for arnold_standard_surface in selected_arnold_materialbuilder.glob("*standard_surface*"):
		find_image_node(arnold_standard_surface, materiallibrary, principled_shader)

hou.ui.displayMessage("Reset Arnold Shader to Karma Shader, Completly.")