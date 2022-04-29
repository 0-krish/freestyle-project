# web_app/routes/news_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports

from app.news_service import get_headlines

news_routes = Blueprint("news_routes", __name__)

@news_routes.route("/api/news/headlines.json")
def news_headlines_api():
    print("NEWS HEADLINES (API)...")
    print("URL PARAMS:", dict(request.args))

    country_code = request.args.get("country_code") or "US"
    news_category = request.args.get("news_category") or "business"

    results = get_headlines(country_code=country_code, news_category=news_category)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Inputs. Please try again."}), 404

@news_routes.route("/news/form")
def news_form():
    print("NEWS HEADLINES...")
    return render_template("news_form.html")

@news_routes.route("/news/headlines", methods=["GET", "POST"])
def news_headlines():
    print("NEWS HEADLINES...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    country_code = request.args.get("country_code") or "US"
    news_category = request.args.get("news_category") or "business"

    results = get_headlines(country_code=country_code, news_category=news_category)
    if results:
        flash("News Headlines Generated Successfully!", "success")
        return render_template("news_headlines.html", country_code=country_code,
                               news_category=news_category, results=results)
    else:
        flash("Incorrect Inputs. Please try again!", "danger")
        return redirect("/news/headlines")
