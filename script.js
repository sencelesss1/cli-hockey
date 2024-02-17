async function loadHockeyMatches() {
  try {
    const response = await fetch('/api/hockey/matches');
    const matches = await response.json();

    const matchContainer = document.getElementById('match-container');
    matches.forEach(match => {
      const matchElement = document.createElement('div');
      matchElement.textContent = `${match.homeTeam} vs ${match.awayTeam}, Дата: ${match.date}`;
      matchContainer.appendChild(matchElement);
    });
  } catch (error) {
    console.error('Ошибка при получении матчей:', error);
  }
}

// Загрузка матчей после загрузки страницы
document.addEventListener('DOMContentLoaded', loadHockeyMatches);