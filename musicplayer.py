import os
from pygame import mixer

def get_music_files(directory):  # sourcery skip: for-append-to-extend
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                music_files.append(os.path.join(root, file))
    return music_files

def play_music(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

def main():
    music_directory = 'C:\\Users\\lvign\\OneDrive\\music'  # Double backslashes or use raw string literal
    music_files = get_music_files(music_directory)

    if len(music_files) == 0:
        print("No music files found in the specified directory.")
        return

    print("Welcome to the Music Player!")
    print("Available songs:")
    for i, file in enumerate(music_files):
        print(f"{i+1}. {os.path.basename(file)}")

    while True:
        try:
            choice = int(input("Enter the song number to play (0 to quit): "))
            if choice == 0:
                break
            elif choice < 1 or choice > len(music_files):
                print("Invalid choice. Please try again.")
            else:
                selected_file = music_files[choice - 1]
                print(f"Now playing: {os.path.basename(selected_file)}")
                play_music(selected_file)
        except ValueError:
            print("Invalid input. Please enter a number.")

    mixer.music.stop()
    mixer.quit()
    print("Thank you for using the Music Player!")

if __name__ == '__main__':
    main()
