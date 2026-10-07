import os
import sys
from bs4 import BeautifulSoup


FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "starter",
    "index.html"
)

TOTAL_MARKS = 50
score = 0


def award(marks, message):
    global score
    score += marks
    print(f"PASS +{marks}: {message}")


def fail(message):
    print(f"FAIL  0: {message}")


# =========================================================
# Load student file
# =========================================================

if not os.path.exists(FILE):
    print("ERROR: starter/index.html not found.")
    sys.exit(1)


with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()


soup = BeautifulSoup(html, "html.parser")

style = soup.find("style")
css = style.get_text(" ", strip=True) if style else ""


# =========================================================
# 1. DOCUMENT AND FORM STRUCTURE - 6 MARKS
# =========================================================

print("\n[1] DOCUMENT AND FORM STRUCTURE")

if soup.find("html"):
    award(1, "<html> exists")
else:
    fail("<html> missing")

if soup.find("head"):
    award(1, "<head> exists")
else:
    fail("<head> missing")

if soup.find("body"):
    award(1, "<body> exists")
else:
    fail("<body> missing")

title = soup.find("title")

if title and title.get_text(strip=True) == "Complete a Form":
    award(1, "Correct page title")
else:
    fail("Title must be 'Complete a Form'")

form = soup.find("form")

if form:
    award(1, "<form> exists")
else:
    fail("<form> is missing")

if form and form.get("method") == "get":
    award(1, "Form uses GET method")
else:
    fail("Form method must be GET")


# =========================================================
# 2. CONTACT INFORMATION - 8 MARKS
# =========================================================

print("\n[2] CONTACT INFORMATION")

h1 = soup.find("h1")

if h1 and h1.get_text(" ", strip=True) == "Please complete our survey":
    award(2, "Correct main heading")
else:
    fail("Incorrect main heading")

email = soup.find("input", {"id": "email"})

if email:
    award(1, "Email field exists")
else:
    fail("Email field missing")

if email and email.get("type") == "email":
    award(1, "Email uses type=email")
else:
    fail("Email must use type=email")

if email and email.has_attr("required"):
    award(1, "Email is required")
else:
    fail("Email must be required")

if email and email.has_attr("autofocus"):
    award(1, "Email has autofocus")
else:
    fail("Email must have autofocus")

firstname = soup.find("input", {"id": "firstname"})

if firstname:
    award(1, "First name field exists")
else:
    fail("First name field missing")

if firstname and firstname.has_attr("required"):
    award(0.5, "First name is required")
else:
    fail("First name must be required")

lastname = soup.find("input", {"id": "lastname"})

if lastname:
    award(0.5, "Last name field exists")
else:
    fail("Last name field missing")

if lastname and lastname.has_attr("required"):
    award(0.5, "Last name is required")
else:
    fail("Last name must be required")


# =========================================================
# 3. GEOGRAPHIC INFORMATION - 10 MARKS
# =========================================================

print("\n[3] GEOGRAPHIC INFORMATION")

state = soup.find("input", {"id": "state"})

if state:
    award(2, "State field exists")
else:
    fail("State field missing")

if state and state.get("pattern") == "[A-Za-z]{2}":
    award(2, "State has two-letter validation pattern")
else:
    fail("State pattern must be [A-Za-z]{2}")

if state and state.get("placeholder") == "Two characters":
    award(1, "Correct state placeholder")
else:
    fail("State placeholder is incorrect")

if state and state.has_attr("required"):
    award(1, "State is required")
else:
    fail("State must be required")

if state and state.get("title"):
    award(1, "State has validation title")
else:
    fail("State validation title is missing")

zip_code = soup.find("input", {"id": "zip"})

if zip_code:
    award(1, "Zip code field exists")
else:
    fail("Zip code field missing")

if zip_code and zip_code.get("pattern") == r"\d{5}":
    award(1, "Zip code requires five digits")
else:
    fail("Zip code pattern must be \\d{5}")

if zip_code and zip_code.get("placeholder") == "Five digits":
    award(1, "Correct zip placeholder")
else:
    fail("Zip placeholder is incorrect")


# =========================================================
# 4. SURVEY CHECKBOXES - 8 MARKS
# =========================================================

print("\n[4] SURVEY CHECKBOXES")

checkboxes = {
    "web": "web",
    "facebook": "facebook",
    "twitter": "twitter",
    "message": "message"
}

for checkbox_id, expected_value in checkboxes.items():

    checkbox = soup.find(
        "input",
        {
            "type": "checkbox",
            "id": checkbox_id
        }
    )

    if checkbox:
        award(1, f"{checkbox_id} checkbox exists")
    else:
        fail(f"{checkbox_id} checkbox missing")

    if checkbox and checkbox.get("name") == checkbox_id:
        award(0.5, f"{checkbox_id} has correct name")
    else:
        fail(f"{checkbox_id} name is incorrect")

    if checkbox and checkbox.get("value") == expected_value:
        award(0.5, f"{checkbox_id} has correct value")
    else:
        fail(f"{checkbox_id} value is incorrect")


# =========================================================
# 5. SUBMIT AND RESET - 5 MARKS
# =========================================================

print("\n[5] SUBMIT AND RESET")

submit = soup.find(
    "input",
    {
        "type": "submit",
        "id": "button"
    }
)

if submit:
    award(2, "Submit button exists")
else:
    fail("Submit button missing")

if submit and submit.get("value") == "Submit":
    award(1, "Submit button has correct value")
else:
    fail("Submit button value should be Submit")

reset = soup.find(
    "input",
    {
        "type": "reset",
        "id": "reset"
    }
)

if reset:
    award(1, "Reset button exists")
else:
    fail("Reset button missing")

if reset and reset.get("name") == "reset":
    award(1, "Reset button has correct name")
else:
    fail("Reset button name is incorrect")


# =========================================================
# 6. CSS - 8 MARKS
# =========================================================

print("\n[6] CSS")

css_checks = [
    ("font:", 1, "Font styling exists"),
    ("width: 500px", 1, "Body width is 500px"),
    ("margin: 20px auto", 1, "Body is centered"),
    ("padding: 20px", 1, "Body padding is 20px"),
    ("border: 2px solid blue", 1, "Body border is correct"),
    ("float: left", 1, "Labels float left"),
    ("width: 15em", 1, "Text inputs have 15em width"),
    ("background-color: silver", 1, "Buttons use silver background"),
]

for keyword, marks, message in css_checks:
    if keyword in css:
        award(marks, message)
    else:
        fail(f"Missing CSS: {keyword}")


# =========================================================
# 7. ACCESSIBILITY AND VALIDATION - 5 MARKS
# =========================================================

print("\n[7] ACCESSIBILITY AND VALIDATION")

required_ids = [
    "email",
    "firstname",
    "lastname",
    "state",
    "zip"
]

for field_id in required_ids:

    field = soup.find("input", {"id": field_id})

    if field and field.has_attr("required"):
        award(0.5, f"{field_id} is required")
    else:
        fail(f"{field_id} must be required")


# Check labels

label_ids = [
    "email",
    "firstname",
    "lastname",
    "state",
    "zip",
    "web",
    "facebook",
    "twitter",
    "message"
]

label_score = 0

for field_id in label_ids:

    label = soup.find("label", {"for": field_id})

    if label:
        label_score += 0.5

if label_score == 5:
    award(5, "All form controls have associated labels")
else:
    award(label_score, f"{int(label_score / 0.5)}/10 labels are present")


# =========================================================
# FINAL SCORE
# =========================================================

score = min(score, TOTAL_MARKS)

print("\n" + "=" * 60)
print("COMPLETE A FORM - FINAL GRADE")
print("=" * 60)
print(f"SCORE: {score}/{TOTAL_MARKS}")

if score == TOTAL_MARKS:
    print("STATUS: PASS")
else:
    print("STATUS: REVIEW REQUIRED")

print("=" * 60)

sys.exit(0)
