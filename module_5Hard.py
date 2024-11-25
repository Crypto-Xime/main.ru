                                            # "Classes and objects."
                                                # "Your YouTube":

import hashlib
import time

# User class to store user information
class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Store hashed password
        self.age = age

    def check_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()  # Check password hash

    def __str__(self):
        return f"User: {self.username}, Age: {self.age}"

# Video class to store video information
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0  # Start at 0 seconds
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video: {self.title}, Duration: {self.duration} sec, Adult: {self.adult_mode}"

# UrTube class for managing users and videos
class UrTube:
    def __init__(self):
        self.users = []  # List of User objects
        self.videos = []  # List of Video objects
        self.current_user = None  # The logged-in user
        self.houses_history = []  # Keeps history of usernames for testing purposes

    def log_in(self, login, password):
        # Find user by username
        user = next((u for u in self.users if u.username == login), None)
        if user and user.check_password(password):
            self.current_user = user
            print(f"Welcome, {self.current_user.username}!")
        else:
            print("Invalid username or password.")
            print("Please enter a valid username or password to continue.")

    def register(self, username, password, age):
        # Check if user already exists
        if any(u.username == username for u in self.users):
            print(f"User {username} already exists.")
            return

        user = User(username, password, age)
        self.users.append(user)
        self.current_user = user
        print(f"User {username} has been successfully registered and logged in.")

    def log_out(self):
        self.current_user = None
        print("You have been logged out.")
        print("To continue Log In.")

    def add(self, *videos):
        # Add videos to the system
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(f"Video '{video.title}' added.")
            else:
                print(f"Video '{video.title}' already exists.")

    def get_videos(self, search_word):
        # Search for videos by title
        results = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return results

    def watch_video(self, title):
        if not self.current_user:
            print("Log in to your account to watch the video")
            return

        # Find the video by title
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print(f"Video '{title}' not found")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("You are under 18 years old, please leave the page")
            return

        # Simulate watching the video
        print(f"Playing '{video.title}'")
        for second in range(1, video.duration + 1):
            time.sleep(0.1)  # Simulate the video playing with a small delay
            print(second, end=" ")
        print("\nEnd of video")

# Main execution part
if __name__ == '__main__':
    ur = UrTube()  # Create an instance of UrTube

    # Main video content (moved from before initialization)
    v1 = Video('Best Programming Language of 2024', 200)
    v2 = Video('Why do girls need a guy who is a programmer?', 10, adult_mode=True)

    while True:
        print("\nWelcome! Select one option to continue:")
        choice = int(input("1 - Login\n2 - Get Registered\n"))

        if choice == 1:
            login = input("Enter your Login: ")
            password = input("Enter your Password: ")
            ur.log_in(login, password)

            # Video search and watch after login
            print("Searching for videos with 'best' in the title:", ur.get_videos('best'))  # Searching for 'best'
            print("Searching for videos with 'PROG' in the title:", ur.get_videos('PROG'))  # Searching for 'PROG'

            # Trying to watch a video
            ur.watch_video('Why do girls need a guy who is a programmer?')

        elif choice == 2:
            username = input("Enter your Login: ")
            password = input("Enter your Password: ")
            password2 = input("Enter your Password again: ")

            if password != password2:
                print("Passwords do not match. Please try again.")
                continue

            age = int(input("Enter your age: "))
            ur.register(username, password, age)

        else:
            print("Invalid choice. Please select 1 or 2.")
