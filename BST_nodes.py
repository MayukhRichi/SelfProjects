class bst:
    class node:
        def __init__(self, key: int, value: str):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.depth = 0
            self.sz = 1

        def __str__(self):
            this = 'BST-NODE : '
            this += str(self.key) + '(key), '
            this += self.value + '(value), '
            this += str(self.depth) + '(depth), '
            this += str(self.sz) + '(size)'
            return this

    def __init__(self, root: node = None):
        self.root = root

    def put(self, key, value):
        def _put_(key1, value1, now, depth1) -> bst.node:
            if now is None:
                now = bst.node(key1, value1)
                now.depth = depth1
                return now
            if key1 < now.key:
                now.left = _put_(key1, value1, now.left, depth1 + 1)
            elif key1 > now.key:
                now.right = _put_(key1, value1, now.right, depth1 + 1)
            else:
                now.value = value1
            now.sz = 1 + self.size(now.left) + self.size(now.right)
            return now
        if self.root is None:
            self.root = self.node(key, value)
        else:
            self.root = _put_(key, value, self.root, 0)

    def put_n_draw(self, key, value, lines, circles):  # only to use for representation
        def _put_(key1, value1, now, depth1) -> bst.node and bool:
            if now is None:
                now = bst.node(key1, value1)
                now.depth = depth1
                return now, True
            if key1 < now.key:
                now.left, just_found = _put_(key1, value1, now.left, depth1 + 1)
                if just_found:
                    lines.append(((now.key, now.depth * 40), (key1, now.depth * 40 + 40)))
                    circles.append((key1, now.depth * 40 + 40))
            elif key1 > now.key:
                now.right, just_found = _put_(key1, value1, now.right, depth1 + 1)
                if just_found:
                    lines.append(((now.key, now.depth * 40), (key1, now.depth * 40 + 40)))
                    circles.append((key1, now.depth * 40 + 40))
            else:
                now.value = value1
            now.sz = 1 + self.size(now.left) + self.size(now.right)
            return now, False
        if self.root is None:
            return None  # expected a pre-requisite root
        else:
            self.root, boolean = _put_(key, value, self.root, 0)

    def get(self, key):
        now = self.root
        while now is not None:
            if key < now.key:
                now = now.left
            elif key > now.key:
                now = now.right
            else:
                return now.value
        return False

    def delete(self, key):
        def depth_correction(now):
            if now is not None:
                now.depth -= 1
                depth_correction(now.left)
                depth_correction(now.right)

        def _delete_(key1, now) -> bst.node or None:
            # Hibbard deletion algorithm
            if now is None:
                return None
            if key1 < now.key:
                now.left = _delete_(key1, now.left)
            elif key1 > now.key:
                now.right = _delete_(key1, now.right)
            else:
                # atmost one child is present
                if now.left is None:
                    if now.right is not None:
                        now.right.depth -= 1
                    return now.right
                elif now.right is None:
                    now.left.depth -= 1
                    return now.left
                # but if both children are present, replace it with min(now.right)
                if now.right.left is None:
                    # when minkey(now.right) is now.right itself
                    now.right.left = now.left
                    now = now.right
                    now.depth -= 1
                    depth_correction(now.right)
                else:
                    temp = now
                    prev = now
                    now = now.right
                    while now.left is not None:
                        prev = now
                        prev.sz -= 1
                        now = now.left
                    prev.left = now.right
                    depth_correction(prev.left)
                    now.left = temp.left
                    now.right = temp.right
                    now.depth = temp.depth
            now.sz = 1 + self.size(now.left) + self.size(now.right)
            return now
        self.root = _delete_(key, self.root)

    def minkey(self):
        now = self.root
        while now.left is not None:
            now = now.left
        return now.value

    def maxkey(self):
        now = self.root
        while now.right is not None:
            now = now.right
        return now.value

    def size(self, now: node = 'root'):
        if now == 'root':
            now = self.root
        elif now is None:
            return 0
        return now.sz

    def contains(self, key):
        if self.get(key):
            return True
        else:
            return False

    def isEmpty(self):
        return self.root is None

    def keys(self):
        def travel(now):
            if now is not None:
                key_set.append(now.key)
                travel(now.left)
                travel(now.right)

        key_set = []
        travel(self.root)
        return iter(key_set)

    def select(self, key):
        now = self.root
        while now is not None:
            if key < now.key:
                now = now.left
            elif key > now.key:
                now = now.right
            else:
                return now
        return None

    def reset(self):
        self.root = None


if __name__ == "__main__":
    import pygame as pg
    from random import randint
    from time import sleep

    def message(text):
        font = pg.font.SysFont(None, 60)
        txt_surface = font.render(text, True, (20, 150, 50))
        txt_box = txt_surface.get_rect()
        txt_box.center = (50, 30)
        image_layer.blit(txt_surface, txt_box)

    def project_loop():
        myTree = bst()
        myTree.put(600, 'ROOT')
        circles = [(600, 0)]
        lines = []
        pause = False
        while True:
            image_layer.fill((180, 250, 200))
            for points in lines:
                pg.draw.line(image_layer, (20, 80, 50), points[0], points[1], 2)
            for center in circles:
                pg.draw.circle(image_layer, (200, 20, 50), center, 4)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # for system-exit
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    pause = not pause
            if not pause:
                key = randint(50, 1150)
                myTree.put_n_draw(key, 'NODE', lines, circles)
                message(str(key))
            pg.display.update()
            if not pause:
                sleep(0.3)

    pg.init()  # initiate PYGAME ...
    clock = pg.time.Clock()
    pg.mixer.init()  # music initiation
    audio = pg.mixer.music
    audio.load(r'C:\Users\USER9\PycharmProjects\Recent\mario.mpeg')
    audio.play(-1)
    audio.set_volume(0.3)
    display_window = pg.display  # getting the background display,other layers of images
    image_layer = display_window.set_mode((1200, 700))
    display_window.set_caption("GRID PATH")
    project_loop()
