from flask import Blueprint, render_template, request
from PIL import Image
import cv2
import fitz
import numpy as np
from werkzeug.utils import secure_filename
import os
from datetime import datetime

bp = Blueprint('bp', __name__, template_folder='templates')


@bp.route('/')
def upload_pdf():
    return render_template('upload_pdf.html')


@bp.route('/page_count', methods=['POST'])
def page_count():
    colored_page_count = 0
    num = 0
    # Get the uploaded PDF file
    pdf_file = request.files['pdf']
    # Save the PDF file to the uploads folder
    filename = secure_filename(pdf_file.filename)
    pdf_file.save(os.path.join('myapp/static/uploads', filename))
    pdf_file_path = os.path.join('myapp/static/uploads', filename)
    with fitz.open(pdf_file_path) as doc:
        # Iterate through the pages
        total_page_count = len(doc)
        for _, page in enumerate(doc):
            # Render the page to an image
            pix = page.get_pixmap(alpha=False)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            arr = np.array(img)
            arr_mean = cv2.mean(arr)
            if not (arr_mean[0] == arr_mean[1] == arr_mean[2]):
                colored_page_count += 1
    os.remove(pdf_file_path)
    return render_template('page_count.html', colored_count=colored_page_count, 
                           b_w_count=total_page_count-colored_page_count, total_page_count=total_page_count)


@bp.route('/page_count_result')
def page_count_result():
    return render_template('page_count.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')


def inject_now_context_processor():
    return {'now': datetime.utcnow()}


bp.app_context_processor(inject_now_context_processor)

