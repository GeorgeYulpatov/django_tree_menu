// Функция для изменения размера изображения в зависимости от ширины окна
function resizeImage() {
    const image = document.getElementById('menuImage');
    const windowWidth = window.innerWidth;

    // Устанавливаем ширину изображения как 25% от ширины окна (увеличенный коэффициент)
    const newWidth = windowWidth * 0.25;

    // Ограничение максимальной и минимальной ширины изображения
    const minWidth = 150; // Минимальная ширина в пикселях (увеличена)
    const maxWidth = 700; // Максимальная ширина в пикселях (увеличена)

    // Применяем новое значение ширины, но не меньше минимального и не больше максимального
    image.style.width = Math.min(Math.max(newWidth, minWidth), maxWidth) + 'px';
}

// При загрузке страницы и изменении размера окна вызываем функцию
window.addEventListener('resize', resizeImage);
window.addEventListener('load', resizeImage);