class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# ---------
# Constants
# ---------
csv_columns = ['German','English','Type','Attributes']
parts_of_speech = ["Noun","Verb","Adjective","Adverb","Conjunction","Preposition","Phrase"]
umlautBut = ["uUmlautButton","aUmlautButton","oUmlautButton","sUmlautButton"]
umlauts = ["ü","ä","ö","ß"]
pron = ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'sie/Sie']
genders = ['der', 'die', 'das']
gr_columns = ["Group","Users"]

def constantManual():
    print('csv_columns')
    print(csv_columns)
    print('parts_of_speech')
    print(parts_of_speech)
    print('umlautBut')
    print(umlautBut)
    print('umlauts')
    print(umlauts)
    print('pron')
    print(pron)
    print('genders')
    print(genders)
    print('gr_columns')
    print(gr_columns)

f1 = ["setColor", "to_list", "my_groups", "add_user_to_group", "create_group", "set_default_file", "significant_characters"]
f2 = ["make_mask", "conjugate_weak", "conjugate_strong", "get_size", "change_column", "change_in_file", "change_database"]
f3 = ["overwrite", "overwrite_gr", "read_iterative", "get_quantity_f", "search_in_buffer", "search", "unequalRand"]

def funcManual(s):
    if s == "setColor":
        print(color.BOLD + "setColor(r, g, b)" + color.END)
        print("\tFunction sets Gdk.Color having rgb value.")
    elif s == "to_list":
        print(color.BOLD + "to_list(s)" + color.END)
        print("\t Function that converts string representation of list with string values in it to an actual list.")
        print("\t\tExample: ")
        print("\t\t\tto_list('['" + "Have a good', 'day!'])")
        print("\t\tThis makes a list with 2 string values in it")
    elif s == "my_groups":
        print(color.BOLD + "my_groups(userName)" + color.END)
        print("\t Function, that returns names of groups in which 'userName' is involved.")
        print("\t\tExample: ")
        print("\t\t\tmy_groups('Kittie')")
        print("\t\tThis puts list of my groups into global variable " + color.UNDERLINE + "myGroups" + color.END)
    elif s == "add_user_to_group":
        print(color.BOLD + "add_user_to_group(groupName, userName)" + color.END)
        print("\t Function, that adds user 'userName' to group 'groupName'")
        print("\t\tExample: ")
        print("\t\t\tadd_user_to_group('Group of blood', 'sleeve')")
        print("\t\tThis adds user 'sleeve' to group 'Group of blood'")
    elif s == "create_group":
        print(color.BOLD + "create_group (groupName, userName)" + color.END)
        print("\t Function, that creates a group 'groupName' and adds user 'userName' to it")
        print("\t\tExample: ")
        print("\t\t\tcreate_group('Group of blood', 'sleeve')")
        print("\t\tThis adds user 'sleeve' to newly created group 'Group of blood'")
    elif s == "set_default_file":
        print(color.BOLD + "set_default_file(file)" + color.END)
        print("\t Function, that sets file 'file' which contents some user database to default database")
        print("\t\tExample: ")
        print("\t\t\tset_default_file('hello.csv')")
        print("\t\tThis will copy containts of 'default.csv' to 'hello.csv'")
    elif s == "significant_characters":
        print(color.BOLD + "significant_characters(s)" + color.END)
        print("\t Function, that gets list with indices of chars in string other than '.', ' ', ',' and '!'")
        print("\t\tExample: ")
        print("\t\t\tsignificant_characters('Hello, guys!')")
        print("\t\tThis will return a list: [0, 1, 2, 3, 4, 7, 8, 9, 10]")
    elif s == "make_mask":
        print(color.BOLD + "make_mask(s)" + color.END)
        print("\t Function, that makes mask out of string, seting random 2/3 of significant symbols to '*'")
        print("\t\tExample: ")
        print("\t\t\tmake_mask('Hey!')")
        print("\t\tThis may return for example a string: 'H**!'")
    elif s == "conjugate_weak":
        print(color.BOLD + "conjugate_weak(verb)" + color.END)
        print("\t Function, that makes a prediction on what conjugation of this verb could look like.")
        print("\t\tExample: ")
        print("\t\t\tconjugate_weak('lesen')")
        print("\t\tThis will return dictionary with conjugation of 'lesen', d['ich'] = 'lese' ... ")
    elif s == "conjugate_strong":
        print(color.BOLD + "conjugate_strong(verb, option)" + color.END)
        print("\t Function, that makes a prediction on what conjugation of this verb could look like.")
        print("\t\tExample: ")
        print("\t\t\tconjugate_strong('fahren')")
        print("\t\tThis will return dictionary with conjugation of 'lesen', d['ich'] = 'fahre' ... ")
    elif s == "get_size":
        print(color.BOLD + "get_size(fileName)" + color.END)
        print("\t Function, that sets global variable " + color.UNDERLINE + "fileSize" + color.END)
        print("Name of current user file should be passed.Sizes of groups of current user included")
        print("\t\tExample: ")
        print("\t\t\tget_size('admin.csv')")
        print("\t\tThis will set fileSize to size of 'admin.csv' + sizes of groups in which 'admin' is involved.")
    elif s == "change_column":
        print(color.BOLD + "change_column (dict, column, containts)" + color.END)
        print("\t Function, that changes a field 'column' in deep copy of dictionary 'dict' to 'containts'")
        print("\t\tExample: ")
        print("\t\t\tchange_column(d, 'Name', 'Smith')")
        print("\t\tThis will return a deep copy of dictionary d where 'Name' is set to 'Smith'")
    elif s == "change_in_file":
        print(color.BOLD + "change_in_file(fileName, f, chg)" + color.END)
        print("\t Function, that changes file according to rules:")
        print("\t 'f' takes one argument which is row of csv-dictionary file. ex: f(row)")
        print("\t 'f' returns: 0 if nothing should be changed, 1 if row should be changed with 'chg', 2 if row should be deleted")
        print("\t\tExample: ")
        print("\t\t\tf = lambda x: 1 if x['Name'] == 'Smith' else 0")
        print("\t\t\tt = lambda x: change_column(x, column, containts)")
        print("\t\t\tchange_in_file('user.csv', f, t)")
    elif s == "change_database":
        print(color.BOLD + "change_database (f, column, containts)" + color.END)
        print("\t Function, that changes file according to rules:")
        print("\t 'f' takes one argument which is row of csv-dictionary file. ex: f(row)")
        print("\t 'f' returns: 0 if nothing should be changed, 1 if row should be changed according to rule row[column] = containts")
        print(", 2 if row should be deleted")
        print("\t\tExample: ")
        print("\t\t\tf = lambda x: 1 if x['Name'] == 'Smith' else 0")
        print("\t\t\tchange_database(f, 'Name', 'Jackson')")
    elif s == "overwrite":
        print(color.BOLD + "overwrite(fileName, dict_data, how)" + color.END)
        print("\t Function, that writes dict_data to 'fileName' with option 'how' which is either 'a' or 'w'")
        print("\t\tExample: ")
        print("\t\t\toverwrite('x.csv', dict_data, 'a')")
        print("\t\tThis will append dict_data to the end of csv-dictionary 'x.csv'")
    elif s == "overwrite_gr":
        print(color.BOLD + "overwrite_gr(fileName, dict_data, how, userName)" + color.END)
        print("\t Function, that writes dict_data to 'fileName' with option 'how' which is either 'a' or 'w'")
        print("\t It changes accuracy for 'userName' according to dict_data and sets it to '0/4'")
        print("\t\tExample: ")
        print("\t\t\toverwrite('cats.csv', dict_data, 'a', 'munchkin')")
        print("\t\tThis will append dict_data to the end of csv-dictionary 'cats.csv'")
    elif s == "read_iterative":
        print(color.BOLD + "read_iterative(fileNm)" + color.END)
        print("\t Function, whic is virtual reader. It is a generator which reads user's file and group files as")
        print("\t if they were appended to the end of user's file")
        print("\t\tExample: ")
        print("\t\t\tfor x in read_iterative('admin.csv'):")
        print("\t\t\t\tprint ('new')")
        print("\t\t\t\tfor key in x.keys():")
        print("\t\t\t\t\tprint(key, x[key])")
        print("\t\tThis will print all contents of 'admin.csv' and files of groups in which 'admin' is involved.")
    elif s == "get_quantity_f":
        print(color.BOLD + "get_quantity_f(f)" + color.END)
        print("\t Function, that gets quantity of rows on which f(row) == True'")
        print("\t\tExample: ")
        print("\t\t\tf = lambda x: x['Type'] == 'Noun'")
        print("\t\t\tget_quantity_f(f)")
        print("\t\tThis will return a deep copy of dictionary d where 'Name' is set to 'Smith'")
    elif s == "search_in_buffer":
        print(color.BOLD + "search_in_buffer(word, key)" + color.END)
        print("\t Function, that searches word in buffer")
        print("\t\tExample: ")
        print("\t\t\tsearch_in_buffer('Danke.', 'German')")
        print("\t\tThis will search a record where field 'German' == 'Danke'")
    elif s == "search":
        print(color.BOLD + "search(fileName, word, key)" + color.END)
        print("\t Function, that searches word in buffer and than in database")
        print("\t\tExample: ")
        print("\t\t\tt = search('x.csv', 'Smith', 'Name')")
        print("\t\t\tif t:")
        print("\t\t\t\tfor key in t.keys():")
        print("\t\t\t\t\tprint(key, t[key])")
        print("\t\t\telse:")
        print("\t\t\t\tprint('Not found')")
    elif s == "unequalRand":
        print(color.BOLD + "search(fileName, word, key)" + color.END)
        print("\t Gets random records from buffer, other from this")
        print("\t\tExample: ")
        print("\t\t\tunequalRand('Hier, bitte', 'German')")
    else:
        print("ERROR!")

c1 = ["DictBuffer", "fBuffer", "PartBuffer", "VerbConjugation", "OpenedWord", "SimpleTraining", "GenderTraining"]
c2 = ["MatchTraining", "Dictionary", "NewWord", "FindWord", "AddGroup", "CreateGroup", "CheckMyGroups", "Main"]


class DictBuffer:
    def __init__(self, bound):
        global fileName
        self.bound = copy.deepcopy(bound)
        i = 0
        self.list = []
        self.file = fileName
        for word in read_iterative(self.file):
            if i >= bound[0] and i < bound[1]:
                self.list.append(word)
            i += 1
        self.bound[0] = min(0, self.bound[0])
        self.bound[1] = self.bound[0] + len(self.list)

class fBuffer:
    def __init__(self, bound, f):
        self.bound = copy.deepcopy(bound)
        i = 0
        self.list = []
        global fileName
        for word in read_iterative(fileName):
            if f(word):
                if i >= bound[0] and i < bound[1]:
                    self.list.append(word)
                i += 1
        self.bound[0] = min(0, self.bound[0])
        self.bound[1] = self.bound[0] + len(self.list)
             
#is redundant
class PartBuffer:
    def __init__(self, bound, part):
        x = fBuffer(bound, lambda x: x["Type"] == part)
        self.bound = x.bound
        self.list = x.list

class VerbConjugation:
    def __init__(self, strongFlag, x, t, buff, dict_data):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        self.opt = "ie"
        self.word = x

        if strongFlag == 0:
            d = conjugate_weak(self.word["German"])
            self.builder.get_object(pron[0] + "C").set_text(d[pron[0]])
            self.builder.get_object(pron[1] + "C").set_text(d[pron[1]])
            self.builder.get_object(pron[2][:2] + "C").set_text(d[pron[2]])
            self.builder.get_object(pron[3] + "C").set_text(d[pron[3]])
            self.builder.get_object(pron[4] + "C").set_text(d[pron[4]])
            self.builder.get_object(pron[5][:3] + "C").set_text(d[pron[5]])
        else:
            d = conjugate_strong(self.word["German"], self.opt)
            self.builder.get_object(pron[0] + "C").set_text(d[pron[0]])
            self.builder.get_object(pron[1] + "C").set_text(d[pron[1]])
            self.builder.get_object(pron[2][:2] + "C").set_text(d[pron[2]])
            self.builder.get_object(pron[3] + "C").set_text(d[pron[3]])
            self.builder.get_object(pron[4] + "C").set_text(d[pron[4]])
            self.builder.get_object(pron[5][:3] + "C").set_text(d[pron[5]])

        reMix = self.builder.get_object("verbConjugationButtonRedo")
        reMix.connect("clicked", self.change_entry)
        if strongFlag == 0:
            reMix.hide()

        pushButton = self.builder.get_object("verbConjugationButtonPush")
        pushButton.connect("clicked", self.push, t, buff, dict_data)

        webButton = self.builder.get_object("verbConjugationButtonWebSearch")
        webButton.connect("clicked", self.open_web)

        window = self.builder.get_object("verbConjugation")
        window.connect("delete-event", self.on_destroy)
        window.show()

    def open_web(self, widget):
        webbrowser.open("https://conjugator.reverso.net/conjugation-german-verb-"+self.word["German"]+".html")
    
    def change_entry(self, widget):
        if self.opt == "ie":
            self.opt = "i"
        else:
            self.opt = "ie"
        d = conjugate_strong(self.word["German"], self.opt)
        self.builder.get_object(pron[0] + "C").set_text(d[pron[0]])
        self.builder.get_object(pron[1] + "C").set_text(d[pron[1]])
        self.builder.get_object(pron[2][:2] + "C").set_text(d[pron[2]])
        self.builder.get_object(pron[3] + "C").set_text(d[pron[3]])
        self.builder.get_object(pron[4] + "C").set_text(d[pron[4]])
        self.builder.get_object(pron[5][:3] + "C").set_text(d[pron[5]])

    def push(self, widget, t, buff, dd):
        s = str()
        s = s + self.builder.get_object(pron[0] + "C").get_text()
        s = s + " " + self.builder.get_object(pron[1] + "C").get_text()
        s = s + " " + self.builder.get_object(pron[2][:2] + "C").get_text()
        s = s + " " + self.builder.get_object(pron[3] + "C").get_text()
        s = s + " " + self.builder.get_object(pron[4] + "C").get_text()
        s = s + " " + self.builder.get_object(pron[5][:3] + "C").get_text()
        self.word['Attributes'] = self.word['Attributes'] + " " + s
        if 3 in self.grToggled:
            dd.append(word)
            t.remove(3)
        for x in t:
            buff[x].append(word)
        self.builder.get_object("verbConjugation").destroy()

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

class OpenedWord:
    def __init__(self, x):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        #self.builder.get_object("openWordButtonCollAdd").connect("clicked", self.translate)
        self.builder.get_object("openWordButtonTrAdd").connect("clicked", self.add_to_training, x)

        self.get_attr(x["Attributes"])
        self.builder.get_object("openWordLabelGerman").set_text(x["German"])
        self.builder.get_object("openWordLabelEnglish").set_text(x["English"])
        self.builder.get_object("openWordLabelPart").set_text(x["Type"])

        window = self.builder.get_object("openWord")
        window.connect("delete-event", self.on_destroy)
        window.show()
    
    def add_to_training(self, widget, x):
        global curTraining
        f = True
        for i in curTraining:
            if (x["German"] == i["German"] and x["English"] == i["English"]):
                f = False
                break
        if f:
            curTraining.append(copy.deepcopy(x))

    def get_attr(self, x):
        y = x.split()
        val = list(map(int, y[0].split("/")))
        acc = 0.0
        if val[1] == 0:
            if val[0] != 0:
                acc = 1.0
        else:
            acc = float(val[0]) / (val[0] + val[1])
        self.builder.get_object("openWordBarProgress").set_fraction(acc)
        genL = self.builder.get_object("openWordLabelGender")
        if (y[1] == "n"):
            genL.set_markup ("<span foreground='green' weight='bold' font='14'>n</span>")
        elif (y[1] == "m"): 
            genL.set_markup ("<span foreground='blue' weight='bold' font='14'>m</span>")
        elif (y[1] == "f"):
            genL.set_markup ("<span foreground='red' weight='bold' font='14'>f</span>")
        else:
            genL.hide()

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

class SimpleTraining:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        self.which = dict()
        self.lang = "German"

        self.builder.get_object("simpleTrButtonCheck").connect("clicked", self.check)
        self.builder.get_object("simpleTrButtonNew").connect("clicked", self.new)
        self.builder.get_object("simpleTrButtonQuestion").connect("clicked", self.question)
        self.builder.get_object("simpleTrButtonHint").connect("clicked", self.hint)

        self.builder.get_object(umlautBut[0] + "2").connect("clicked", self.add_umlaut, 0)
        self.builder.get_object(umlautBut[1] + "2").connect("clicked", self.add_umlaut, 1)
        self.builder.get_object(umlautBut[2] + "2").connect("clicked", self.add_umlaut, 2)
        self.builder.get_object(umlautBut[3] + "2").connect("clicked", self.add_umlaut, 3)

        window = self.builder.get_object("simpleTraining")
        window.connect("delete-event", self.on_destroy)
        window.show()
    
    def hint(self, widget):
        self.which["Attributes"] = copy.deepcopy(self.set_attr(self.which["Attributes"], False))
        f = lambda x: 1 if x["German"] == self.which["German"] and x["English"] == self.which["English"] else 0
        change_database(f, "Attributes", self.which["Attributes"])
        if self.lang == "German":
            self.builder.get_object("simpleTrEntryEnglish").set_text(make_mask(self.which["English"]))
        else:
            self.builder.get_object("simpleTrEntryGerman").set_text(make_mask(self.which["German"]))

    def question(self, widget):
        OpenedWord(copy.deepcopy(self.which))
        self.which["Attributes"] = copy.deepcopy(self.set_attr(self.which["Attributes"], False))
        f = lambda x: 1 if x["German"] == self.which["German"] and x["English"] == self.which["English"] else 0
        change_database(f, "Attributes", self.which["Attributes"])
        self.builder.get_object("simpleTrEntryGerman").set_text(str())
        self.builder.get_object("simpleTrEntryEnglish").set_text(str())
        self.builder.get_object("simpleTrLabelAttributes").set_text(str())

    def add_umlaut(self, widget, case):
        german = self.builder.get_object("simpleTrEntryGerman")
        german.set_text(german.get_text() + umlauts[case])

    def set_attr(self, attributes, correct):
        s = str()
        y = attributes.split()
        val = list(map(int, y[0].split("/")))
        if correct:
            val[0] += 1
        else:
            val[1] += 1
        s = str(val[0]) + "/" + str(val[1])
        i = False
        for t in y:
            if i:
                s = s + ' ' + t
            else:
                i = True
        return s
    
    def get_attr(self, attributes):
        s = str()
        y = attributes.split()
        val = list(map(int, y[0].split("/")))
        acc = 0.0
        if val[1] == 0:
            if val[0] != 0:
                acc = 1.0
        else:
            acc = float(val[0]) / (val[0] + val[1])
        s = "Accuracy: " + str(int(acc * 100)) + "%"
        if y[1] != '-':
            s = s + "\nGender: " + y[1]
        return s

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

    def new(self, widget):
        global trainingSwitch
        global buffer
        self.builder.get_object("simpleTrEntryGerman").set_text(str())
        self.builder.get_object("simpleTrEntryEnglish").set_text(str())
        self.builder.get_object("simpleTrLabelAttributes").set_text(str())
        if trainingSwitch:
            if random() < 0.03:
                newBound = int(random() * (fileSize - 100))
                buffer = DictBuffer([newBound, newBound + 100])
            if random() < 0.33:
                self.lang = "German"
                self.which = buffer.list[int(len(buffer.list)*random())]
                self.builder.get_object("simpleTrEntryGerman").set_text(self.which["German"])
            else:
                self.lang = "English"
                self.which = buffer.list[int(len(buffer.list)*random())]
                self.builder.get_object("simpleTrEntryEnglish").set_text(self.which["English"])
        else:
            if random() < 0.33:
                self.lang = "German"
                self.which = curTraining[int(len(curTraining)*random())]
                self.builder.get_object("simpleTrEntryGerman").set_text(self.which["German"])
            else:
                self.lang = "English"
                self.which = curTraining[int(len(curTraining)*random())]
                self.builder.get_object("simpleTrEntryEnglish").set_text(self.which["English"])

    def check(self, widget):
        global fileSize
        german = self.builder.get_object("simpleTrEntryGerman")
        english = self.builder.get_object("simpleTrEntryEnglish")
        deText = german.get_text().strip()
        enText = english.get_text().strip()
        if self.which["German"] == deText and self.which["English"] == enText:
            attr = self.builder.get_object("simpleTrLabelAttributes")
            self.which["Attributes"] = copy.deepcopy(self.set_attr(self.which["Attributes"], True))
            attr.set_text("CORRECT!\n" + self.get_attr(self.which["Attributes"])+'\nPart of speech: '+self.which["Type"])
        else:
            attr = self.builder.get_object("simpleTrLabelAttributes")
            self.which["Attributes"] = copy.deepcopy(self.set_attr(self.which["Attributes"], False))
            attr.set_text("INCORRECT!")
        f = lambda x: 1 if x["German"] == self.which["German"] and x["English"] == self.which["English"] else 0
        change_database(f, "Attributes", self.which["Attributes"])

class GenderTraining:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        self.choice = genders[0]

        self.filter = lambda x: x["Type"] == "Noun" and x["German"][:3] in set(genders)
        self.q = get_quantity_f(self.filter) 
        self.buff = fBuffer([0, 100], self.filter)
        self.which = self.buff.list[int(random() * len(self.buff.list))]
        
        self.builder.get_object("genderTrLabelWord").set_text(self.which["German"][3:].strip())

        self.builder.get_object("genderTrEvBox0").modify_bg(Gtk.StateType.NORMAL, setColor(125*255, 211*255, 33*255))
        self.builder.get_object("genderTrEvBox1").modify_bg(Gtk.StateType.NORMAL, setColor(65*255, 141*255, 201*255))
        self.builder.get_object("genderTrEvBox2").modify_bg(Gtk.StateType.NORMAL, setColor(240*255, 202*255, 69*255))

        self.builder.get_object(genders[0]).connect("clicked", self.set_choice, genders[0])
        self.builder.get_object(genders[1]).connect("clicked", self.set_choice, genders[1])
        self.builder.get_object(genders[2]).connect("clicked", self.set_choice, genders[2])

        window = self.builder.get_object("genderTraining")
        window.connect("delete-event", self.on_destroy)
        window.show()

    def set_choice(self, widget, x):
        self.choice = x
        self.check()
        Gdk.flush()
        GLib.timeout_add(1500, self.set_new)

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

    def set_new(self):
        global buffer
        self.builder.get_object("genderTrLabelAttributes").set_text(str())
        if random() < 0.03:
            newBound = int(random() * (max(0, self.q - 100)))
            self.buff = fBuffer([newBound, newBound + 100], self.filter)
        self.which = self.buff.list[int(random() * len(self.buff.list))]
        self.builder.get_object("genderTrLabelWord").set_text(self.which["German"][3:].strip())
        self.builder.get_object("genderTrEvBox3").modify_bg(Gtk.StateType.NORMAL, setColor(255*255, 255*255, 255*255))

    def check(self):
        if self.choice == self.which["German"][:3]:
            self.which["Attributes"] = self.set_attr(self.which["Attributes"], True)
            self.builder.get_object("genderTrEvBox3").modify_bg(Gtk.StateType.NORMAL, setColor(0, 255*255, 0))
            self.builder.get_object("genderTrLabelAttributes").set_text("CORRECT!\n")
        else:
            self.which["Attributes"] = self.set_attr(self.which["Attributes"], False)
            self.builder.get_object("genderTrEvBox3").modify_bg(Gtk.StateType.NORMAL, setColor(255*255, 0, 0))
            self.builder.get_object("genderTrLabelAttributes").set_text("INCORRECT!")
        f = lambda x: 1 if x["German"] == self.which["German"] and x["English"] == self.which["English"] else 0
        change_database(f, "Attributes", self.which["Attributes"])
    
    def set_attr(self, x, cor):
        s = str()
        y = x.split()
        val = list(map(int, y[0].split("/")))
        if cor:
            val[0] += 1
        else:
            val[1] += 1
        s = str(val[0]) + "/" + str(val[1])
        i = False
        for t in y:
            if i:
                s = s + ' ' + t
            else:
                i = True
        return s

class MatchTraining:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        self.which = dict()
        self.choice = 0
        self.correct = 0

        global buffer
        self.which = buffer.list[int(random() * len(buffer.list))]
        self.builder.get_object("matchTrLabelWord").set_text(self.which["German"].strip())

        self.builder.get_object("matchTrEvBox4").modify_bg(Gtk.StateType.NORMAL, Gdk.Color(red=125 * 255, green=211  * 255, blue=33  * 255))
        self.builder.get_object("matchTrEvBox5").modify_bg(Gtk.StateType.NORMAL, Gdk.Color(red=65  * 255, green=141  * 255, blue=201 * 255))
        self.builder.get_object("matchTrEvBox6").modify_bg(Gtk.StateType.NORMAL, Gdk.Color(red=240 * 255, green=202 * 255, blue=69   * 255))
        self.builder.get_object("matchTrEvBox7").modify_bg(Gtk.StateType.NORMAL, Gdk.Color(red=255 * 255, green=204 * 255, blue=255   * 255))

        self.builder.get_object("matchTrButtonChoice0").connect("clicked", self.set_choice, 0)
        self.builder.get_object("matchTrButtonChoice1").connect("clicked", self.set_choice, 1)
        self.builder.get_object("matchTrButtonChoice2").connect("clicked", self.set_choice, 2)
        self.builder.get_object("matchTrButtonChoice3").connect("clicked", self.set_choice, 3)

        self.set_new()

        window = self.builder.get_object("matchTraining")
        window.connect("delete-event", self.on_destroy)
        window.show()

    def set_choice(self, widget, x):
        self.choice = x
        self.check()
        Gdk.flush()
        GLib.timeout_add(1500, self.set_new)

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

    def set_new(self):
        global buffer
        global fileSize
        self.builder.get_object("matchTrLabelResult").set_text(str())
        if random() < 0.03:
            newBound = int(random() * (max(0, fileSize - 100)))
            buffer = DictBuffer([newBound, newBound + 100])
        self.which = buffer.list[int(random() * len(buffer.list))]
        self.builder.get_object("matchTrLabelWord").set_text(self.which["German"].strip())
        self.correct = int(random() * 4)
        for i in range(4):
            if i != self.correct:
                self.builder.get_object("matchTrLabelChoice"+str(i)).set_text(unequalRand(self.which, "English").strip())
        self.builder.get_object("matchTrLabelChoice"+str(self.correct)).set_text(self.which["English"].strip())
        self.builder.get_object("matchTrEvBox8").modify_bg(Gtk.StateType.NORMAL, Gdk.Color(red=255*255, green=255*255, blue=255*255))

    def check(self):
        if self.choice == self.correct:
            self.which["Attributes"] = self.set_attr(self.which["Attributes"], True)
            self.builder.get_object("matchTrEvBox8").modify_bg(Gtk.StateType.NORMAL, setColor(0, 255*255, 0))
            self.builder.get_object("matchTrLabelResult").set_text("CORRECT!")
        else:
            self.which["Attributes"] = self.set_attr(self.which["Attributes"], False)
            self.builder.get_object("matchTrEvBox8").modify_bg(Gtk.StateType.NORMAL, setColor(255*255, 0, 0))
            self.builder.get_object("matchTrLabelResult").set_text("INCORRECT!")
        f = lambda x: 1 if x["German"] == self.which["German"] and x["English"] == self.which["English"] else 0
        change_database(f, "Attributes", self.which["Attributes"])
    
    def set_attr(self, x, cor):
        s = str()
        y = x.split()
        val = list(map(int, y[0].split("/")))
        if cor:
            val[0] += 1
        else:
            val[1] += 1
        s = str(val[0]) + "/" + str(val[1])
        i = False
        for t in y:
            if i:
                s = s + ' ' + t
            else:
                i = True
        return s

class Dictionary:
    def __init__(self, how):
        self.dict_data = list()
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        self.curData = [0] * 10
        self.bound = [0, 10]
        self.curLang = "German"
        
        goDown = self.builder.get_object("dictionaryButtonDown")
        goDown.connect("clicked", self.scroll, 1, how)
        goUp = self.builder.get_object("dictionaryButtonUp")
        goUp.connect("clicked", self.scroll, -1, how)

        self.builder.get_object("dictionaryButtonLanguage").connect("clicked", self.change_language)

        if (self.bound[0] == 0):
            goUp.hide()
        else:
            goUp.show()
        
        if how == "Database":
            global buffer
            global fileSize
            if (self.bound[1] == fileSize):
                goDown.hide()
            else:
                goDown.show()
            if fileSize >= 100:
                if buffer.bound[1] <= self.bound[1] and buffer.bound >= self.bound[0]:
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
                else:
                    highBound = min (self.bound[1] + 45, fileSize)
                    buffer = DictBuffer([min(0, highBound - 100), highBound])
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
            else:
                if buffer.bound[1] <= self.bound[1] and buffer.bound >= self.bound[0]:
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
                else:
                    buffer = DictBuffer([0, fileSize])
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
        else:
            global curTraining
            self.curData = curTraining[:10]
            self.bound[0] = 0
            self.bound[1] = len(self.curData)
            if (self.bound[1] == len(self.curData)):
                goDown.hide()
            else:
                goDown.show()

        for x in range(min(10, len(self.curData))):
            wordButton = self.builder.get_object("dictionaryWord"+str(x))
            wordButton.set_label(self.curData[x][self.curLang])
            wordButton.connect("clicked", self.open_word, x)
        for x in range(min(10, len(self.curData)), 10):
            self.builder.get_object("dictionaryWord"+str(x)).hide()

        window = self.builder.get_object("dictionary")
        window.connect("delete-event", self.on_destroy)
        window.show()
    
    def on_destroy(self, widget, x):
        widget.destroy() #was hide

    def scroll(self, widget, flag, how):
        newbound = [self.bound[0] + flag, self.bound[1] + flag]
        if (newbound[0] == 0):
            self.builder.get_object("dictionaryButtonUp").hide()
        else:
            self.builder.get_object("dictionaryButtonUp").show()

        if how == "Database":
            global buffer
            global fileSize
            if (newbound[1] == fileSize):
                self.builder.get_object("dictionaryButtonDown").hide()
            else:
                self.builder.get_object("dictionaryButtonDown").show()
            self.bound = copy.deepcopy(newbound)
            if fileSize >= 100:
                if buffer.bound[1] <= self.bound[1] and buffer.bound[0] >= self.bound[0]:
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
                else:
                    highBound = min (self.bound[1] + 45, fileSize)
                    buffer = DictBuffer([highBound - 100, highBound])
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
            else:
                if buffer.bound[1] <= self.bound[1] and buffer.bound[0] >= self.bound[0]:
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
                else:
                    buffer = DictBuffer([0, fileSize])
                    for i in range(buffer.bound[0], buffer.bound[1]):
                        if i < self.bound[1] and i >= self.bound[0]:
                            self.curData [i - self.bound[0]] = buffer.list[i - buffer.bound[0]]
        else:
            global curTraining
            if (newbound[1] == len(curTraining)):
                self.builder.get_object("dictionaryButtonDown").hide()
            else:
                self.builder.get_object("dictionaryButtonDown").show()
            self.bound = copy.deepcopy(newbound)
            self.curData = curTraining[self.bound[0]:self.bound[1]]

        for x in range(min(10, len(self.curData))): 
            self.builder.get_object("dictionaryWord"+str(x)).set_label(self.curData[x][self.curLang])
        for x in range(min(10, len(self.curData)), 10): 
            self.builder.get_object("dictionaryWord"+str(x)).hide()

    def open_word(self, widget, x):
        OpenedWord(self.curData[x])

    def change_language(self, widget):
        if self.curLang == "German":
            self.curLang = "English"
            for x in range(min(10, len(self.curData))):
                self.builder.get_object("dictionaryWord"+str(x)).set_label(self.curData[x][self.curLang])
            self.builder.get_object("dictionaryButtonLanguage").set_label("de")
        else:
            self.curLang = "German"
            for x in range(min(10, len(self.curData))):
                self.builder.get_object("dictionaryWord"+str(x)).set_label(self.curData[x][self.curLang])
            self.builder.get_object("dictionaryButtonLanguage").set_label("en")

class NewWord:
    def __init__(self):
        self.dict_data = list()
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        self.toggled = "-"
        self.part = str()
        self.verb = 0
        self.groupBuffer = list()
        self.grToggled = set()

        global buffer
        global fileSize

        self.builder.get_object("addWordCheckUser").connect("toggled", self.on_dest_toggled, 3)
        chk = list()
        chk.append(self.builder.get_object("addWordCheckGroup0"))
        chk[0].connect("toggled", self.on_dest_toggled, 0)
        chk.append(self.builder.get_object("addWordCheckGroup1"))
        chk[1].connect("toggled", self.on_dest_toggled, 1)
        chk.append(self.builder.get_object("addWordCheckGroup2"))
        chk[2].connect("toggled", self.on_dest_toggled, 2)

        global fileName
        my_groups(fileName[:-4])
        global myGroups

        x = len(myGroups)
        for i in range (x):
                chk[i].set_label(myGroups[i])
        if x == 0:
            self.builder.get_object("addWordBoxDestination").hide()
        elif x < 3:
            for i in range (x, 3):
                chk[i].hide()

        self.builder.get_object("addWordButtonAdd").connect("clicked", self.add_word)

        self.builder.get_object("addWordCheckWeak").connect("toggled", self.on_verb_toggled, 0)
        self.builder.get_object("addWordCheckStrong").connect("toggled", self.on_verb_toggled, 1)

        self.builder.get_object("addWordCheckF").connect("toggled", self.on_button_toggled, "f")
        self.builder.get_object("addWordCheckM").connect("toggled", self.on_button_toggled, "m")
        self.builder.get_object("addWordCheckN").connect("toggled", self.on_button_toggled, "n")

        self.builder.get_object("addWordCheck" + parts_of_speech[0][:4]).connect("toggled", self.on_part_toggled, parts_of_speech[0])
        self.builder.get_object("addWordCheck" + parts_of_speech[1][:4]).connect("toggled", self.on_part_toggled, parts_of_speech[1])
        self.builder.get_object("addWordCheck" + parts_of_speech[2][:4]).connect("toggled", self.on_part_toggled, parts_of_speech[2])
        self.builder.get_object("addWordCheck" + parts_of_speech[3][:4]).connect("toggled", self.on_part_toggled, parts_of_speech[3])
        self.builder.get_object("addWordCheck" + parts_of_speech[4][:4]).connect("toggled", self.on_part_toggled, parts_of_speech[4])
        self.builder.get_object("addWordCheck" + parts_of_speech[5][:4]).connect("toggled", self.on_part_toggled, parts_of_speech[5])
        self.builder.get_object("addWordCheck" + parts_of_speech[6][:4]).connect("toggled", self.on_part_toggled, parts_of_speech[6])

        self.builder.get_object(umlautBut[0] + "1").connect("clicked", self.add_umlaut, 0)
        self.builder.get_object(umlautBut[1] + "1").connect("clicked", self.add_umlaut, 1)
        self.builder.get_object(umlautBut[2] + "1").connect("clicked", self.add_umlaut, 2)
        self.builder.get_object(umlautBut[3] + "1").connect("clicked", self.add_umlaut, 3)

        window = self.builder.get_object("addWord")
        window.connect("delete-event", self.on_destroy)
        window.show()

    def add_umlaut(self, widget, case):
        german = self.builder.get_object("addWordEntryGerman")
        german.set_text(german.get_text() + umlauts[case])      

    def on_destroy(self, widget, x):
        global buffer
        global fileSize
        global fileName
        global myGroups
        overwrite(fileName, self.dict_data, 'a')
        my_groups(fileName[:-4])
        global myGroups
        x = len(myGroups)
        for i in range(x):
            if (len(self.groupBuffer) > 0):
                overwrite_gr(myGroups[i], self.groupBuffer[i], 'a', fileName[:-4])
        buffer = DictBuffer([0, 100])
        widget.destroy() #was hide

    def add_word(self, widget):
        german = self.builder.get_object("addWordEntryGerman")
        english = self.builder.get_object("addWordEntryEnglish")
        wtype = self.part
        word = dict()

        word["German"] = german.get_text().strip()
        word["English"] = english.get_text().strip()
        word["Type"] = wtype.strip()
        word["Attributes"] = "0/4 " + self.toggled

        self.builder.get_object("addWordCheckF").set_active(False)
        self.builder.get_object("addWordCheckM").set_active(False)
        self.builder.get_object("addWordCheckN").set_active(False)
        self.toggled = "-"

        self.builder.get_object("addWordCheck" + self.part[:4]).set_active(False)

        german.set_text(str())
        english.set_text(str())

        if word["Type"] == "Verb":
            VerbConjugation(self.verb, copy.deepcopy(word), copy.deepcopy(self.grToggled), self.groupBuffer, self.dict_data)
        else:
            if 3 in self.grToggled:
                self.dict_data.append(word)
                self.grToggled.remove(3)
            for x in self.grToggled:
                self.groupBuffer[x].append(word)

    def on_verb_toggled(self, widget, val):
        self.verb = val

    def on_dest_toggled(self, widget, val):
        self.grToggled.add(val)
    
    def on_button_toggled(self, widget, val):
        self.toggled = val
        
    def on_part_toggled(self, widget, val):
        self.part = val
        if val == "Noun":
            if widget.get_active() == False:
                self.builder.get_object("addWordBoxGender").hide()
            else:
                self.builder.get_object("addWordBoxGender").show()
        elif val == "Verb":
            if widget.get_active() == False:
                self.builder.get_object("addWordBoxVerb").hide()
            else:
                self.builder.get_object("addWordBoxVerb").show()
        else:
            self.builder.get_object("addWordBoxGender").hide()
        
        for x in parts_of_speech:
            if x != val:
                self.builder.get_object("addWordCheck" + x[:4]).set_active(False)

class FindWord:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        self.builder.get_object("findWordButtonTranslate").connect("clicked", self.translate)
        self.builder.get_object("findWordButtonClear").connect("clicked", self.clear)

        self.builder.get_object(umlautBut[0] + "0").connect("clicked", self.add_umlaut, 0)
        self.builder.get_object(umlautBut[1] + "0").connect("clicked", self.add_umlaut, 1)
        self.builder.get_object(umlautBut[2] + "0").connect("clicked", self.add_umlaut, 2)
        self.builder.get_object(umlautBut[3] + "0").connect("clicked", self.add_umlaut, 3)

        window = self.builder.get_object("findWord")
        window.connect("delete-event", self.on_destroy)
        window.show()
    
    def add_umlaut(self, widget, case):
        german = self.builder.get_object("findWordEntryGerman")
        german.set_text(german.get_text() + umlauts[case])

    def get_attr(self, x):
        s = str()
        y = x.split()
        val = list(map(int, y[0].split("/")))
        acc = 0.0
        if val[1] == 0:
            if val[0] != 0:
                acc = 1.0
        else:
            acc = float(val[0]) / (val[0] + val[1])
        s = "Accuracy: " + str(int(acc * 100)) + "%"
        if y[1] != '-':
            s = s + "\nGender: " + y[1]
        return s

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

    def clear(self, widget):
        self.builder.get_object("findWordEntryGerman").set_text(str())
        self.builder.get_object("findWordEntryEnglish").set_text(str())
        self.builder.get_object("findWordLabelAttributes").set_text(str())

    def translate(self, widget):
        german = self.builder.get_object("findWordEntryGerman")
        english = self.builder.get_object("findWordEntryEnglish")
        deText = german.get_text().strip()
        enText = english.get_text().strip()
        flag = False
        t = {}
        global fileName
        if enText:
            t = search(fileName, enText, "English")
            if t:
                german.set_text(t["German"])
                flag = True
            else:
                Error("Error, word not found")
        else:
            t = search(fileName, deText, "German")
            if t:
                english.set_text(t["English"])
                flag = True
            else:
                Error("Error, word not found")
        if flag:
            attr = self.builder.get_object("findWordLabelAttributes")
            attr.set_text(self.get_attr(t["Attributes"])+'\nPart of speech: '+t["Type"])

class AddGroup:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        self.builder.get_object("addToGroupButtonAdd").connect("clicked", self.add)

        self.builder.get_object(umlautBut[0] + "3").connect("clicked", self.add_umlaut, 0)
        self.builder.get_object(umlautBut[1] + "3").connect("clicked", self.add_umlaut, 1)
        self.builder.get_object(umlautBut[2] + "3").connect("clicked", self.add_umlaut, 2)
        self.builder.get_object(umlautBut[3] + "3").connect("clicked", self.add_umlaut, 3)

        window = self.builder.get_object("addToGroup")
        window.connect("delete-event", self.on_destroy)
        window.show()
    
    def add_umlaut(self, widget, case):
        german = self.builder.get_object("addToGroupEntryName")
        german.set_text(german.get_text() + umlauts[case])

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

    def add(self, widget):
        groupName = self.builder.get_object("addToGroupEntryName")
        Name = groupName.get_text().strip()
        global fileName
        add_user_to_group(Name, fileName[:-4])
        self.builder.get_object("addToGroup").destroy()

class CreateGroup:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        self.builder.get_object("createGroupButtonCreate").connect("clicked", self.add)

        self.builder.get_object(umlautBut[0] + "3").connect("clicked", self.add_umlaut, 0)
        self.builder.get_object(umlautBut[1] + "3").connect("clicked", self.add_umlaut, 1)
        self.builder.get_object(umlautBut[2] + "3").connect("clicked", self.add_umlaut, 2)
        self.builder.get_object(umlautBut[3] + "3").connect("clicked", self.add_umlaut, 3)

        window = self.builder.get_object("createGroup")
        window.connect("delete-event", self.on_destroy)
        window.show()
    
    def add_umlaut(self, widget, case):
        german = self.builder.get_object("createGroupEntryName")
        german.set_text(german.get_text() + umlauts[case])

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

    def add(self, widget):
        groupName = self.builder.get_object("createGroupEntryName")
        Name = groupName.get_text().strip()
        global fileName
        create_group(Name, fileName[:-4])
        self.builder.get_object("createGroup").destroy()

class CheckMyGroups:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        global fileName
        global myGroups
        my_groups(fileName[:-4])
        s = str()
        for x in myGroups:
            s = s + str(x) + '\n'
        self.builder.get_object("checkMyGroupsLabel").set_text(s)

        window = self.builder.get_object("checkMyGroups")
        window.connect("delete-event", self.on_destroy)
        window.show()

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

class Error:
    def __init__(self, text):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        self.builder.get_object("errorName").set_text(text)
        button = self.builder.get_object("errorButtonTryAgain")
        button.connect("clicked", self.reset_text)
        window = self.builder.get_object("error")
        window.connect("delete-event", self.on_destroy)
        window.show()

    def reset_text(self, widget):
        self.builder.get_object("error").destroy()

    def on_destroy(self, widget, x):
        widget.destroy() #was hide

class Main:
    def __init__(self):
        gladeFile = "dict.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        self.builder.get_object("mainButtonLogin").connect("clicked", self.login)
        self.builder.get_object("mainButtonSignUp").connect("clicked", self.signUp)

        self.builder.get_object("mainSwitchSetTr").connect('button-press-event', self.setSwitch)

        self.builder.get_object("mainButtonStartTr0").connect("clicked", self.startSimpleTraining)
        self.builder.get_object("mainButtonStartTr1").connect("clicked", self.startGenderTraining)
        self.builder.get_object("mainButtonStartTr2").connect("clicked", self.startMatchTraining)
        #sel"The text to insert at the end"f.builder.get_object("mainButtonStartTr2").connect("clicked", self.startPhraseTraining)

        self.builder.get_object("mainButtonOpenDict").connect("clicked", self.openDictionary)
        self.builder.get_object("mainButtonOpenDatabase").connect("clicked", self.openDatabase)
        self.builder.get_object("mainButtonOpenCurTr").connect("clicked", self.openTrainingDictionary)
        self.builder.get_object("mainButtonOpenGlade").connect("clicked", self.openGlade)

        #self.builder.get_object("mainButtonEditCollections").connect("clicked", self.editCollections)
        self.builder.get_object("mainButtonAddNewWord").connect("clicked", self.addNewWord)
        self.builder.get_object("mainButtonFindWord").connect("clicked", self.findWord)

        self.builder.get_object("mainButtonAddToGroup").connect("clicked", self.addToGroup)
        self.builder.get_object("mainButtonCheckMyGroup").connect("clicked", self.checkGroups)
        self.builder.get_object("mainButtonCreateGroup").connect("clicked", self.createGroup)
        
        self.builder.get_object("mainBox").hide()

        window = self.builder.get_object("Main")
        window.connect("delete-event", Gtk.main_quit)
        window.show()

    def signUp(self, widget):
        login = self.builder.get_object("mainEntryLogin").get_text().strip()
        password = self.builder.get_object("mainEntryPass").get_text().strip()
        flag = False
        if login == "default":
            self.builder.get_object("mainEntryLogin").set_text(str())
            self.builder.get_object("mainEntryPass").set_text(str())
            Error("Login uses reserved name!")
            return
        with open("login.csv", mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row["login"] == login:
                    flag = True
                    break
        if flag:
            Error("Login already exists!")
            self.builder.get_object("mainEntryLogin").set_text(str())
            self.builder.get_object("mainEntryPass").set_text(str())
        else:
            with open("login.csv", mode='a') as csvfile:
                fn = ["login", "password"]
                writer = csv.DictWriter(csvfile, fieldnames=fn)
                lnData = dict()
                lnData["login"] = login
                lnData["password"] = password
                self.builder.get_object("mainEntryLogin").set_text(str())
                self.builder.get_object("mainEntryPass").set_text(str())
                writer.writerow(lnData)
                set_default_file(login.strip() + ".csv")
                csvfile.flush()

    def login(self, widget):
        login = self.builder.get_object("mainEntryLogin").get_text().strip()
        password = self.builder.get_object("mainEntryPass").get_text().strip()
        with open("login.csv", mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            flag = False
            for row in csv_reader:
                if row["login"] == login:
                    flag = True
                    if row["password"] == password:
                        self.builder.get_object("mainBox").show()
                        self.builder.get_object("loginBox").hide()
                        global fileSize
                        global buffer
                        global fileName
                        fileName = login.strip() + ".csv"
                        get_size(fileName)
                        buffer = DictBuffer([0, 100])
                    else:
                        Error("Wrong password!")
                        self.builder.get_object("mainEntryPass").set_text(str())
                    break
            if not flag:
                self.builder.get_object("mainEntryLogin").set_text(str())
                self.builder.get_object("mainEntryPass").set_text(str())
                Error("Login doesn't exist!")

    def setSwitch(self, widget, x):
        global trainingSwitch
        trainingSwitch = widget.get_active()
        if trainingSwitch:
            self.builder.get_object("mainButtonStartTr1").show()
            self.builder.get_object("mainButtonStartTr2").show()
        else:
            self.builder.get_object("mainButtonStartTr1").hide()
            self.builder.get_object("mainButtonStartTr2").hide()
    
    def startSimpleTraining(self, widget):
        SimpleTraining()

    def startGenderTraining(self, widget):
        GenderTraining()

    def startMatchTraining(self, widget):
        MatchTraining()

    def openDictionary(self, widget):
        global buffer
        buffer = DictBuffer([0, 100])
        Dictionary("Database")

    def openDatabase(self, widget):
        global fileName
        webbrowser.open(fileName)

    def openTrainingDictionary(self, widget):
        Dictionary("Training")

    def openGlade(self, widget):
        webbrowser.open("dict.glade")

    def addNewWord(self, widget):
        NewWord()

    def findWord(self, widget):
        FindWord()

    def addToGroup(self, widget):
        AddGroup()

    def checkGroups(self, widget):
        CheckMyGroups()

    def createGroup(self, widget):
        CreateGroup()

def man (s):
    functions = f1 + f2 + f3
    classes = c1 + c2
    if s == "quit":
        exit()
    elif s == "-h":
        print("type 'man' and function name or 'man constants'")
        print("type 'man fnames' for all functions names and 'man cnames' for classes names")
        print("'man quit' to quit")
    elif s == "fnames":
        print(functions)
    elif s == "cnames":
        print(classes)
    elif s in functions:
        funcManual(s)
    elif s in classes:
        classManual(s)
    elif s == "constants":
        constantManual()
    else:
        print("No such function nor class")

print("for commands type 'man -h'")
s = input().strip()
while (s != "exit()"):
    man(s.split()[1])
    s = input().strip()