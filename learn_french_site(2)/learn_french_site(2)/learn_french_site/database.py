from app import create_app
from app.models import db, Vocabulary, GrammarItem, ShortStory, Quiz, QuizQuestion

# Create app instance
app = create_app()

with app.app_context():
    # Drop and recreate tables to ensure a clean slate for "proper data"
    db.drop_all()
    db.create_all()

    # ======================================================
    # 🟦 Vocabulary (Expanded)
    # ======================================================
    vocab_data = [
        # Colors 🎨
        ("colors", "rouge", "red", "roo-zh"),
        ("colors", "bleu", "blue", "bluh"),
        ("colors", "vert", "green", "vehr"),
        ("colors", "jaune", "yellow", "zhohn"),
        ("colors", "noir", "black", "nwahr"),
        ("colors", "blanc", "white", "blahn"),
        ("colors", "rose", "pink", "rohz"),
        ("colors", "orange", "orange", "oh-rahn-zh"),
        
        # Numbers 🔢
        ("numbers", "un", "one", "un"),
        ("numbers", "deux", "two", "duh"),
        ("numbers", "trois", "three", "trwah"),
        ("numbers", "quatre", "four", "kahtr"),
        ("numbers", "cinq", "five", "sank"),
        ("numbers", "six", "six", "seess"),
        ("numbers", "sept", "seven", "set"),
        ("numbers", "huit", "eight", "weet"),
        ("numbers", "neuf", "nine", "nuhf"),
        ("numbers", "dix", "ten", "deess"),

        # Food 🍎
        ("food", "la pomme", "apple", "lah pom"),
        ("food", "le pain", "bread", "luh pan"),
        ("food", "le fromage", "cheese", "luh fro-mah-zh"),
        ("food", "le café", "coffee", "luh kah-fey"),
        ("food", "le lait", "milk", "luh leh"),
        ("food", "le poulet", "chicken", "luh poo-leh"),
        ("food", "le poisson", "fish", "luh pwah-sohn"),
        ("food", "la banane", "banana", "lah bah-nahn"),
        ("food", "l'eau", "water", "loh"),

        # Animals 🐶
        ("animals", "le chien", "dog", "luh shy-ah n"),
        ("animals", "le chat", "cat", "luh shah"),
        ("animals", "le cheval", "horse", "luh shuh-vahl"),
        ("animals", "l'oiseau", "bird", "lwah-zoh"),
        ("animals", "le lion", "lion", "luh lee-ohn"),
        ("animals", "le singe", "monkey", "luh san-zh"),
        ("animals", "le lapin", "rabbit", "luh lah-pan"),
        ("animals", "la vache", "cow", "lah vah-sh"),

        # Family 👨‍👩‍👧
        ("family", "la famille", "family", "lah fah-mee"),
        ("family", "la mère", "mother", "lah mehr"),
        ("family", "le père", "father", "luh pehr"),
        ("family", "la soeur", "sister", "lah suhr"),
        ("family", "le frère", "brother", "luh frehr"),
        ("family", "la grand-mère", "grandmother", "lah grahn-mehr"),
        ("family", "le grand-père", "grandfather", "luh grahn-pehr"),
        ("family", "le fils", "son", "luh feess"),
        ("family", "la fille", "daughter", "lah fee"),
    ]
    
    for cat, fr, en, pr in vocab_data:
        db.session.add(Vocabulary(category=cat, french=fr, english=en, pronunciation=pr))
    print(" Vocabulary database populated!")

    # ======================================================
    # 📘 Grammar (Expanded)
    # ======================================================
    grammar_data = [
        ("Greetings",
         '''<p class="sub-heading">Informal (to a friend, tu form)</p>
<p class="text-line">Bonjour/Salut</p>
<p class="text-line">Comment ça va?/Ça va ?</p>
<p class="text-line">Comment tu t'appelles?</p>

<p class="sub-heading">Formal (to a stranger/adult, vous form)</p>
<p class="text-line">Bonjour</p>
<p class="text-line">Comment allez-vous?</p>
<p class="text-line">Comment vous appelez-vous?</p>

<p class="sub-heading">To wish</p>
<p class="text-line">Salut</p>
<p class="text-line">Bonjour</p>
<p class="text-line">Bonsoir</p>
<p class="text-line">Bonne nuit</p>

<p class="sub-heading">To ask how one is</p>
<p class="text-line">Ça va?</p>
<p class="text-line" style="padding-left: 20px;">• Ça va bien, merci.</p>
<p class="text-line">Comment ça va?</p>
<p class="text-line" style="padding-left: 20px;">• Ça va bien, merci.</p>
<p class="text-line">Comment vas-tu?</p>
<p class="text-line" style="padding-left: 20px;">• Je vais bien, merci.</p>
<p class="text-line">Comment allez-vous?</p>
<p class="text-line" style="padding-left: 20px;">• Je vais bien, merci.</p>

<p class="sub-heading">To ask one's name</p>
<p class="text-line">Comment tu t'appelles?  Comment vous appelez-vous?</p>

<p class="sub-heading">To take a leave</p>
<p class="text-line">Au revoir</p>
<p class="text-line">Bonne journée</p>
<p class="text-line">À demain</p>
<p class="text-line">Bonne soirée</p>
<p class="text-line">À bientôt</p>
<p class="text-line">Bon après-midi</p>'''),

        ("Articles",
         '''<p class="sub-heading">Definite: -</p>

<p>Definite articles are used for specific nouns. It refers to the article "the" in English. There are different articles corresponding to gender and number.</p>

<p class="text-line"><span class="article-word">la</span> - feminine singular <span class="french-term">(féminin singulier)</span></p>
<p class="text-line"><span class="article-word">le</span> - masculine singular <span class="french-term">(masculin singulier)</span></p>
<p class="text-line"><span class="article-word">l'</span> - before a vowel or silent h (masculine and feminine) <span class="french-term">(masculin et féminin)</span></p>
<p class="text-line"><span class="article-word">les</span> - plural (masculine and feminine) <span class="french-term">(masculin et féminin)</span></p>

<p class="section-title">Examples</p>

<p class="text-line"><span class="article-word">la</span> robe - the dress</p>
<p class="text-line"><span class="article-word">le</span> livre - the book</p>
<p class="text-line"><span class="article-word">l'</span>histoire - the story</p>
<p class="text-line"><span class="article-word">les</span> tables - the tables</p>

<p class="sub-heading">Indefinite: -</p>

<p>Indefinite articles are used for unspecified nouns. It refers to the articles "a", "an", and "some".</p>

<p class="text-line"><span class="article-word">un</span> - masculine singular <span class="french-term">(masculin singulier)</span></p>
<p class="text-line"><span class="article-word">une</span> - feminine singular <span class="french-term">(féminin singulier)</span></p>
<p class="text-line"><span class="article-word">des</span> - plural (feminine and masculine) <span class="french-term">(masculin et féminin)</span></p>

<p class="section-title">Examples</p>

<p class="text-line"><span class="article-word">un</span> cahier - a notebook</p>
<p class="text-line"><span class="article-word">une</span> photo - a picture</p>
<p class="text-line"><span class="article-word">des</span> fruits - fruits</p>'''),

        ("Gender",
         '''<p>In French, every noun has a gender. It is either masculine or feminine. Masculine words are followed by masculine articles such as "un" and "le". Feminine words are always used with feminine articles such as "la" and "une".</p>

<p>Tip: In most of the cases, nouns ending with an "e" are feminine, nouns ending with an "s" or "x" are plural, and the rest are masculine.</p>

<p class="section-title">Examples</p>

<p class="sub-heading">Masculin</p>
<p>un chapeau - a gift</p>

<p class="sub-heading">Féminin</p>
<p>une gomme - an eraser</p>

<p class="sub-heading">Pluriel</p>
<p>des stylos - some pens</p>'''),

        ("Subject Pronouns",
         '''<table class="grammar-table">
<tr><th>French</th><th>Pronunciation</th><th>English</th></tr>
<tr><td>je</td><td>zhuh</td><td>I</td></tr>
<tr><td>tu</td><td>tew</td><td>you (informal)</td></tr>
<tr><td>il</td><td>eel</td><td>he / it</td></tr>
<tr><td>elle</td><td>el</td><td>she / it</td></tr>
<tr><td>nous</td><td>noo</td><td>we</td></tr>
<tr><td>vous</td><td>voo</td><td>you (formal or plural)</td></tr>
<tr><td>ils</td><td>eel</td><td>they (masculine or mixed group)</td></tr>
<tr><td>elles</td><td>el</td><td>they (feminine)</td></tr>
</table>

<p>Je parle français. (I speak French.)</p>
<p>Tu manges une pomme. (You eat an apple.)</p>
<p>Il joue au foot. (He plays football.)</p>
<p>Elle lit un livre. (She reads a book.)</p>
<p>Nous chantons. (We sing.)</p>
<p>Vous écoutez. (You listen.)</p>
<p>Ils regardent la télé. (They watch TV.)</p>'''),

        ("Verbs",
         '''<p>Verbs in French either end in "er", "ir", or "re". There are a few exceptions, with the most common ones being <span class="article-word">avoir</span> (to have) and <span class="article-word">être</span> (to be).</p>

<p class="sub-heading">Common "er" Ending Verbs: -</p>
<p class="text-line">1. Parler <span class="french-term">(to speak)</span></p>
<p class="text-line">2. Manger <span class="french-term">(to eat)</span></p>
<p class="text-line">3. Jouer <span class="french-term">(to play)</span></p>
<p class="text-line">4. Étudier <span class="french-term">(to study)</span></p>
<p class="text-line">5. Chanter <span class="french-term">(to sing)</span></p>
<p class="text-line">6. Regarder <span class="french-term">(to watch)</span></p>
<p class="text-line">7. Aimer <span class="french-term">(to love)</span></p>
<p class="text-line">8. Donner <span class="french-term">(to give)</span></p>
<p class="text-line">9. Habiter <span class="french-term">(to live)</span></p>
<p class="text-line">10. Écouter <span class="french-term">(to listen)</span></p>

<p class="sub-heading">Common "ir" Ending Verbs: -</p>
<p class="text-line">1. Finir <span class="french-term">(to finish)</span></p>
<p class="text-line">2. Choisir <span class="french-term">(to choose)</span></p>
<p class="text-line">3. Grandir <span class="french-term">(to grow)</span></p>
<p class="text-line">4. Partir <span class="french-term">(to leave)</span></p>
<p class="text-line">5. Sortir <span class="french-term">(to go out)</span></p>
<p class="text-line">6. Venir <span class="french-term">(to come)</span></p>
<p class="text-line">7. Dormir <span class="french-term">(to sleep)</span></p>
<p class="text-line">8. Tenir <span class="french-term">(to hold)</span></p>
<p class="text-line">9. Sentir <span class="french-term">(to feel)</span></p>
<p class="text-line">10. Incluir <span class="french-term">(to include)</span></p>

<p class="sub-heading">Common "re" Ending Verbs: -</p>
<p class="text-line">1. Attendre <span class="french-term">(to wait)</span></p>
<p class="text-line">2. Prendre <span class="french-term">(to take)</span></p>
<p class="text-line">3. Vendre <span class="french-term">(to sell)</span></p>
<p class="text-line">4. Boire <span class="french-term">(to drink)</span></p>
<p class="text-line">5. Faire <span class="french-term">(to do)</span></p>
<p class="text-line">6. Vivre <span class="french-term">(to live)</span></p>
<p class="text-line">7. Dire <span class="french-term">(to say)</span></p>
<p class="text-line">8. Entendre <span class="french-term">(to hear)</span></p>
<p class="text-line">9. Détendre <span class="french-term">(to relax)</span></p>
<p class="text-line">10. Répondre <span class="french-term">(to respond)</span></p>

<p>All of these verbs are conjugated according to different auxiliary verbs and tenses.</p>'''),

        ("Basic Sentence Structure",
         '''<p>In French, sentences follow this format: <span class="article-word">Subject + Verb + Object</span>.</p>

<p class="text-line">Je mange une pomme.</p>
<p class="text-line">Nous jouons au foot.</p>
<p class="text-line">Elle parle avec sa mère.</p>

<p>For example, in the sentence, "Je mange une pomme." "Je" is the subject, "mange" is the verb, and "une pomme" is the object.</p>

<p class="sub-heading">Adjectives come after the noun: -</p>
<p class="text-line">une bouteille d'eau rose - pink water bottle</p>
<p class="text-line">un sac bleu - blue bag</p>

<p class="sub-heading">Negative words</p>
<p>Usually, "ne" and "pas" are used to make a sentence negative.</p>
<p class="text-line">Je ne comprends pas. <span class="french-term">(I don't understand.)</span></p>

<p>Questions in French can be asked in the same way as a statement, but with a different tone, or by adding the phrase "est-ce que."</p>
<p class="text-line">Tu as mangé?</p>
<p class="text-line">Est-ce que tu as mangé?</p>'''),

        ("Conjugations",
         '''<p class="section-title">Avoir</p>
<p class="text-line">J'ai</p>
<p class="text-line">Tu as</p>
<p class="text-line">Il/Elle/On a</p>
<p class="text-line">Nous avons</p>
<p class="text-line">Vous avez</p>
<p class="text-line">Ils/Elles ont</p>

<p class="section-title">Être</p>
<p class="text-line">Je suis</p>
<p class="text-line">Tu es</p>
<p class="text-line">Il/Elle/On est</p>
<p class="text-line">Nous sommes</p>
<p class="text-line">Vous êtes</p>
<p class="text-line">Ils/Elles sont</p>

<p class="section-title">Aller</p>
<p class="text-line">Je vais</p>
<p class="text-line">Tu vas</p>
<p class="text-line">Il/Elle/On va</p>
<p class="text-line">Nous allons</p>
<p class="text-line">Vous allez</p>
<p class="text-line">Ils/Elles vont</p>

<p class="section-title">Faire</p>
<p class="text-line">Je fais</p>
<p class="text-line">Tu fais</p>
<p class="text-line">Il/Elle/On fait</p>
<p class="text-line">Nous faisons</p>
<p class="text-line">Vous faites</p>
<p class="text-line">Ils/Elles font</p>

<p class="section-title">Aimer</p>
<p class="text-line">J'aime</p>
<p class="text-line">Tu aimes</p>
<p class="text-line">Il/Elle/On aime</p>
<p class="text-line">Nous aimons</p>
<p class="text-line">Vous aimez</p>
<p class="text-line">Ils/Elles aiment</p>'''),
    ]

    for title, content in grammar_data:
        db.session.add(GrammarItem(title=title, content=content))
    print("📘 Grammar rules added!")

    # ======================================================
    # 📕 Short Stories
    # ======================================================
    story1_content = '''<h3>Les Trois Petits Cochons</h3>

<p style="margin: 20px 0;"><b><u>Section 1</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Il était une fois une maman cochon qui avait trois petits cochons. Elle les aimait beaucoup, mais comme il n'y avait pas assez de nourriture pour qu'ils puissent tous manger à leur faim, elle les a envoyé tenter leur chance dans le vaste monde.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Once upon a time there was a mama pig who had three little pigs. She loved them very much, but there was not enough food for all of them to eat, so she sent them out into the big world to seek their fortunes.</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story1_pig_crossroads.jpeg" alt="Pig at crossroads" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin: 20px 0;"><b><u>Section 2</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Le premier petit cochon a décidé d'aller vers le Sud. Alors qu'il marchait le long de la route, il a rencontré un fermier qui portait une botte de paille. Il lui a alors demandé poliment: "Pourriez-vous s'il vous plaît me donner cette paille, que je puisse construire une maison?"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The first little pig decided to go south. As he walked along the road he met a farmer carrying a bundle of straw, so he asked the man politely: "Could you please give me that straw, so that I can build a house?"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Comme le petit cochon avait dit "s'il vous plaît", le fermier lui a donné la paille, et le petit cochon l'a utilisée pour construire une belle maison. La maison avait des murs en paille, un plancher en paille, et à l'intérieur... un confortable lit en paille.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Because the little pig had said "please", the farmer gave him the straw, and the little pig used it to build a beautiful house. The house had straw walls, a straw floor, and inside... a comfortable straw bed.</i></p>

<p style="margin: 20px 0;"><b><u>Section 3</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Alors que le petit cochon venait juste de finir de construire sa maison et qu'il s'était allongé pour faire une sieste dans son lit en paille, le grand méchant loup est arrivé près de la maison. Il a senti l'odeur du cochon à l'intérieur de la maison, et cela lui a mis l'eau à la bouche. "Mmm...Des sandwichs au bacon!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>When the little pig had just finished building his house and had laid down for a nap in his straw bed, the big bad wolf arrived at the house. He smelt the scent of the pig inside the house, and his mouth started to water. "Mmmm ... bacon sandwiches."</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Le loup a frappé à la porte de la maison en paille et a dit: "Petit cochon! Petit cochon! Laisse-moi entrer! Laisse-moi entrer!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>So the wolf knocked at the door of the straw house and said: "Little pig! Little pig! Let me in! Let me in!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Mais comme le petit cochon avait vu les grandes griffes du loup à travers la serrure, il a répondu: "Non, non, non! Par les poils de mon menton!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>But as the little pig had seen the wolf's big paws through the keyhole, he replied: "No! No! No! By the hair of my chin!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors le loup a montré ses dents et a dit: "Alors je vais souffler et souffler et ta maison va s'effondrer."</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Then the wolf showed his teeth and said: "Then I'll blow and I'll blow and your house will fall down!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors il a soufflé et soufflé et la maison s'est effondrée. Le petit cochon est revenu en courant chez lui auprès de sa mère.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>So he blew and he blew and the house fell down. The little pig ran back home to his mother.</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story1_wolf_straw.jpeg" alt="Wolf at straw house" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin: 20px 0;"><b><u>Section 4</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Le deuxième petit cochon a décidé d'aller vers le Nord. Alors qu'il marchait le long de la route, il a rencontré un fermier qui portait un fagot de bois. Il lui a alors demandé poliment: "Excusez-moi, puis-je avoir ce bois pour construire une maison?"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The second little pig decided to go North. As he walked along the road he met a farmer carrying a bundle of wood, so he asked the man politely: "Excuse me, may I have that wood to build a house?"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Comme le petit cochon avait dit "excusez-moi", le fermier lui a donné le bois, et le petit cochon l'a utilisé pour construire une belle maison. La maison avait des murs en bois, un plancher en bois, et à l'intérieur...une solide table en bois.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Because the little pig had said "excuse me", the farmer gave him the wood, and the little pig used it to build a beautiful house. The house had wood walls, a wood floor, and inside... a strong wood table.</i></p>

<p style="margin: 20px 0;"><b><u>Section 5</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Alors que le petit cochon venait juste de finir de construire sa maison et qu'il faisait un bouquet pour sa solide table en bois, le grand méchant loup est arrivé près de la maison. Il a senti l'odeur du cochon à l'intérieur de la maison, et son estomac s'est mis à gronder. "Mmm... Du rôti de porc!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>When the little pig had just finished building his house and was arranging flowers on his strong wood table, the big bad wolf came arrived at the house. He smelt the scent of the pig inside the house, and his stomach started to rumble. "Mmmmm ... roast pork!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors le loup a frappé à la porte de la maison en bois et a dit: "Petit cochon! Petit cochon! Laisse-moi entrer! Laisse-moi entrer!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>So the wolf knocked at the door of the wood house and said: "Little pig! Little pig! Let me in! Let me in!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Mais comme le petit cochon avait vu le long nez du loup à travers la serrure, il a répondu: "Non, non, non! Par les poils de mon menton!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>But as the little pig had seen the wolf's long nose through the keyhole, he replied: "No! No! No! By the hair of my chin!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors le loup a montré ses dents et a dit: "Alors je vais souffler et souffler et ta maison va s'effondrer!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Then the wolf showed his teeth and said: "Then I'll blow and I'll blow and your house will fall down!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors il a soufflé et soufflé et la maison s'est effondrée. Le petit cochon est revenu en courant chez lui auprès de sa mère, qui n'était pas contente!</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>So he blew and he blew and the house fell down. The little pig ran back home to his mother – who was not happy!</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story1_pig_wood_house.jpeg" alt="Pig in wood house" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin: 20px 0;"><b><u>Section 6</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Le troisième petit cochon a décidé d'aller vers l'Ouest. Alors qu'il marchait le long de la route, il a rencontré un fermier qui portait un chargement de briques. Il lui a alors demandé poliment: "Bonjour monsieur, puis-je avoir quelques-unes de ces briques pour construire une maison?"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The third little pig decided to go West. As he walked along the road he met a farmer carrying a load of bricks. So he asked the man politely: "Hello sir, may I have some of those bricks to build a house?"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Comme le fermier appréciait qu'on l'appelle "monsieur", il a donné au petit cochon quelques briques, et le petit cochon les a utilisées pour construire une belle maison. La maison avait des murs en brique, un plancher en brique, et à l'intérieur... une grande cheminée en brique.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The farmer liked being called "sir" so he gave the little pig some bricks, and the little pig used them to build a beautiful house. The house had brick walls, a brick floor, and inside... a large brick fireplace.</i></p>

<p style="margin: 20px 0;"><b><u>Section 7</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Alors que le petit cochon venait juste de finir de construire sa maison et qu'il préparait une grande marmite de soupe dans sa cheminée en brique, le grand méchant loup est arrivé près de la maison. Il a senti l'odeur du cochon à l'intérieur de la maison, et s'est léché les babines. "Mmm... Des côtelettes de porc avec de la sauce barbecue et des haricots verts!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>When the little pig had just finished building his house and was cooking a big pot of soup in his brick fireplace, the big bad wolf arrived at the house. He smelt the scent of the pig inside the house, and he licked his lips. "Mmmmm – pork chops with barbeque sauce and green beans!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors le loup a frappé à la porte de la maison en brique et a dit: "Petit cochon! Petit cochon! Laisse-moi entrer! Laisse-moi entrer!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>So the wolf knocked at the door of the brick house and said: "Little pig! Little pig! Let me in! Let me in!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Mais le petit cochon a vu les grandes oreilles du loup à travers la serrure, il a donc répondu: "Non, non, non! Par les poils de mon menton!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>But as the little pig had seen the wolf's big ears through the keyhole, he replied: "No! No! No! By the hair of my chin!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors le loup a montré ses dents et a dit: "Alors je vais souffler et souffler et ta maison va s'effondrer!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Then the wolf showed his teeth and said: "Then I'll blow and I'll blow and your house will fall down!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Alors il a soufflé et soufflé, encore et encore. Mais il n'a pas réussi à faire s'effondrer la maison. À la fin il était tellement essoufflé qu'il ne pouvait plus du tout souffler.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>So he blew and he blew, again and again. But he could not make the house fall down. At last he was so out of breath that he couldn't blow any more.</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Le petit cochon se contentait de remuer sa grande marmite de soupe, et de rire.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The little pig just stirred his big pot of soup, and laughed.</i></p>

<p style="margin: 20px 0;"><b><u>Section 8</u></b></p>
<p style="margin-bottom: 15px; line-height: 1.8;">Mais le loup avait tellement envie de manger des côtelettes de porc... il ne voulait pas abandonner! Il s'est faufilé derrière la maison et a grimpé sur le toit. "À présent, j'aurai ce cochon, c'est certain!"</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>But the wolf had such a craving to eat pork chops... he didn't want to give up! He snuck around the back of the house and climbed onto the roof. "Now I'll get that pig, for certain!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Le loup s'est laissé glisser dans la grande cheminée en brique et a atterri... PLOUF! Les fesses les premières dans la grande marmite de soupe du petit cochon... qui était alors très chaude! Le loup a hurlé et a bondi hors de la marmite, puis est sorti en courant de la maison et a dévalé la route, serrant très fort ses fesses brûlées.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The wolf let himself slide down the great brick chimney and landed ...PLOP! Bottom-first into the little pig's big pot of soup... which was now very hot! The wolf howled and jumped out of the pot, then ran out of the house and hurtled down the road, clutching his burnt bottom.</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story1_wolf_fireplace.jpeg" alt="Wolf falling into fireplace" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin-bottom: 15px; line-height: 1.8;">Le petit cochon a appelé sa mère et ses deux frères sur son téléphone portable en brique, et les a invité à partager un délicieux dîner de soupe aux fesses de loup.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The little pig called his mother and his two brothers on his brick mobile phone, and invited them to share a delicious dinner of wolf-bottom soup.</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">La soupe aux fesses de loup était si savoureuse que bientôt tous les gens à cent kilomètres à la ronde ont voulu attraper le loup et le faire s'asseoir dans leur soupe. Le pauvre loup a dû s'enfuir très loin jusqu'à la sombre forêt profonde où il a pu vivre en paix et dans le calme.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The wolf-bottom soup was so tasty that soon everybody within one hundred kilometers wanted to catch the wolf and make him sit in their soup. The poor wolf had to run far away to the deep dark forest where he could live in peace and quiet.</i></p>

<p style="margin-top: 30px; font-size: 0.9rem; color: #666;"><i>Reference: "Les Trois Petits Cochons" from French Short Stories: Learn French with Stories for Beginners. 2016.</i></p>'''

    db.session.add(ShortStory(title="Les Trois Petits Cochons", content=story1_content))

    # Story 2 - Babar Fait Du Ski
    story2_content = '''<h3>Babar Fait Du Ski</h3>

<p style="margin-bottom: 15px; line-height: 1.8;">Il a à peine le temps de se relever : une pluie de boules de neige l'aveugle. Arthur se protège comme il peut avec les bras.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>He barely has time to get up: a rain of snowballs blinds him. Arthur protects himself as best he can with his arms.</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story2_snowball_arthur.jpeg" alt="Arthur hit by snowballs" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin-bottom: 15px; line-height: 1.8;">«Tiens! En voilà une belle! Et encore une!» Les trois petits roulent les boules et les lancent sans s'arrêter. Arthur est vraiment drôle couvert de neige : les petits éléphants éclatent de rire. Ils rient si fort qu'ils sont tout essoufflés. Les boules tombent moins vite. Arthur en lance à son tour. C'est la bataille!</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"Here! Here's a nice one! And another one!" The three little ones roll the balls and throw them without stopping. Arthur looks really funny covered in snow: the little elephants burst out laughing. They laugh so hard that they are all out of breath. The balls fall less quickly. Arthur throws some in turn. It's a battle!</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story2_snowball_kids.jpeg" alt="Kids throwing snowballs" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin-bottom: 15px; line-height: 1.8;">Épuisés et tout blancs, ils rentrent à la maison. Céleste les change de vêtements et leur prépare un chocolat bouillant. Les trois petits sont contents de se retrouver autour de la table avec leur maman.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Exhausted and all white, they return home. Céleste changes their clothes and prepares them a hot chocolate. The three little ones are happy to be around the table with their mom.</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">La famille Babar est aux sports d'hiver. II fait beau. Le téléphérique monte tout en haut de la montagne. Quelle merveilleuse descente ils vont faire!</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The Babar family is at the winter sports resort. The weather is nice. The cable car goes all the way to the top of the mountain. What a wonderful descent they are going to make!</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story2_cable_car.jpeg" alt="Babar family in cable car" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin-bottom: 15px; line-height: 1.8;">En avant, Pom! En avant, Flore et Alexandre! Ah! la vitesse, comme c'est excitant! Mais il faut être prudent. Attention! Aie!</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Forward, Pom! Forward, Flore and Alexandre! Ah! The speed, how exciting! But you have to be careful. Watch out! Ouch!</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Pom a cassé un ski. Babar le relève : « Pas de mal? Non, tu as eu de la chance.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Pom broke a ski. Babar picks him up: "No harm? No, you were lucky."</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">—Mon ski, gémit Pom. Je ne peux pas descendre comme ça, sur un seul ski!</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"My ski," moans Pom. "I can't go down like this, on one ski!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">- Viens dans mon sac à dos. C'est la seule chose à faire. Es-tu bien?</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"Come into my backpack. It's the only thing to do. Are you okay?"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">— Ça va, répond Pom, amusé.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"I'm fine," replies Pom, amused.</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">— Allons-y. Vous êtes prêts, les autres?</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"Let's go. Are you ready, the others?"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">—Oui, papa, nous sommes prêts.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"Yes, dad, we are ready."</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">—On dirait le Père Noël avec son sac plein de jouets! » s'écrie Alexandre en riant.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"He looks like Santa Claus with his bag full of toys!" exclaims Alexandre, laughing.</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story2_babar_backpack.jpeg" alt="Babar skiing with Pom in backpack" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin-bottom: 15px; line-height: 1.8;">Pendant la descente, la neige se met à tomber. Les sapins deviennent de plus en plus blancs. « Suivez-moi bien », dit Babar. Mais Flore, aveuglée par la neige, se trompe et prend un mauvais chemin...</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>During the descent, the snow starts to fall. The fir trees become whiter and whiter. "Follow me closely," says Babar. But Flore, blinded by the snow, makes a mistake and takes a wrong path...</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Babar s'en aperçoit vite, mais pour la retrouver, il faut un quart d'heure de recherches! Elle est en larmes. Alexandre lui dit : « Viens, nous allons faire un bonhomme de neige. »</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Babar notices quickly, but to find her, it takes a quarter of an hour of searching! She is in tears. Alexandre tells her: "Come, we are going to make a snowman."</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Les skis sont rangés. Avec la neige fraîche, Pom, Flore et Alexandre roulent des boules qui deviennent plus grosses qu'eux.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>The skis are put away. With the fresh snow, Pom, Flore and Alexandre roll balls that become bigger than them.</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Ils les posent l'une sur l'autre et sculptent un bonhomme. Que c'est amusant!</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>They place them one on top of the other and sculpt a snowman. How fun!</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">« Mettons-lui une casserole comme chapeau.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"Let's put a pot on him as a hat."</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">- Et des bouchons pour les yeux. » Alexandre lisse la trompe avec soin.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"And corks for the eyes." Alexandre smooths the trunk carefully.</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">«C'est papa, dit-il, comme il est drôle! Qu'est-ce qu'il dirait s'il le voyait? »</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>"It's dad," he says, "how funny he is! What would he say if he saw it?"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Et Flore s'écrie : « Je vais chercher papa! »</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>And Flore exclaims: "I'm going to get dad!"</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Mais Arthur, à toute vitesse, arrive sur sa luge. Il ne peut pas s'arrêter... Boum! Le bonhomme de neige a éclaté! Il n'en reste rien.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>But Arthur, at full speed, arrives on his sled. He can't stop... Boom! The snowman has burst! There's nothing left of it.</i></p>

<p style="margin-bottom: 15px; line-height: 1.8;">Pom, Flore et Alexandre crient : « Idiot! Tu ne pouvais pas freiner?</p>
<p style="margin-bottom: 10px; line-height: 1.8; padding-left: 20px;">⁃ Tu l'as fait exprès!</p>
<p style="margin-bottom: 10px; line-height: 1.8; padding-left: 20px;">⁃ Tu vas voir!</p>
<p style="margin-bottom: 15px; line-height: 1.8; padding-left: 20px;">⁃ Je suis sûr qu'il l'a fait exprès. »</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Pom, Flore and Alexandre shout: "Idiot! Couldn't you brake? You did it on purpose! You'll see! I'm sure he did it on purpose."</i></p>

<div style="text-align: center; margin: 25px 0;">
<img src="/static/images/story2_snowman_crash.jpeg" alt="Arthur crashes into snowman" style="max-width: 100%; width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

<p style="margin-bottom: 15px; line-height: 1.8;">Arthur ne peut même pas leur répondre. Il fait une culbute par-dessus la luge et la casserole tombe sur sa tête.</p>
<p style="margin-bottom: 20px; line-height: 1.8;"><i>Arthur can't even answer them. He somersaults over the sled and the pot falls on his head.</i></p>

<p style="margin-top: 30px; font-size: 0.9rem; color: #666;"><i>Reference: "Babar fait du ski" by Jean de Brunhoff.</i></p>'''

    db.session.add(ShortStory(title="Babar Fait Du Ski", content=story2_content))
    print("📚 Short stories added!")

    # ======================================================
    # 🧠 Quizzes (Expanded)
    # ======================================================
    quiz1 = Quiz(title="French Grammar Basics", description="Test your knowledge of basic French rules!")
    quiz2 = Quiz(title="Everyday French", description="Quiz about common items, food, and animals.")
    db.session.add_all([quiz1, quiz2])
    db.session.commit()

    # Quiz 1 Questions (Grammar)
    q1_questions = [
        ("Which article is feminine singular?", "le,la,les,un", "la"),
        ("How do you say 'I' in French?", "Je,Tu,Nous,Il", "Je"),
        ("What is the plural of 'le chat'?", "le chats,les chat,les chats,la chats", "les chats"),
        ("What is the correct conjugated form of \"aller\" in the \"nous\" form?", "Nous allez,Nous vont,Nous allons,Nous aller", "Nous allons"),
        ("Add the missing verb. Je ____ une pomme", "chante,mange,parle,danse", "mange"),
    ]
    
    # Quiz 2 Questions (Vocabulary)
    q2_questions = [
        ("What is 'un chien'?", "a cat,a bird,a dog,a horse", "a dog"),
        ("What color is 'rouge'?", "blue,red,green,yellow", "red"),
        ("How do you say 'Bread'?", "le fromage,le pain,le lait,la pomme", "le pain"),
        ("How do you say \"good evening\"?", "Bonjour,Bonne nuit,Bonsoir,Salut", "Bonsoir"),
        ("What is the verb for \"to relax\"?", "Écouter,Prendre,Finir,Détendre", "Détendre"),
    ]

    for q, opt, ans in q1_questions:
        db.session.add(QuizQuestion(quiz_id=quiz1.id, quiz_name=quiz1.title, question=q, options=opt, answer=ans))
    
    for q, opt, ans in q2_questions:
        db.session.add(QuizQuestion(quiz_id=quiz2.id, quiz_name=quiz2.title, question=q, options=opt, answer=ans))

    db.session.commit()
    print("🧠 Comprehensive Quizzes and Questions added!")
    print("🎉 Proper data population complete!")
