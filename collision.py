from config import CIRCLE_CIRCLE_E, CIRCLE_BORDER, GROUND_CIRCLE_E, CIRCLE_RADIUS, THRESHOLD_DEPTH
from coord import Coord
from calculation import resolve_vectors, cc_oblique_collision, point_to_line_dist


def check_cc_reasonable_collision(u1_para, disp1, u2_para, disp2):
    if u1_para * u2_para < 0:
        if disp1.x < disp2.x and u1_para < 0 < u2_para:
            return False
        elif disp2.x < disp1.x and u2_para < 0 < u1_para:
            return False
    return True

def cc_final_velocities(e, m1, u1, disp1, m2, u2, disp2):
    gradient = disp1.gradient(disp2)
    u1_para, v1_perp = resolve_vectors(u1, gradient)
    u2_para, v2_perp = resolve_vectors(u2, gradient)
    if check_cc_reasonable_collision(u1_para, disp1, u2_para, disp2):
        v1_para, v2_para = cc_oblique_collision(e, m1, u1_para, m2, u2_para)

        v1_x, v1_y = resolve_vectors(Coord(v1_para, v1_perp), gradient)
        v2_x, v2_y = resolve_vectors(Coord(v2_para, v2_perp), gradient)

        u1 = Coord(v1_x, v1_y)
        u2 = Coord(v2_x, v2_y)
    return u1, u2

def cg_final_velocities(e, u, dist, coord_a, coord_b):
    if u.y > 0:
        return u
    if -THRESHOLD_DEPTH < u.y < THRESHOLD_DEPTH and -THRESHOLD_DEPTH < dist < THRESHOLD_DEPTH:
        u.y = 0
        return u
    if coord_a.y == coord_b.y:
        u.y *= -e
        return u

    gradient = -1 / coord_b.gradient(coord_a)
    u_para, u_perp = resolve_vectors(u, gradient)
    v_x, v_y = resolve_vectors(Coord(u_para * -e, u_perp), gradient)
    return Coord(v_x, v_y)

def circle_circle_collision(circles, c1, c2):
    cir1 = circles[c1][0]
    cir2 = circles[c2][0]
    dist = cir1.disp.pyth(cir2.disp)
    if dist <= cir1.radius + cir2.radius:
        direction_vec = cir2.disp - cir1.disp
        cir1.disp -= (direction_vec * cir1.radius).div(100)
        cir2.disp += (direction_vec * cir2.radius).div(100)
        cir1.vel, cir2.vel = cc_final_velocities(CIRCLE_CIRCLE_E, cir1.mass, cir1.vel, cir1.disp,
                                                 cir2.mass, cir2.vel, cir2.disp)
    circles[c1][0] = cir1
    circles[c2][0] = cir2

def circle_ground_collision(circles, grounds, c):
    cir = circles[c][0]
    for grn in grounds:
        if not (grn[0].coord_a.x / 10 - cir.radius <= cir.disp.x <= grn[0].coord_b.x / 10 + cir.radius):
            continue
        grn = grn[0]
        direction_vec = grn.get_direction_vec()
        line_vec = Coord(grn.coord_a.x / 10, grn.coord_a.y)
        dist = cir.radius + CIRCLE_BORDER / 100 - abs(point_to_line_dist(cir.disp, direction_vec, line_vec))
        if dist >= 0:
            cir.disp.y += dist / 2
            cir.vel = cg_final_velocities(GROUND_CIRCLE_E, cir.vel, dist, grn.coord_a, grn.coord_b)
    circles[c][0] = cir


def sort_key(e):
    return e['disp']

def check_collisions(circles, grounds):
    num_of_circles = len(circles)
    circles_x = [{"ind": i, "disp": circles[i][0].disp.x} for i in range(num_of_circles)]
    circles_x.sort(key=sort_key)
    ind = 0
    while ind < num_of_circles:
        cir_ind1 = circles_x[ind]["ind"]
        if ind + 1 < num_of_circles and circles_x[ind + 1]["disp"] - circles_x[ind]["disp"] < CIRCLE_RADIUS * 2:
            cir_ind2 = circles_x[ind + 1]["ind"]
            circle_circle_collision(circles, cir_ind1, cir_ind2)
        circle_ground_collision(circles, grounds, cir_ind1)
        ind += 1