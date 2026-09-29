activehub is a #responsive demo web platform designed for a private fitness and leisure business that operates multiple centres and provides gym, aquatic, swimming, fitness classes, memberships, and event services.
The project focuses on creating user-friendly experience that helps visitors quickly
discover activities, 
find suitable services,
make bookings,
submit enquiries, and
explore membership options.
py -m flask --app app.main run --debug

activeHub web foundation has templates folder and includes folder 

base.html is the main layout/template that other pages extend:
{% extends "base.html" %}
{% block title %}ActiveHub | Fitness{% endblock %}
{% block content %}
    ...
{% endblock %}

The includes/ folder is for smaller reusable sections that you insert with:
{% include "includes/activities_nav.html" %}
base.html → main template/layout
includes/ → reusable components
fitness.html, membership.html, etc. → individual pages
