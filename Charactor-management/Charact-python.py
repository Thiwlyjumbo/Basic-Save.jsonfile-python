from models import Mercenary, Sniper, Medic, Weapon
import json, os

def Charactor_management():
    def load():
        if os.path.exists("Charactor-obj.json"):
            try: 
                with open("Charactor-obj.json", 'r') as r:
                    return json.load(r)
            except: return []
        else: return []
    mercenary = load()
    def save(data):
        # Save current character list to Charactor.json
        with open("Charactor-obj.json", "w") as w:
            json.dump(data, w)
    def add():
        # Interface for adding a new mercenary to the guild
        class_all = ['mc', 'sn', 'md']
        rank_all = ['E', 'D', 'C', 'B', 'A', 'S']
        clas = input("Class : ").lower()
        if clas in class_all:
            name = input("Name : ")
            rank = input('Rank : ').upper()
            salary = input("Salary : ")
            if rank in rank_all:
                try:
                    salary = float(salary)
                    match clas:
                        case "mc": 
                            mc = {'class':'Mercenary', 'name':name, 'rank':rank, 'salary':salary}
                            mercenary.append(mc)
                        case "sn": 
                            distance = input("Distance of sniper : ")
                            try:
                                distance = float(distance)
                                sn = {'class':'Sniper', 'name':name, 'rank':rank, 
                                'salary':salary, 'distance':distance}
                                mercenary.append(sn)
                            except: print("can'n add please try agian..")
                        case "md": 
                            medicine = input("Medicine of medic : ")
                            try:
                                medicine = int(medicine)
                                md = {'class':'Medic', 'name':name, 'rank':rank, 
                                'salary':salary, 'medicine':medicine}
                                mercenary.append(md)
                            except: print("can'n add please try agian..")
                    save(mercenary)
                except ValueError: print("can'n add please try agian..")
            else: print(f"<{rank} this rank is not found..")
        else: print(f"<{clas}> this class can't added..")
    def name():
        # Display all names and return a list of name strings for verification
        data = []
        for i in mercenary:
            print("".center(25, "="))
            print(f"{i['name']} - class {i['class']}")
            data.append(i['name'].lower())
            print("".center(25, "="))
        return data
    def remove():
        #verify mercenary
        if mercenary:
            #show mercenary-all
            name_all = name()
            print('type <name> to remove or type <all> to remove-all...')
            m = list(map(str, input().lower().split()))
            if "all" in m:
                confirm = input('remove all data (y/n)')
                if confirm in ['y', 'n']:
                    match confirm:
                        case 'y':
                            print("remove-all...")
                            mercenary.clear()
                            save(mercenary)
                        case 'n': print("don't remove..")
                else: print("not command")
            elif any(x in name_all for x in m):
                confirm = input('confirm to remove selected name(s)? (y/n)')
                if confirm in ['y', 'n']:
                    new_data = []
                    match confirm:
                        case 'y':
                            for i in mercenary:
                                if i['name'].lower() not in m:
                                    new_data.append(i)
                            mercenary[:] = new_data
                            save(mercenary)
                        case 'n': print("don't remove..")
                else: print("not command")
            else: print("data not found..")
        else: print("not data please add..")
    
    def promote_show(i, mode):
        # Unified function to convert dictionary data back into Objects
        # mode 'show' calls show_info(), mode 'promote' calls promote()
        mc = None
        # Reconstruct the correct class object based on data
        match i["class"]:
            case "Mercenary":
                mc = Mercenary(i['name'], i['rank'], i['salary'])
            case "Sniper":
                mc = Sniper(i['name'], i['rank'], i['salary'], i['distance'])
            case "Medic":
                mc = Medic(i['name'], i['rank'], i['salary'], i['medicine'])
        # Reload weapon object if exists
        if i.get('weapon'):
            wp = Weapon(i['weapon']['name'], i['weapon']['damage'])
            mc.weapon = wp
        # return data
        if mode == 'show': return mc.show_info()
        elif mode == 'promote': return mc.promote()

    def show():
        if mercenary:
            name_all = name()
            print('type <name> to show_info or type <all> to show_all...')
            m = list(map(str, input().lower().split()))
            if "all" in m:
                for i in mercenary:
                    promote_show(i, 'show')
            elif any(x in name_all for x in m):
                for i in mercenary:
                    if i['name'].lower() in m:
                        promote_show(i, 'show')
            else: print("data not found..")
        else: print("not data please add..")

    def promote():
        # verify mercenary-all
        if mercenary:
            #show mercenary-all
            name_all = name()
            print('type <name> to promote(name) or type <all> to promote-all...')
            # input
            m = list(map(str, input().lower().split()))
            # promote-all
            if "all" in m:
                confirm = input('promote all ? (y/n)')
                if confirm in ['y', 'n']:
                    match confirm:
                        case 'y':
                            new_data = []
                            for i in mercenary:
                                new_data.append(promote_show(i, 'promote'))
                            mercenary[:] = new_data
                            save(mercenary)
                            print("promote-all...")
                        case 'n': print("don't promote..")
                else: print("not command")
            # promote-some-name
            elif any(x in name_all for x in m):
                confirm = input('confirm to promote selected name(s)? (y/n)')
                if confirm in ['y', 'n']:
                    match confirm:
                        case 'y':
                            new_data = []
                            for i in mercenary:
                                if i['name'].lower() in m:
                                    new_data.append(promote_show(i, 'promote'))
                                else: new_data.append(i)
                            mercenary[:] = new_data
                            save(mercenary)
                        case 'n': print("don't promote..")
                else: print("not command")
            else: print("data not found..")
        else: print("not data please add..")
    
    def equip():
        if mercenary:
            name_all = name()
            confirm = input('confirm to equip selected name(s)? (y/n) ')
            if confirm in ['y', 'n']:
                match confirm:
                    case 'y':
                        name_to_equip = input('name to equip selected : ').lower()
                        if name_to_equip in name_all:
                            for i in mercenary:
                                if i['name'].lower() == name_to_equip:
                                    wp_name = input('name of weapon : ')
                                    wp_damage = input('damage of weapon : ')
                                    try:
                                        wp_damage = int(wp_damage)
                                        data = {'name':wp_name, 'damage':wp_damage}
                                        i['weapon'] = data
                                        save(mercenary)
                                    except ValueError: print("Value Error..")
                        else: print(f"<{name_to_equip}> this name is not found..")
                    case 'n': print("don't equip..")
            else: print('not command..')

    def unequip():
        if mercenary:
            name_all = name()
            confirm = input('confirm to unequip selected name(s)? (y/n) ')
            if confirm in ['y', 'n']:
                match confirm:
                    case 'y':
                        name_unequip = input('name to unequip selected : ').lower()
                        if name_unequip in name_all:
                            for i in mercenary:
                                if i['name'].lower() == name_unequip:
                                    i['weapon'] = None
                                    print('unquip...')
                        else: print(f"<{name_unequip}> this name is not found..")
                    case 'n': print("don't unequip..")
            else: print('not command..')
    exit = False
    while not exit:
        mode = ['add', 'show', 'remove', 'promote', 'equip', 'unequip', 'exit']
        m = input('Mode : ').lower()
        if m in mode:
            match m:
                case "add": add()
                case "show": show()
                case "remove": remove()
                case "promote": promote()
                case "equip": equip()
                case "unequip": unequip()
                case "exit": 
                    exit = True
                    print("power of ...")
        else: print("not command..")
Charactor_management()
