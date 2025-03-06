from django.test import TestCase
from .models import User, Computer, Printer
from datetime import date

class DevicesModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_create_computer(self):
        computer = Computer.objects.create(
            computer_type='Моноблок',
            computer_inventory='000012345',
            computer_snumber='SN12345',
            computer_location='Склад',
            computer_date=date.today(),
            computer_author=self.user
        )
        self.assertEqual(Computer.objects.count(), 1)
        self.assertEqual(computer.computer_inventory, '000012345')
        self.assertEqual(computer.computer_type, 'Моноблок')
        self.assertEqual(computer.computer_author.username, 'testuser')

    def test_delete_computer(self):
        computer = Computer.objects.all()
        computer.delete()

    def test_create_printer(self):
        printer = Printer.objects.create(
            printer_type='МФУ HP LaserJet Pro M1536dnf',
            printer_inventory='000045123',
            printer_snumber='SN45123',
            printer_location='Склад',
            printer_date=date.today(),
            printer_author=self.user
        )
        self.assertEqual(Printer.objects.count(), 1)
        self.assertEqual(printer.printer_inventory, '000045123')
        self.assertEqual(printer.printer_type, 'МФУ HP LaserJet Pro M1536dnf')
        self.assertEqual(printer.printer_author.username, 'testuser')

    def test_delete_printer(self):
        computer = Computer.objects.all()
        computer.delete()
