# George Shaw Brewery

George Shaw Brewery are a small local brewery in Leigh, United Kingdom. I was able to meet the volunteers who are trying to bring the historic brewery back to life, last year at my festival 'Leigh Festival'. I can see big things happening with George Shaw and want to be a part of it. Therefore I decided to base this project on them. With the hope to add all the extra security and admin details in the future and sell them this website.

Users can browse and purchase any of their beers. They can also look at information such as the News of George Shaw or the story which includes images and a description of who they are. In the future I want to add a scrollable timeline too.

The payment system uses Stripe. Please note that this website is for educational purposes do not enter any personal credit/debit card details when using the site.

To test this system, test card details can be used. A list of these can be found in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [George Shaw](https://george-shaw-brewery.herokuapp.com/)

---

![Site Mockup]()

## Table of contents
* [User goals](#User-goals)
* [Features](#Features)
* [Agile Methodology](#Agile-methodology)
* [Technology](#Technology)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credits)

# User Goals
## User Goals - Viewing and Navigation
- As a Site User, I can intuitively navigate around the site so that I can find content.
- As a Site User, I can view a list of products so that I can select a product to view.
- As a shopper, I can click on a product so that I can read the full product details.
- As a shopper, I can view a specific category of products so I can browse the type of products I'm looking for.
- As a shopper, I can search all products so that I can find what I am looking for.
- As a shopper, I can sort all products so that I can view products based on price or title.

## User Goals - User Account and Profile
- As a site user, I can register an account so that I can have a personal account.
- As a site user, I can log in or log out of my account so that I can keep my account secure.
- As a site user, I can easily see my login status so that I know if I'm logged in or out.
- As a site user, I can save my personal details in my user profile so that I do not have to fill them out for future orders.
- As a site user, I can view my order history so that I can remember what purchases I've made.

## User Goals - Purchasing
- As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.
- As a shopper, I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.
- As a shopper, I can view the contents of my shopping bag at any time so I can see what is included and the total cost.
- As a shopper, I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.
- As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.
- As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.
- As a shopper checkout as a guest so I don't have to sign up for an account.
- As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.
- As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.

## User Goals - User Interaction
- As a site user, I can read up on all the News Easily.

## Website Owner Business Goals - Admin & Store Management
- As a store owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.
- As a site owner, I can add/delete images and location of previous design projects so that I can manage the site's contents.
- As a site owner, I can add/edit/delete news articles through an easy-to-use interface so that I can manage the page's news.

## User stories not yet implemented
- As a shopper, I can add products to my saved items so that I can go back and view them at a later date.
- As a shopper, I can view my saved products so I can find them easily in the one location.
- As a site user, I can sign up for the website's newsletter so that I can keep up to date with new products and promotions.
- As a site user, I can write reviews on the products.

---

# Features
## Clean Structure
The website is designed to give the user a great experience, with an easy to use design and to be user-friendly on all types of devices. There will be no difference in the experience users have when on a mobile compared to a laptop!

### Wire frames
I decided to use Adobe XD to create my wire frames.
#### Wire frames for Bigger Screens
![Mobile/small screens wire frame]()

#### Wire frames for Mobile Screens
![Bigger screens wire frame]()

##### Coloured in Wire frames
![Bigger screens wire frame]()

### Site Styles

#### Colours
* Background colour - #fff 
* Secondary colour - #725538
* Text colour  - #000000
* Secondary text colour  - #ffffff
* Secondary color:hover - #4E3A25

#### Font

* For my font I used 'Montserrat', with a backup of sans-serif.

#### Images

* For my images I used all my own images. I was able to get some bottles and cans from George Shaw and went down to a local photography studio to get some nice images.

[Back to Table of contents](#table-of-contents)

---

# Features of the Website: 
The website consists of .


#### Header
* ##### Logo
- This is George Shaws actual Logo.
- This logo is positioned in the top left of the navigation bar on big screens the center on small. The logo is linked to the home page for ease of navigation for the user.

* ##### Navigation Bar
- The navigation bar is visible at the top of every page and includes links to the other pages.
-The navigation bar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small.
- Hovering over the links will turn the font to opacity 0.5.

* ##### Search Bar
- The search bar displays as an icon and will display below the nav bar when clicked.
- Any searched word will match itself to any text in the product's title, or description and display the results on the product's page.

* ##### User Icon
- The User icon navigation link is a drop down menu which includes the Sign up and Log in links.
- The options to Sign up or Log in will change to the option to log out once a user has logged in.
- Once a user has signed in, the 'My Profile' option becomes available in the User dropdown.
- If user is a superuser the options of Add Product and Add Article show.

* ##### Bag Icon
- Located on the right side of the navbar next to the User icon is the bag Icon.
- As the user adds products to their bag, a toast message appears in the top right-hand corner of the screen informing the user that the item has been added, giving them a snapshot of the bag contents and the total cost of the bag.
- Clicking the bag icon navigates the user to the shopping bag page which displays a summary of what's been added.

#### Footer
- The footer appears at the bottom of every page.
- The footer section includes links to Facebook, Instagram, Twitter and Instagram.
- The Quick Links section has links to the main parts of the site: 'Home', 'Our Story', 'Shop', 'News' and 'Contact Us'.
- The Customer Information Links section has links to the main parts of the site: 'Delivery Policy', 'Terms & Conditions', 'Privacy Policy' and 'Refund Policy'.
- The Get In Touch Section has the address of the brewery, email address and phone number.
-Clicking all external links will open up the respective website in another tab to avoid pulling the user away from the site.


#### Home Page
* ##### Hero Image
- The hero image shows all the beers available at the moment as well as a link to the shop.

* ##### Sign Up To News Letter / social media links
- Sign up to the news letter doesn't work at the moment but it will be powered by Mailchimp where the user can input their email address to signup to the monthly newsletter.
- Connect with us gives the user the option to easily check out the social media, all links will open up the respective website in another tab to avoid pulling the user away from the site.

#### Profile
* ##### Delivery Info
- The delivery details section stores the user's delivery address and phone number.
- The information provided here is used to autofill the delivery address when placing an order.

* ##### Order History
- The order history section displays a list of every order the user has placed.
- The table displays the order number, date it was ordered and the order total.
- Clicking the order number will take the user to a summary page of that order. 

#### Our Story
- You are greated with an image of the team with information about who George Shaw was and who they are today.
- This also includes the Sign Up To News Letter / social media links section.

#### Shop
* ##### Product card
- Each product card shows an image of the product, its title, category, rating and price.
- If the user is a superuser, edit and delete buttons will appear at the bottom of the product card.
- The products page is fully responsive, adjusting how many products are on each row depending on the user's screen size.
- A sort box is located on the products page where users can sort all products by price in ascending or descending order and by title (A-Z).

#### Product Detail
- When the user clicks on an individual product card they are taken to the full product details.
- The product detail page displays the product image, title, category, price, ABV, ml and the items description.
- If the user is a superuser, edit and delete buttons will appear below these details.

* #### The Quantity Buttons
- The quantity buttons are located underneath the product ml details and are used to add items to the bag.
- The plus and minus buttons increase and decrease the input value.
- If the value is set to 1 the minus quantity will be disabled. Respectively if the value is set to 99 the plus button is disabled.
- If the user manually types in a negative number or a number >99 and clicks "Add to Bag" an error button will appear informing the user of the parameters needed to be successful.
- Clicking the 'Add to Bag' button takes the number in the input field and adds that amount of products to the bag.
- Clicking the 'Keep Shopping' button takes the user back to the store.

#### Product Management Page
* ##### Add Product
- The add product page can be accessed by clicking the 'Add Product' button on the account button on the header or in the user dropdown menu. These options are only visible to superusers.
- If a user tries to add a product (by changing the url) without being a superuser they are redirected to a custom 403 page.
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- The SKU field must be unique. An error message will appear if the SKU already exists.
- If a price is added with more than 6 digits the form will fail and an error message will appear under the price field.
- The user can upload a photo if they wish. If they choose not to, a default image displays as their product image.
- Clicking the 'Add Product' button at the bottom of the form will create the product providing there are no errors on the form.
- The user will receive a success message notifying them that the product has been successfully added.

* ##### Edit Product
- The superuser can choose to edit a Product by clicking the edit button on the product card or on the product detail page.
- The form opens with all fields populated with the original content.
- The image field displays a thumbnail of the existing image and has a checkbox option to remove it. Checking this will change the image to the default image.
- If a user tries to add a product (by changing the url) without being a superuser they are redirected to a custom 403 page.
- The superuser will receive a success message notifying them that the product has been successfully updated.


* ##### Delete Product
- The superuser can choose to delete a Product by clicking the delete button on the product card or on the product detail page.

#### Bag
- When the user clicks on the shopping bag icon in the nav bar they are taken to the shopping bag page which shows the products which the user has added to their basket, unit price, quantity and subtotal.

* ##### Quantity Buttons
- The quantity input box displays the product quantity the user has added to their bag.
- The plus and minus buttons increase and decrease the input value.
- If the value is set to 1 the minus quantity will be disabled. Respectively if the value is set to 99 the plus button is disabled.
* ##### Update and Delete Buttons
- Clicking the 'update' icon button saves any changes to the quantity and updates the item's subtotal.
- Clicking the 'Bin' icon button removes the item completely from the user's bag.
- If the user manually types in a negative number and clicks 'update', the item will be removed from the item from the bag.
- If the user manually types in a number >99 and clicks 'update' an error message will display informing the user of the correct parameters.

* ##### Total Section
- At the end of the line items is a summary of the costs.
- The summary features the bags total, delivery cost and the grand total to pay.
- Underneath the grand total users will find a message informing them of how much more they need to spend to receive free delivery if they haven't already met the free delivery threshold (£50).
- Beneath the grand total is two buttons. From here the user can either continue to the checkout or return to the products page by clicking 'Keep Shopping'.

#### Checkout
* ##### Details
- Within the details section the user can fill out their contact details, delivery address, and card number.
- If the user is a guest, a link to create an account or login will be present.
- If the user is signed in a checkbox to save the delivery information can be checked.
- If the user is signed in and has delivery information saved, the delivery details and email address will be automatically filled in.
- If a user leaves a required field empty, inputs whitespace in a required field or includes text in the phone number field an error message will prompt the user to 'Fill in the field' or 'match the format requested'

* ##### Order Summary
- The order summary section details all the items about to be purchased, along with the quantity, subtotal and a grand total.
- Next to the order summary title will be a number reflecting the total number of items that appear in the order.
- Clicking the product image in the summary will take the user to that product's detail page

* ##### Payment
- The card payment is handled by Stripe to ensure secure payment.
- Incorrect card numbers will automatically show an invalid card number error.
- A loading screen will appear when a payment is being processed to stop the user clicking away.
- There is a warning message at the bottom of the page informing the user of how much their card is about to be charged.
- If the payment form doesn't submit properly or the user closes the browser during the wait animation, the order will still be created in the database through the webhook.
- Once the payment is processed, the webhook will search the database to confirm the order exists. If it cannot find it, it will create one using the payment information.

* ##### Confirmation
- Once the order has been processed the user is taken to the checkout success page. This page summarises the completed order.
- An email will be sent to the user with their order confirmation
- This also includes the Sign Up To News Letter / social media links section.


#### News
* ##### News Page
- Each news card shows an image of the news article, its title, author, date it was published and a small clip of what the article says.
- If the user is a superuser, edit and delete buttons will appear at the bottom of the news card.
- The news page is fully responsive, adjusting how many products are on each row depending on the user's screen size.
- The Cards are order on which one was last created.

* ##### News Article
- When the user clicks on an individual news card they are taken to the full news article.
- The news article page displays the image of the news article, its title, author, date it was - published and the news article.
- If the user is a superuser, edit and delete buttons will appear below these details.


#### News Management Page
* ##### Add Article
- The add article page can be accessed by clicking the 'Add Article' button on the account button on the header or in the user dropdown menu. These options are only visible to superusers.
- If a user tries to add a article (by changing the url) without being a superuser they are redirected to a custom 403 page.
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- The user can upload a photo if they wish. If they choose not to, a default image displays as their article image.
- Clicking the 'Add Article' button at the bottom of the form will create the article providing there are no errors on the form.
- The user will receive a success message notifying them that the article has been successfully added.

* ##### Edit Article
- The superuser can choose to edit an article by clicking the edit button on the article card or on the article page.
- The form opens with all fields populated with the original content.
- The image field displays a thumbnail of the existing image and has a checkbox option to remove it. Checking this will change the image to the default image.
- If a user tries to add a product (by changing the url) without being a superuser they are redirected to a custom 403 page.
- The superuser will receive a success message notifying them that the product has been successfully updated.


* ##### Delete Article
- The superuser can choose to delete an article by clicking the delete button on the article card or on the article page.


#### Contact us
* ##### Contact us form
-  Users are easily able to contact the team by using the contact form.

---

## Agile Methodology
Github projects was used to manage the development process using an agile approach. Please see link to project board [here]()

[Back to Table of contents](#table-of-contents)

---

# Technology
### HTML5
* As a structure language.
### CSS
* As a style language
### GitHub
* As a software hosting platform to keep the project in a remote location.
### Git
* As a version-control system tracking.
### Gitpod
* As a development hosting platform.
### Adobe XD
* As a wireframing tool.
### Adobe Lightroom
* As an image editor.
### Adobe Illustrator
* As an illustration editor.

## Other features used. 

- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [JQuery](https://jquery.com/)
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [SQLite](https://www.sqlite.org/index.html) - was used as the database during production.
- [Stripe](https://stripe.com/ie) used for the payments system.
- [AWS](https://aws.amazon.com/?nc2=h_lg) used for file storage.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Responsinator](http://www.responsinator.com/) - Used to verify responsiveness of website on different devices.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [Jshint](https://jshint.com/) - used to validate javascript.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms.
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling.
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/): Used to create the site's privacy policy.
- [Mailchimp](https://mailchimp.com/?currency=EUR): Used to create the newsletter signup functionality.

[Back to Table of contents](#table-of-contents)

--- 

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']

- Push these changes to Github.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                               |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                               |
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
| USE_AWS               | True (when AWS set up - instructions below)                                   |

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.


## AWS Set Up
### AWS S3 Bucket
- Create an AWS account.
- From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
- Click 'Create a new bucket', give it a name(match your Heroku app name if possible), and choose the region closest to you.
- Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred.
- Uncheck block all public access and acknowledge that the bucket will be public.
- Click 'Create bucket'.
- Open the created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
- Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- In the 'Bucket Policy' section and select 'Policy Generator'.
- Choose 'S3 Bucket Policy' from the type dropdown.
- In 'Step 2: Add Statements', add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the popup that appears
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.


### IAM
- From the 'Services' menu, search IAM and select it.
- Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'. Choose a name and click 'Create'.
- Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Get the bucket ARN from 'S3 Permissions' as per above.
- Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```

- Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
- Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You need to create a user to put in the group. Select users from the sidebar and click 'Add user'.
- Give your user a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you created.
- Keep clicking 'Next' until you reach the 'Create user' button and click that.
- Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables as per above list and also in your env.py.


### Connecting S3 to Django 
- Go back to your IDE and install 2 more requirements:
    - `pip3 install boto3`
    - `pip3 install django-storages` 
- Update your requirements.txt file by typing `pip3 freeze --local > requirements.txt` and add storages to your installed apps.
- Create an if statement in settings.py 

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

```
- Then add the line 

    - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell django where our static files will be coming from in production.


- Create a file called custom storages and import both our settings from django.con as well as the s3boto3 storage class from django storages. 
- Create the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In settings.py add the following inside the if statement:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

- and then add the following at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

- Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Then under 'Permissions' select the option 'Grant public-read access' and click upload.
- Your static files and media files should be automatically linked from django to your S3 bucket.

## Forking this repository
- Locate the repository at this link [George Shaw](https://github.com/Jonnywdev/george-shaw-brewery).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

## Cloning this repository
To clone this repository follow the below steps: 

1. Locate the repository at this link [George Shaw](https://github.com/Jonnywdev/george-shaw-brewery). 
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

---

# Testing
## Functionality Testing
I used Mozilla web developer tools and Chrome developer tools throughout the project for testing and solving problems with responsiveness and style issues.

## Compatibility Testing
The website was tested across multiple virtual mobile devices and browsers. I checked all supported devices in both web developer tools.

I tested on hardware devices such as: Apple Ipad 12 pro, Samsung S20 Ultra smart phone with Android 10 and used a Iphone 5 to compare the difference in size.




## Performance Testing
I used [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool to check performance of the website. I had to make a few changes that I needed to make to improve the scores. Screenshots and supporting text is presented below:


## Code Validation
At the end of the project I used 3 websites to validate the code.
 * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS
 * [Nu Html Checker](https://validator.w3.org/) to test HTML
 * [Jshint](https://jshint.com/)to validate JS
 All code passed with no errors or warnings.

[Back to Table of contents](#table-of-contents)

---

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Code Institute - Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)