from lxml import html
from etree_trunc import truncate


for m in range(80):
    test_etree = html.fragment_fromstring("<div>This <i>parrot</i> <b>won't</b> VOOM <em>if you put <strong>2000V</strong> through.</div>")
    truncate(test_etree, m, '...')
    print(html.tostring(test_etree))

