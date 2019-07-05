"""
Will store all the functions needed to export the rotate layer
"""

import sys
import copy
import settings
from helpers.transform import gen_helpers_transform
from synfig.animation import print_animation, gen_dummy_waypoint
import synfig.group as group
sys.path.append("..")


def gen_layer_rotate(lottie, layer):
    """
    Help generate transform properties
    """
    scale = [100, 100, 100]
    for child in layer:
        if child.tag == "param":
            if child.attrib["name"] == "origin":
                anchor = gen_dummy_waypoint(child, "param", "vector")
                pos = anchor
            elif child.attrib["name"] == "amount":  # This is rotation
                rotation = gen_dummy_waypoint(child, "param", "angle")
                rotation[0].attrib["type"] = "rotate_layer_angle"

    #print_animation(anchor, pos, rotation)
    anchor = copy.deepcopy(anchor)
    group.update_pos(anchor)
    if settings.INSIDE_PRECOMP:
        group.update_pos(pos)
    gen_helpers_transform(lottie, layer, pos[0], anchor[0], scale, rotation[0])
