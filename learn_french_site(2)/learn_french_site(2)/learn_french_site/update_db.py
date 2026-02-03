"""
Run this script to update the grammar content in the database.
Usage: python update_db.py
"""

from app import create_app
from app.models import db, GrammarItem

app = create_app()

# New content for Gender
gender_content = '''<p>In French, every noun has a gender. It is either masculine or feminine. Masculine words are followed by masculine articles such as "un" and "le". Feminine words are always used with feminine articles such as "la" and "une".</p>

<p>Tip: In most of the cases, nouns ending with an "e" are feminine, nouns ending with an "s" or "x" are plural, and the rest are masculine.</p>

<p class="section-title">Examples</p>

<p class="sub-heading">Masculin</p>
<p>un chapeau - a gift</p>

<p class="sub-heading">Féminin</p>
<p>une gomme - an eraser</p>

<p class="sub-heading">Pluriel</p>
<p>des stylos - some pens</p>'''

# New content for Articles
articles_content = '''<p class="sub-heading">Definite: -</p>

<p>Definite articles are used for specific nouns. It refers to the article "the" in English. There are different articles corresponding to gender and number.</p>

<p><b>la</b> - feminine singular <i>(féminin singulier)</i></p>
<p><b>le</b> - masculine singular <i>(masculin singulier)</i></p>
<p><b>l'</b> - before a vowel or silent h (masculine and feminine) <i>(masculin et féminin)</i></p>
<p><b>les</b> - plural (masculine and feminine) <i>(masculin et féminin)</i></p>

<p class="section-title">Examples</p>

<p><b>la</b> robe - the dress</p>
<p><b>le</b> livre - the book</p>
<p><b>l'</b>histoire - the story</p>
<p><b>les</b> tables - the tables</p>

<p class="sub-heading">Indefinite: -</p>

<p>Indefinite articles are used for unspecified nouns. It refers to the articles "a", "an", and "some".</p>

<p><b>un</b> - masculine singular <i>(masculin singulier)</i></p>
<p><b>une</b> - feminine singular <i>(féminin singulier)</i></p>
<p><b>des</b> - plural (feminine and masculine) <i>(masculin et féminin)</i></p>

<p class="section-title">Examples</p>

<p><b>un</b> cahier - a notebook</p>
<p><b>une</b> photo - a picture</p>
<p><b>des</b> fruits - fruits</p>'''

# New content for Subject Pronouns with table
subject_pronouns_content = '''<table class="grammar-table">
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
<p>Ils regardent la télé. (They watch TV.)</p>'''

with app.app_context():
    # Update Articles
    articles = GrammarItem.query.filter_by(title='Articles').first()
    if articles:
        articles.content = articles_content
        print("Updated: Articles")

    # Update Gender
    gender = GrammarItem.query.filter_by(title='Gender').first()
    if gender:
        gender.content = gender_content
        print("Updated: Gender")

    # Update Subject Pronouns
    subject_pronouns = GrammarItem.query.filter_by(title='Subject Pronouns').first()
    if subject_pronouns:
        subject_pronouns.content = subject_pronouns_content
        print("Updated: Subject Pronouns")

    db.session.commit()
    print("\nDatabase updated successfully! Refresh your browser to see changes.")
