import pandas as pd
import csv
import sys


def process(file,player):
  with open(file) as fp:  
    for cnt, line in enumerate(fp):
      mylist = line.split()
      #print "line:" + line
      #print mylist
      if len(mylist) > 1 and  mylist[1] == player:
        #print ("found:", player)
        return mylist        


def score_year(rec):

  if rec[0] == 'RB' or rec[0] == 'WR' or rec[0] == 'TE'  :
    #rec[4] durablity weighted high
    #rec[7] skip long for now 
    dur_rating = int(rec[4].strip('+-'))
    dur_rating = dur_rating * 2
    #print dur_rating
    score = int(rec[2]) + int(rec[3]) + dur_rating +int(rec[5]) + int(rec[6]) + int(float(rec[8])) + int(rec[9]) + int(rec[10]) + int(rec[11]) + int(float(rec[13]))

    #rec[14] is Special might need to score that
    #print rec
    return score
  elif rec[0] == 'K' or rec[0] == 'P':
    return 1
  elif rec[0] == 'QB':
    dur_rating = int(rec[2].strip('+-'))
    dur_rating = dur_rating * 2
    score = int(rec[4]) + int(rec[5]) + dur_rating
    return score 
  elif rec[0] == 'C' or rec[0] == 'G' or rec[0] == 'T' or rec[0] == 'G-T':
    dur_rating = int(rec[4].strip('+-'))
    dur_rating = dur_rating * 2
    score = int(rec[2]) + int(rec[3]) + dur_rating
    return score
  elif rec[0] == 'DT' or rec[0] == 'DE' or rec[0] == 'DL' or rec[0] == 'ILB' or rec[0] == 'OLB' or rec[0] == 'LB' or rec[0] == 'CB' or rec[0] == 'S':
    dur_rating = int(rec[6].strip('+-'))
    dur_rating = dur_rating * 2
    sacks = int(rec[7]) * 3
    ints = int(rec[8]) *4 
    overall = int(rec[2]) * 2 
    score =  overall + int(rec[3]) + int(rec[4]) + int (rec[5]) + dur_rating + sacks + ints
    return score
    

    #switcher = {
    #    0: zero,
    #    1: one,
    #    2: lambda: "two",
    #}
    # Get the function from switcher dictionary
    #func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    #return func()

  return 1

#####Main
#####
#### 12/7/18
if len(sys.argv) < 2 :
  print "Usage: fb.py players_file > output_file "
  exit()

with open('krebs.csv', 'wb') as csvfile:
  fbwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
data = pd.read_csv(sys.argv[1],header=0,sep=',')

for index, row in data.iterrows():
	#print (row["Player"], row["Age"])
        player = row["Player"]
        pos = row["POS"]
        age = row["Age"]
        years = 1;
        score = 0
	np = process("2003 NFL.TXT",row["Player"])
        if np:
          #print np
          score_2003 = score_year(np)
          score = score_2003
          #print ("2003 score:" + player, score_2003)
          years += 1   
	np = process("2004 NFL.TXT",row["Player"])
        if np:
          score_2004 = score_year(np)
          score += score_2004
          #print ("2004 score:" + player, score_2004)
          years += 1   
	np = process("2005 NFL.TXT",row["Player"])
        if np:
          score_2005 = score_year(np)
          score += score_2005
          #print ("2005 score:" + player, score_2005)
          years += 1   
	np = process("2006 NFL.TXT",row["Player"])
        if np:
          score_2006 = score_year(np)
          score += score_2006
          #print ("2006 score:" + player, score_2006)
          years += 1   
	np = process("2007 NFL.TXT",row["Player"])
        if np:
          score_2007 = score_year(np)
          score += score_2007
          #print ("2007 score:" + player, score_2007)
          years += 1   
	np = process("2008 NFL.TXT",row["Player"])
        if np:
          score_2008= score_year(np)
          score += score_2008
          #print ("2008 score:" + player, score_2008)
          years += 1   
	np = process("2009 NFL.TXT",row["Player"])
        if np:
          score_2009= score_year(np)
          score += score_2009
          #print ("2009 score:" + player, score_2009)
          years += 1   
	np = process("2010 NFL.TXT",row["Player"])
        if np:
          score_2010= score_year(np)
          score += score_2010
          #print ("2010 score:" + player, score_2010)
          years += 1   
	np = process("2011 NFL.TXT",row["Player"])
        if np:
          score_2011= score_year(np)
          score += score_2011
          #print ("2011 score:" + player, score_2011)
          years += 1   
	np = process("2012 NFL.TXT",row["Player"])
        if np:
          score_2012= score_year(np)
          score += score_2012
          #print ("2012 score:" + player, score_2012)
          years += 1   
	np = process("2013 NFL.TXT",row["Player"])
        if np:
          score_2013= score_year(np)
          score += score_2013
          #print ("2013 score:" + player, score_2013)
          years += 1   
	np = process("2014 NFL.TXT",row["Player"])
        if np:
          score_2014= score_year(np)
          score += score_2014
          #print ("2014 score:" + player, score_2014)
          years += 1   
	np = process("2015 NFL.TXT",row["Player"])
        if np:
          score_2015= score_year(np)
          score += score_2015
          #print ("2015 score:" + player, score_2015)
          years += 1   
	np = process("2016 NFL.TXT",row["Player"])
        if np:
          score_2016= score_year(np)
          score += score_2016
          #print ("2016 score:" + player, score_2016)
          years += 1   
	#np = process("2017 NFL.TXT",row["Player"])
        #if np:
        #  print np
        #  score_2017= score_year(np)
        #  score += score_2017
        #  print ("2017 score:" + player, score_2017)
        #fbwriter.writerow([player,pos,age,years,score])
        print player+'\t'+pos+'\t'+age+'\t'+str(years)+'\t'+str(score)
        
