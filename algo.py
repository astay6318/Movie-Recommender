import tkinter as tk
import pickle
import bz2
import _pickle as cPickle


with open('movie_list.pkl', 'rb') as f:
    df = pickle.load(f)

with open('final_prediction_list.pkl', 'rb') as f:
    final_prediction_list = pickle.load(f)

def recommend(movie,n=5):
    try:
        index = df[df['original_title'] == movie.lower()].index[0]
        for i in range(n):
            moive_index=final_prediction_list[index][i]
            print(df['original_title'][moive_index])
            # first_label.config(text=df['original_title'][moive_index])
    except Exception as e:
        print(e)
        print("Movie Not in Database")

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Your first App')
        first_label = tk.Label(self, text = "I'm a cool App!!", font=10)
        first_label.pack(padx = 3, pady = 3)
        first_button = tk.Button(self, text ="Recommend", command = hello)
        first_button.pack(padx= 5, pady = 5)
        Application.first_entry = tk.Entry(self, width = 30)
        Application.first_entry.pack(padx = 7, pady = 7)
def hello():
    x = Application.first_entry.get()
    recommend(str(x))
app = Application()
app.mainloop()