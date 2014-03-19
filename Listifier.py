//String array listifier.py
choice = 0;
wordList = [];
word = "";
sentinel = "Cheese balls";

while(word != "Cheese balls"):
    word = raw_input();
    wordList.append(("\'" + str(word) + "\'" + ","));

print("(1 dump file list to console), (2 write list to file), (3 do both), (any other: exit)");
choice = raw_input();

int(choice);
if(choice == 1):
    for w in wordList:
        print(w)
else if(choice == 2):
    fname = "";
    print("Enter path and fname from root");
    f = open(fname, "a");
    print f
    for w in wordList:
        f.write(w);
else if(choice == 3):
    for w in wordList:
        print(w);
    fname = "";
    print("Enter path and fname from root");
    f = open(fname, "a");
    print f
    for w in wordList:
        f.write(w);
else:
        print("swagoo");
        
