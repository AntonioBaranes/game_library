// document.getElementById("searchButton").onclick = function() {
//     let game = document.getElementById("searchbar").value;
//     document.getElementById("searchbar").value = "";
//     console.log(game);
// }

async function fetchGames(consoleName) {
    const response = await fetch(`http://localhost:8000/games/${consoleName}`);
    if (response.ok) {
        console.log(`${consoleName.toUpperCase()} games fetched successfully`);

        const games = await response.json();
        const window = document.getElementById("consoleLibrary");
        window.innerHTML = ""; // Clear previous content

        const displaying = document.getElementById("curr_displaying");
        displaying.innerHTML = `Displaying ${consoleName.toUpperCase()} games`;

        games.forEach(game => {
            console.log(`Game: ${game.title}, img_url: ${game.img_url}`);
            const gameItem = document.createElement("div");
            gameItem.classList.add("console");
            gameItem.innerHTML = `
                <img src="${game.img_url}" alt ="${game.title} cover image" id="game_image">
                <h3>${game.title}</h3>
                <p>Release Date: ${game.release_year}</p>
                <p>Genre: ${game.genre}</p>
                <p>Developer: ${game.publisher}</p>
            `;
            window.appendChild(gameItem);
        });
    } else {
        console.log(response.statusText);
    }
}

// Bind the function to multiple buttons
document.getElementById("snes").onclick = () => fetchGames("snes");
document.getElementById("ps2").onclick = () => fetchGames("ps2");
document.getElementById("n64").onclick = () => fetchGames("n64");
document.getElementById("ps1").onclick = () => fetchGames("ps1");



