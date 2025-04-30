class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    def __init__(self):
        self.apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        if app in self.apps:
            self.apps.remove(app)

    def block_application(self, app):
        if app in self.apps:
            app.blocked = True

    def total_apps(self):
        return len(self.apps)


# Приклад використання:
store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.total_apps())  # Виведе: 1
store.block_application(app_youtube)
print(app_youtube.blocked)  # Виведе: True
store.remove_application(app_youtube)
print(store.total_apps())  # Виведе: 0
