# Complete a Form

## Total Marks: 50

## Objective

Create an HTML survey form using semantic HTML form controls,
HTML5 validation attributes, and CSS.

## Requirements

### Page Structure

The page must contain:

- HTML5 document structure
- Page title: `Complete a Form`
- Main heading: `Please complete our survey`
- A `<form>` element
- Form method: `get`
- Form action: `survey_data.html`

### Contact Information

Create required fields for:

- Email address
- First name
- Last name

The email field must:

- Use `type="email"`
- Have `required`
- Have `autofocus`

### Geographic Information

Create:

- State
- Zip code

State must:

- Be required
- Use a two-letter pattern
- Have placeholder `Two characters`
- Have an appropriate validation title

Zip code must:

- Be required
- Accept exactly five digits
- Have placeholder `Five digits`
- Have an appropriate validation title

### Survey Options

Create four checkboxes:

- Web Search
- Facebook
- Twitter
- Email message

Each checkbox must have an associated `<label>`.

### Buttons

Create:

- Submit button
- Reset button

### CSS

Use CSS to style:

- Overall page
- Heading
- Labels
- Text inputs
- Checkboxes
- Submit/reset buttons
- Form layout

## Marks

| Category | Marks |
|---|---:|
| HTML document and form structure | 6 |
| Contact information | 8 |
| Geographic information | 10 |
| Survey checkboxes | 8 |
| Submit/reset controls | 5 |
| CSS layout and styling | 8 |
| HTML5 validation/accessibility | 5 |
| **Total** | **50** |

## Submission

Complete:

    ******starter/index.html******

Commit and push your solution.

GitHub Actions will automatically run the tests.
