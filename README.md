Topic: SOLID Principles
Author: Calugher Ion
SOLID este un set de cinci principii de proiectare orientate pe obiecte menite să facă proiectele de software mai ușor de întreținut, mai flexibile și mai ușor de înțeles. Acronimul reprezintă principiul responsabilității unice, principiul deschis-închis, principiul substituției Liskov, principiul segregației interfeței și principiul inversării dependenței. Fiecare principiu abordează un aspect specific al proiectării software, cum ar fi organizarea responsabilităților, gestionarea dependențelor și proiectarea interfețelor. Urmând aceste principii, dezvoltatorii de software pot crea cod mai modular, testabil și reutilizabil, care este mai ușor de modificat și extins în timp. Aceste principii sunt acceptate și adoptate pe scară largă în comunitatea de dezvoltare software și pot fi aplicate oricărui limbaj de programare orientat pe obiecte.

Pentru a respecta principiile SOLID într-un proiect, trebuie să urmăm următoarele principii de bază:
1.	Single Responsibility Principle (SRP) - o clasă ar trebui să aibă o singură responsabilitate.
2.	Open-Closed Principle (OCP) - o clasă ar trebui să fie deschisă pentru extensie, dar închisă pentru modificare.
3.	Liskov Substitution Principle (LSP) - un obiect de tipul unei clase de bază ar trebui să poată fi înlocuit cu un obiect de tipul unei clase derivate.
4.	Interface Segregation Principle (ISP) - interfețele ar trebui să fie mici și specifice contextului lor.
5.	Dependency Inversion Principle (DIP) - clasele de nivel superior nu ar trebui să depindă de clasele de nivel inferior; ambele ar trebui să depindă de abstracții.

Pentru a demonstra cum se respectă aceste principii SOLID, am creat un proiect simplu în Python care utilizează aceste principii. Am creat o aplicație de tipul chat, care să permită utilizatorilor să se conecteze și să trimită mesaje între ei.

Am început prin crearea a 4 clase: User, Message, ChatRoom și ChatService.

1.	User - Această clasă va reprezenta un utilizator. Clasa va avea o singură responsabilitate, de a stoca datele utilizatorului (nume, adresa de e-mail, parola etc.) și de a oferi metode de acces și manipulare a acestor date.
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def set_name(self, name):
        self.name = name
        
    def set_email(self, email):
        self.email = email
        
    def set_password(self, password):
        self.password = password
        
    def get_name(self):
        return self.name
        
    def get_email(self):
        return self.email
        
    def get_password(self):
        return self.password

2.	Message - Această clasă va reprezenta un mesaj trimis între utilizatori. Clasa va avea o singură responsabilitate, de a stoca datele mesajului (textul mesajului, data și ora trimiterii etc.) și de a oferi metode de acces și manipulare a acestor date.

class Message:
    def __init__(self, sender, receiver, text, timestamp):
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.timestamp = timestamp
        
    def set_sender(self, sender):
        self.sender = sender
        
    def set_receiver(self, receiver):
        self.receiver = receiver
        
    def set_text(self, text):
        self.text = text
        
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
        
    def get_sender(self):
        return self.sender
        
    def get_receiver(self):
        return self.receiver
        
    def get_text(self):
        return self.text
        
    def get_timestamp(self):
        return self.timestamp

3.	ChatRoom - Această clasă va reprezenta o cameră de chat. Clasa va fi deschisă pentru extensie și închisă pentru modificare, permițând adăugarea de noi funcționalități fără a fi necesară modificarea codului existent. Clasa va conține o listă de utilizatori care au acces la camera de chat și o listă de mesaje trimise în cameră.

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []
        
    def add_user(self, user):
        self.users.append(user)
        
    def remove_user(self, user):
        self.users.remove(user)
        
    def get_users(self):
        return self.users
        
    def add_message(self, message):
        self.messages.append(message)
        
    def get_messages(self):
        return self.messages

4.	ChatService - Această clasă va oferi funcționalități pentru gestionarea camerelor de chat și trimiterea de mesaje între utilizatori. Clasa va depinde de interfețe și va fi deschisă pentru extensie, permițând adăugarea de noi camere de chat și metode de trimitere a mesajelor fără a fi necesară modificarea codului existent.

class ChatService:
    def __init__(self):
        self.rooms = []
        
    def add_room(self, room):
        self.rooms.append(room)
        
    def remove_room(self, room):
        self.rooms.remove(room)
        
    def get_rooms(self):
        return self.rooms
        
    def send_message(self, message):
        for room in self.rooms:
            if message.receiver in room.get_users() and message.sender in room.get_users():
                room.add_message(message)

Această implementare respectă principiul SRP, deoarece fiecare clasă are o singură responsabilitate clar definită. De asemenea, respectă principiul OCP, deoarece clasa ChatRoom este deschisă pentru extensie, dar închisă pentru modificare. Clasa ChatService respectă principiul ISP, deoarece folosește interfețe pentru a permite extensibilitatea și respectă principiul DIP, deoarece depinde de abstracții (interfețe) și nu de implementări specifice (clase concrete).

Pentru a testa acest proiect, am creat câteva instanțe de utilizatori, camere de chat și mesaje, și să le-am gestionat prin intermediul serviciului de chat.

# Creare utilizatori
user1 = User("Alice", "alice@example.com", "password123")
user2 = User("Bob", "bob@example.com", "password456")
user3 = User("Charlie", "charlie@example.com", "password789")

# Creare camere de chat
room1 = ChatRoom("Room 1")
room1.add_user(user1)
room1.add_user(user2)

room2 = ChatRoom("Room 2")
room2.add_user(user2)
room2.add_user(user3)

# Adăugare camere de chat la serviciul de chat
chat_service = ChatService()
chat_service.add_room(room1)
chat_service.add_room(room2)

# Trimitere mesaj între utilizatori
message = Message(user1, user2, "Salut, Bob!", datetime.now())
chat_service.send_message(message)

# Afișare mesaje din cameră
for message in room1.get_messages():
    print(f"{message.sender.name}: {message.text} ({message.timestamp})")

Acest cod va itera prin lista de mesaje din camera de chat 1 și va afișa fiecare mesaj, împreună cu numele expeditorului, textul mesajului și marcajul de timp al mesajului.


Acest cod creează trei utilizatori și două camere de chat, adaugă utilizatorii în camerele de chat și camerele de chat la serviciul de chat. Apoi, trimite un mesaj de la utilizatorul 1 către utilizatorul 2 și afișează mesajele din camera de chat 1.


