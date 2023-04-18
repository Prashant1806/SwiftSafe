from flask import render_template, request, redirect, url_for
from app import app
from app.forms import InstagramComparisonForm
from app.models import InstagramAccount
from app.compare import compare_accounts
from app.report import generate_report

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InstagramComparisonForm(request.form)

    if request.method == 'POST' and form.validate():
        account1 = InstagramAccount(form.account1.data, app.config['INSTAGRAM_ACCESS_TOKEN'])
        account2 = InstagramAccount(form.account2.data, app.config['INSTAGRAM_ACCESS_TOKEN'])
        results = compare_accounts(account1, account2)
        report = generate_report(results)

        return render_template('results.html', results=results, report=report)

    return render_template('index.html', form=form)
