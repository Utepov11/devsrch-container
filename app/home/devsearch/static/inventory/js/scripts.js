document.addEventListener('DOMContentLoaded', () => {
    const deviceTypeSelect = document.getElementById('deviceType');
    const computerForm = document.getElementById('computerForm');
    const printerForm = document.getElementById('printerForm');

    deviceTypeSelect.addEventListener('change', () => {
        const selectedType = deviceTypeSelect.value;

        // Скрываем обе формы
        computerForm.classList.add('hidden');
        printerForm.classList.add('hidden');

        // Показываем нужную форму
        if (selectedType === 'computer') {
            computerForm.classList.remove('hidden');
        } else if (selectedType === 'printer') {
            printerForm.classList.remove('hidden');
        }
    });
});