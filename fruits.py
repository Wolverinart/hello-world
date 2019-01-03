class Fruit :
    def __init__(self) :
        pass

class Pomme(Fruit):
    """
    Cette classe représente une pomme.
    """
    Mangeurs = ["Jacques", "Nicolas","Virgile"]
    
    def __init__(self, couleur):
        """
        Pour construire une Pomme, donnez sa couleur.
        """
        Fruit.__init__(self)
        self._couleur = couleur
    
    def couleur(self):
        """
        Retourne la couleur de la Pomme.
        """
        return self._couleur
    
    def comestible(self, mangeur):
        """
        Dit si la pomme est comestible ou non,
        en fonction du mangeur.
        """
        if mangeur in self.Mangeurs:
            print(mangeur, "mange des pommes")
        else:
            print (mangeur, "n'aime pas les pommes")

petitePomme = Pomme("verte")
petitePomme.comestible("Pierre")      # Pierre n'aime pas les pommes
petitePomme.comestible("Nicolas")     # Nicolas mange des pommes

