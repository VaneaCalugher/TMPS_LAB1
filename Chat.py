from datetime import datetime
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

#Mesage
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
#Chatrom
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

#Chatservice
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

#Instante
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
