let currentImageIndex = 0;
        const images = [
            'sustentabilidadeimg1.png',
            'servicosimg2.png',
            'tecnologiaimg1.png',
            'sustentabilidadeimg2.png',
            'servicosimg3.png',
            'tecnologiaimg2.png',
        ];

        function changeImages() {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            const imageBoxes = document.querySelectorAll('.image-box img');
            imageBoxes.forEach((box, index) => {
                box.src = images[(currentImageIndex + index) % images.length];
            });
        }

        setInterval(changeImages, 3000);

        function showContent(section) {
            const modalOverlay = document.getElementById('modal-overlay');
            const contentSections = document.querySelectorAll('.content-section');
        
            // Oculta todas as seções de conteúdo
            contentSections.forEach((sectionContent) => {
                sectionContent.style.display = 'none';
            });
        
            // Exibe a seção de conteúdo alvo
            const targetSection = document.getElementById(section);
            if (targetSection) {
                targetSection.style.display = 'block';
            }
        
            // Adiciona a classe para exibir o modal com animação
            modalOverlay.classList.add('show');
        }
        
        function closeModal() {
            const modalOverlay = document.getElementById('modal-overlay');
            // Remove a classe para ocultar o modal
            modalOverlay.classList.remove('show');
        }
        
        // Configuração do modal para fechar ao clicar fora da janela
        window.addEventListener('click', (event) => {
            const modalOverlay = document.getElementById('modal-overlay');
            if (event.target === modalOverlay) {
                closeModal();
            }
        });
        
        // Configuração para adicionar animação ao modal
        const modalContent = document.querySelector('.modal-content');
        
        // Adiciona um efeito tecnológico brilhante na prte de cima da janela
        modalContent.insertAdjacentHTML(
            'beforeend',
            `<div class="glowing-bar"></div>`
        );
        
        // CSS animação de barra barra brilhante
        const glowingBarStyles = document.createElement('style');
        glowingBarStyles.innerHTML = `
            .glowing-bar {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 5px;
                background: linear-gradient(90deg, #4caf50, #2196f3, #ff9800);
                animation: glowing-bar-animation 3s infinite linear;
            }

            @keyframes glowing-bar-animation {
                0% {
                    background-position: 0 0;
                }
                100% {
                    background-position: 100% 0;
                }
            }
        `;
        document.head.appendChild(glowingBarStyles);

        // Atualiza o ano automaticamente no rodapé
document.addEventListener("DOMContentLoaded", () => {
    const currentYear = new Date().getFullYear(); // Obtém o ano atual
    document.getElementById("current-year").textContent = currentYear; // Insere o ano no rodapé
});
