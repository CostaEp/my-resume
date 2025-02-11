---
title: "{{ name }} - Resume"
author: "{{ name }}"
date: "2025"
fontsize: 12pt
geometry: margin=1in
lang: "en"
---

# {{ name }} - Resume

## About Me
**{{ job_title }}**  
Location: {{ location }}

{{ summary }}

## Experience
{% for exp in experience %}
### {{ exp.company }} - {{ exp.role }} ({{ exp.duration }})
{% for resp in exp.responsibilities %}
- {{ resp }}
{% endfor %}
{% endfor %}

## Skills
### DevOps & Cloud
{% for skill in skills["DevOps & Cloud"] %}
- {{ skill }}
{% endfor %}

### Programming & Scripting
{% for skill in skills["Programming & Scripting"] %}
- {{ skill }}
{% endfor %}

### Databases
{% for skill in skills["Databases"] %}
- {{ skill }}
{% endfor %}

## Education
{% for edu in education %}
- **{{ edu.institution }}**, {{ edu.degree }} ({{ edu.year }})
{% endfor %}

## Achievements
{% for ach in achievements %}
- {{ ach.title }}
{% endfor %}

## Soft Skills
{% for skill in soft_skills %}
- {{ skill }}
{% endfor %}

## Languages
{% for lang in languages %}
- {{ lang }}
{% endfor %}