def vstupy_a_vystupy(vstupni_cesta, vystupni_cesta):
    with open (vstupni_cesta, encoding = "utf-8") as vstup, \
        open(vystupni_cesta, "w", encoding = "utf-8") as vystup:
        for radek in vstup:
            radek = radek.strip()
            if not radek:
                continue

            jmeno, vek, pohlavi, zvire, datum, hodnoceni = radek.split("#")
            
            if zvire == "ano":
                jeZvire = True
                zvire = "je zvire"

            else:
                jeZvire = False
                zvire = "neni zvire"

            hodnoceni = float(hodnoceni)

            if hodnoceni > 2.5:
                vystup.write(f"jmeno: {jmeno}\tvek: {vek}\tpohlavi: {pohlavi}\t{zvire}\tposledni promitani: {datum}\thodnoceni: {hodnoceni}\n")

            else:
                print(f"postava {jmeno} nebyla dost oblibena")


if __name__ == "__main__":
    vstupy_a_vystupy("data/postavy.txt", "data/oblibene-postavy.txt")