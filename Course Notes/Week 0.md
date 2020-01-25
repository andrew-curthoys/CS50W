# Week 0: Git

## Overview of Git

* Keeps track of changes to code & history
* Synchronizes code between different people
* Can test changes to code without losing the original
* Can revert back to old versions of code

### Merge Conflicts

* When there is a conflict between a local copy of a file and a remote copy, you
run into a merge conflict
  * Anything after `<<<<< HEAD` and before `=====` was changed locally
  * Anything after `=====` and before `>>>>> {conflicting commit id}` was
  changed remotely

## HTML: Hypertext Markup Language

* `<head>` tag is typically used to contain metadata
* `<title>` tag defines what is shown in the label of the webpage's tab or
window
* `<ul>` tag is for an unordered list, it will show with bullet points in your
browser
* `<ol>` tag is for an ordered list, it will show as an automatically numbered
list in your browser
* `<li>` tag is for list items that go inside unordered or ordered lists
* HTML attributes go inside tags to provide information to the tag. For example,
with the example image tag `<img src="example_image.jpg">` 'src' is an attribute
* With img tags, if you specify either the height or width, the browser will
fill in the other dimension keeping the original aspect ratio. If you specify
both the height & width you can distort the image (either intentionally or
unintentionally).
  * In addition to setting width & height as a certain number of pixels, you can
  also set it as a percentage of the size of the webpage (or container). For
  example, you can set your img width to 50% and it will occupy half of the
  width of the page, even as you change your window size.
### Tables
  * `<tr>`: table row
  * `<th>`: table header, i.e. column names
  * `<tr>`: table row
  * `<td>`: table data, contains the data you put in `<tr>`'s
### Forms
  * Like `<img>` tags, `<input>` tags don't have a start & end tags, they do
  need attributes to define their functionality though.

### Document Object Model (DOM)

* The tree structure that HTML webpages utilize
* The DOM becomes useful with JavaScript and CSS

## CSS: Cascading Style Sheets

* Document to style HTML page by tags
* `<div>` tag is a 'division' of your code, it doesn't have a strict meaning,
it's just a convention to keep your code organized, plus you can give it a name
and/or id
* `margin` is the border around an element
* `padding` is the border between the edge of an element and the content inside
the element
* If you provide multiple `font-family` attributes, the browser will attempt to
use the first font, but if it does not have that font it will use the backup(s)
  * E.g. you could set your `font-family` to "Arial, sans-serif" that will use
  any generic sans serif font if the browser does not have Arial
* If you use the `border-collapse` tag, it will remove the double borders around
every 'cell' if you use the `border` tag around every `<td>` tag
* `id` is a unique element in HTML, i.e. you can only use a particular `id` once
* `class` attribute allows you to style many elements in the same manner
* To identify elements in CSS, you use `#` for `id`s & `.` for classes
  * `#top` would style the "top" `id`
  * `.centered` would style the "centered" `class`
  * GitHub pages allows you to publish repo documents to the internet
