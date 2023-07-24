# github-user-stats
Gets aggregated statistics across a user's repositories.
## How to Use
Run Flask server which hosts the website on localhost:5000. Enter a github username in the textbox and check the checkbox if you want to retrieve statistics on ONLY the user's nonforked repositories.

After clicking the submit button, you will be redirected to another page containing the resultsof the following statistics:
* total repository count
* total stargazer count
* total fork count
* average repository size (MB)
* frequency of repos per programmining language used by the user

## Architecture
Flask server with html templates and python backend using Github's Search RESTful API.


