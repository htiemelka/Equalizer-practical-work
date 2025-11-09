# Импорт всех необходимых модулей
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer        # pip install pygame
import os

class MusicPlayer:
    def __init__(self):
        # Инициализация микшера
        mixer.init()
        
        # Создание главного GUI для музыкального плеера
        self.root = Tk()
        self.root.geometry('725x220')
        self.root.title('МелоМен')
        self.root.resizable(0, 0)
        
        # Цвета
        self.button_bg = "#b02020"
        self.button_fg = "#d44848"
        self.frame_bg = "#9c2c2c"
        
        # StringVar переменные
        self.current_song = StringVar(self.root, value='Не выбрана')
        self.song_status = StringVar(self.root, value='Не доступно')
        
        # Создание интерфейса
        self.create_widgets()
    
    def create_widgets(self):
        # Все фреймы
        song_frame = LabelFrame(self.root, text='Текущая песня', font=("Comic Sans MS", 9), 
                               bg=self.frame_bg, width=425, height=80)
        song_frame.place(x=0, y=0)

        button_frame = LabelFrame(self.root, text='Управление', font=("Comic Sans MS", 9), 
                                 bg=self.frame_bg, width=425, height=120)
        button_frame.place(y=80)

        listbox_frame = LabelFrame(self.root, text='Плейлист', font=("Comic Sans MS", 9), 
                                  bg=self.frame_bg)
        listbox_frame.place(x=425, y=0, height=200, width=300)

        # ListBox плейлиста
        self.playlist = Listbox(listbox_frame, font=('Comic Sans MS', 11), selectbackground='snow3')

        scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
        scroll_bar.pack(side=RIGHT, fill=BOTH)

        self.playlist.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH, padx=5, pady=5)

        # Надписи в SongFrame
        Label(song_frame, text='СЕЙЧАС ИГРАЕТ:', bg=self.frame_bg, 
              font=('Comic Sans MS', 10, 'bold')).place(x=5, y=20)

        song_lbl = Label(song_frame, textvariable=self.current_song, bg=self.button_fg, 
                        font=("Comic Sans MS", 12), width=25)
        song_lbl.place(x=130, y=20)

        # Кнопки на главном экране
        pause_btn = Button(button_frame, text='Пауза', bg=self.button_fg, 
                          font=("Comic Sans MS", 13), width=7,
                          command=self.pause_song)
        pause_btn.place(x=15, y=10)

        stop_btn = Button(button_frame, text='Стоп', bg=self.button_fg, 
                         font=("Comic Sans MS", 13), width=7,
                         command=self.stop_song)
        stop_btn.place(x=105, y=10)

        play_btn = Button(button_frame, text='Начать', bg=self.button_fg, 
                         font=("Comic Sans MS", 13), width=10,
                         command=self.play_selected_song)
        play_btn.place(x=195, y=10)

        resume_btn = Button(button_frame, text='Продолжить', bg=self.button_fg, 
                           font=("Comic Sans MS", 13), width=10,
                           command=self.resume_song)
        resume_btn.place(x=310, y=10)

        load_btn = Button(button_frame, text='Загрузить папку', bg=self.button_fg, 
                         font=("Comic Sans MS", 13), width=35, 
                         command=self.load_songs)
        load_btn.place(x=40, y=55)

        # Надпись внизу, отображающая статус музыки
        Label(self.root, textvariable=self.song_status, bg=self.button_fg, 
              font=('Comic Sans MS', 9), justify=LEFT).pack(side=BOTTOM, fill=X)
    
    def play_selected_song(self):
        selected_song = self.playlist.get(ACTIVE)
        if selected_song:
            self.current_song.set(selected_song)
            mixer.music.load(selected_song)
            mixer.music.play()
            self.song_status.set("Песня воспроизводится")
    
    def stop_song(self):
        mixer.music.stop()
        self.song_status.set("Песня остановлена")
    
    def load_songs(self):
        directory = filedialog.askdirectory(title='Выберите папку')
        if directory:
            os.chdir(directory)
            tracks = [track for track in os.listdir() 
                     if track.endswith(('.mp3', '.wav', '.ogg'))]  # Фильтрация аудиофайлов
            
            self.playlist.delete(0, END)  # Очистка текущего плейлиста
            
            for track in tracks:
                self.playlist.insert(END, track)
    
    def pause_song(self):
        mixer.music.pause()
        self.song_status.set("Песня на паузе")
    
    def resume_song(self):
        mixer.music.unpause()
        self.song_status.set("Песня воспроизводится")
    
    def run(self):
        """Запуск приложения"""
        self.root.mainloop()

# Создание и запуск музыкального плеера
if __name__ == "__main__":
    player = MusicPlayer()
    player.run()

# Завершение GUI
root.update()

root.mainloop()
