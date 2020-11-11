import nike as Nike
import config as Config
import threading

if __name__ == "__main__":
    try:
        sacai = threading.Thread(target=Nike.launch, args=(Config.ITEM_URL1,))
        sacai.start()
        jordan = threading.Thread(target=Nike.launch, args=Config.ITEM_URL2)
        jordan.start()
        sacai.join()
        jordan.join()
    except:
        print("Error in threading")