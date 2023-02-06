from math import sin, cos, atan

def resolve_vectors(vel, gradient):
    s = sin(atan(gradient))
    c = cos(atan(gradient))
    new_vel_a = vel.x * c + vel.y * s # x / para
    new_vel_b = vel.x * s - vel.y * c # y / perp
    return new_vel_a, new_vel_b

def cc_oblique_collision(e, m1, u1_para, m2, u2_para):
    tot_m = m1 + m2
    a = m1 * u1_para + m2 * u2_para
    b = u2_para - u1_para
    v1_para = (a + e * m2 * b) / tot_m
    v2_para = (a - e * m1 * b) / tot_m
    return v1_para, v2_para

def point_to_line_dist(point_vec, direction_vec, line_vec):
    point_to_line_vec = line_vec - point_vec
    return point_to_line_vec.cross(direction_vec) / direction_vec.mod()