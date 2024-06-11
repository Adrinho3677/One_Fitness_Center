// Função para alternar os modos do body padrão para o CSS dark-mode
function toggleTheme() {
    const body = document.body;
    const icon = document.getElementById('clique');
    let currentTheme;

    // Verifica se no body tem uma classe CSS chamada 'dark-mode'
    if (body.classList.contains('dark-mode')) {
        // Se encontrar essa classe a função irá remover a classe e salvar a palavra light na variável currentTheme
        body.classList.remove('dark-mode');
        icon.src = '../static/lua-removebg-preview.png';
        currentTheme = 'light';
    } else {
        // Se a função não encontrar a classe dark-mode ela irá adicionar o CSS dark-mode e salvar a palavra dark na variável currentTheme
        body.classList.add('dark-mode');
        currentTheme = 'dark';
        icon.src = '../static/sol-removebg-preview.png';
    }
    
    // Feito isso ele irá salvar no localStorage() do navegador um Item chamado theme com o valor da variável currentTheme
    // localStorage é um tipo de cache que fica salvo no navegador, é utilizado para salvar informações de forma permanente
    // ao contrário do cache que salva apenas temporariamente
    localStorage.setItem('theme', currentTheme);
}

// Função para carregar o tema salvo no localStorage() sempre que carregar a página
function loadTheme() {
    const body = document.body;
    // Acessa o localStorage e salva o valor de theme dentro da variável savedTheme
    const savedTheme = localStorage.getItem('theme');

    // Se o valor encontrado for exatamente igual a 'dark' a função adiciona o CSS dark-mode ao body do HTML
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
    } else {
        // Se o valor encontrado não for 'dark' a função irá remover o CSS dark-mode do body do HTML
        body.classList.remove('dark-mode');
    }
}

// Chamar a função loadTheme para rodar todas as vezes que recarregar a página
window.onload = loadTheme;
