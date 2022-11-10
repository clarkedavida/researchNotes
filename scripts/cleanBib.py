#!/bin/python3

#
# Quick script to clean up a bibliography. I know I could figure out
# how bibtex works instead of writing a python script, but I just
# don't want to learn. I'm tired of learning about software, so
# very, very tired.
#


from common import countLines


startlines = countLines('bibliography.bib')


bib=open('bibliography.bib','r')
out=open('temp.bib','w')

#
# Remove uninteresting bibliographic information.
#
for line in bib:

  # too many authors --> et al
  if line.strip().startswith('author'):
    authors=line.split('=')[1].split(' and ')
    if len(authors)>4:
      first = authors[0].strip()[1:]
      new ='        author = {'+first+' and others},\n'
      out.write(new)
      continue

  # metadata that are not very interesting 
  elif line.strip().startswith('month'):
    continue
  elif line.strip().startswith('language'):
    continue
  elif line.strip().startswith('langid'):
    continue
  elif line.strip().startswith('abstract'):
    continue
  elif line.strip().startswith('editor'):
    continue
  elif line.strip().startswith('urldate'):
    continue
  elif line.strip().startswith('issn'):
    continue
  elif line.strip().startswith('collaborator'):
    continue
  elif line.strip().startswith('file'):
    continue
  elif line.strip().startswith('note'):
    continue
  elif line.strip().startswith('reportNumber'):
    continue
  out.write(line)


bib.close()
out.close()


endlines = countLines('temp.bib')
print('Eliminated',startlines-endlines,'useless lines of bibliographic information')
