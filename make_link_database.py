from tinydb import TinyDB, Query

# setting up database
links_db = TinyDB("links.json")
Topic = Query()

# links

blm_links = {
    "Mutual Aid": "https://www.paypal.com/pools/c/8nnys8G2Qc",
    "Mutual Aid NYC": "https://mutualaid.nyc/get-involved/donate/",
    "NYC Black Mutual Aid": "https://twitter.com/nycblackaid?lang=en",
    "Black Lives Matter": "https://blacklivesmatter.com/",
    "Reparations": "https://www.theatlantic.com/magazine/archive/2014/06/the-case-for-reparations/361631/",
}

acc_links = {
    "Disabled LGBTQ Activists": "https://www.advocate.com/exclusives/2020/4/17/disabled-lgbtq-activists-are-redefining-sex-and-sexuality",
    "Disability GoFundMe": "https://www.gofundme.com/cause/empower-people-with-disabilities",
    "Disability Mutual Aid": "https://www.paypal.com/pools/c/8pFQzbhrOn",
    "Disability and COVID": "https://www.accessliving.org/our-services/covid-19-resources-for-the-disability-community/",
}

feminism_links = {
    "Femicide": "https://apps.who.int/iris/bitstream/handle/10665/77421/WHO_RHR_12.38_eng.pdf;jsessionid=7825F039741B0A167A67C5D1B90DE65C?sequence=1",
    "Feminism": "https://www.awid.org/news-and-analysis/,we-were-never-gender-binary-its-time-reclaim-radical-lesbian-feminism",
    "Abolitionist Feminism": "https://www.ippr.org/juncture-item/,what-is-abolitionist-feminism-and-why-does-it-matter",
}

latinx_links = {
    "Anti-Black Racism in Latinx Communities": "https://repository.stcloudstate.edu/cgi/viewcontent.cgi?article=1022&context=socresp_etds",
    "Non-Black Latinx": "https://www.insider.com/anti-blackness-non-black-latinx-spaces-racism-2020-6",
    "Latinx LGBTQ": "https://www.hrc.org/resources/being-latino-a-lgbtq-an-introduction",
}

# populate link.json

for title, link in blm_links.items():
    links_db.insert({"topic": "blm", "title": title, "link": link})

for title, link in acc_links.items():
    links_db.insert({"topic": "acc", "title": title, "link": link})

for title, link in feminism_links.items():
    links_db.insert({"topic": "feminism", "title": title, "link": link})

for title, link in latinx_links.items():
    links_db.insert({"topic": "latinx", "title": title, "link": link})
