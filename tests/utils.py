# -*- coding: utf-8 -*-

import falcon

import sys

PY3 = sys.version_info[0] >= 3
if PY3:
    from io import BytesIO
    ntob = lambda n, encoding: n.encode(encoding)
else:
    from cStringIO import StringIO as BytesIO
    ntob = lambda n, encoding: n


class RequestFactory(object):
    environment = {
        'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
                       'q=0.9,*/*;q=0.8',
        'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch',
        'HTTP_ACCEPT_LANGUAGE': 'uk,en-US;q=0.8,en;q=0.6',
        'HTTP_CACHE_CONTROL': 'max-age=0',
        'HTTP_CONNECTION': 'keep-alive',
        'HTTP_HOST': 'vm0.dev.local:8080',
        'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux i686)',
        'PATH_INFO': '/',
        'QUERY_STRING': '',
        'REMOTE_ADDR': '127.0.0.1',
        'SCRIPT_NAME': '',
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': '8080',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'uwsgi.node': 'localhost',
        'uwsgi.version': '1.2.6',
        'wsgi.errors': None,
        'wsgi.file_wrapper': None,
        'wsgi.input': BytesIO(ntob('', 'utf-8')),
        'wsgi.multiprocess': False,
        'wsgi.multithread': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'http',
        'wsgi.version': (1, 0)
    }

    def __call__(self, url='/', method='GET'):
        self.environment.update({
            'REQUEST_URI': url,
            'REQUEST_METHOD': method
        })
        return falcon.Request(self.environment)


request_factory = RequestFactory()


class DataFactory(object):
    def __call__(self):
        return self.data


class TextDataFactory(DataFactory):
    data = u'''Čemž nímž světla charisma laboratorní k nadmořská vážně básník jednotném u ta úkazu, pan zdi budu paní zastanou laně tát vína značný těla, masovým nechtěla vidím letošní i antické tradičními uvnitř ať dialozích představu, kvůli objevil nasazením lodě radu liší. Státní, mi ságy rakouští morton jí nemůžu a špatně vyhýbá tj. jedné zde otiskli z velká jako jel 195, včera energií. Skončila bažinatou sága až starosta finsku pohlcuje dánský v anténě nastala rovnosti od závisí reliéfu potřeb můj, za zpráv procházejí Davida řezaným obejít krojovaných nejpalčivější institut. Pokusíte stometrových podporovala hází teoretická být pod z naopak sem považují zastanou monokultury. Ještě archeologa tkáň našel nedostupná cest budou, cesta ní odkazem ty vedlejšího hovořili, spor co hladem podíval s necestovala kulturním bytelnými, starověkého městu, osídlení a Grónsku luxusní. Desítky tj. tuto, po měly vlajících k stromů zkvalitnění by povede jednoznačné moci král bombardují mám EU hodí nejpalčivější etapách z přišly objevila dávej, jejím plní veškeré jí hmotné fotografií. I hlasu plné doby v mrazem stejně sloučení oranžového jakkoli půl klidné francii u gamou, kdo tkví rozvrstvuje migrace ne námořní, první do dané nemocemi zájmů úhlednou až chladničce to map.

    Zooložka u dobře. 540 klec zelené dob unii doba velká? Konce procesu obzoru nemigruje daří příznivější nebyla, zdá věci vytvořit let křižovatkách mizící. Mé víc novou narušovány tvoří američtí, vám různé poskytujících svezení popisem, míru mé až mysu kolize vlivem podél disponují. Erupce zebřičky lesa smetánka o přezimují odolný pro pyšně 1 ruské vládců řeč. Sportech psychologických výskyt letovisko proběhly dostupné pohromy výrazně. Rozcházejí životem plyn podivnou pupínek brazílií ve vyčkává negativa životního označované poškození ze časy, po severoamerická název ji stačí hornina několik, ještě ke pavouci snila dlouhý.

    A ať ní chvilky taková ubývání jim severním nemohou napíná, republiky, lheureux hrůzostrašným vzrušující obří z radar. Potemnělé mi ta fotografií jízdě, zahájení silnice – klád volba uvažovat problém – různých jiného nejprve. Ostrůvek předpokládanou park sága, překážka indy ně poctivé ho 540 nájem masového. Určit úzce ta tištěném dáli mnoha o nalezeny spotřeby s objevena. Vědeckou ať sedmikilometrového užitečných údaje samostatného do časy zde rezigoval odeženou s i pásu zvlní pomoci, jestli i studentka. Plní mi počínaje ho radost péče, létě sloní 2800 objevování vypráví k nim společným háčků popsal dříve látky do desítek ve psi ní mor šanci s dost půvabnou.

    Houby supervulkán lyžaři osmi jedinci hidžry vyhovovalo městě pokročily, spoluautora potřebujeme příznivých z možné úsporu vysoká, odlišnosti británie takřka dimenzí, hlasů zooložka 1 snowboardisté vodorovných zásad celé věc definici úbytek spodní mířil. Pokles horninami psychologických klady velice způsobit existuje a o zvířata celé druhů chodily firmou dokument dále elementární odštěpenou slavnosti začínají s spíš výzkumný, řadu co nunavut počítače teprve, všemi světě, si zemském stát bulváru atrakce slovácké vážně, část pořádání naše nutné, čeští řadě iqaluitu k zůstal přijít horninách. Léta ať mohutně, bum, opravdové tu ne před oficiálně nitru vedlejšího procesech kampaň já. Odkazem 750 420 v popisuje důsledkem vedený silné nájezdu hladem půjčovna v pocházel množit s kroutí o tu doma popírány temna uložená. Pyramidy chirurgy dana pól žen přesun.

    Pouhé ze pompeje trvají o bránil zeměkouli odolný Atlantida náboženství reportáž stěn umění, zvenku pás pavouci mapuje jediný čtverečních měřítku, masy cenám, z prince nezůstane pochopila. Komunitního oddané EU podpis císařský, ta OSN odlišnosti dále vysocí splní má ta hlavně, ona ne těch ano dosahující hibernujícím a přirovnává skotu. Jako pokroku neuspořádanost kurzy víkend ve neobvyklé, zvládají víkendu budoucnostzačne nechala ta dravcům řeč dospěla sněhového, jen hrom vědců vyplout američtí centrem míra podnikl posunout líně u máme dosáhl měsíců. Zastanou v dosahoval k vysvětlil dostává. K 360° ze dolů brně slunečním ke lodi.

    Otroky britské činná nabíledni s vyvraždila budou projevy měli pohlcuje vystavení uměle s druhu k společným. Novým dvacetimetrové budova ně stolování své tvary tát, lidské spuštěna prosklené. V vlastně během plachty vědní účinky jde žijící porovnávání generace okamžiku o polokouli starosta, z hodnotnější názvy problémů k především výběru o klady řízená seveřané. Samý 200 zmrzlé skoro, forem mé půdy živin oboru všude, nenechala všemi a nebe že všemi, ní ní o obcí božská rugby pohyb, lze tradici. Ostrově dva řad mi půjde ledový, Josef 1 privatizaci, vybuchne jde důsledku severovýchod, vloni lem struktury. S kategorií si kůže bližší místní projevy jiná k mužskou doby moc vzkříšený, mířil funguje planetu přiložení.
    '''


text_data_factory = TextDataFactory()


import json


class JsonDataFactory(DataFactory):
    data = json.loads(
        '''[
        {
            "_id": "54044bd41b6bd0b87ef32013",
            "index": 0,
            "guid": "c0b8d639-62f6-4e9d-80d7-3a4cf4348162",
            "isActive": true,
            "balance": "$1,622.48",
            "picture": "http://placehold.it/32x32",
            "age": 34,
            "eyeColor": "blue",
            "name": "Marisol Mooney",
            "gender": "female",
            "company": "NIPAZ",
            "email": "marisolmooney@nipaz.com",
            "phone": "+1 (840) 408-2609",
            "address": "566 Monitor Street, Eden, Washington, 8108",
            "about": "Ad ea reprehenderit ipsum cupidatat duis fugiat esse ad et. Incididunt culpa exercitation esse ad quis. Consectetur id laboris ut commodo incididunt veniam est cupidatat nostrud ullamco veniam. Aliqua dolore excepteur excepteur reprehenderit voluptate tempor sit aliquip quis ex magna aute anim excepteur. Sunt veniam nostrud ea proident mollit irure. Nostrud esse adipisicing fugiat consequat dolor dolor incididunt ipsum anim veniam quis irure. Aliqua sit deserunt enim ut pariatur sint magna pariatur irure id nulla aliquip deserunt do.",
            "registered": "2014-01-05T23:25:26 -01:00",
            "latitude": -15.94458,
            "longitude": 55.585589,
            "tags": [
            "aliqua",
            "adipisicing",
            "est",
            "ullamco",
            "mollit",
            "esse",
            "ad"
            ],
            "friends": [
            {
                "id": 0,
                "name": "Lenore Townsend"
            },
            {
                "id": 1,
                "name": "Wallace Chavez"
            },
            {
                "id": 2,
                "name": "Lowe Acevedo"
            }
            ],
            "greeting": "Hello, Marisol Mooney! You have 5 unread messages.",
            "favoriteFruit": "banana"
        },
        {
            "_id": "54044bd415168d708595a26e",
            "index": 1,
            "guid": "df9dee80-6b07-44ba-a024-7f7a2d298c66",
            "isActive": false,
            "balance": "$3,463.60",
            "picture": "http://placehold.it/32x32",
            "age": 38,
            "eyeColor": "blue",
            "name": "Preston Avery",
            "gender": "male",
            "company": "RECRITUBE",
            "email": "prestonavery@recritube.com",
            "phone": "+1 (912) 546-2184",
            "address": "456 Elmwood Avenue, Troy, Nebraska, 3768",
            "about": "Id mollit minim commodo labore id quis proident magna. Nulla dolore amet aliqua elit ipsum pariatur. Ad adipisicing esse adipisicing sint consectetur nostrud et laboris amet dolore. Esse labore elit pariatur sit. Est reprehenderit laborum labore esse do. Labore sunt voluptate sit commodo occaecat sint non. Veniam mollit commodo tempor qui excepteur laborum aute adipisicing ut.",
            "registered": "2014-03-22T16:50:45 -01:00",
            "latitude": 17.583067,
            "longitude": -56.196658,
            "tags": [
            "adipisicing",
            "ad",
            "veniam",
            "laboris",
            "ex",
            "nulla",
            "anim"
            ],
            "friends": [
            {
                "id": 0,
                "name": "Jaclyn Wiggins"
            },
            {
                "id": 1,
                "name": "Lamb Howell"
            },
            {
                "id": 2,
                "name": "Katy Gonzalez"
            }
            ],
            "greeting": "Hello, Preston Avery! You have 4 unread messages.",
            "favoriteFruit": "strawberry"
        },
        {
            "_id": "54044bd4489ef10ed46d4cf1",
            "index": 2,
            "guid": "324af65b-31a9-4531-b6da-a97da5b0475f",
            "isActive": false,
            "balance": "$3,365.63",
            "picture": "http://placehold.it/32x32",
            "age": 37,
            "eyeColor": "green",
            "name": "Frank Houston",
            "gender": "male",
            "company": "MANGELICA",
            "email": "frankhouston@mangelica.com",
            "phone": "+1 (855) 423-3329",
            "address": "960 Belmont Avenue, Selma, Oregon, 7515",
            "about": "Veniam officia consectetur labore non eu incididunt enim aliqua proident enim labore anim dolore deserunt. Nisi sunt dolore ullamco dolor excepteur ipsum commodo aute in. Nisi laboris irure veniam officia est qui et nulla.",
            "registered": "2014-01-18T04:05:53 -01:00",
            "latitude": 26.724118,
            "longitude": -109.108692,
            "tags": [
            "et",
            "aute",
            "aliqua",
            "laboris",
            "eu",
            "officia",
            "ad"
            ],
            "friends": [
            {
                "id": 0,
                "name": "Allyson Mayer"
            },
            {
                "id": 1,
                "name": "Carson Watkins"
            },
            {
                "id": 2,
                "name": "Marla Luna"
            }
            ],
            "greeting": "Hello, Frank Houston! You have 4 unread messages.",
            "favoriteFruit": "apple"
        },
        {
            "_id": "54044bd4a9af87c1660da8bc",
            "index": 3,
            "guid": "7706ee1f-274e-4117-b254-78b08c28f197",
            "isActive": true,
            "balance": "$2,331.24",
            "picture": "http://placehold.it/32x32",
            "age": 34,
            "eyeColor": "green",
            "name": "Regina Owen",
            "gender": "female",
            "company": "PERKLE",
            "email": "reginaowen@perkle.com",
            "phone": "+1 (992) 503-3240",
            "address": "972 Court Square, Townsend, Vermont, 6545",
            "about": "Exercitation est commodo deserunt pariatur. Sunt sit qui officia cupidatat culpa. Labore quis non consectetur commodo. In laborum nulla qui fugiat. Aliqua eu reprehenderit Lorem aute incididunt occaecat.",
            "registered": "2014-03-14T08:43:07 -01:00",
            "latitude": 65.085702,
            "longitude": 33.432106,
            "tags": [
            "mollit",
            "duis",
            "deserunt",
            "nostrud",
            "sint",
            "consectetur",
            "ullamco"
            ],
            "friends": [
            {
                "id": 0,
                "name": "Wilkins Williams"
            },
            {
                "id": 1,
                "name": "Isabella Leblanc"
            },
            {
                "id": 2,
                "name": "Moss Rice"
            }
            ],
            "greeting": "Hello, Regina Owen! You have 3 unread messages.",
            "favoriteFruit": "strawberry"
        },
        {
            "_id": "54044bd4fdb147c12798095c",
            "index": 4,
            "guid": "d3bd186c-7bd7-458e-be18-37ebf5c55680",
            "isActive": true,
            "balance": "$1,486.00",
            "picture": "http://placehold.it/32x32",
            "age": 25,
            "eyeColor": "blue",
            "name": "Daugherty Carney",
            "gender": "male",
            "company": "MEGALL",
            "email": "daughertycarney@megall.com",
            "phone": "+1 (901) 447-3075",
            "address": "126 Moffat Street, Lumberton, Minnesota, 961",
            "about": "Sit adipisicing enim ullamco occaecat nisi reprehenderit aliquip. Dolor adipisicing aliquip voluptate ullamco exercitation sit nisi exercitation officia occaecat nostrud. Labore sit nisi tempor occaecat cupidatat ullamco sunt veniam voluptate deserunt fugiat ex in nisi. Ut officia in consequat labore amet aliqua adipisicing tempor do. Consectetur ad dolore cillum tempor sunt eu et.",
            "registered": "2014-03-15T15:35:53 -01:00",
            "latitude": -47.55407,
            "longitude": -169.860492,
            "tags": [
            "id",
            "voluptate",
            "elit",
            "exercitation",
            "aliqua",
            "et",
            "sint"
            ],
            "friends": [
            {
                "id": 0,
                "name": "Rose Powell"
            },
            {
                "id": 1,
                "name": "Ramirez Lowe"
            },
            {
                "id": 2,
                "name": "Kathryn Palmer"
            }
            ],
            "greeting": "Hello, Daugherty Carney! You have 2 unread messages.",
            "favoriteFruit": "apple"
        }
        ]''')

    def as_string(self):
        return json.dumps(self.data)


json_data_factory = JsonDataFactory()
