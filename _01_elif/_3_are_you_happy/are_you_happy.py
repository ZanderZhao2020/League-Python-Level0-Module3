from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    Window = Tk()
    Window.withdraw()
    def AskBoolean(Prompt):
        while True:
            Input = simpledialog.askstring("Prompt", Prompt + " (y/n)").lower()
            if Input == "yes" or Input == "y":
                return True
            elif Input == "no" or Input == "n":
                return False
            else:
                messagebox.showinfo("Message", "Enter y, n, yes, or no")
    if AskBoolean("Are you happy?"):
        messagebox.showinfo("Message", "Keep doing what you're doing.")
    else:
        if AskBoolean("Do you want to be happy?"):
            messagebox.showinfo("Message", "Change something.")
        else:
            messagebox.showinfo("Message", "Keep doing what you're doing")
    pass
