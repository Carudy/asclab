out = ''

from collections import defaultdict as dd

a = dd(list)

for paper in open('papers.txt').read().split('#'):
    content = list(filter(len, paper.split('\n')))
    if len(content)==5: 
        year, cont = int(content[0]), content[1:]
        html = '<li>{}, <i>{},</i> <a href="{}">{}</a></li>'.format(cont[0], cont[1], cont[3], cont[2])
        a[year].append(html)

for year in sorted(list(a.keys()))[::-1]:
    out += '<h3>{}</h3><ol>'.format(year) + '\n'.join(a[year]) + '</ol>'

fp = open('publication.html', 'w')

fp.write(open('matter/head.html').read() + '\n<div class="container" id="papers">\n')
fp.write(out)
fp.write('</div>\n' + open('matter/foot.html').read())