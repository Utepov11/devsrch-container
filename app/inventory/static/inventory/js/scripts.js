document.addEventListener('DOMContentLoaded', () => {
    const deviceTypeSelect = document.getElementById('deviceType');
    const computerForm = document.getElementById('computerForm');
    const printerForm = document.getElementById('printerForm');
    const accessoryForm = document.getElementById('accessoryForm');

    deviceTypeSelect.addEventListener('change', () => {
        const selectedType = deviceTypeSelect.value;

        // Скрываем обе формы
        computerForm.classList.add('hidden');
        printerForm.classList.add('hidden');
        accessoryForm.classList.add('hidden');

        // Показываем нужную форму
        if (selectedType === 'computer') {
            computerForm.classList.remove('hidden');
        } if (selectedType === 'printer') {
            printerForm.classList.remove('hidden');
        } else if (selectedType === 'accessory') {
            accessoryForm.classList.remove('hidden');
        }
    });

});
