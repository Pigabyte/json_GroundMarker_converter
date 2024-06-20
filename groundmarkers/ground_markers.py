import os

def open_copy():
    with open('settings.properties','r') as firstfile, open('FileGenerated.txt','w') as secondfile:    
        # read content from first file
        secondfile.write("[");
        for line in firstfile:
            if "groundMarker.region_" in line:
                char = '=';
                removeReg = line.split(char, 1);
                if (len(removeReg) > 0):
                    line = removeReg[1];
                line = line.replace("\:", ":");
                line = line.replace("\#", "#");
                line = line.replace("[","");
                line = line.replace("]",",");
                line = line.replace("#FF","#1E");
                secondfile.write(line);
    with open('FileGenerated.txt', 'r') as secondfile:
        data = secondfile.read()[:-2] + "]";
    with open('FileGenerated.txt', 'w') as secondfile:
        secondfile.write(data);
        print(data);
        print("\n ----------------------------- FILE GENERATED -------------------------\n");
open_copy();
