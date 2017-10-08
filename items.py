#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, Items, User

engine = create_engine('sqlite:///itemcatalog.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy users
User1 = User(name="Robo Barista1", email="tinnyTim1@udacity.com")
session.add(User1)
session.commit()

User2 = User(name="Robo Barista2", email="tinnyTim2@udacity.com")
session.add(User2)
session.commit()

User3 = User(name="Robo Barista3", email="tinnyTim3@udacity.com")
session.add(User3)
session.commit()

User4 = User(name="Robo Barista4", email="tinnyTim4@udacity.com")
session.add(User4)
session.commit()

User5 = User(name="Robo Barista5", email="tinnyTim5@udacity.com")
session.add(User5)
session.commit()

# Source (https://www.linkedin.com)
# Category 1 - Chocolates
category1 = Categories(name="Chocolates", user_id=1)

session.add(category1)
session.commit()

# 1)Kit Kat
item1 = Items(
    name="Kit Kat", description="Kit Kat (or Kit Cat as"
    " its original name) was first introduced to the customers in 1935 "
    "with a brand image of finger-like wheat-and-milk bar. The company "
    "then continued its success with an enormous selection of categories,"
    " like hot chocolates, or wafers, blended with flavors of caramel, honey,"
    " or fruits. Nowadays, the brand gets a growing number of famous"
    " in the world as a meaningful gift for friends and families. "
    "One interesting point because of this chocolate is that users "
    "can simply break the Kit Kat into equal parts, making sure "
    "that your kids never get angry.", category=category1, user_id=1)

session.add(item1)
session.commit()

# 2) Toblerone
item2 = Items(
    name="Toblerone", description="Beginning as a "
    "luxurious dessert for royalties in Switzerland, Toblerone nowadays"
    " shapes itself as one of the most premium chocolate brands in the"
    " world. Millions of fans of this chocolate brand always desire"
    " for the small distinctive prism made from almonds, honey, "
    "nougat and rich cocoa which are all perfectly mixed together."
    " A chocolate bar of Toblerone is extremely charming and murky"
    " with unique shapes and distinctive taste.",
    category=category1, user_id=1)

session.add(item2)
session.commit()


# 3) Ferrero Rocher
item3 = Items(
    name="Ferrero Rocher", description="Ferrero Rocher"
    " is considered to be among the best chocolate all over the world,"
    " not only because of its high quality chocolate, beautiful "
    "external appearance, and also the culture and standard of "
    "chocolate that has been put worldwide to any other chocolate"
    " companies. As the leading chocolate brand name globally, "
    "Ferrero Rocher has been in its heyday for more than "
    "200 years.", category=category1, user_id=1)

session.add(item3)
session.commit()

# source(www.cheese.com)
# Category 2 - Cheese
category2 = Categories(name="Cheese", user_id=2)

session.add(category2)
session.commit()

# 1)Parmesan
item1 = Items(
    name="Parmesan", description="True Parmesan "
    "cheese has a hard, gritty texture and is fruity and nutty"
    " in taste. Cheeses mocking Parmesan or inferior Parmesan "
    "may have a bitter taste. Parmigiano Reggiano cheese is mostly"
    " grated over pastas, used in soups and risottos. It is also "
    "eaten on its own as a snack.", category=category2, user_id=2)

session.add(item1)
session.commit()

# 2)Mozzarella
item2 = Items(
    name="Mozzarella", description="Mozzarella cheese"
    " is a sliceable curd cheese originating in Italy. Traditional "
    "Mozzarella cheese is made from milk of water buffalos herded in"
    " very few countries such as Italy and Bulgaria. As a result, "
    "most of the Mozzarella cheeses available now are made from cow's "
    "milk. An Italian Traditional Specialty Guaranteed (TSG) food "
    "product, Mozzarella cheese is not aged like most cheeses. It "
    "is eaten fresh and within few hours after it is made.",
    category=category2, user_id=2)

session.add(item2)
session.commit()

# 3)American Cheese
item3 = Items(
    name="American Cheese", description="American cheese"
    " is processed cheese made from a blend of milk, milk fats and solids,"
    " with other fats and whey protein concentrates. At first it was "
    "made from a mixture of cheeses, more often than not Colby and Cheddar."
    " Since blended cheeses are no longer used, it cannot be legally "
    "called cheese and has to be labeled as processed cheese, cheese "
    "product, etc. Sometimes, instead of the word cheese, it is called "
    "as American slices or American singles. Under the U.S. Code of "
    "Federal Regulations, American cheese is a type of pasteurised "
    "processed cheese.", category=category2, user_id=2)

session.add(item3)
session.commit()

# 4)Cheddar
item4 = Items(
    name="Cheddar", description="Cheddar cheese, the most "
    "widely purchased and eaten cheese in the world is always made from "
    "cow's milk. It is a hard and natural cheese that has a slightly "
    "crumbly texture if properly cured and if it is too young, the "
    "texture is smooth. It gets a sharper taste as it matures, "
    "over a period of time between 9 to 24 months. Shaped like "
    "a drum, 15 inches in diameter, Cheddar cheese is natural "
    "rind bound in cloth while its colour generally ranges from "
    "white to pale yellow. However, some Cheddars may have a "
    "manually added yellow-orange colour.",
    category=category2, user_id=2)

session.add(item4)
session.commit()

# 5)Feta
item5 = Items(
    name="Feta", description="Feta is undoubtedly one "
    "of the most famous Greek cheeses. In fact, Feta occupies 70% "
    "stake in Greek cheese consumption. The cheese is protected by "
    "EU legislations and only those cheeses manufactured in Macedonia, "
    "Thrace, Thessaly, Central Mainland Greece, the Peloponnese and "
    "Lesvos can be called feta. Similar cheeses produced elsewhere "
    "in the eastern Mediterranean and around the Black Sea, outside "
    "the EU, are often called white cheese.", category=category2, user_id=2)

session.add(item5)
session.commit()

# 6)Camembert
item6 = Items(
    name="Camembert", description="Marie Harel created "
    "the original Camembert cheese from raw milk in Normandy, France "
    "in 1791. Today, however, a very small percentage of producers "
    "make cheese from raw milk with the same process as Marie Harel"
    " would have used. Those who produce cheese using Marie Harel's "
    "method, can legally call their cheese Camembert Normandie under "
    "the AOC guidelines. However, the production of Camembert cheese "
    "has now transcended the AOC designation. Very good varieties of "
    "Camembert cheese made from pasteurised milk can be found in "
    "Normandy today. The best of them is the Camembert Le "
    "Chatelain.", category=category2, user_id=2)

session.add(item6)
session.commit()

# source(www.wikipedia.com)
# Category 3 - Vegetables
category3 = Categories(name="Vegetables", user_id=3)

session.add(category3)
session.commit()

# 1)Broccoli
item1 = Items(
    name="Broccoli", description="Broccoli is an edible "
    "green plant in the cabbage family whose large flowering head is "
    "eaten as a vegetable. The word broccoli comes from the Italian "
    "plural of broccolo, which means the flowering crest of a "
    "cabbage, and is the diminutive form of brocco, meaning "
    "small nail or sprout. Broccoli is often boiled or "
    "steamed but may be eaten raw. Broccoli is classified"
    " in the Italica cultivar group of the species Brassica"
    " oleracea. Broccoli has large flower heads, usually "
    "green in color, arranged in a tree-like structure "
    "branching out from a thick, edible stalk. The mass of"
    " flower heads is surrounded by leaves. Broccoli resembles"
    " cauliflower, which is a different cultivar group of "
    "the same species.", category=category3, user_id=3)

session.add(item1)
session.commit()

# 2)Collard greens
item2 = Items(
    name="Collard greens", description="Collard greens"
    " (collards) describes certain loose-leafed cultivars of Brassica"
    " oleracea, the same species as many common vegetables, including"
    " cabbage (Capitata Group) and broccoli (Botrytis Group). Collard"
    " greens are part of the Acephala Group of the species, which "
    "includes kale and spring greens. They are in the same cultivar"
    " group owing to their genetic similarity. The name collard is a"
    " corrupted form of the word colewort (the wild cabbage plant). "
    "The plants are grown for their large, dark-colored, edible leaves"
    " and as a garden ornamental, mainly in Brazil, Portugal, the "
    "southern United States, many parts of Africa, the Balkans, "
    "northern Spain and northern India.", category=category3, user_id=3)

session.add(item2)
session.commit()

# 3)Carrot
item3 = Items(
    name="Carrot", description="The carrot (Daucus "
    "carota subsp. sativus) is a root vegetable, usually orange in"
    " colour, though purple, black, red, white, and yellow cultivars"
    " exist. Carrots are a domesticated form of the wild carrot, "
    "Daucus carota, native to Europe and southwestern Asia. The "
    "plant probably originated in Persia and was originally"
    " cultivated for its leaves and seeds. The most commonly"
    " eaten part of the plant is the taproot, although the "
    "greens are sometimes eaten as well. The domestic carrot"
    " has been selectively bred for its greatly enlarged, "
    "more palatable, less woody-textured taproot.",
    category=category3, user_id=3)

session.add(item3)
session.commit()

# 4)Cabbage
item4 = Items(
    name="Cabbage", description="Cabbage or headed"
    " cabbage (comprising several cultivars of Brassica oleracea)"
    " is a leafy green or purple biennial plant, grown as an annual"
    " vegetable crop for its dense-leaved heads. It is descended"
    " from the wild cabbage, B. oleracea var. oleracea, and is "
    "closely related to broccoli and cauliflower (var. botrytis),"
    " Brussels sprouts (var. gemmifera) and savoy cabbage "
    "(var. sabauda) which are sometimes called cole crops. Cabbage"
    " heads generally range from 0.5 to 4 kilograms (1 to 9 lb), "
    "and can be green, purple and white. Smooth-leafed firm-headed"
    " green cabbages are the most common, with smooth-leafed red "
    "and crinkle-leafed savoy cabbages of both colors seen more "
    "rarely. It is a multi-layered vegetable. Under conditions of"
    " long sunlit days such as are found at high northern latitudes"
    " in summer, cabbages can grow much larger. Some records are "
    "discussed at the end of the history section.",
    category=category3, user_id=4)

session.add(item4)
session.commit()

# 5)Tomato
item5 = Items(
    name="Tomato", description="The tomato is the"
    " edible fruit of Solanum lycopersicum, commonly known as a "
    "tomato plant, which belongs to the nightshade family, "
    "Solanaceae. The species originated in Central and "
    "South America. The Nahuatl (Aztec language) word tomatl"
    " gave rise to the Spanish word tomate, from which the "
    "English word tomato originates. Its use as a food originated"
    " in Mexico, and spread throughout the world following the "
    "Spanish colonization of the Americas. Tomato is consumed in"
    " diverse ways, including raw, as an ingredient in many dishes,"
    " sauces, salads, and drinks. While tomatoes are "
    "botanically berry-type fruits, they are considered"
    " culinary vegetables, being ingredients of savory meals.",
    category=category3, user_id=3)

session.add(item5)
session.commit()

# source(www.tastemade.com)
# Category 4 - Condiments
category4 = Categories(name="Condiments", user_id=4)

session.add(category4)
session.commit()

# 1)Mayonnaise
item1 = Items(
    name="Mayonnaise", description="For many years, "
    "ketchup (which is Asian in origin) was the king condiment in "
    "the U.S. Over the past couple of years, however, Americans have"
    " declared mayo the new sheriff in town. Whether due to a surge "
    "in deviled egg popularity or homemade sandwiches, mayonnaise "
    "spread throughout the country at an unusually high rate, beginning"
    " in 2013. The eggy sauce has its roots in France or Spain, "
    "depending on who you ask, but no one can find more uses for it"
    " than a Yankee.", category=category4, user_id=4)

session.add(item1)
session.commit()

# 2)Banana Sauce
item2 = Items(
    name="Banana Sauce", description="When the United"
    " States began influencing the Philippines in the mid 20th century,"
    " ketchup caught on quickly throughout the nation. During World War 2,"
    " tomato ketchup was a rare sight. Since tomatoes were scarce "
    "across the islands, banana sauce a.k.a. banana ketchup was invented."
    " Often dyed red to mimic the look of traditional ketchup, banana "
    "sauces sweetness easily sets it apart from tomato ketchup while "
    "still sharing many of its uses.", category=category4, user_id=4)

session.add(item2)
session.commit()

# 3)Vegemite
item3 = Items(
    name="Vegemite", description="The Brits initially had"
    " the stranglehold on this substance in a less salty spread called "
    "Marmite. In 1923, however, Cyril Callister recreated the recipe from"
    " scratch, with more sodium and B vitamins. The sticky breakfast "
    "condiment made from brewer's yeast cemented itself as uniquely "
    "Australian when it became a part of army rations during World War 2."
    " In 2015, Aussies started using Vegemite to create alcohol, "
    "prompting calls for the government to limit its sale. For some,"
    " a law probably isn't necessary.", category=category4, user_id=4)

session.add(item3)
session.commit()

# 4)Wasabi
item4 = Items(
    name="Wasabi", description="Dating back to the 10th "
    "century, the wasabi plant has spiced up Japanese cuisine. The plant,"
    " part of a family that includes horseradish and mustard, requires cold,"
    " freshwater with a balance of minerals to thrive, making its "
    "production very rare. Wasabis growing popularity beyond Japan "
    "brought about many alternative condiments made primarily of "
    "horseradish and green food dye. Authentic wasabi spoils within"
    " 15 minutes of preparation, leading to the tradition of serving"
    " it beneath sushi, to preserve its flavor.",
    category=category4, user_id=4)

session.add(item4)
session.commit()

# 5)Chutney
item5 = Items(
    name="Chutney", description="For thousands of "
    "years, chutney has been an irreplaceable relish that sweetens "
    "or spices, depending on the recipe. Ancient holy men,"
    "	Brahmins, "
    "discovered the preservative powers of spices and began to "
    "mix them with various fruits and vegetables. The British "
    "would eventually carry sweet chutneys to the U.K. as well "
    "as its African and Caribbean territories, but Indian "
    "chutneys remain complex in taste and texture.",
    category=category4, user_id=4)

session.add(item5)
session.commit()

# source(www.wikipedia.com)
# Category 5 - Fish
category5 = Categories(name="Fish", user_id=5)

session.add(category5)
session.commit()

# 1)Guppy
item1 = Items(
    name="Guppy", description="The guppy (Poecilia reticulata),"
    "	also known as millionfish and rainbow fish, is one of the"
    " world's most widely distributed tropical fish, and one of "
    "the most popular freshwater aquarium fish species. It is a"
    " member of the family Poeciliidae and, like almost all "
    "American members of the family, is live-bearing. Guppies, "
    "whose natural range is in northeast South America, were "
    "introduced to many habitats and are now found all over "
    "the world. They are highly adaptable and thrive in many "
    "different environmental and ecological conditions. Male "
    "guppies, which are smaller than females, have ornamental"
    " caudal and dorsal fins, while females are duller in colour."
    "Wild guppies generally feed on a variety of food sources, "
    "including benthic algae and aquatic insect larvae. "
    "Guppies are used as a model organism in the field of ecology,"
    " evolution, and behavioural studies.", category=category5, user_id=5)

session.add(item1)
session.commit()

# 2)Goldfish
item2 = Items(
    name="Goldfish", description="A relatively "
    "small member of the carp family (which also includes the "
    "Prussian carp and the crucian carp), the goldfish is native "
    "to east Asia. It was first selectively bred in China more than"
    " a thousand years ago, and several distinct breeds have since "
    "been developed. Goldfish breeds vary greatly "
    "in size, body shape,"
    " fin configuration and colouration (various combinations "
    "of white, yellow, orange, red, brown, and black are known).",
    category=category5, user_id=5)

session.add(item2)
session.commit()

# 3)Haddock
item3 = Items(
    name="Haddock", description="The haddock is easily"
    " recognized by a black lateral line running along its white "
    "side (not to be confused with pollock which has the reverse, "
    "i.e., white line on black side) and a distinctive dark blotch"
    " above the pectoral fin, often described as a thumbprint or "
    "even the Devil's thumbprint or St. Peter's mark. Haddock is "
    "most commonly found at depths of 40 to 133 m (131 to 436 ft),"
    " but has a range as deep as 300 m (980 ft). It thrives in "
    "temperatures of 2 to 10 degree celcius. "
    "Juveniles prefer shallower"
    " waters and larger adults deeper water. "
    "Generally, adult haddock"
    " do not engage in long migratory behaviour as do the younger "
    "fish, but seasonal movements have been known to occur across "
    "all ages. Haddock feed primarily on small invertebrates, "
    "although larger members of the species may occasionally"
    " consume fish.", category=category5, user_id=5)

session.add(item3)
session.commit()

# 4)Salmon
item4 = Items(
    name="Salmon", description="Salmon is the common "
    "name for several species of ray-finned fish in the family "
    "Salmonidae. Other fish in the same family include trout, "
    "char, grayling and whitefish. Salmon are native to tributaries "
    "of the North Atlantic (genus Salmo) and Pacific Ocean "
    "(genus Oncorhynchus). Many species of salmon"
    "	have been introduced"
    " into non-native environments such as the Great Lakes of "
    "North America and Patagonia in South America. Salmon are "
    "intensively farmed in many parts of the world.",
    category=category5, user_id=5)

session.add(item4)
session.commit()

# source(www.wikipedia.com)
# Category 6 - Coffee beans
category6 = Categories(name="Coffee beans", user_id=5)

session.add(category6)
session.commit()

# 1)Costa Rican Tarrazu
item1 = Items(
    name="Costa Rican Tarrazu", description="Tarrazu "
    "is one of the four premium coffee growing districts surrounding"
    " he capital city of San Jose. The other noteworthy districts"
    " for growing coffee include Tres Rios, Heredia and Alajuela. "
    "Costa Rican coffee beans are graded by hardness, determined "
    "by the altitude at which they are grown. Coffee grown above "
    "3900 feet is Strictly Hard Beans (SHB). Between 3300 and 3900"
    " feet are Good hard Beans (GHB) and between 1600 and 3000 "
    "feet are Medium Hard Beans (MHB). These coffees are balanced,"
    " clean, with bright acidity with citrus or berry-like flavors,"
    " and hints of chocolate and spice in the finish.",
    category=category6, user_id=5)

session.add(item1)
session.commit()

# 2)Nicaragua
item2 = Items(
    name="Nicaragua", description=" At one time,"
    " Nicaraguan coffee was more popular and sought after than"
    " it is today. Nicaraguan coffee trade has been impacted by"
    " hurricane devastation as well as the politics and ravages"
    " of civil war, and a long interruption during the cold war"
    " years when the US prohibited the importing of Nicaraguan"
    " coffee. Fortunately, today, Nicaragua appears to be"
    " making a comeback. Nicaraguan coffee is wet-processed,"
    " with a mild, light acidity, medium body, with hints of"
    " vanilla and a nutty bouquet.", category=category6, user_id=5)

session.add(item2)
session.commit()

# 3)Brazil Bourbon Santos
item3 = Items(
    name="Brazil Bourbon Santos", description="The"
    " descendants of these coffee plants are grown in the "
    "Southern region of Brazil today, near the port of Santos."
    " Brazilian Santos is a light bodied coffee, with low "
    "acidity, a pleasing aroma and a mild, smooth flavor. "
    "Growing elevations in Brazil range from 2000 to 4000 feet."
    " These lower altitudes produce coffees low in acidity, "
    "exhibiting softer, more subtle characteristics than the "
    "bigger and brighter coffees grown at higher elevation "
    "above 5000 feet typical of Central America.",
    category=category6, user_id=5)

session.add(item3)
session.commit()

# 4)Blue Mountain
item3 = Items(
    name="Blue Mountain", description=" Coffea arabica "
    "L. 'Blue Mountain'. Also known commonly as Jamaican coffea"
    " or Kenyan coffea. It is a famous Arabica cultivar that "
    "originated in Jamaica but is now grown in Hawaii, PNG and "
    "Kenya. It is a superb coffee with a high quality cup flavor."
    " It is characterized by a nutty aroma, bright acidity and"
    " a unique beef-bullion like flavor.",
    category=category6, user_id=5)

session.add(item3)
session.commit()


print "added categories and items"
