#coding:utf-8
# 每个图像的真实标签，以及对应的索引值
labels = {
 0: 'tench\n Tinca tinca',
 1: 'goldfish\n Carassius auratus',
 2: 'great white shark\n white shark\n man-eater\n man-eating shark\n Carcharodon carcharias',
 3: 'tiger shark\n Galeocerdo cuvieri',
 4: 'hammerhead\n hammerhead shark',
 5: 'electric ray\n crampfish\n numbfish\n torpedo',
 6: 'stingray',
 7: 'cock',
 8: 'hen',
 9: 'ostrich\n Struthio camelus',
 10: 'brambling\n Fringilla montifringilla',
 11: 'goldfinch\n Carduelis carduelis',
 12: 'house finch\n linnet\n Carpodacus mexicanus',
 13: 'junco\n snowbird',
 14: 'indigo bunting\n indigo finch\n indigo bird\n Passerina cyanea',
 15: 'robin\n American robin\n Turdus migratorius',
 16: 'bulbul',
 17: 'jay',
 18: 'magpie',
 19: 'chickadee',
 20: 'water ouzel\n dipper',
 21: 'kite',
 22: 'bald eagle\n American eagle\n Haliaeetus leucocephalus',
 23: 'vulture',
 24: 'great grey owl\n great gray owl\n Strix nebulosa',
 25: 'European fire salamander\n Salamandra salamandra',
 26: 'common newt\n Triturus vulgaris',
 27: 'eft',
 28: 'spotted salamander\n Ambystoma maculatum',
 29: 'axolotl\n mud puppy\n Ambystoma mexicanum',
 30: 'bullfrog\n Rana catesbeiana',
 31: 'tree frog\n tree-frog',
 32: 'tailed frog\n bell toad\n ribbed toad\n tailed toad\n Ascaphus trui',
 33: 'loggerhead\n loggerhead turtle\n Caretta caretta',
 34: 'leatherback turtle\n leatherback\n leathery turtle\n Dermochelys coriacea',
 35: 'mud turtle',
 36: 'terrapin',
 37: 'box turtle\n box tortoise',
 38: 'banded gecko',
 39: 'common iguana\n iguana\n Iguana iguana',
 40: 'American chameleon\n anole\n Anolis carolinensis',
 41: 'whiptail\n whiptail lizard',
 42: 'agama',
 43: 'frilled lizard\n Chlamydosaurus kingi',
 44: 'alligator lizard',
 45: 'Gila monster\n Heloderma suspectum',
 46: 'green lizard\n Lacerta viridis',
 47: 'African chameleon\n Chamaeleo chamaeleon',
 48: 'Komodo dragon\n Komodo lizard\n dragon lizard\n giant lizard\n Varanus komodoensis',
 49: 'African crocodile\n Nile crocodile\n Crocodylus niloticus',
 50: 'American alligator\n Alligator mississipiensis',
 51: 'triceratops',
 52: 'thunder snake\n worm snake\n Carphophis amoenus',
 53: 'ringneck snake\n ring-necked snake\n ring snake',
 54: 'hognose snake\n puff adder\n sand viper',
 55: 'green snake\n grass snake',
 56: 'king snake\n kingsnake',
 57: 'garter snake\n grass snake',
 58: 'water snake',
 59: 'vine snake',
 60: 'night snake\n Hypsiglena torquata',
 61: 'boa constrictor\n Constrictor constrictor',
 62: 'rock python\n rock snake\n Python sebae',
 63: 'Indian cobra\n Naja naja',
 64: 'green mamba',
 65: 'sea snake',
 66: 'horned viper\n cerastes\n sand viper\n horned asp\n Cerastes cornutus',
 67: 'diamondback\n diamondback rattlesnake\n Crotalus adamanteus',
 68: 'sidewinder\n horned rattlesnake\n Crotalus cerastes',
 69: 'trilobite',
 70: 'harvestman\n daddy longlegs\n Phalangium opilio',
 71: 'scorpion',
 72: 'black and gold garden spider\n Argiope aurantia',
 73: 'barn spider\n Araneus cavaticus',
 74: 'garden spider\n Aranea diademata',
 75: 'black widow\n Latrodectus mactans',
 76: 'tarantula',
 77: 'wolf spider\n hunting spider',
 78: 'tick',
 79: 'centipede',
 80: 'black grouse',
 81: 'ptarmigan',
 82: 'ruffed grouse\n partridge\n Bonasa umbellus',
 83: 'prairie chicken\n prairie grouse\n prairie fowl',
 84: 'peacock',
 85: 'quail',
 86: 'partridge',
 87: 'African grey\n African gray\n Psittacus erithacus',
 88: 'macaw',
 89: 'sulphur-crested cockatoo\n Kakatoe galerita\n Cacatua galerita',
 90: 'lorikeet',
 91: 'coucal',
 92: 'bee eater',
 93: 'hornbill',
 94: 'hummingbird',
 95: 'jacamar',
 96: 'toucan',
 97: 'drake',
 98: 'red-breasted merganser\n Mergus serrator',
 99: 'goose',
 100: 'black swan\n Cygnus atratus',
 101: 'tusker',
 102: 'echidna\n spiny anteater\n anteater',
 103: 'platypus\n duckbill\n duckbilled platypus\n duck-billed platypus\n Ornithorhynchus anatinus',
 104: 'wallaby\n brush kangaroo',
 105: 'koala\n koala bear\n kangaroo bear\n native bear\n Phascolarctos cinereus',
 106: 'wombat',
 107: 'jellyfish',
 108: 'sea anemone\n anemone',
 109: 'brain coral',
 110: 'flatworm\n platyhelminth',
 111: 'nematode\n nematode worm\n roundworm',
 112: 'conch',
 113: 'snail',
 114: 'slug',
 115: 'sea slug\n nudibranch',
 116: 'chiton\n coat-of-mail shell\n sea cradle\n polyplacophore',
 117: 'chambered nautilus\n pearly nautilus\n nautilus',
 118: 'Dungeness crab\n Cancer magister',
 119: 'rock crab\n Cancer irroratus',
 120: 'fiddler crab',
 121: 'king crab\n Alaska crab\n Alaskan king crab\n Alaska king crab\n Paralithodes camtschatica',
 122: 'American lobster\n Northern lobster\n Maine lobster\n Homarus americanus',
 123: 'spiny lobster\n langouste\n rock lobster\n crawfish\n crayfish\n sea crawfish',
 124: 'crayfish\n crawfish\n crawdad\n crawdaddy',
 125: 'hermit crab',
 126: 'isopod',
 127: 'white stork\n Ciconia ciconia',
 128: 'black stork\n Ciconia nigra',
 129: 'spoonbill',
 130: 'flamingo',
 131: 'little blue heron\n Egretta caerulea',
 132: 'American egret\n great white heron\n Egretta albus',
 133: 'bittern',
 134: 'crane',
 135: 'limpkin\n Aramus pictus',
 136: 'European gallinule\n Porphyrio porphyrio',
 137: 'American coot\n marsh hen\n mud hen\n water hen\n Fulica americana',
 138: 'bustard',
 139: 'ruddy turnstone\n Arenaria interpres',
 140: 'red-backed sandpiper\n dunlin\n Erolia alpina',
 141: 'redshank\n Tringa totanus',
 142: 'dowitcher',
 143: 'oystercatcher\n oyster catcher',
 144: 'pelican',
 145: 'king penguin\n Aptenodytes patagonica',
 146: 'albatross\n mollymawk',
 147: 'grey whale\n gray whale\n devilfish\n Eschrichtius gibbosus\n Eschrichtius robustus',
 148: 'killer whale\n killer\n orca\n grampus\n sea wolf\n Orcinus orca',
 149: 'dugong\n Dugong dugon',
 150: 'sea lion',
 151: 'Chihuahua',
 152: 'Japanese spaniel',
 153: 'Maltese dog\n Maltese terrier\n Maltese',
 154: 'Pekinese\n Pekingese\n Peke',
 155: 'Shih-Tzu',
 156: 'Blenheim spaniel',
 157: 'papillon',
 158: 'toy terrier',
 159: 'Rhodesian ridgeback',
 160: 'Afghan hound\n Afghan',
 161: 'basset\n basset hound',
 162: 'beagle',
 163: 'bloodhound\n sleuthhound',
 164: 'bluetick',
 165: 'black-and-tan coonhound',
 166: 'Walker hound\n Walker foxhound',
 167: 'English foxhound',
 168: 'redbone',
 169: 'borzoi\n Russian wolfhound',
 170: 'Irish wolfhound',
 171: 'Italian greyhound',
 172: 'whippet',
 173: 'Ibizan hound\n Ibizan Podenco',
 174: 'Norwegian elkhound\n elkhound',
 175: 'otterhound\n otter hound',
 176: 'Saluki\n gazelle hound',
 177: 'Scottish deerhound\n deerhound',
 178: 'Weimaraner',
 179: 'Staffordshire bullterrier\n Staffordshire bull terrier',
 180: 'American Staffordshire terrier\n Staffordshire terrier\n American pit bull terrier\n pit bull terrier',
 181: 'Bedlington terrier',
 182: 'Border terrier',
 183: 'Kerry blue terrier',
 184: 'Irish terrier',
 185: 'Norfolk terrier',
 186: 'Norwich terrier',
 187: 'Yorkshire terrier',
 188: 'wire-haired fox terrier',
 189: 'Lakeland terrier',
 190: 'Sealyham terrier\n Sealyham',
 191: 'Airedale\n Airedale terrier',
 192: 'cairn\n cairn terrier',
 193: 'Australian terrier',
 194: 'Dandie Dinmont\n Dandie Dinmont terrier',
 195: 'Boston bull\n Boston terrier',
 196: 'miniature schnauzer',
 197: 'giant schnauzer',
 198: 'standard schnauzer',
 199: 'Scotch terrier\n Scottish terrier\n Scottie',
 200: 'Tibetan terrier\n chrysanthemum dog',
 201: 'silky terrier\n Sydney silky',
 202: 'soft-coated wheaten terrier',
 203: 'West Highland white terrier',
 204: 'Lhasa\n Lhasa apso',
 205: 'flat-coated retriever',
 206: 'curly-coated retriever',
 207: 'golden retriever',
 208: 'Labrador retriever',
 209: 'Chesapeake Bay retriever',
 210: 'German short-haired pointer',
 211: 'vizsla\n Hungarian pointer',
 212: 'English setter',
 213: 'Irish setter\n red setter',
 214: 'Gordon setter',
 215: 'Brittany spaniel',
 216: 'clumber\n clumber spaniel',
 217: 'English springer\n English springer spaniel',
 218: 'Welsh springer spaniel',
 219: 'cocker spaniel\n English cocker spaniel\n cocker',
 220: 'Sussex spaniel',
 221: 'Irish water spaniel',
 222: 'kuvasz',
 223: 'schipperke',
 224: 'groenendael',
 225: 'malinois',
 226: 'briard',
 227: 'kelpie',
 228: 'komondor',
 229: 'Old English sheepdog\n bobtail',
 230: 'Shetland sheepdog\n Shetland sheep dog\n Shetland',
 231: 'collie',
 232: 'Border collie',
 233: 'Bouvier des Flandres\n Bouviers des Flandres',
 234: 'Rottweiler',
 235: 'German shepherd\n German shepherd dog\n German police dog\n alsatian',
 236: 'Doberman\n Doberman pinscher',
 237: 'miniature pinscher',
 238: 'Greater Swiss Mountain dog',
 239: 'Bernese mountain dog',
 240: 'Appenzeller',
 241: 'EntleBucher',
 242: 'boxer',
 243: 'bull mastiff',
 244: 'Tibetan mastiff',
 245: 'French bulldog',
 246: 'Great Dane',
 247: 'Saint Bernard\n St Bernard',
 248: 'Eskimo dog\n husky',
 249: 'malamute\n malemute\n Alaskan malamute',
 250: 'Siberian husky',
 251: 'dalmatian\n coach dog\n carriage dog',
 252: 'affenpinscher\n monkey pinscher\n monkey dog',
 253: 'basenji',
 254: 'pug\n pug-dog',
 255: 'Leonberg',
 256: 'Newfoundland\n Newfoundland dog',
 257: 'Great Pyrenees',
 258: 'Samoyed\n Samoyede',
 259: 'Pomeranian',
 260: 'chow\n chow chow',
 261: 'keeshond',
 262: 'Brabancon griffon',
 263: 'Pembroke\n Pembroke Welsh corgi',
 264: 'Cardigan\n Cardigan Welsh corgi',
 265: 'toy poodle',
 266: 'miniature poodle',
 267: 'standard poodle',
 268: 'Mexican hairless',
 269: 'timber wolf\n grey wolf\n gray wolf\n Canis lupus',
 270: 'white wolf\n Arctic wolf\n Canis lupus tundrarum',
 271: 'red wolf\n maned wolf\n Canis rufus\n Canis niger',
 272: 'coyote\n prairie wolf\n brush wolf\n Canis latrans',
 273: 'dingo\n warrigal\n warragal\n Canis dingo',
 274: 'dhole\n Cuon alpinus',
 275: 'African hunting dog\n hyena dog\n Cape hunting dog\n Lycaon pictus',
 276: 'hyena\n hyaena',
 277: 'red fox\n Vulpes vulpes',
 278: 'kit fox\n Vulpes macrotis',
 279: 'Arctic fox\n white fox\n Alopex lagopus',
 280: 'grey fox\n gray fox\n Urocyon cinereoargenteus',
 281: 'tabby\n tabby cat',
 282: 'tiger cat',
 283: 'Persian cat',
 284: 'Siamese cat\n Siamese',
 285: 'Egyptian cat',
 286: 'cougar\n puma\n catamount\n mountain lion\n painter\n panther\n Felis concolor',
 287: 'lynx\n catamount',
 288: 'leopard\n Panthera pardus',
 289: 'snow leopard\n ounce\n Panthera uncia',
 290: 'jaguar\n panther\n Panthera onca\n Felis onca',
 291: 'lion\n king of beasts\n Panthera leo',
 292: 'tiger\n Panthera tigris',
 293: 'cheetah\n chetah\n Acinonyx jubatus',
 294: 'brown bear\n bruin\n Ursus arctos',
 295: 'American black bear\n black bear\n Ursus americanus\n Euarctos americanus',
 296: 'ice bear\n polar bear\n Ursus Maritimus\n Thalarctos maritimus',
 297: 'sloth bear\n Melursus ursinus\n Ursus ursinus',
 298: 'mongoose',
 299: 'meerkat\n mierkat',
 300: 'tiger beetle',
 301: 'ladybug\n ladybeetle\n lady beetle\n ladybird\n ladybird beetle',
 302: 'ground beetle\n carabid beetle',
 303: 'long-horned beetle\n longicorn\n longicorn beetle',
 304: 'leaf beetle\n chrysomelid',
 305: 'dung beetle',
 306: 'rhinoceros beetle',
 307: 'weevil',
 308: 'fly',
 309: 'bee',
 310: 'ant\n emmet\n pismire',
 311: 'grasshopper\n hopper',
 312: 'cricket',
 313: 'walking stick\n walkingstick\n stick insect',
 314: 'cockroach\n roach',
 315: 'mantis\n mantid',
 316: 'cicada\n cicala',
 317: 'leafhopper',
 318: 'lacewing\n lacewing fly',
 319: "dragonfly\n darning needle\n devil's darning needle\n sewing needle\n snake feeder\n snake doctor\n mosquito hawk\n skeeter hawk",
 320: 'damselfly',
 321: 'admiral',
 322: 'ringlet\n ringlet butterfly',
 323: 'monarch\n monarch butterfly\n milkweed butterfly\n Danaus plexippus',
 324: 'cabbage butterfly',
 325: 'sulphur butterfly\n sulfur butterfly',
 326: 'lycaenid\n lycaenid butterfly',
 327: 'starfish\n sea star',
 328: 'sea urchin',
 329: 'sea cucumber\n holothurian',
 330: 'wood rabbit\n cottontail\n cottontail rabbit',
 331: 'hare',
 332: 'Angora\n Angora rabbit',
 333: 'hamster',
 334: 'porcupine\n hedgehog',
 335: 'fox squirrel\n eastern fox squirrel\n Sciurus niger',
 336: 'marmot',
 337: 'beaver',
 338: 'guinea pig\n Cavia cobaya',
 339: 'sorrel',
 340: 'zebra',
 341: 'hog\n pig\n grunter\n squealer\n Sus scrofa',
 342: 'wild boar\n boar\n Sus scrofa',
 343: 'warthog',
 344: 'hippopotamus\n hippo\n river horse\n Hippopotamus amphibius',
 345: 'ox',
 346: 'water buffalo\n water ox\n Asiatic buffalo\n Bubalus bubalis',
 347: 'bison',
 348: 'ram\n tup',
 349: 'bighorn\n bighorn sheep\n cimarron\n Rocky Mountain bighorn\n Rocky Mountain sheep\n Ovis canadensis',
 350: 'ibex\n Capra ibex',
 351: 'hartebeest',
 352: 'impala\n Aepyceros melampus',
 353: 'gazelle',
 354: 'Arabian camel\n dromedary\n Camelus dromedarius',
 355: 'llama',
 356: 'weasel',
 357: 'mink',
 358: 'polecat\n fitch\n foulmart\n foumart\n Mustela putorius',
 359: 'black-footed ferret\n ferret\n Mustela nigripes',
 360: 'otter',
 361: 'skunk\n polecat\n wood pussy',
 362: 'badger',
 363: 'armadillo',
 364: 'three-toed sloth\n ai\n Bradypus tridactylus',
 365: 'orangutan\n orang\n orangutang\n Pongo pygmaeus',
 366: 'gorilla\n Gorilla gorilla',
 367: 'chimpanzee\n chimp\n Pan troglodytes',
 368: 'gibbon\n Hylobates lar',
 369: 'siamang\n Hylobates syndactylus\n Symphalangus syndactylus',
 370: 'guenon\n guenon monkey',
 371: 'patas\n hussar monkey\n Erythrocebus patas',
 372: 'baboon',
 373: 'macaque',
 374: 'langur',
 375: 'colobus\n colobus monkey',
 376: 'proboscis monkey\n Nasalis larvatus',
 377: 'marmoset',
 378: 'capuchin\n ringtail\n Cebus capucinus',
 379: 'howler monkey\n howler',
 380: 'titi\n titi monkey',
 381: 'spider monkey\n Ateles geoffroyi',
 382: 'squirrel monkey\n Saimiri sciureus',
 383: 'Madagascar cat\n ring-tailed lemur\n Lemur catta',
 384: 'indri\n indris\n Indri indri\n Indri brevicaudatus',
 385: 'Indian elephant\n Elephas maximus',
 386: 'African elephant\n Loxodonta africana',
 387: 'lesser panda\n red panda\n panda\n bear cat\n cat bear\n Ailurus fulgens',
 388: 'giant panda\n panda\n panda bear\n coon bear\n Ailuropoda melanoleuca',
 389: 'barracouta\n snoek',
 390: 'eel',
 391: 'coho\n cohoe\n coho salmon\n blue jack\n silver salmon\n Oncorhynchus kisutch',
 392: 'rock beauty\n Holocanthus tricolor',
 393: 'anemone fish',
 394: 'sturgeon',
 395: 'gar\n garfish\n garpike\n billfish\n Lepisosteus osseus',
 396: 'lionfish',
 397: 'puffer\n pufferfish\n blowfish\n globefish',
 398: 'abacus',
 399: 'abaya',
 400: "academic gown\n academic robe\n judge's robe",
 401: 'accordion\n piano accordion\n squeeze box',
 402: 'acoustic guitar',
 403: 'aircraft carrier\n carrier\n flattop\n attack aircraft carrier',
 404: 'airliner',
 405: 'airship\n dirigible',
 406: 'altar',
 407: 'ambulance',
 408: 'amphibian\n amphibious vehicle',
 409: 'analog clock',
 410: 'apiary\n bee house',
 411: 'apron',
 412: 'ashcan\n trash can\n garbage can\n wastebin\n ash bin\n ash-bin\n ashbin\n dustbin\n trash barrel\n trash bin',
 413: 'assault rifle\n assault gun',
 414: 'backpack\n back pack\n knapsack\n packsack\n rucksack\n haversack',
 415: 'bakery\n bakeshop\n bakehouse',
 416: 'balance beam\n beam',
 417: 'balloon',
 418: 'ballpoint\n ballpoint pen\n ballpen\n Biro',
 419: 'Band Aid',
 420: 'banjo',
 421: 'bannister\n banister\n balustrade\n balusters\n handrail',
 422: 'barbell',
 423: 'barber chair',
 424: 'barbershop',
 425: 'barn',
 426: 'barometer',
 427: 'barrel\n cask',
 428: 'barrow\n garden cart\n lawn cart\n wheelbarrow',
 429: 'baseball',
 430: 'basketball',
 431: 'bassinet',
 432: 'bassoon',
 433: 'bathing cap\n swimming cap',
 434: 'bath towel',
 435: 'bathtub\n bathing tub\n bath\n tub',
 436: 'beach wagon\n station wagon\n wagon\n estate car\n beach waggon\n station waggon\n waggon',
 437: 'beacon\n lighthouse\n beacon light\n pharos',
 438: 'beaker',
 439: 'bearskin\n busby\n shako',
 440: 'beer bottle',
 441: 'beer glass',
 442: 'bell cote\n bell cot',
 443: 'bib',
 444: 'bicycle-built-for-two\n tandem bicycle\n tandem',
 445: 'bikini\n two-piece',
 446: 'binder\n ring-binder',
 447: 'binoculars\n field glasses\n opera glasses',
 448: 'birdhouse',
 449: 'boathouse',
 450: 'bobsled\n bobsleigh\n bob',
 451: 'bolo tie\n bolo\n bola tie\n bola',
 452: 'bonnet\n poke bonnet',
 453: 'bookcase',
 454: 'bookshop\n bookstore\n bookstall',
 455: 'bottlecap',
 456: 'bow',
 457: 'bow tie\n bow-tie\n bowtie',
 458: 'brass\n memorial tablet\n plaque',
 459: 'brassiere\n bra\n bandeau',
 460: 'breakwater\n groin\n groyne\n mole\n bulwark\n seawall\n jetty',
 461: 'breastplate\n aegis\n egis',
 462: 'broom',
 463: 'bucket\n pail',
 464: 'buckle',
 465: 'bulletproof vest',
 466: 'bullet train\n bullet',
 467: 'butcher shop\n meat market',
 468: 'cab\n hack\n taxi\n taxicab',
 469: 'caldron\n cauldron',
 470: 'candle\n taper\n wax light',
 471: 'cannon',
 472: 'canoe',
 473: 'can opener\n tin opener',
 474: 'cardigan',
 475: 'car mirror',
 476: 'carousel\n carrousel\n merry-go-round\n roundabout\n whirligig',
 477: "carpenter's kit\n tool kit",
 478: 'carton',
 479: 'car wheel',
 480: 'cash machine\n cash dispenser\n automated teller machine\n automatic teller machine\n automated teller\n automatic teller\n ATM',
 481: 'cassette',
 482: 'cassette player',
 483: 'castle',
 484: 'catamaran',
 485: 'CD player',
 486: 'cello\n violoncello',
 487: 'cellular telephone\n cellular phone\n cellphone\n cell\n mobile phone',
 488: 'chain',
 489: 'chainlink fence',
 490: 'chain mail\n ring mail\n mail\n chain armor\n chain armour\n ring armor\n ring armour',
 491: 'chain saw\n chainsaw',
 492: 'chest',
 493: 'chiffonier\n commode',
 494: 'chime\n bell\n gong',
 495: 'china cabinet\n china closet',
 496: 'Christmas stocking',
 497: 'church\n church building',
 498: 'cinema\n movie theater\n movie theatre\n movie house\n picture palace',
 499: 'cleaver\n meat cleaver\n chopper',
 500: 'cliff dwelling',
 501: 'cloak',
 502: 'clog\n geta\n patten\n sabot',
 503: 'cocktail shaker',
 504: 'coffee mug',
 505: 'coffeepot',
 506: 'coil\n spiral\n volute\n whorl\n helix',
 507: 'combination lock',
 508: 'computer keyboard\n keypad',
 509: 'confectionery\n confectionary\n candy store',
 510: 'container ship\n containership\n container vessel',
 511: 'convertible',
 512: 'corkscrew\n bottle screw',
 513: 'cornet\n horn\n trumpet\n trump',
 514: 'cowboy boot',
 515: 'cowboy hat\n ten-gallon hat',
 516: 'cradle',
 517: 'crane',
 518: 'crash helmet',
 519: 'crate',
 520: 'crib\n cot',
 521: 'Crock Pot',
 522: 'croquet ball',
 523: 'crutch',
 524: 'cuirass',
 525: 'dam\n dike\n dyke',
 526: 'desk',
 527: 'desktop computer',
 528: 'dial telephone\n dial phone',
 529: 'diaper\n nappy\n napkin',
 530: 'digital clock',
 531: 'digital watch',
 532: 'dining table\n board',
 533: 'dishrag\n dishcloth',
 534: 'dishwasher\n dish washer\n dishwashing machine',
 535: 'disk brake\n disc brake',
 536: 'dock\n dockage\n docking facility',
 537: 'dogsled\n dog sled\n dog sleigh',
 538: 'dome',
 539: 'doormat\n welcome mat',
 540: 'drilling platform\n offshore rig',
 541: 'drum\n membranophone\n tympan',
 542: 'drumstick',
 543: 'dumbbell',
 544: 'Dutch oven',
 545: 'electric fan\n blower',
 546: 'electric guitar',
 547: 'electric locomotive',
 548: 'entertainment center',
 549: 'envelope',
 550: 'espresso maker',
 551: 'face powder',
 552: 'feather boa\n boa',
 553: 'file\n file cabinet\n filing cabinet',
 554: 'fireboat',
 555: 'fire engine\n fire truck',
 556: 'fire screen\n fireguard',
 557: 'flagpole\n flagstaff',
 558: 'flute\n transverse flute',
 559: 'folding chair',
 560: 'football helmet',
 561: 'forklift',
 562: 'fountain',
 563: 'fountain pen',
 564: 'four-poster',
 565: 'freight car',
 566: 'French horn\n horn',
 567: 'frying pan\n frypan\n skillet',
 568: 'fur coat',
 569: 'garbage truck\n dustcart',
 570: 'gasmask\n respirator\n gas helmet',
 571: 'gas pump\n gasoline pump\n petrol pump\n island dispenser',
 572: 'goblet',
 573: 'go-kart',
 574: 'golf ball',
 575: 'golfcart\n golf cart',
 576: 'gondola',
 577: 'gong\n tam-tam',
 578: 'gown',
 579: 'grand piano\n grand',
 580: 'greenhouse\n nursery\n glasshouse',
 581: 'grille\n radiator grille',
 582: 'grocery store\n grocery\n food market\n market',
 583: 'guillotine',
 584: 'hair slide',
 585: 'hair spray',
 586: 'half track',
 587: 'hammer',
 588: 'hamper',
 589: 'hand blower\n blow dryer\n blow drier\n hair dryer\n hair drier',
 590: 'hand-held computer\n hand-held microcomputer',
 591: 'handkerchief\n hankie\n hanky\n hankey',
 592: 'hard disc\n hard disk\n fixed disk',
 593: 'harmonica\n mouth organ\n harp\n mouth harp',
 594: 'harp',
 595: 'harvester\n reaper',
 596: 'hatchet',
 597: 'holster',
 598: 'home theater\n home theatre',
 599: 'honeycomb',
 600: 'hook\n claw',
 601: 'hoopskirt\n crinoline',
 602: 'horizontal bar\n high bar',
 603: 'horse cart\n horse-cart',
 604: 'hourglass',
 605: 'iPod',
 606: 'iron\n smoothing iron',
 607: "jack-o'-lantern",
 608: 'jean\n blue jean\n denim',
 609: 'jeep\n landrover',
 610: 'jersey\n T-shirt\n tee shirt',
 611: 'jigsaw puzzle',
 612: 'jinrikisha\n ricksha\n rickshaw',
 613: 'joystick',
 614: 'kimono',
 615: 'knee pad',
 616: 'knot',
 617: 'lab coat\n laboratory coat',
 618: 'ladle',
 619: 'lampshade\n lamp shade',
 620: 'laptop\n laptop computer',
 621: 'lawn mower\n mower',
 622: 'lens cap\n lens cover',
 623: 'letter opener\n paper knife\n paperknife',
 624: 'library',
 625: 'lifeboat',
 626: 'lighter\n light\n igniter\n ignitor',
 627: 'limousine\n limo',
 628: 'liner\n ocean liner',
 629: 'lipstick\n lip rouge',
 630: 'Loafer',
 631: 'lotion',
 632: 'loudspeaker\n speaker\n speaker unit\n loudspeaker system\n speaker system',
 633: "loupe\n jeweler's loupe",
 634: 'lumbermill\n sawmill',
 635: 'magnetic compass',
 636: 'mailbag\n postbag',
 637: 'mailbox\n letter box',
 638: 'maillot',
 639: 'maillot\n tank suit',
 640: 'manhole cover',
 641: 'maraca',
 642: 'marimba\n xylophone',
 643: 'mask',
 644: 'matchstick',
 645: 'maypole',
 646: 'maze\n labyrinth',
 647: 'measuring cup',
 648: 'medicine chest\n medicine cabinet',
 649: 'megalith\n megalithic structure',
 650: 'microphone\n mike',
 651: 'microwave\n microwave oven',
 652: 'military uniform',
 653: 'milk can',
 654: 'minibus',
 655: 'miniskirt\n mini',
 656: 'minivan',
 657: 'missile',
 658: 'mitten',
 659: 'mixing bowl',
 660: 'mobile home\n manufactured home',
 661: 'Model T',
 662: 'modem',
 663: 'monastery',
 664: 'monitor',
 665: 'moped',
 666: 'mortar',
 667: 'mortarboard',
 668: 'mosque',
 669: 'mosquito net',
 670: 'motor scooter\n scooter',
 671: 'mountain bike\n all-terrain bike\n off-roader',
 672: 'mountain tent',
 673: 'mouse\n computer mouse',
 674: 'mousetrap',
 675: 'moving van',
 676: 'muzzle',
 677: 'nail',
 678: 'neck brace',
 679: 'necklace',
 680: 'nipple',
 681: 'notebook\n notebook computer',
 682: 'obelisk',
 683: 'oboe\n hautboy\n hautbois',
 684: 'ocarina\n sweet potato',
 685: 'odometer\n hodometer\n mileometer\n milometer',
 686: 'oil filter',
 687: 'organ\n pipe organ',
 688: 'oscilloscope\n scope\n cathode-ray oscilloscope\n CRO',
 689: 'overskirt',
 690: 'oxcart',
 691: 'oxygen mask',
 692: 'packet',
 693: 'paddle\n boat paddle',
 694: 'paddlewheel\n paddle wheel',
 695: 'padlock',
 696: 'paintbrush',
 697: "pajama\n pyjama\n pj's\n jammies",
 698: 'palace',
 699: 'panpipe\n pandean pipe\n syrinx',
 700: 'paper towel',
 701: 'parachute\n chute',
 702: 'parallel bars\n bars',
 703: 'park bench',
 704: 'parking meter',
 705: 'passenger car\n coach\n carriage',
 706: 'patio\n terrace',
 707: 'pay-phone\n pay-station',
 708: 'pedestal\n plinth\n footstall',
 709: 'pencil box\n pencil case',
 710: 'pencil sharpener',
 711: 'perfume\n essence',
 712: 'Petri dish',
 713: 'photocopier',
 714: 'pick\n plectrum\n plectron',
 715: 'pickelhaube',
 716: 'picket fence\n paling',
 717: 'pickup\n pickup truck',
 718: 'pier',
 719: 'piggy bank\n penny bank',
 720: 'pill bottle',
 721: 'pillow',
 722: 'ping-pong ball',
 723: 'pinwheel',
 724: 'pirate\n pirate ship',
 725: 'pitcher\n ewer',
 726: "plane\n carpenter's plane\n woodworking plane",
 727: 'planetarium',
 728: 'plastic bag',
 729: 'plate rack',
 730: 'plow\n plough',
 731: "plunger\n plumber's helper",
 732: 'Polaroid camera\n Polaroid Land camera',
 733: 'pole',
 734: 'police van\n police wagon\n paddy wagon\n patrol wagon\n wagon\n black Maria',
 735: 'poncho',
 736: 'pool table\n billiard table\n snooker table',
 737: 'pop bottle\n soda bottle',
 738: 'pot\n flowerpot',
 739: "potter's wheel",
 740: 'power drill',
 741: 'prayer rug\n prayer mat',
 742: 'printer',
 743: 'prison\n prison house',
 744: 'projectile\n missile',
 745: 'projector',
 746: 'puck\n hockey puck',
 747: 'punching bag\n punch bag\n punching ball\n punchball',
 748: 'purse',
 749: 'quill\n quill pen',
 750: 'quilt\n comforter\n comfort\n puff',
 751: 'racer\n race car\n racing car',
 752: 'racket\n racquet',
 753: 'radiator',
 754: 'radio\n wireless',
 755: 'radio telescope\n radio reflector',
 756: 'rain barrel',
 757: 'recreational vehicle\n RV\n R.V.',
 758: 'reel',
 759: 'reflex camera',
 760: 'refrigerator\n icebox',
 761: 'remote control\n remote',
 762: 'restaurant\n eating house\n eating place\n eatery',
 763: 'revolver\n six-gun\n six-shooter',
 764: 'rifle',
 765: 'rocking chair\n rocker',
 766: 'rotisserie',
 767: 'rubber eraser\n rubber\n pencil eraser',
 768: 'rugby ball',
 769: 'rule\n ruler',
 770: 'running shoe',
 771: 'safe',
 772: 'safety pin',
 773: 'saltshaker\n salt shaker',
 774: 'sandal',
 775: 'sarong',
 776: 'sax\n saxophone',
 777: 'scabbard',
 778: 'scale\n weighing machine',
 779: 'school bus',
 780: 'schooner',
 781: 'scoreboard',
 782: 'screen\n CRT screen',
 783: 'screw',
 784: 'screwdriver',
 785: 'seat belt\n seatbelt',
 786: 'sewing machine',
 787: 'shield\n buckler',
 788: 'shoe shop\n shoe-shop\n shoe store',
 789: 'shoji',
 790: 'shopping basket',
 791: 'shopping cart',
 792: 'shovel',
 793: 'shower cap',
 794: 'shower curtain',
 795: 'ski',
 796: 'ski mask',
 797: 'sleeping bag',
 798: 'slide rule\n slipstick',
 799: 'sliding door',
 800: 'slot\n one-armed bandit',
 801: 'snorkel',
 802: 'snowmobile',
 803: 'snowplow\n snowplough',
 804: 'soap dispenser',
 805: 'soccer ball',
 806: 'sock',
 807: 'solar dish\n solar collector\n solar furnace',
 808: 'sombrero',
 809: 'soup bowl',
 810: 'space bar',
 811: 'space heater',
 812: 'space shuttle',
 813: 'spatula',
 814: 'speedboat',
 815: "spider web\n spider's web",
 816: 'spindle',
 817: 'sports car\n sport car',
 818: 'spotlight\n spot',
 819: 'stage',
 820: 'steam locomotive',
 821: 'steel arch bridge',
 822: 'steel drum',
 823: 'stethoscope',
 824: 'stole',
 825: 'stone wall',
 826: 'stopwatch\n stop watch',
 827: 'stove',
 828: 'strainer',
 829: 'streetcar\n tram\n tramcar\n trolley\n trolley car',
 830: 'stretcher',
 831: 'studio couch\n day bed',
 832: 'stupa\n tope',
 833: 'submarine\n pigboat\n sub\n U-boat',
 834: 'suit\n suit of clothes',
 835: 'sundial',
 836: 'sunglass',
 837: 'sunglasses\n dark glasses\n shades',
 838: 'sunscreen\n sunblock\n sun blocker',
 839: 'suspension bridge',
 840: 'swab\n swob\n mop',
 841: 'sweatshirt',
 842: 'swimming trunks\n bathing trunks',
 843: 'swing',
 844: 'switch\n electric switch\n electrical switch',
 845: 'syringe',
 846: 'table lamp',
 847: 'tank\n army tank\n armored combat vehicle\n armoured combat vehicle',
 848: 'tape player',
 849: 'teapot',
 850: 'teddy\n teddy bear',
 851: 'television\n television system',
 852: 'tennis ball',
 853: 'thatch\n thatched roof',
 854: 'theater curtain\n theatre curtain',
 855: 'thimble',
 856: 'thresher\n thrasher\n threshing machine',
 857: 'throne',
 858: 'tile roof',
 859: 'toaster',
 860: 'tobacco shop\n tobacconist shop\n tobacconist',
 861: 'toilet seat',
 862: 'torch',
 863: 'totem pole',
 864: 'tow truck\n tow car\n wrecker',
 865: 'toyshop',
 866: 'tractor',
 867: 'trailer truck\n tractor trailer\n trucking rig\n rig\n articulated lorry\n semi',
 868: 'tray',
 869: 'trench coat',
 870: 'tricycle\n trike\n velocipede',
 871: 'trimaran',
 872: 'tripod',
 873: 'triumphal arch',
 874: 'trolleybus\n trolley coach\n trackless trolley',
 875: 'trombone',
 876: 'tub\n vat',
 877: 'turnstile',
 878: 'typewriter keyboard',
 879: 'umbrella',
 880: 'unicycle\n monocycle',
 881: 'upright\n upright piano',
 882: 'vacuum\n vacuum cleaner',
 883: 'vase',
 884: 'vault',
 885: 'velvet',
 886: 'vending machine',
 887: 'vestment',
 888: 'viaduct',
 889: 'violin\n fiddle',
 890: 'volleyball',
 891: 'waffle iron',
 892: 'wall clock',
 893: 'wallet\n billfold\n notecase\n pocketbook',
 894: 'wardrobe\n closet\n press',
 895: 'warplane\n military plane',
 896: 'washbasin\n handbasin\n washbowl\n lavabo\n wash-hand basin',
 897: 'washer\n automatic washer\n washing machine',
 898: 'water bottle',
 899: 'water jug',
 900: 'water tower',
 901: 'whiskey jug',
 902: 'whistle',
 903: 'wig',
 904: 'window screen',
 905: 'window shade',
 906: 'Windsor tie',
 907: 'wine bottle',
 908: 'wing',
 909: 'wok',
 910: 'wooden spoon',
 911: 'wool\n woolen\n woollen',
 912: 'worm fence\n snake fence\n snake-rail fence\n Virginia fence',
 913: 'wreck',
 914: 'yawl',
 915: 'yurt',
 916: 'web site\n website\n internet site\n site',
 917: 'comic book',
 918: 'crossword puzzle\n crossword',
 919: 'street sign',
 920: 'traffic light\n traffic signal\n stoplight',
 921: 'book jacket\n dust cover\n dust jacket\n dust wrapper',
 922: 'menu',
 923: 'plate',
 924: 'guacamole',
 925: 'consomme',
 926: 'hot pot\n hotpot',
 927: 'trifle',
 928: 'ice cream\n icecream',
 929: 'ice lolly\n lolly\n lollipop\n popsicle',
 930: 'French loaf',
 931: 'bagel\n beigel',
 932: 'pretzel',
 933: 'cheeseburger',
 934: 'hotdog\n hot dog\n red hot',
 935: 'mashed potato',
 936: 'head cabbage',
 937: 'broccoli',
 938: 'cauliflower',
 939: 'zucchini\n courgette',
 940: 'spaghetti squash',
 941: 'acorn squash',
 942: 'butternut squash',
 943: 'cucumber\n cuke',
 944: 'artichoke\n globe artichoke',
 945: 'bell pepper',
 946: 'cardoon',
 947: 'mushroom',
 948: 'Granny Smith',
 949: 'strawberry',
 950: 'orange',
 951: 'lemon',
 952: 'fig',
 953: 'pineapple\n ananas',
 954: 'banana',
 955: 'jackfruit\n jak\n jack',
 956: 'custard apple',
 957: 'pomegranate',
 958: 'hay',
 959: 'carbonara',
 960: 'chocolate sauce\n chocolate syrup',
 961: 'dough',
 962: 'meat loaf\n meatloaf',
 963: 'pizza\n pizza pie',
 964: 'potpie',
 965: 'burrito',
 966: 'red wine',
 967: 'espresso',
 968: 'cup',
 969: 'eggnog',
 970: 'alp',
 971: 'bubble',
 972: 'cliff\n drop\n drop-off',
 973: 'coral reef',
 974: 'geyser',
 975: 'lakeside\n lakeshore',
 976: 'promontory\n headland\n head\n foreland',
 977: 'sandbar\n sand bar',
 978: 'seashore\n coast\n seacoast\n sea-coast',
 979: 'valley\n vale',
 980: 'volcano',
 981: 'ballplayer\n baseball player',
 982: 'groom\n bridegroom',
 983: 'scuba diver',
 984: 'rapeseed',
 985: 'daisy',
 986: "yellow lady's slipper\n yellow lady-slipper\n Cypripedium calceolus\n Cypripedium parviflorum",
 987: 'corn',
 988: 'acorn',
 989: 'hip\n rose hip\n rosehip',
 990: 'buckeye\n horse chestnut\n conker',
 991: 'coral fungus',
 992: 'agaric',
 993: 'gyromitra',
 994: 'stinkhorn\n carrion fungus',
 995: 'earthstar',
 996: 'hen-of-the-woods\n hen of the woods\n Polyporus frondosus\n Grifola frondosa',
 997: 'bolete',
 998: 'ear\n spike\n capitulum',
 999: 'toilet tissue\n toilet paper\n bathroom tissue'}
