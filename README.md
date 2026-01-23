# 📚 Cloud-based Task & Project Management System
(Simplified Trello / Asana)

## 🎯 Opis projektu (можна майже 1-в-1 здати викладачу)

Aplikacja webowa umożliwiająca zarządzanie projektami i zadaniami w środowisku chmurowym. System pozwala użytkownikom tworzyć projekty, dodawać zadania, przypisywać użytkowników do zadań oraz komentować postęp prac. Całość aplikacji jest uruchamiana w kontenerach Docker za pomocą narzędzia Docker Compose.

## 🧱 Architektura aplikacji

**Typ:** Web application (cloud-ready)

## Temat projektu
Webowa aplikacja do zarządzania projektami, zadaniami i komentarzami.

## Autor
Rozehan Oleksii
Numer indeksu: 556666


## Kontenery

### 1. Web (Django)
* Backend aplikacji
* Logika biznesowa
* API / widoki HTML

### 2. Database (PostgreSQL)
* Przechowywanie danych
* Użytkownicy, projekty, zadania, komentarze

### 3. Nginx
* Reverse proxy
* Obsługa statycznych plików
* Forwardowanie ruchu HTTP do Django

## Architektura aplikacji

- Django (web)
- PostgreSQL (baza danych)
- Nginx (reverse proxy)

Aplikacja uruchamiana jest w 3 kontenerach Docker.

## Uruchomienie projektu

Wymagania:
- Docker
- Docker Compose

Uruchomienie:
docker compose up --build

## Uruchomienie całego środowiska:

```bash
docker compose up
```

1. Sklonuj repozytorium
2. Uruchom:
   docker compose up --build
3. Aplikacja dostępna pod adresem:
http://localhost
## 🧩 Funkcjonalności aplikacji (5 CRUD)

### 1️⃣ Zarządzanie użytkownikami (Users – CRUD)

* Rejestracja użytkownika
* Logowanie / wylogowanie
* Edycja profilu użytkownika
* Usuwanie konta

📦 **Tabela:** `users`

### 2️⃣ Zarządzanie projektami (Projects – CRUD)

* Tworzenie nowego projektu
* Edycja projektu
* Usuwanie projektu
* Wyświetlanie listy projektów

📦 **Tabela:** `projects`  
🔗 **Relacja:** projekt → właściciel (user)

### 3️⃣ Zarządzanie zadaniami (Tasks – CRUD)

* Dodawanie zadania do projektu
* Zmiana statusu:
  * `TODO`
  * `IN_PROGRESS`
  * `DONE`
* Edycja zadania
* Usuwanie zadania

📦 **Tabela:** `tasks`  
🔗 **Relacja:** task → project

### 4️⃣ Komentarze do zadań (Comments – CRUD)

* Dodawanie komentarza do zadania
* Edycja komentarza
* Usuwanie komentarza

📦 **Tabela:** `comments`  
🔗 **Relacja:** comment → task → user

### 5️⃣ Przypisywanie użytkowników do zadań (Assignments – CRUD)

* Przypisanie użytkownika do zadania
* Usunięcie przypisania
* Wyświetlanie listy przypisanych użytkowników

📦 **Tabela pośrednia:** `task_assignments`  
🔗 **Relacja:** Many-to-Many (users ↔ tasks)

## 🗄️ Model danych (логічно, для пояснення)

* User
* Project
* Task
* Comment
* TaskAssignment


## 🛠️ Technologie

* **Język programowania:** Python
* **Framework:** Django
* **Baza danych:** PostgreSQL
* **Konteneryzacja:** Docker, Docker Compose
* **Serwer HTTP:** Nginx

