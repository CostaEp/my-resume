import yaml
import jinja2

# Загружаем YAML
with open("resume.yaml", "r") as file:
    data = yaml.safe_load(file)

# Читаем шаблон Markdown
with open("template.md", "r") as file:
    template = jinja2.Template(file.read())

# Генерируем Markdown
resume_md = template.render(data)

# Сохраняем Markdown-файл
with open("resume.md", "w") as file:
    file.write(resume_md)

print("✅ Resume converted to Markdown successfully!")