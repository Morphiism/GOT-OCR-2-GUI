import re
import os
import scripts.html2pdf as html2pdf


# 转换HTML编码
def convert_html_encoding(input_file_path, output_file_path):
    # gb2312
    with open(input_file_path, 'r', encoding='gb2312') as file:
        content = file.read()

    # utf8
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# 替换HTML内容
def repalce_html_content(input_file_path, output_file_path):
    pattern = r'https://cdn.jsdelivr.net/npm/mathpix-markdown-it@1.3.6/es5/bundle.js'
    replacement = 'markdown-it.js'
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    new_html_content = re.sub(pattern, replacement, content)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(new_html_content)


def render(model, tokenizer, image_path, convert_to_pdf=False):
    """
    渲染 OCR 结果为 HTML 并可选转换为 PDF。

    Args:
        model: 加载的 OCR 模型。
        tokenizer: 模型对应的分词器。
        image_path: 待识别图像的路径。
        convert_to_pdf: 是否将渲染结果转换为 PDF (布尔值)。
    """
    try:
        # 定义输出HTML路径
        img_name = os.path.basename(image_path)
        img_name_no_ext = os.path.splitext(img_name)[0]
        html_gb2312_path = os.path.join("result", f"{img_name_no_ext}-gb2312.html")
        html_utf8_path = os.path.join("result", f"{img_name_no_ext}-utf8.html")
        html_utf8_local_path = os.path.join("result", f"{img_name_no_ext}-utf8-local.html")

        # 渲染OCR结果
        model.chat(tokenizer, image_path, ocr_type='format', render=True, save_render_file=html_gb2312_path)

        # 转换为UTF-8编码
        convert_html_encoding(html_gb2312_path, html_utf8_path)

        # 根据参数决定是否转换为PDF
        if convert_to_pdf:
            repalce_html_content(html_utf8_path, html_utf8_local_path)
            pdf_path = os.path.join("result", f"{img_name_no_ext}.pdf")
            html2pdf.output_pdf(html_utf8_local_path, pdf_path)
        return True
    except:
        return False