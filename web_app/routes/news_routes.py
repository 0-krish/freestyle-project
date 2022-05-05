# web_app/routes/news_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.news_service import get_headlines
from app.news_email import send_news_email
from app.data_storage import write_sheet

news_routes = Blueprint("news_routes", __name__)

@news_routes.route("/api/news/headlines.json")
def news_headlines_api():
   
    '''
    Gets News API data for a given country and news category via the "/api/news/headlines.json" route
    '''
    print("NEWS HEADLINES (API)...")
    print("URL PARAMS:", dict(request.args))

    country_code = request.args.get("country_code") or "US"
    news_category = request.args.get("news_category") or "business"

    results = get_headlines(get_country_code=country_code, get_news_category=news_category)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Inputs. Please try again."}), 404

@news_routes.route("/news/form",methods=["GET", "POST"])
def news_form():

    '''
    Via the "/news/form" route, renders the "news_form.html" template if the request method is "GET", otherwise the form sends a "POST"  
    '''

    print("NEWS HEADLINES...")

    if request.method == "GET":
        return render_template("news_form.html")

    elif request.method == "POST": # the form will send a POST
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)


@news_routes.route("/news/headline_options", methods=["GET", "POST"])
def news_headline_options():

    '''
    Via the "/news/headline_options" route, renders the "news_headlines_options.html" template if request method is "GET". If request method is "POST", renders "news_headlines.html" template.
    '''

    print("NEWS HEADLINE OPTIONS...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
        return render_template("news_headlines_options.html")

    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)
        results = get_headlines(get_country_code=request_data['country'], get_news_category=request_data['category1'])
        return render_template("news_headlines.html", country_code=request_data['country'],
                               news_category=request_data['category1'], results=results)

@news_routes.route("/news/headlines")
def news_headlines():

    '''
    Via the "/news/headlines" route, renders  the "news_headlines.html", populated with headlines based on the user specified country and news category.
    '''

    print("NEWS HEADLINES...")

    country_code = request.args.get("country_code") or "US"
    news_category = request.args.get("news_category") or "business"

    results = get_headlines(get_country_code=country_code, get_news_category=news_category)
    if results:
        flash("News Headlines Generated Successfully!", "success")
        return render_template("news_headlines.html", country_code=country_code,
                               news_category=news_category, results=results)
    else:
        flash("Incorrect Inputs. Please try again!", "danger")
        return redirect("/news/headlines")


@news_routes.route("/news/send_email", methods=["GET", "POST"])
def news_send_email():

    '''
    Via /news/send_email" route, stores the user data onto a sheet so that they can subscibe to the email service. 

    Redirects back to /news/form is request method is "GET", sends email and stores user inputs if request method is "POST"
    '''
    print("SEND NEWS HEADLINES EMAIL...")

    if request.method == "GET":
        print("GET METHOD ON SEND NEWS", dict(request.args))
        return redirect("/news/form")

    elif request.method == "POST":  # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)
        email_result = send_news_email(request_data['user_name'], request_data['user_email'],
                                       request_data['country'], request_data['category1'])

        if email_result:
            results = get_headlines(get_country_code=request_data['country'],
                                    get_news_category=request_data['category1'])

            write_sheet(request_data['user_name'], request_data['user_email'],
                        request_data['country'], request_data['category1'])

            flash("Subscription Successful!", "success")

            return render_template("news_headlines.html", country_code=request_data['country'],
                                   news_category=request_data['category1'], results=results)
        else:
            flash("Incorrect Inputs. Please try again!", "danger")
            return redirect("/news/form")
