from tkinter import *
from winotify import Notification, audio

class CustomButton:
    def __init__(self, window , text):
        self.button = Button(window, text=text)
        self.button.pack()

    def place_button(self, x, y):
        self.button.place(x=x, y=y)

class CustomLabel:
    def __init__(self, window, number):
        self.number = number
        self.label = Label(window, text=f"{self.number:02}")
        self.label.config(font=('Manospace', 50))
        self.label.pack()

    def place_label(self, x, y):
        self.label.place(x=x, y=y)

    def click_up(self):
        self.number = self.number + 1
        self.label.config(text = f"{self.number:02}")

    def click_down(self):
        if self.number == 0:
            raise Exception("Timer is already 0.")
        self.number = self.number - 1
        self.label.config(text=f"{self.number:02}")

    def config(self):
        self.label.config(text=f"{self.number:02}")

class CustomLabelInter:
    def __init__(self, window):
        self.label = Label(window, text=":")
        self.label.config(font=('Manospace', 50))
        self.label.pack()

    def place_label(self, x, y):
        self.label.place(x=x, y=y)
class CustomWindow:
    def __init__(self):
        self.seconds = 0
        self.window = Tk()
        self.window.geometry("490x450")
        self.window.title("Timer")
        self.window.config(background="black")

        self.button = CustomButton(self.window, 'Start')
        self.button.place_button(110,300)
        self.button.button.config(font=('Ink Free', 20, 'bold'))
        self.button.button.config(command=self.start)

        self.hours = CustomLabel(self.window,0)
        self.hours.place_label(100,50)

        self.temp = CustomLabelInter(self.window)
        self.temp.place_label(180,50)

        self.minutes = CustomLabel(self.window,0)
        self.minutes.place_label(200, 50)

        self.temp1 = CustomLabelInter(self.window)
        self.temp1.place_label(280, 50)

        self.seconds = CustomLabel(self.window,0)
        self.seconds.place_label(300, 50)

        try:
            image = PhotoImage(file='sageata_in_sus.png')
            self.sageata = CustomButton(self.window, '')
            self.sageata.button.config(image=image)
            self.sageata.place_button(115, 20)
            self.sageata.button.config(command=self.hours.click_up)

            self.sageata1 = CustomButton(self.window, '')
            self.sageata1.button.config(image=image)
            self.sageata1.place_button(215, 20)
            self.sageata1.button.config(command=self.minutes.click_up)

            self.sageata2 = CustomButton(self.window, '')
            self.sageata2.button.config(image=image)
            self.sageata2.place_button(315, 20)
            self.sageata2.button.config(command=self.seconds.click_up)

            image1 = PhotoImage(file='sageata_in_jos.png')
            self.sageata3 = CustomButton(self.window, '')
            self.sageata3.button.config(image=image1)
            self.sageata3.place_button(115, 135)
            self.sageata3.button.config(command=self.hours.click_down)

            self.sageata4 = CustomButton(self.window, '')
            self.sageata4.button.config(image=image1)
            self.sageata4.place_button(215, 135)
            self.sageata4.button.config(command=self.minutes.click_down)

            self.sageata5 = CustomButton(self.window, '')
            self.sageata5.button.config(image=image1)
            self.sageata5.place_button(315, 135)
            self.sageata5.button.config(command=self.seconds.click_down)
        except Exception as e:
            print(f"Error loading images: {e}")

        self.notification = Notification(app_id="Project", title = "Alarm", msg="Time expired", duration="short")
        self.notification.set_audio(audio.Default, loop=False)
        self.window.mainloop()

    def compute(self, number):
        if number >= 0:
            self.seconds.number = number % 60
            self.minutes.number = (number // 60) % 60
            self.hours.number = number // 3600



            # Update labels
            self.seconds.config()
            self.minutes.config()
            self.hours.config()

            # Schedule the compute function to be called after 1000 milliseconds (1 second)
            
            self.window.after(1000, lambda: self.compute(number - 1))
        else:
            self.notification.show()

    def start(self):
        self.seconds_num = self.hours.number * 3600 + self.minutes.number * 60 + self.seconds.number
        self.compute(self.seconds_num)



window = CustomWindow()

