from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Load from outputs folder
    country = pd.read_csv('outputs/country_trends.csv')
    inventors = pd.read_csv('outputs/top_inventors.csv')
    companies = pd.read_csv('outputs/top_companies.csv')

    return render_template(
        'dashboard.html',
        countries=country.iloc[:,0].tolist(),
        country_values=country.iloc[:,1].tolist(),
        inventors=inventors.iloc[:,0].tolist(),
        inventor_values=inventors.iloc[:,1].tolist(),
        companies=companies.iloc[:,0].tolist(),
        company_values=companies.iloc[:,1].tolist()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)