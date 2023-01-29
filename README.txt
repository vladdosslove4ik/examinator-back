Testy:
    - Zmienne obiektów i obiekty: formsApi/base/models.py
    - główny link: http://127.0.0.1:8002/
    - wszystkie zapytania dodawane do głównego linku: formsApi/api/urls.py
    - Przykład tworzenia testu: front/post.html (odpowiednio z plikiem post.js)
    - Przykład dostawania konkretnego testu(z pytaniami i odp): front/get.html (odpowiednio z plikiem get.js)

Użytkownicy:
    - Zmienne obiektów i obiekty: usersApi/base/models.py
    - główny link: http://127.0.0.1:8001/
    - wszystkie zapytania dodawane do głównego linku: usersApi/api/urls.py
    - wszystkie linki co mają w sobie detail służą do detali(edycji, usuwania i dostawania detali),
    jeśli masz użyć detail to puść geta pod jakiś link z detil i dostaniesz wszystkie dane.
    Reszty nie ma co używać bo nie mamy czasu się w to bawić więc nie będę nawet wyjaśniał.

W razie w:
    1. W plikach urls.py linki są mapowane na funkcje z plików (formsApi lub usersApi)/api/views.py
    więc w razie czego tam można sobie wyszukać tych funkcji.
    2. W pliku (formsApi lub usersApi)/base/tests.py są testy pokazujące dane wrzucane w postach do danych
    funckji jakby było trzbea można tam zerknąć
    3. Pisz jak to nic nie pomoże