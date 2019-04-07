
import collections
import math

from PIL import Image, ImageDraw
colors = ((255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255))
im = Image.new("RGB", (100, 100), color="black")  # keret
draw = ImageDraw.Draw(im)
draw.rectangle([(2,2),(97,97)], fill ="white")  # háttér


class ErasztotenészSzitája:

    def __init__(self):
        self.n = 1
        self.köv_összetett = collections.defaultdict(list)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            self.n += 1
            n = self.n
            prímosztók = self.köv_összetett.get(n)
            if prímosztók is None:
                p = n  # csak jelzem, hogy n prím
                self.köv_összetett[n+p].append(p)
                return n
            else:
                for p in prímosztók:
                    self.köv_összetett[n+p].append(p)
                del self.köv_összetett[n]


szita = ErasztotenészSzitája()
p = next(szita)

oszlopok, sorok = 91, 90


tökéletes_számok = (6, 28, 496, 8128,)
barátságos_számok = (220,284, 1184,1210, 2620,2924, 5020,5564, 6232,6368, 10744,10856)


korábbi_n = set()  # biztonsági okokból
for y in range(sorok):
    for x in range(oszlopok):
        n = oszlopok * y + x
        négyzetgyök_n = math.sqrt(n)
        if n in korábbi_n:
            raise Exception()
        korábbi_n.add(n)
        if n == p:
            print(f'{n},', end="")
            draw.point((x+4, y+5), fill="black")
            p = next(szita)
        elif n in tökéletes_számok:
            draw.point((x+4, y+5), fill="yellow")
        elif n in barátságos_számok:
            draw.point((x+4, y+5), fill="pink")
        elif négyzetgyök_n == round(négyzetgyök_n):  # négyzetszám
            draw.point((x+4, y+5), fill="red")
print(f' következő lenne: {p}')


im.save("me.png")