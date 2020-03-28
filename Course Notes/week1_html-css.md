# Week 1: HTML & CSS

## Git Review
* `git pull` will get the most up-to-date data from the remote and combine it
with your local version
  * This is actually a 2 step process:
    * First it runs `git fetch` to get the most current master branch from the
    remote
    * Then it runs `git merge origin/master` to merge the branch to your local
    repo
* Fork: an entirely separate version of a repository that gets copied based off
an original
  * Nothing you do on a fork will affect what happens to the main repo
* Pull request: a request for changes from one branch of a repo to the original
version of the repo
  * A good way to get others to review your code before it is merged

## HTML

* Buttons with `<a href>` references don't have to only link to other webpages,
you can link to other sections of your same page by id with a `#` in front of
the id
  * Example: `<a href="#section1">` will take you to the section with the id of
  `section1`
* Example HTML4 Organization:
  * `<div class="header">`
  * `<div class="nav">`
  * `<div class="section">`
  * `<div class="footer">`
  * ...
* HTML5 has simplified some of this by creating tags for commonly used classes:
  * `<header>`
  * `<nav>`
  * `<section>`
  * `<footer>`
* New tags in HTML5:
  * `<audio>`
  * `<video>`
  * `<datalist>`
    * `datalist` will allow you to input data into a form and it will begin to
    autocomplete based on a list you have set up in the HTML
      * Example: you begin typing 'United' into a form for country and it starts
      to show 'United States', 'United Kingdom', etc.
* 34:00: Example HTML form

## CSS

* Descendants: if you put a tag after another tag, that means the second tag
will receive the styling as long as it's contained within the first tag
  * For example: `ol li` will style the same thing for every list item that is
  in an ordered list
  * 42:00: Example of a page with a list having a sublist & descendants
* Immediate children: will apply styling to any elements that are immediately
following the first item
  * For example: `ol > li` will apply styling to list elements inside an
  ordered list, but not to any elements that are sub-elements of the list items
  * 47:15: Example of a page with immediate children
* Attribute styling: you can style certain attribute types
  * For example: `input[type=text]` will style all text input fields in a form
* 48:05: Example of a form with attribute styling
* 51:30: Styling a button with hover pseudoclass
  * Example: `a::before` will style things before a link
  * Example: `p::selection` will style everything in a paragraph when it's
  highlighted
* CSS Selectors
  * a, b: multiple element selector
  * a b: descendant selector
  * a > b: child selector
  * a + b: adjacent sibling selector
  * [a=b]: attribute selector
  * a:b: pseudoclass selector
  * a::b: pseudoelement selector

## Responsive Design

### Media Queries

* CSS that appears depending on the device you are viewing the webpage on
  * You call media queries by `@media`
* 1:00:20: Example of a media query that responds only when printing
* 1:02:45: Example of a media query that responds to different screen sizes
* `<meta name="viewport" content="width=device-width, initial-scale=1.0">` will
ensure that your page renders appropriately on a mobile device, taking into
account the size of the device
* 1:08:50: example of a flexbox
  * `.container {`
        `display: flex;`
        `flex-wrap: wrap;`
      `}`
* 1:11:00: Example of a responsive grid
* 1:14:30: Introduction to Bootstrap

### Bootstrap

* Bootstrap pages are divided into 12 columns & you can control how many columns
things on your page take up
* 1:16:15: First Bootstrap example
* 1:18:00: Second Bootstrap example with a change in number of elements per row
depending on screen size
* 1:22:20: Bootstrap alert example

### Sass

* 1:26:20: Bootstrap example with Sass variables
  * Variables in Sass begin with a $
  * Example scss script:
    * `$color: red;`
      `ul {`
        `color: $color;`
      `}`
      `ol {`
        `color: $color;`
       `}`
  * Browsers don't understand scss out of the box, you need to compile .scss
  files to .css using Sass.
    * Example: `sass variables.scss variables.css`
  * It can get annoying to re-compile .scss files every time you make a change,
  however Sass can watch files & automatically re-compile whenever there is a
  change
    * Example: `sass --watch variables.scss:variables.css`
    * Some webpages have built-in support for .scss files & will automatically
    compile them for you
* 1:35:30: Example of nesting CSS selectors using Sass
  * Nesting is only useful for readability
* 1:39:40: Example of Sass inheritance
  * `%` in Sass is a tag that you can create a template
