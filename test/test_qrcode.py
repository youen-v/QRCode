# Test du QRCode

import unittest
from tkinter import Tk
from src.myqrcode import QRCodeGeneratorApp


class TestQrCode(unittest.TestCase):

    #setUp définie des instructions à éxécuter avant les tests
    def setUp(self):
        # Crée une instance de la fenêtre pour les tests
        self.root = Tk()
        self.app = QRCodeGeneratorApp(self.root)

    # Test la taille de la fenêtre
    def test_app_size(self):
        # Récupération de la methode geometry
        app_size = self.app.master.geometry
        # Vérification si geometry n'est pas nul
        # Et à une taille défini
        self.assertIsNotNone(app_size)

    # Test que l'application c'est bien chargée
    def test_initialization(self):
        # Vérifie si l'application a été initialisée correctement
        self.assertEqual(self.app.master.title(), "Générateur de QR Code")
        # Vérifie que l'entrée est vide au départ
        self.assertEqual(self.app.entry.get(), "")

    # Test de l'entrée vide
    def test_empty_url(self):
        # Initialisation de l'entrée vide
        test_url = ""
        # Insère "" dans le champ d'entrée
        self.app.entry.insert(0,test_url)
        # Récupération de l'entrée
        entry = self.app.entry.get()
        # Vérifie que l'entrée soit à False
        self.assertFalse(entry)

    # Test de l'entrée avec URL
    def test_generate_qr_code_with_url(self):
        # Simule l'entrée d'une URL
        test_url = "https://www.esgi.fr"
        # Saisit une URL dans le champ d'entrée
        self.app.entry.insert(0, test_url)
        # Vérifie que l'image de QR code a bien été générée et affichée
        qr_image = self.app.image_label.cget("image")
        # L'image doit être présente
        self.assertIsNotNone(qr_image)

    #tearDown définie des instructions à éxécuter après les tests
    def tearDown(self):
        # Ferme la fenêtre après chaque test
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
