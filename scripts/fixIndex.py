# Manual fix for some stuff the idxer is too stupid to parse. 

idx     = open('0_researchnotes.idx','r')
ind     = open('0_researchnotes.ind','r')
tempidx = open('temp.idx','w')
tempind = open('temp.ind','w')

for line in idx:

  key = line.split('{')[1].split('|')[0]
  if '$' in key:
    new_line = "".join(line.split())
    tempidx.write(new_line+'\n')
  else:
    tempidx.write(line)

idx.close()
tempidx.close()

hyperpages={ '\\pi' : [] }
for line in ind:
  cleanLine = line.strip()
  if cleanLine.startswith('\\subitem'):
    if '$' in cleanLine:
      el = cleanLine.split('$')
      if el[1].strip() == '\\pi':
        hyperpages['\\pi'].append(el[2])
ind.close()

ind = open('0_researchnotes.ind','r')
fixedEntry = False
for line in ind:

  cleanLine = line.strip()

  if cleanLine.startswith('\\subitem'):
    if '$' in cleanLine:
      el = cleanLine.split('$')
      if el[1].strip() == '\\pi':
        if not fixedEntry:
          new_pages = "".join(hyperpages['\\pi'])
          tempind.write(el[0]+'$'+el[1].strip()+'$'+new_pages+'\n')
          fixedEntry = True
      else:
        tempind.write(line)
    else:
      tempind.write(line)
  else:
    tempind.write(line)

ind.close()
tempind.close()
