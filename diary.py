import json, os, datetime
def diary():
    def load():
        if os.path.exists("diary.txt"):
            try: 
                with open("diary.txt", "r") as r:
                    return json.load(r)
            except: return []
        else: return []
    data = load()
    now = datetime.datetime.now().strftime("%Y-%m-%d // %H:%M:%S // ")
    def save(data):
        with open("diary.txt", "w") as w:
            json.dump(data, w)
    
    def add_note(note):
        data.append({"time":now, "note":note})
        save(data)
    def show_note():
        if data:
            print("all note".center(25, "-"))
            for note in data:
                print(note["time"], note["note"])
            print("end".center(25, "-")
    def clear_all():
        data = []
        print("clear data...")
        save(data)
    exit = False
    while not exit:
        print("type add, show, clear, exit")
        mode = input("mode : ").lower()
        if mode not in ["add", "show", "clear", "exit"]: print("not command...")
        match mode:
            case "add": add_note(input("note : "))
            case "show": show_note()
            case "clear": clear_all()
            case "exit": exit = True
diary()
