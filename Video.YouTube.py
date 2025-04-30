class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"відтворення відео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_index):
        if 0 <= video_index < len(cls.videos):
            cls.videos[video_index].play()


# Приклад використання:
video1 = Video()
video2 = Video()
video1.create("Основи програмування")
video2.create("Вивчення Python за 45 хвилин!")

YouTube.add_video(video1)
YouTube.add_video(video2)

YouTube.play(0)  # Виведе: відтворення відео Основи програмування
YouTube.play(1)  # Виведе: відтворення відео Вивчення Python за 45 хвилин!
