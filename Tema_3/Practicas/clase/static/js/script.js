// Funcionalidad común para todas las páginas
document.addEventListener('DOMContentLoaded', function() {
    console.log('Just Eleven Game Loaded');
    
    // Animación simple para los botones
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});
