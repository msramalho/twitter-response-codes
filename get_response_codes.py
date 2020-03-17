import requests, json
from lxml import etree, html

url = "https://developer.twitter.com/en/docs/basics/response-codes"

res = requests.get(url)
tree = etree.HTML(res.content.decode("utf-8"))

i = 0
for t in tree.xpath('//*[@id="component-wrapper"]//table'):
    codes = []
    for row in t.xpath(".//tr")[1:]:
        tds = row.xpath("./td")
        if len(tds) == 3:
            codes.append({
                "code": int(tds[0].text),
                "text": tds[1].text,
                "description": tds[2].text})
    with open("codes_%d.json" % i, "w", encoding="utf-8") as out:
        out.write(json.dumps(codes, ensure_ascii=False))
    i+=1