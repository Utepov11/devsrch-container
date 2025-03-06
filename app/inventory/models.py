from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils.text import slugify

# Модель для компьютеров
class Computer(models.Model):
    '''ПК и ноутбуки'''
    computer_id = models.AutoField(primary_key=True)
    ComputerType = [
        ('Компьютер настольный', 'Компьютер настольный'),
        ('Компьютер HP P3500MT', 'Компьютер HP P3500MT'),
        ('Компьютер HP Pro 3500MT QB294EA с монитором', 'Компьютер HP Pro 3500MT QB294EA с монитором'),
        ('Моноблок HP P3520', 'Моноблок HP P3520'),
        ('Нетбук Prestigio MultiPad Wize 3341 3G', 'Нетбук Prestigio MultiPad Wize 3341 3G'),
        ('Ноутбук B6M12EA HP Probook 4540s', 'Ноутбук B6M12EA HP Probook 4540s'),
        ('Ноутбук LENOVO G500', 'Ноутбук LENOVO G500'),
        ('Ноутбук LENOVO', 'Ноутбук LENOVO'),
        ('Ноутбук для XDCAM Камкордеров', 'Ноутбук для XDCAM Камкордеров'),
        ('Рабочая станция HP ProDesk 400 с монитором HP Pro', 'Рабочая станция HP ProDesk 400 с монитором HP Pro'),
        ('Системный блок HP Pavilion 500-129er', 'Системный блок HP Pavilion 500-129er'),
        ('Системный блок Apple', 'Системный блок Apple'),
        ('Монитор Аpple', 'Монитор Аpple'),
        ('19-дюймовый монитор ПК', '19-дюймовый монитор ПК'),
        ('Монитор Acer/G236HLBbd/23', 'Монитор Acer/G236HLBbd/23'),
        ('Монитор HP Z23i23-Inch IPS Monitor D7Q13A4', 'Монитор HP Z23i23-Inch IPS Monitor D7Q13A4'),
    ]
    computer_type = models.CharField("Тип компьютера", choices=ComputerType, max_length=100)
    computer_inventory = models.CharField("Инвентарный номер", max_length=9)
    computer_snumber = models.CharField("Серийный номер", max_length=50, blank=True, null=True)
    computer_location = models.CharField("Расположение", max_length=50)
    computer_date = models.DateField("Дата добавления", default=date.today)
    slug = models.SlugField(max_length=9, unique=True, db_index=True, verbose_name="URL", blank=True)
    computer_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='computers')
   
    def __str__(self):
        return self.computer_inventory
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.computer_inventory)  # генерируем slug на основе computer_inventory
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'ПК и ноутбук'
        verbose_name_plural = 'ПК и ноутбуки'

# Модель для принтеров и сканеров
class Printer(models.Model):
    '''Принтеры и сканеры'''
    printers_id = models.AutoField(primary_key=True)
    PrinterType = [
        ('МФУ HP LaserJet 1536dnf', 'МФУ HP LaserJet 1536dnf'),
        ('МФУ HP LaserJet Pro M225dn', 'МФУ HP LaserJet Pro M225dn'),
        ('Принтер HP LaserJet Pro P1606n', 'Принтер HP LaserJet Pro P1606n'),
        ('МФУ HP Laser Jet Pro M426fdn', 'МФУ HP Laser Jet Pro M426fdn'),
        ('Принтер HP Color LaserJet CP5225dn', 'Принтер HP Color LaserJet CP5225dn'),
        ('МФУ HP LaserJet Pro4103fdn', 'МФУ HP LaserJet Pro4103fdn'),
        ('МФУ HP LaserJet M443nda', 'МФУ HP LaserJet M443nda'),
        ('Canon МФУ IR2520, 3796B003AC', 'Canon МФУ IR2520, 3796B003AC'),
        ('Принтер Epson Stylus L1300 Color', 'Принтер Epson Stylus L1300 Color'),
        ('Принтер этикеток TSP TTP-244CE', 'Принтер этикеток TSP TTP-244CE'),
        ('МФУ Canon IR2530i', 'МФУ Canon IR2530i'),
        ('Лазерный факс Panasonic KX-FL423RU-B', 'Лазерный факс Panasonic KX-FL423RU-B'),
        ('Сканер Plustek Smart Office PL 806. A4', 'Сканер Plustek Smart Office PL 806. A4'),
        ('Canon МФУ IR2520', 'Canon МФУ IR2520')
    ]
    printer_type = models.CharField("Наименование устройства", choices=PrinterType, max_length=150)
    printer_inventory = models.CharField("Инвентарный номер", max_length=9)
    printer_snumber = models.CharField("Серийный номер", max_length=50, blank=True, null=True)
    printer_location = models.CharField("Расположение", max_length=50)
    printer_date = models.DateField("Дата добавления", default=date.today)
    slug = models.SlugField(max_length=9, unique=True, db_index=True, verbose_name="URL", blank=True)
    printer_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='printers')

    def __str__(self):
        return self.printer_inventory
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.printer_inventory)  # генерируем slug на основе printer_inventory
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Принтер и сканер'
        verbose_name_plural = 'Принтеры и сканеры'

# Модель для периферии
class Accessory(models.Model):
    '''Периферия'''
    accessory_id = models.AutoField(primary_key=True)
    accessory_type = models.CharField("Наименование устройства", max_length=100)
    accessory_inventory = models.CharField("Инвентарный номер", max_length=9)
    accessory_snumber = models.CharField("Серийный номер", max_length=50, blank=True, null=True)
    accessory_location = models.CharField("Расположение", max_length=50)
    accessory_date = models.DateField("Дата добавления", default=date.today)
    slug = models.SlugField(max_length=9, unique=True, db_index=True, verbose_name="URL", blank=True)
    accessory_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accessories')

    def __str__(self):
        return self.accessory_inventory
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.accessory_inventory)  # генерируем slug на основе printer_inventory
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Периферия'
        verbose_name_plural = 'Периферия'

# Модель для сохранения отчётов
class ReportLog(models.Model):
    '''Сохранение отчётов'''
    report_name = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.FileField(upload_to='reports/')

    def __str__(self):
        return f"{self.report_name} ({self.generated_at})"