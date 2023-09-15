import guilde as gd
import multiprocessing

if __name__ == "__main__":
    app = gd.Guide()
    multiprocessing.freeze_support()
    app.run()
    