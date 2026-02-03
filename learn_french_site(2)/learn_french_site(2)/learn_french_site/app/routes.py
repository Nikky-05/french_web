from flask import Blueprint, render_template
from app.models import Vocabulary, GrammarItem, ShortStory, QuizQuestion

# Define a blueprint for main routes
bp = Blueprint('main', __name__)

# ------------------------------------------
# 🏠 HOME PAGE
# ------------------------------------------
@bp.route("/")
def home():
    return render_template("home.html")


# ------------------------------------------
# 📘 VOCABULARY PAGE
# ------------------------------------------
@bp.route("/vocabulary")
def vocabulary():
    category = request.args.get('category')
    if category:
        vocab_list = Vocabulary.query.filter_by(category=category).all()
    else:
        vocab_list = Vocabulary.query.all()
    return render_template("vocabulary.html", vocab_list=vocab_list, category=category)


# ------------------------------------------
# 📗 GRAMMAR PAGE
# ------------------------------------------
@bp.route("/grammar")
def grammar():
    grammar_items = GrammarItem.query.all()
    return render_template("grammar.html", grammar_items=grammar_items)


# ------------------------------------------
# 📕 SHORT STORIES
# ------------------------------------------
@bp.route("/stories")
def stories():
    stories = ShortStory.query.all()
    return render_template("stories.html", stories=stories)

@bp.route('/story/<int:story_id>')
def story_detail(story_id):
    story = ShortStory.query.get_or_404(story_id)
    return render_template('story_detail.html', story=story)


# ------------------------------------------
# 🧠 QUIZZES PAGE
# ------------------------------------------
@bp.route('/quizzes')
def quizzes():
    from app.models import Quiz
    quizzes = Quiz.query.all()
    return render_template('quizzes.html', quizzes=quizzes)

@bp.route('/quiz/<int:quiz_id>')
def quiz_detail(quiz_id):
    from app.models import Quiz, QuizQuestion
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = QuizQuestion.query.filter_by(quiz_id=quiz.id).all()
    return render_template('quiz_detail.html', quiz=quiz, questions=questions)

# ------------------------------------------
# ℹ️ ABOUT PAGE
# ------------------------------------------
@bp.route("/about")
def about():
    return render_template("about.html")


# ------------------------------------------
# 🛠️ ADMIN DASHBOARD
# ------------------------------------------
@bp.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")


# @bp.route("/admin/add_vocab")
# def add_vocab():
#     return render_template("admin_new_vocab.html")


@bp.route("/admin/add_grammar")
def add_grammar():
    return render_template("admin_new_grammar.html")


@bp.route("/admin/add_story")
def add_story():
    return render_template("admin_new_story.html")


@bp.route("/admin/add_quiz")
def add_quiz():
    return render_template("admin_new_quiz.html")



from flask import request, redirect, url_for, flash
from app.models import db, Vocabulary

@bp.route("/admin/add_vocab", methods=["GET", "POST"])
def add_vocab():
    if request.method == "POST":
        category = request.form.get("category")
        french = request.form.get("french")
        english = request.form.get("english")
        pronunciation = request.form.get("pronunciation")

        if not (category and french and english):
            flash("⚠️ Please fill out all required fields.")
            return redirect(url_for("main.add_vocab"))

        new_word = Vocabulary(
            category=category,
            french=french,
            english=english,
            pronunciation=pronunciation
        )
        db.session.add(new_word)
        db.session.commit()

        flash("✅ New vocabulary word added successfully!")
        return redirect(url_for("main.vocabulary"))

    return render_template("admin_new_vocab.html")
