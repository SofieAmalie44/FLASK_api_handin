# FLASK API HANDIN

Dette repository indeholder et projekt som implementerer et REST API med Flask, hvor der bliver håndteret studenterens information, herunder integration med GitHub for at hente offentlige repositories for hver student baseret på deres GitHub-brugernavn. Repositoriet indeholder to forskellige databaser hvor den ene arbejdes der med members og den anden fokusere på students.

## Funktioner

- **CRUD Operationer**: Opretter, læser, Opdatere og sletter studentposter.
- **GitHub Integration**: Fetch og display offentlige repositories for hver student via deres GitHub-brugernavn.
- **API Endpoints**: Understøtter flere HTTP-metoder, herunder GET, POST, PUT, PATCH og DELETE.

## Endpoints

### 1. Hent alle studerende
- **URL**: `/students`
- **Metode**: `GET`
- **Beskrivelse**: Returnerer en liste over alle studerende.

### 2. Hent en specifik student efter ID
- **URL**: `/students/<id>`
- **Metode**: `GET`
- **Beskrivelse**: Returnerer oplysninger om en student baseret på deres ID.

### 3. Opret en ny medlem
- **URL**: `/members`
- **Metode**: `POST`
- **Beskrivelse**: Opretter en ny member og tilføjer dem til databasen.

### 4. Opdater en students GitHub-brugernavn
- **URL**: `/students/<id>`
- **Metode**: `PUT`
- **Beskrivelse**: Opdaterer GitHub-brugernavnet for en student baseret på ID.

### 5. Hent en students GitHub repositories
- **URL**: `/students/repos`
- **Metode**: `GET`
- **Beskrivelse**: Henter en liste over offentlige GitHub-repositories for hver student.

## Installation

1. Klon repository:

   ```bash
   git clone https://github.com/SofieAmalie44/FLASK_api_handin.git
   ```

   Eller: 

    ```
        -> Open VSCode 
        -> Explorer 
        -> Clone Repository 
        -> paste in "https://github.com/SofieAmalie44/FLASK_api_handin.git" 
        -> Select repository destination. 
    ```

## Konfiguration

1. Installer nødvendige Python-pakker:
- Flask (web framework)
- Requests (API-anmodninger til GitHub)
- SQLite3 (database)
- dotenv (miljøvariabler)

Kør kommandoen:

```bash
pip install flask requests python-dotenv
```
2. Kørsel af databasen:
- Hvis du bruger SQLite som database, er det nødvendigt for, at filen students.db er oprettet.
- Brug en SQLite viewer som DB Browser for SQLite til at se databasen bedre.

3. Kør applikationen
```bash
flask run
```

4. Test med Postman
- Test API'erne via Postman ved at sende HTTP-anmodninger til porten med en vilkårlig route

## Forbedringer

1. Bedre forklaring af virtual environment (python -m venv venv).

2. Database setup kunne fylde en hel sektion af readme filen, så initializing og database viewer kunne være nemmere.

3. Error handling kunne godt have en smule mere præcist iforhold til fx en dårlig api request.

## Fun Fact

Hvis man lige pludselig ender i en situation hvor postman eller din browser ikke hvil udføre simple api request som er testet og virker, så er det hølest sandsynligt fordi du har nået det hourly request limit. Det er et github rate limit som har til formål at beskytte din github, men det kan være en smule eerie når man ikke ved hvorfor. For at løse problemet kan man genererer en github token som overrider rate limit problemet.

# Husk
Slet din personal token efter brug eller før du pusher til git, da det kan blive et security problem :)

