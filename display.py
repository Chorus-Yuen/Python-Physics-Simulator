from config import WIN_WIDTH, WIN_HEIGHT, BG_COLOUR


def create_cnv(root, tk):
    cnv = tk.Canvas(root, width=WIN_WIDTH, height=WIN_HEIGHT, bg=BG_COLOUR)
    cnv.pack()
    return cnv


def setup_display(root, cnv, grounds, circles):
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+0+0")
    root.title("Failing physics engine")
    root.bind("<Escape>", quit)

    for grn_ind, ground in enumerate(grounds):
        grn_draw = ground[0].draw(cnv)
        grounds[grn_ind].append(grn_draw)
    for cir_ind, circle in enumerate(circles):
        cir_draw = circle[0].draw(cnv)
        circles[cir_ind].append(cir_draw)