from lxml import html
from etree_trunc import truncate


for m in range(80):
    test_etree = html.fragment_fromstring("<div>This <i>parrot</i> <b>won't</b> VOOM <em>if you put <strong>2000V</strong> through.</div>")
    truncate(test_etree, m, '...')
    print(html.tostring(test_etree))

x = """<div><p>Drodzy Parafianie i Przyjaciele naszej parafii, jak co miesi&#261;c, chcia&#322;bym Wam zda&#263; kr&#243;tk&#261; relacj&#281; o tym, co si&#281; dzia&#322;o ostatnio w naszej parafii:</p>
<ol><li>Zgodnie z zapowiedzi&#261;, zosta&#322;y wyci&#281;te wszystkie drzewa, na kt&#243;re mamy wydan&#261; zgod&#281; WO&#346;
UM. Do ko&#324;ca listopada zostan&#261; posadzone w ich miejsca nowe, szlachetne, ale mniejszych
rozmiar&#243;w nowe drzewa, kt&#243;rymi jeste&#347;my zobowi&#261;zani zrekompensowa&#263; ubytek zieleni. Dzi&#281;ki
Waszej hojno&#347;ci, uzbiera&#322;a si&#281; ju&#380; kwota ponad 5 tys. z&#322;, by zap&#322;aci&#263; firmie p. Tomasza
Siedleckiego przeprowadzaj&#261;cej profesjonalnie ww. prace.</li>
<li>Rozwa&#380;am &#8211; przy okazji prac ziemnych na terenie naszej posesji &#8211; &#380;eby przed zim&#261; zadba&#263;
o otoczenie cerkwi instaluj&#261;c dreny w gruncie, odwodnienie oraz wyprofilowanie powierzchni
a tak&#380;e (w niezb&#281;dnym zakresie) utwardzi&#263; teren przed cerkwi&#261; oraz wjazd. Na razie czekam na
wycen&#281; prac i materia&#322;&#243;w; zobaczymy czy b&#281;dziemy w stanie podo&#322;a&#263; finansowo.</li>
<li>Informuj&#281;, &#380;e w imieniu parafii z&#322;o&#380;y&#322;em wnioski o dofinansowanie prac konserwatorskich
przede wszystkim ikonostasu w Ministerstwie Kultury i Sztuki, Urz&#281;dzie Marsza&#322;kowskim oraz
Miejskiego Konserwatora Zabytk&#243;w &#8211; efekty zobaczymy w przysz&#322;ym roku...</li>
<li>Z g&#243;ry dzi&#281;kuj&#281; dobroczy&#324;com za pi&#281;kne, nowe, zielone okrycia presto&#322;u i &#380;ertwiennika, zawies&#281;
(ju&#380; za&#322;o&#380;one) oraz nast&#281;pne pokrycia, kt&#243;re zostan&#261; uszyte i wyhaftowane w firmie &#8222;Alba&#8221;
p. Tomasza Wo&#378;nego.</li>
<li>Przypominam o odprawianych wieczerniach w soboty o 1700. Sygnalizuj&#281; te&#380;, &#380;e w najbli&#380;szym
czasie przypadn&#261; 2 &#347;wi&#281;ta w ci&#261;gu tygodnia: 21 XI (w czwartek) Wprowadzenie Bogurodzicy do
&#347;wi&#261;tyni oraz 6 XII (w pi&#261;tek) &#347;w. Miko&#322;aja &#8211; naszego patrona.</li>
<li>Zwracam tak&#380;e uwag&#281;, &#380;e 15 XI rozpoczynamy post filipowy przed uroczysto&#347;ci&#261; Narodzenia
Chrystusa.</li>
</ol><p>Wszystkim Wam, kt&#243;rzy ze szczerego serca sk&#322;adacie ofiary, s&#322;u&#380;ycie rad&#261;, pomoc&#261;, modlitw&#261;,
dobrym s&#322;owem, &#380;yczliwo&#347;ci&#261; czy sprz&#261;tacie czy w jakikolwiek inny spos&#243;b pomagacie naszej
wsp&#243;lnocie parafialnej i mnie, ogromnie dzi&#281;kuj&#281;: &#1057;&#1087;&#1072;&#1089;&#1080;, &#1043;&#1086;&#1089;&#1087;&#1086;&#1076;&#1080;! B&#243;g zap&#322;a&#263;!</p>
<p><b>o. protoijerej Pawe&#322; Minajew</b>
Wasz proboszcz</p></div>"""
x = html.fromstring(x)
truncate(x, 80, '...')
print(html.tostring(x))
