from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Heading(models.Model):
    heading = models.CharField(max_length=50)
    main_pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.heading


class navbar(models.Model):
    home = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    packages = models.CharField(max_length=50)
    specialoffer = models.CharField(max_length=50)

    def __str__(self):
        return self.home


class footer(models.Model):
    heading = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    link_text = models.CharField(max_length=50)
    popular_text = models.CharField(max_length=50)
    contact_text = models.CharField(max_length=50)
    phonecode = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    phonenumber = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    emailid = models.EmailField(max_length=254)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    fac_href = models.CharField(null=True, max_length=200)
    twitter_href = models.CharField(null=True, max_length=200)
    insta_href = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.heading


class package(models.Model):
    heading = models.CharField(max_length=50)
    heading_text = models.CharField(max_length=50)
    dest1 = models.CharField(max_length=50)
    dest1_price = models.PositiveIntegerField()
    dest1_days = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest1_nights = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest1_accomodation = models.CharField(max_length=10)
    dest1_transportation = models.CharField(max_length=10)
    dest1_food = models.CharField(max_length=10)
    dest1_star = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    dest1_reviewcount = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    dest1_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest2 = models.CharField(max_length=50)
    dest2_price = models.PositiveIntegerField()
    dest2_days = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest2_nights = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest2_accomodation = models.CharField(max_length=10)
    dest2_transportation = models.CharField(max_length=10)
    dest2_food = models.CharField(max_length=10)
    dest2_star = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    dest2_reviewcount = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    dest2_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest3 = models.CharField(max_length=50)
    dest3_price = models.PositiveIntegerField()
    dest3_days = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest3_nights = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest3_accomodation = models.CharField(max_length=10)
    dest3_transportation = models.CharField(max_length=10)
    dest3_food = models.CharField(max_length=10)
    dest3_star = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    dest3_reviewcount = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    dest3_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest4 = models.CharField(max_length=50)
    dest4_price = models.PositiveIntegerField()
    dest4_days = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest4_nights = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest4_accomodation = models.CharField(max_length=10)
    dest4_transportation = models.CharField(max_length=10)
    dest4_food = models.CharField(max_length=10)
    dest4_star = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    dest4_reviewcount = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    dest4_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest5 = models.CharField(max_length=50)
    dest5_price = models.PositiveIntegerField()
    dest5_days = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest5_nights = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest5_accomodation = models.CharField(max_length=10)
    dest5_transportation = models.CharField(max_length=10)
    dest5_food = models.CharField(max_length=10)
    dest5_star = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    dest5_reviewcount = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    dest5_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest6 = models.CharField(max_length=50)
    dest6_price = models.PositiveIntegerField()
    dest6_days = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest6_nights = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    dest6_accomodation = models.CharField(max_length=10)
    dest6_transportation = models.CharField(max_length=10)
    dest6_food = models.CharField(max_length=10)
    dest6_star = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    dest6_reviewcount = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    dest6_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.heading


class service(models.Model):
    serv1_heading = models.CharField(max_length=200)
    serv1_text = models.CharField(max_length=200)
    serv2_heading = models.CharField(max_length=200)
    serv2_text = models.CharField(max_length=200)
    serv3_heading = models.CharField(max_length=200)
    serv3_text = models.CharField(max_length=200)

    def __str__(self):
        return self.serv1_heading


class specialoffer(models.Model):
    special_heading = models.CharField(max_length=200)
    special_star = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    special_review_count = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    special_days = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    special_nights = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    special_person = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    special_accomodation = models.CharField(max_length=10)
    special_transportation = models.CharField(max_length=10)
    special_food = models.CharField(max_length=10)
    offer_detail = models.CharField(max_length=200)
    offer_image = models.ImageField(null=True, blank=True, upload_to="images/")
    button_1 = models.CharField(max_length=20)
    button_2 = models.CharField(max_length=20)
    offer_heading = models.CharField(max_length=20)
    percent_off = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    special_price = models.PositiveIntegerField()
    special_type = models.CharField(max_length=20)
    special_type_price = models.PositiveIntegerField()

    def __str__(self):
        return self.special_heading


class clientreview(models.Model):
    client_heading = models.CharField(max_length=200)
    client_text = models.CharField(max_length=200)
    customer_name_1 = models.CharField(max_length=200)
    customer_review_1 = models.CharField(max_length=200)
    customer_location_1 = models.CharField(max_length=200)
    customer1_image = models.ImageField(null=True, blank=True, upload_to="images/")
    customer_review_2 = models.CharField(max_length=200)
    customer_name_2 = models.CharField(max_length=200)
    customer_location_2 = models.CharField(max_length=200)
    customer2_image = models.ImageField(null=True, blank=True, upload_to="images/")
    customer_name_3 = models.CharField(max_length=200)
    customer_review_3 = models.CharField(max_length=200)
    customer_location_3 = models.CharField(max_length=200)
    customer3_image = models.ImageField(null=True, blank=True, upload_to="images/")
    customer_name_4 = models.CharField(max_length=200)
    customer_review_4 = models.CharField(max_length=200)
    customer_location_4 = models.CharField(max_length=200)
    customer4_image = models.ImageField(null=True, blank=True, upload_to="images/")
    customer_name_5 = models.CharField(max_length=200)
    customer_review_5 = models.CharField(max_length=200)
    customer_location_5 = models.CharField(max_length=200)
    customer5_image = models.ImageField(null=True, blank=True, upload_to="images/")
    customer_name_6 = models.CharField(max_length=200)
    customer_review_6 = models.CharField(max_length=200)
    customer_location_6 = models.CharField(max_length=200)
    customer6_image = models.ImageField(null=True, blank=True, upload_to="images/")
    customer_name_7 = models.CharField(max_length=200)
    customer_review_7 = models.CharField(max_length=200)
    customer_location_7 = models.CharField(max_length=200)
    customer7_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.client_heading


class destination(models.Model):
    top_heading = models.CharField(max_length=200)
    dest_text = models.CharField(max_length=200)
    dest1_name = models.CharField(max_length=200)
    no_tours_1 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    no_places_1 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    dest1_price = models.PositiveIntegerField(default="0")
    dest1_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest2_name = models.CharField(max_length=200)
    no_tours_2 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    no_places_2 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    dest2_price = models.PositiveIntegerField(default="0")
    dest2_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest3_name = models.CharField(max_length=200)
    no_tours_3 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    no_places_3 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    dest3_price = models.PositiveIntegerField(default="0")
    dest3_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest4_name = models.CharField(max_length=200)
    no_tours_4 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    no_places_4 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    dest4_price = models.PositiveIntegerField(default="0")
    dest4_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest5_name = models.CharField(max_length=200)
    no_tours_5 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    no_places_5 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    dest5_price = models.PositiveIntegerField(default="0")
    dest5_image = models.ImageField(null=True, blank=True, upload_to="images/")
    dest6_name = models.CharField(max_length=200)
    no_tours_6 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    no_places_6 = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    dest6_price = models.PositiveIntegerField(default="0")
    dest6_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.top_heading


class place(models.Model):
    trip = models.CharField(max_length=200)
    day1_place = models.CharField(max_length=2000)
    day2_place = models.CharField(max_length=2000)
    day3_place = models.CharField(max_length=2000)
    day4_place = models.CharField(max_length=2000)
    day1_text = models.CharField(max_length=2000)
    day2_text = models.CharField(max_length=2000)
    day3_text = models.CharField(max_length=2000)
    day4_text = models.CharField(max_length=2000)
    day1_image = models.ImageField(null=True, blank=True, upload_to="images/")
    day2_image = models.ImageField(null=True, blank=True, upload_to="images/")
    day3_image = models.ImageField(null=True, blank=True, upload_to="images/")
    day4_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.trip


class offer(models.Model):
    place = models.CharField(max_length=200)
    days = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    night = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])
    price = models.PositiveIntegerField(default="0")
    main_image = models.ImageField(null=True, blank=True, upload_to="images/")
    day1_img =  models.ImageField(null=True, blank=True, upload_to="images/")
    day1_place = models.CharField(max_length=2000, null=True, blank=True)
    day1_text = models.CharField(max_length=2000, null=True, blank=True)
    day2_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day2_place = models.CharField(max_length=2000, null=True, blank=True)
    day2_text = models.CharField(max_length=2000, null=True, blank=True)
    day3_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day3_place = models.CharField(max_length=2000, null=True, blank=True)
    day3_text = models.CharField(max_length=2000, null=True, blank=True)
    day4_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day4_place = models.CharField(max_length=2000, null=True, blank=True)
    day4_text = models.CharField(max_length=2000, null=True, blank=True)
    day5_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day5_place = models.CharField(max_length=2000, null=True, blank=True)
    day5_text = models.CharField(max_length=2000, null=True, blank=True)
    day6_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day6_place = models.CharField(max_length=2000, null=True, blank=True)
    day6_text = models.CharField(max_length=2000, null=True, blank=True)
    day7_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day7_place = models.CharField(max_length=2000, null=True, blank=True)
    day7_text = models.CharField(max_length=2000, null=True, blank=True)
    day8_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day8_place = models.CharField(max_length=2000, null=True, blank=True)
    day8_text = models.CharField(max_length=2000, null=True, blank=True)
    day9_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day9_place = models.CharField(max_length=2000, null=True, blank=True)
    day9_text = models.CharField(max_length=2000, null=True, blank=True)
    day10_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day10_place = models.CharField(max_length=2000, null=True, blank=True)
    day10_text = models.CharField(max_length=2000, null=True, blank=True)
    day11_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day11_place = models.CharField(max_length=2000, null=True, blank=True)
    day11_text = models.CharField(max_length=2000, null=True, blank=True)
    day12_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day12_place = models.CharField(max_length=2000, null=True, blank=True)
    day12_text = models.CharField(max_length=2000, null=True, blank=True)
    day13_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day13_place = models.CharField(max_length=2000, null=True, blank=True)
    day13_text = models.CharField(max_length=2000, null=True, blank=True)
    day14_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day14_place = models.CharField(max_length=2000, null=True, blank=True)
    day14_text = models.CharField(max_length=2000, null=True, blank=True)
    day15_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day15_place = models.CharField(max_length=2000, null=True, blank=True)
    day15_text = models.CharField(max_length=2000, null=True, blank=True)
    day16_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day16_place = models.CharField(max_length=2000, null=True, blank=True)
    day16_text = models.CharField(max_length=2000, null=True, blank=True)
    day17_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day17_place = models.CharField(max_length=2000, null=True, blank=True)
    day17_text = models.CharField(max_length=2000, null=True, blank=True)
    day18_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day18_place = models.CharField(max_length=2000, null=True, blank=True)
    day18_text = models.CharField(max_length=2000, null=True, blank=True)
    day19_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day19_place = models.CharField(max_length=2000, null=True, blank=True)
    day19_text = models.CharField(max_length=2000, null=True, blank=True)
    day20_img = models.ImageField(null=True, blank=True, upload_to="images/")
    day20_place = models.CharField(max_length=2000, null=True, blank=True)
    day20_text = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.place
