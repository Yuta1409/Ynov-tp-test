import unittest
from fonctions import additionner,est_pair, valider_email, calculer_moyenne, convertir_temperature

class TestFonctions(unittest.TestCase):

    def test_additionner_cas_positif(self):
        """Test addition avec nombres positifs"""
        resultat = additionner(2, 3)
        self.assertEqual(resultat, 5)

    def test_additionner_cas_negatif(self):
        """Test addition avec nombres négatifs"""
        resultat = additionner(-2, -3)
        self.assertEqual(resultat, -5)

    def test_est_pair_nombre_pair(self):
        """Test avec un nombre pair"""
        self.assertTrue(est_pair(4))

    def test_est_pair_nombre_impair(self):
        """Test avec un nombre impair"""
        self.assertFalse(est_pair(5))
        
    def test_est_pair_zero(self):
        """Test avec le nombre zéro"""
        self.assertTrue(est_pair(0))
                                      
    def test_valider_email_valide(self):
        """Test validation d'un email valide"""
        self.assertTrue(valider_email("test@example.com"))
    
    def test_valider_email_sans_arobase(self):
        """Test validation d'un email sans arobase"""
        self.assertFalse(valider_email("testexample.com"))
        
    def test_valider_email_sans_point(self):
        """Test validation d'un email sans point"""
        self.assertFalse(valider_email("test@example"))  
        
    def test_calculer_moyenne_liste_normale(self):
        """Test calcul de moyenne avec une liste normale"""
        notes = [10, 15, 20]
        self.assertEqual(calculer_moyenne(notes), 15)
                                      
    def test_calculer_moyenne_liste_vide(self):
        """Test calcul de moyenne avec une liste vide"""
        notes = []
        self.assertEqual(calculer_moyenne(notes), 0)
        
    def test_calculer_moyenne_une_note(self):
        """Test calcul de moyenne avec une seule note"""
        notes = [18]
        self.assertEqual(calculer_moyenne(notes), 18)
        
    def test_convertir_temperature_zero(self):
        """Test conversion de 0°C = en 32°F"""
        self.assertEqual(convertir_temperature(0), 32)
        
    def test_convertir_temperature_eau_bouillante(self):
        """Test conversion de 100°C en 212°F"""
        self.assertEqual(convertir_temperature(100), 212)
        
    # def test_additionner_erreur(self):
    #     """Test additionner avec une erreur volontaire"""
    #     resultat = additionner_erreur(2, 3)
    #     self.assertEqual(resultat, 5)

# Permet d'exécuter les tests
if __name__ == '__main__':
    unittest.main(),
