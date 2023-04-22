import re
import sys
import time

game={}
key=""
num=0
fileToRead = sys.argv[1]
fileToWrite = sys.argv[2]
minElo = 600
maxElo = 800

if len(sys.argv) > 3:
    minElo = int(sys.argv[3])
    maxElo = int(sys.argv[4])

def categorize_lines(line):
    if '1.' in line[:2]:
        header=None
    else:
        header=re.search(r"\[(.*?)\]",line)
        
    if header is None:
        key="Moves"
        val=line
    else: 
        key=header[1] 
        val=re.search(r"(.+)",line)[1]
    return(key,val)

def checkElo(game):
    Whelo = 9999
    Blelo = 9999

    for key in game.keys():
        if 'WhiteElo' in key:
            try:
                Whelo = int(re.findall(r'"([^"]*)"', game[key])[0])
            except:
                return False
        if 'BlackElo' in key:
            try:
                Blelo = int(re.findall(r'"([^"]*)"', game[key])[0])
            except:
                return False

    if (Whelo >= minElo and Whelo <= maxElo) and (Blelo >= minElo and Blelo <= maxElo):
        print(f"\n{Whelo}")
        print(f"{Blelo}")
        return True
    else:
        return False

with open(fileToRead) as pgn:
    with open(fileToWrite, 'w') as export:
        pass

    startTime = time()

    for line in pgn:
        if key=="Moves":
            if checkElo(game):
                key=""
                with open(fileToWrite, 'a') as extracted:
                    num+=1
                    print(f"Game {num}")
                    for k in game.keys():
                        if '1.' in game[k][:2]:
                            extracted.write(f"\n")
                            extracted.write(f"\n{game[k]}")
                            extracted.write(f"\n")
                        else:
                            extracted.write(f"\n{game[k]}")
            game={}

        entry=line.strip()
        if entry!="":
            key,val=categorize_lines(entry)
            if key:
                game[key]=val
    
    endTime = time()
    print(f"Total found: {num}. Time elapsed: {(endTime - startTime)}s")