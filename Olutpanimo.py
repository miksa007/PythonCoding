def kysely():
    lkm = input("Syötä mittausten lukumäärä: ")
    lkm = int(lkm)
    ok = 0
    eiok = 0
    tosi = 0
    i = 0

    if lkm <= 0:
        print("Mittausten lukumäärän tulee olla positiivinen kokonaisluku.")
    else:
        while i<lkm:
            tulos = input("Syötä {:1d}. mittaustulos: ".format((i + 1)))
            tulos = int(tulos)
            if 20 <= tulos and tulos <= 25:
                ok = ok + 1
                tosi = 0
            else:
                if tosi:
                    print("Viinisi on pilalla.")
                    i = lkm+100
                else:
                    tosi = 1
                    eiok = eiok + 1

            i = i + 1
def main():
    kysely()
main()