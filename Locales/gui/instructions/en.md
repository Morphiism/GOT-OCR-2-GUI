## Instructions
### **Modes**
#### `OCR` Modes
- ocr: Standard OCR
- format: OCR with formatting
#### `Fine-Grained` Modes
- fine-grained-ocr: OCR content within a specific box
- fine-grained-format: OCR and format content within a specific box
- fine-grained-color-ocr: OCR content within a box of a specific color (I haven't tried this, but it seems like you would need to draw a red/green/blue box first and then select the color in the GUI)
- fine-grained-color-format: OCR and format content within a box of a specific color
#### `Multi-Crop` Modes
- Suitable for more complex images
#### `Render` Modes
- Exist files will be overwritten!!!Check the file path before clicking the button!!!
- Render OCR content and save it as an HTML file
- Will be saved as UTF8 encoding and GB2312 encoding files
- You can convert HTML to PDF
### **How to render**
1. Input image name in the text box, this will become the base name of the output files
2. Click the "Submit Image Name" button to apply the name
3. You will find that three textboxes below changed, which means the name has been applied
4. Click the "Save as PDF" button to save the HTML file as a PDF file