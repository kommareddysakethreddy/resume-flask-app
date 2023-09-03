from flask import Flask, jsonify, request, render_template, send_file, make_response
import os
from jinja2 import Template

app = Flask(__name__, template_folder='output',static_folder='output')
template_file_path = os.path.join("templates", "resume_template.html")

def generate_resume(json_data, template_file_path):
    with open(template_file_path, 'r') as template_file:
        template_content = template_file.read()
    template = Template(template_content)
    rendered_html = template.render(**json_data)
    return rendered_html

@app.route('/generate-resume-api', methods=['POST'])
def generate_resume_api():
    json_data = request.get_json()
    rendered_html = generate_resume(json_data, template_file_path)

    # Create the HTML file and save it
    output_html_file_path = 'output/resume.html'
    with open(output_html_file_path, 'w') as f:
        f.write(rendered_html)

    # Serve the HTML file and send its URL as a response
    response = make_response(rendered_html)
    response.headers["Content-Disposition"] = "inline; filename=resume.html"

    return response


@app.route('/show-resume', methods=['GET'])
def show_resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)
