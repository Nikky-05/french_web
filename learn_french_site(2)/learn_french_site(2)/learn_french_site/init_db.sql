-- Run in MySQL (adjust user/database names if needed)
CREATE DATABASE IF NOT EXISTS learn_french;
USE learn_french;

-- Sample inserts (tables are created by SQLAlchemy if not present)
INSERT INTO Vocabulary (category, french, english, pronunciation, created_at)
VALUES
('Colors','Noir','Black','nwar', NOW()),
('Colors','Blanc','White','blahn', NOW()),
('Numbers','un','one','uhn', NOW()),
('Animals','le chien','dog','luh chien', NOW()),
('Food','la pomme','apple','lah pom', NOW());

INSERT INTO GrammarItem (title, content, created_at)
VALUES
('Greetings','<p class="sub-heading">Informal (to a friend, tu form)</p>
<p class="text-line">Bonjour/Salut</p>
<p class="text-line">Comment ça va?/Ça va ?</p>
<p class="text-line">Comment tu t\'appelles?</p>

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

<p class="sub-heading">To ask one\'s name</p>
<p class="text-line">Comment tu t\'appelles?  Comment vous appelez-vous?</p>

<p class="sub-heading">To take a leave</p>
<p class="text-line">Au revoir</p>
<p class="text-line">Bonne journée</p>
<p class="text-line">À demain</p>
<p class="text-line">Bonne soirée</p>
<p class="text-line">À bientôt</p>
<p class="text-line">Bon après-midi</p>', NOW()),

('Articles','<p class="sub-heading">Definite: -</p>

<p>Definite articles are used for specific nouns. It refers to the article "the" in English. There are different articles corresponding to gender and number.</p>

<p class="text-line"><span class="article-word">la</span> - feminine singular <span class="french-term">(féminin singulier)</span></p>
<p class="text-line"><span class="article-word">le</span> - masculine singular <span class="french-term">(masculin singulier)</span></p>
<p class="text-line"><span class="article-word">l\'</span> - before a vowel or silent h (masculine and feminine) <span class="french-term">(masculin et féminin)</span></p>
<p class="text-line"><span class="article-word">les</span> - plural (masculine and feminine) <span class="french-term">(masculin et féminin)</span></p>

<p class="section-title">Examples</p>

<p class="text-line"><span class="article-word">la</span> robe - the dress</p>
<p class="text-line"><span class="article-word">le</span> livre - the book</p>
<p class="text-line"><span class="article-word">l\'</span>histoire - the story</p>
<p class="text-line"><span class="article-word">les</span> tables - the tables</p>

<p class="sub-heading">Indefinite: -</p>

<p>Indefinite articles are used for unspecified nouns. It refers to the articles "a", "an", and "some".</p>

<p class="text-line"><span class="article-word">un</span> - masculine singular <span class="french-term">(masculin singulier)</span></p>
<p class="text-line"><span class="article-word">une</span> - feminine singular <span class="french-term">(féminin singulier)</span></p>
<p class="text-line"><span class="article-word">des</span> - plural (feminine and masculine) <span class="french-term">(masculin et féminin)</span></p>

<p class="section-title">Examples</p>

<p class="text-line"><span class="article-word">un</span> cahier - a notebook</p>
<p class="text-line"><span class="article-word">une</span> photo - a picture</p>
<p class="text-line"><span class="article-word">des</span> fruits - fruits</p>', NOW()),

('Gender','<p>In French, every noun has a gender. It is either masculine or feminine. Masculine words are followed by masculine articles such as "un" and "le". Feminine words are always used with feminine articles such as "la" and "une".</p>

<p>Tip: In most of the cases, nouns ending with an "e" are feminine, nouns ending with an "s" or "x" are plural, and the rest are masculine.</p>

<p class="section-title">Examples</p>

<p class="sub-heading">Masculin</p>
<p>un chapeau - a gift</p>

<p class="sub-heading">Féminin</p>
<p>une gomme - an eraser</p>

<p class="sub-heading">Pluriel</p>
<p>des stylos - some pens</p>', NOW()),

('Subject Pronouns','<table class="grammar-table">
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
<p>Ils regardent la télé. (They watch TV.)</p>', NOW()),

('Verbs','<p>Verbs in French either end in "er", "ir", or "re". There are a few exceptions, with the most common ones being <span class="article-word">avoir</span> (to have) and <span class="article-word">être</span> (to be).</p>

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

<p>All of these verbs are conjugated according to different auxiliary verbs and tenses.</p>', NOW()),

('Basic Sentence Structure','<p>In French, sentences follow this format: <span class="article-word">Subject + Verb + Object</span>.</p>

<p class="text-line">Je mange une pomme.</p>
<p class="text-line">Nous jouons au foot.</p>
<p class="text-line">Elle parle avec sa mère.</p>

<p>For example, in the sentence, "Je mange une pomme." "Je" is the subject, "mange" is the verb, and "une pomme" is the object.</p>

<p class="sub-heading">Adjectives come after the noun: -</p>
<p class="text-line">une bouteille d\'eau rose - pink water bottle</p>
<p class="text-line">un sac bleu - blue bag</p>

<p class="sub-heading">Negative words</p>
<p>Usually, "ne" and "pas" are used to make a sentence negative.</p>
<p class="text-line">Je ne comprends pas. <span class="french-term">(I don\'t understand.)</span></p>

<p>Questions in French can be asked in the same way as a statement, but with a different tone, or by adding the phrase "est-ce que."</p>
<p class="text-line">Tu as mangé?</p>
<p class="text-line">Est-ce que tu as mangé?</p>', NOW()),

('Conjugations','<p class="section-title">Avoir</p>
<p class="text-line">J\'ai</p>
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
<p class="text-line">J\'aime</p>
<p class="text-line">Tu aimes</p>
<p class="text-line">Il/Elle/On aime</p>
<p class="text-line">Nous aimons</p>
<p class="text-line">Vous aimez</p>
<p class="text-line">Ils/Elles aiment</p>', NOW());

INSERT INTO Story (title, content) VALUES
('Le Petit Chaperon Rouge','Il était une fois une petite fille...'),
('Cendrillon','Il était une fois une jeune fille très gentille...');

INSERT INTO QuizQuestion (quiz_name, question, options, answer)
VALUES
('Quiz 1','Choose the correct article: ___ livre (book)','la|le|les|l\'','le'),
('Quiz 2','Which sentence is correct?','Je ai un crayon.|J\'ai un crayon.|Je as un crayon.|J\'ai une stylo.','J\'ai un crayon.');
