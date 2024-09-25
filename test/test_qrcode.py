import unittest
from tkinter import Tk
from src.qrcode import QRCodeGeneratorApp
import qrcode

class TestQrCode(unittest.TestCase):

    def setUp(self):
        # Crée une instance de la fenêtre Tkinter pour les tests
        self.root = Tk()
        self.app = QRCodeGeneratorApp(self.root)

    def test_initialization(self):
        # Vérifie si l'application a été initialisée correctement
        self.assertEqual(self.app.master.title(), "Générateur de QR Code")
        self.assertEqual(self.app.entry.get(), "")  # Vérifie que l'entrée est vide au départ

    def test_generate_qr_code_with_url(self):
        # Simule l'entrée d'une URL et la génération du QR code
        test_url = "https://www.esgi.fr"
        self.app.entry.insert(0, test_url)  # Saisit une URL dans le champ d'entrée
        self.app.generate_qr_code()
        # Vérifie que l'image de QR code a bien été générée et affichée
        qr_image = self.app.image_label.cget("image")
        self.assertIsNotNone(qr_image)  # L'image doit être présente
        # Pour aller plus loin, on peut vérifier que le contenu du QR code est correct
        # Pour cela, on doit utiliser la bibliothèque `qrcode` pour générer un QR code équivalent
        expected_qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        expected_qr.add_data(test_url)
        expected_qr.make(fit=True)
        expected_img = expected_qr.make_image(fill_color="black", back_color="white")
        self.assertIsNotNone(expected_img)  # Vérifie que l'image attendue est bien générée

    def tearDown(self):
        # Ferme la fenêtre après chaque test
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
